# -*- coding: utf-8 -*-
# maze.py - module containing the maze object
# This file is part of brutalmaze
#
# brutalmaze is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# brutalmaze is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with brutalmaze.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2017 Nguyễn Gia Phong

from collections import deque
from math import atan, cos, sin, pi
from random import getrandbits

import pygame

from .characters import pos, regpoly, fill_aapolygon, Hero, Enemy
from .constants import *


def sign(n):
    """Return the sign of number n."""
    return -1 if n < 0 else 1 if n else 0


def cosin(x):
    """Return the sum of cosine and sine of x (measured in radians)."""
    return cos(x) + sin(x)


class Maze:
    """Object representing the maze, including the characters."""
    def __init__(self, size):
        self.w, self.h = size
        self.surface = pygame.display.set_mode(size, RESIZABLE)
        self.distance = int((self.w * self.h / 416) ** 0.5)
        self.step = self.distance // 5
        self.middlex, self.middley = self.x, self.y = self.w >> 1, self.h >> 1
        w, h = self.w//self.distance+2 >> 1, self.h//self.distance+2 >> 1
        self.rangex = range(MIDDLE - w, MIDDLE + w + 1)
        self.rangey = range(MIDDLE - h, MIDDLE + h + 1)

        self.hero = Hero(self.surface)
        self.enemies = [Enemy(self.surface, 4, 34, 34)]
        self.right = self.down = self.offsetx = self.offsety = 0

        def wall(bit, upper=True):
            if bit: return deque([True]*ROAD_WIDTH + [False]*ROAD_WIDTH)
            if upper: return deque([True] * (ROAD_WIDTH<<1))
            return deque([False] * (ROAD_WIDTH<<1))

        self.map = deque()
        for _ in range(MAZE_SIZE):
            upper, lower = deque(), deque()
            for _ in range(MAZE_SIZE):
                b = getrandbits(1)
                upper.extend(wall(b))
                lower.extend(wall(b, False))
            for _ in range(ROAD_WIDTH): self.map.append(upper.__copy__())
            for _ in range(ROAD_WIDTH): self.map.append(lower.__copy__())
        self.draw()

    def draw(self):
        """Draw the maze."""
        self.surface.fill(BG_COLOR)
        for i in self.rangex:
            for j in self.rangey:
                if not self.map[i][j]: continue
                x, y = pos(i, j, self.distance, self.middlex, self.middley)
                square = regpoly(4, int(self.distance / SQRT2), x, y, pi / 4)
                fill_aapolygon(self.surface, square, FG_COLOR)

    def wake(self, enemy):
        """Wake the enemy up if it can see the hero."""
        dx = (enemy.x - MIDDLE)*self.distance + self.offsetx*self.step
        dy = (enemy.y - MIDDLE)*self.distance + self.offsety*self.step
        mind = cosin(abs(atan(dy / dx)) if dx else 0) * self.distance
        startx = starty = MIDDLE
        stopx, stopy = enemy.x, enemy.y
        if startx > stopx : startx, stopx = stopx, startx
        if starty > stopy : starty, stopy = stopy, starty
        for i in range(startx, stopx + 1):
            for j in range(starty, stopy + 1):
                if not self.map[i][j] or (i, j) == (enemy.x, enemy.y): continue
                x, y = pos(i, j, self.distance, self.middlex, self.middley)
                d = abs(dy*(x-self.x) - dx*(y-self.y)) / (dy**2 + dx**2)**0.5
                if d <= mind: return
        enemy.awake = True

    def update(self):
        """Update the maze."""
        modified = False
        self.offsetx += self.right
        s = sign(self.offsetx) * 2
        if ((self.map[MIDDLE - s][MIDDLE - 1]
             or self.map[MIDDLE - s][MIDDLE]
             or self.map[MIDDLE - s][MIDDLE + 1])
            and abs(self.offsetx) > 3):
            self.offsetx -= self.right
        else:
            modified = True

        self.offsety += self.down
        s = sign(self.offsety) * 2
        if ((self.map[MIDDLE - 1][MIDDLE - s]
             or self.map[MIDDLE][MIDDLE - s]
             or self.map[MIDDLE + 1][MIDDLE - s])
            and abs(self.offsety) > 3):
            self.offsety -= self.down
        else:
            modified = True

        if modified:
            if abs(self.offsetx) == 5:
                s = sign(self.offsetx)
                self.offsetx = 0
                self.map.rotate(s)
                for enemy in self.enemies: enemy.place(s, 0)
            if abs(self.offsety) == 5:
                s = sign(self.offsety)
                self.offsety = 0
                for d in self.map: d.rotate(s)
                for enemy in self.enemies: enemy.place(0, s)

            self.middlex = self.x + self.offsetx*self.step
            self.middley = self.y + self.offsety*self.step
            self.draw()
            for enemy in self.enemies:
                if not enemy.awake: self.wake(enemy)

        for enemy in self.enemies:
            enemy.update(self.distance, self.middlex, self.middley)
        self.hero.update()
        pygame.display.flip()

    def resize(self, w, h):
        """Resize the maze."""
        size = self.w, self.h = w, h
        self.surface = pygame.display.set_mode(size, RESIZABLE)
        self.hero.resize()

        self.distance = int((w * h / 416) ** 0.5)
        self.step = self.distance // 5
        self.middlex = self.x + self.offsetx*self.step
        self.middley = self.y + self.offsety*self.step
        self.x, self.y = w >> 1, h >> 1
        w, h = self.w//self.distance+2 >> 1, self.h//self.distance+2 >> 1
        self.rangex = range(MIDDLE - w, MIDDLE + w + 1)
        self.rangey = range(MIDDLE - h, MIDDLE + h + 1)
        self.draw()

    def move(self, x, y):
        """Command the maze to move x step/frame faster to the left and
        y step/frame faster upward so the hero will move in the reverse
        direction.
        """
        self.right += x
        self.down += y
        self.right, self.down = sign(self.right), sign(self.down)