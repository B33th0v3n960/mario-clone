import pygame
from os import walk


def import_folder(path):
    output = []
    for _, __, image_file in walk(path):
        list = sorted(image_file)
        for image in list:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            output.append(image_surf)

    return output
