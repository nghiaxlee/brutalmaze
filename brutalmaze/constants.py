# -*- coding: utf-8 -*-
# constants.py - shared constants
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

from pygame.locals import *
from pygame.math import Vector2

EPSILON = 8 ** -8
SQRT2 = 2 ** 0.5

FPS = 30
SIZE = 400, 400
MAZE_SIZE = 8
ROAD_WIDTH = 5
MIDDLE = (MAZE_SIZE + (MAZE_SIZE&1) - 1)*ROAD_WIDTH + (ROAD_WIDTH >> 1)

TANGO = {'Butter': ((252, 233, 79), (237, 212, 0), (196, 160, 0)),
         'Orange': ((252, 175, 62), (245, 121, 0), (206, 92, 0)),
         'Chocolate': ((233, 185, 110), (193, 125, 17), (143, 89, 2)),
         'Chameleon': ((138, 226, 52), (115, 210, 22), (78, 154, 6)),
         'Sky Blue': ((114, 159, 207), (52, 101, 164), (32, 74, 135)),
         'Plum': ((173, 127, 168), (117, 80, 123), (92, 53, 102)),
         'Scarlet Red': ((239, 41, 41), (204, 0, 0), (164, 0, 0)),
         'Aluminium': ((238, 238, 236), (211, 215, 207), (186, 189, 182),
                       (136, 138, 133), (85, 87, 83), (46, 52, 54))}
TANGO_KEYS = ('Butter', 'Orange', 'Chocolate', 'Chameleon',
              'Sky Blue', 'Plum', 'Scarlet Red', 'Aluminium')
BG_COLOR = TANGO['Aluminium'][-1]
FG_COLOR = TANGO['Aluminium'][0]