import pygame
from tiles import Tile
from settings import *
from player import Player


class Level:
    def __init__(self, level_data):
        # Level Setup
        self.display_surface = pygame.display.get_surface()
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # Iterate throught level_data and draw the map
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "P":
                    player = Player((x, y))
                    self.player.add(player)

    def run(self):
        # Draw tiles
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)

        # Draw Player
        self.player.draw(self.display_surface)
        self.player.update()
