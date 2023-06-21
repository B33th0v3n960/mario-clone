import pygame
from tiles import Tile
from settings import tile_size, screen_width
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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width * 0.75 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def run(self):
        # Draw tiles
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)

        # Draw Player
        self.player.draw(self.display_surface)
        self.player.update()

        # Movement
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()
