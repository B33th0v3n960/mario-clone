import pygame
from tiles import Tile
from settings import *


class Level:
    def __init__(self, level_data):
        # Level Setup
        self.display_surface = pygame.display.get_surface()
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

        # Iterate throught level_data and draw the map
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(0)
        self.tiles.draw(self.display_surface)
