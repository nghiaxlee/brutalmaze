# -*- coding: utf-8 -*-
# constants.py - module for shared constants
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

from pygame import image
from pygame.locals import *
from pkg_resources import resource_filename

__doc__ = 'brutalmaze module for shared constants'

ICON = image.load(resource_filename('brutalmaze', 'icon.png'))

SQRT2 = 2 ** 0.5
GOLDEN_MEAN = 5**0.5/2 + 0.5

INIT_FPS = 30.0
SIZE = 640, 480
MAZE_SIZE = 12
ROAD_WIDTH = 5
CELL_WIDTH = ROAD_WIDTH * 2
MIDDLE = (MAZE_SIZE + MAZE_SIZE%2 - 1)*ROAD_WIDTH + ROAD_WIDTH//2
LAST_ROW = (MAZE_SIZE-1) * ROAD_WIDTH * 2
INIT_SCORE = 208.2016
MOVE_SPEED = 5  # grid/s
HEAL_SPEED = 1.0    # HP/s

EMPTY, WALL, HERO, ENEMY = range(4)
ADJACENT_GRIDS = (1, 0), (0, 1), (-1, 0), (0, -1)

TANGO = {'Butter': ((252, 233, 79), (237, 212, 0), (196, 160, 0)),
         'Orange': ((252, 175, 62), (245, 121, 0), (206, 92, 0)),
         'Chocolate': ((233, 185, 110), (193, 125, 17), (143, 89, 2)),
         'Chameleon': ((138, 226, 52), (115, 210, 22), (78, 154, 6)),
         'Sky Blue': ((114, 159, 207), (52, 101, 164), (32, 74, 135)),
         'Plum': ((173, 127, 168), (117, 80, 123), (92, 53, 102)),
         'Scarlet Red': ((239, 41, 41), (204, 0, 0), (164, 0, 0)),
         'Aluminium': ((238, 238, 236), (211, 215, 207), (186, 189, 182),
                       (136, 138, 133), (85, 87, 83), (46, 52, 54))}
ENEMIES = ('Butter', 'Orange', 'Chocolate', 'Chameleon',
           'Sky Blue', 'Plum', 'Scarlet Red')
BG_COLOR = TANGO['Aluminium'][-1]
FG_COLOR = TANGO['Aluminium'][0]
