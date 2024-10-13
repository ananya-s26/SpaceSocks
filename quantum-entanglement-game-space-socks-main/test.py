import pygame
import random
import sys
import math
import time
import os

#directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

#full path to the background.wav file
background_music_path = os.path.join(base_dir, 'assets', 'background.wav')
pygame.init()
backp=os.path.join(base_dir,'assets','background-pic.jpg')
back=pygame.image.load(backp)