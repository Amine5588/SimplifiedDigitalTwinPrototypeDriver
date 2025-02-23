from pathlib import Path
import pygame
from pygame.locals import *
import os

def load_image(file, transparent=True):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_folder = os.path.join(project_root, "media")
    file_to_open = os.path.join(data_folder, file)

    image = pygame.image.load(str(file_to_open))

    if transparent == True:
        image = image.convert()
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image
