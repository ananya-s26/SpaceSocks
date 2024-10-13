'''import pygame
import os
import math
import random
import subprocess

pygame.init()
pygame.mixer.init()

# Directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

font5 = pygame.font.SysFont('monospace', 100, bold=True)  # Big bold font for "Space Socks"

# Full path to the background.wav file
background_music_path = os.path.join(base_dir, 'assets', 'background.wav')

# Check for background music file
if not os.path.exists(background_music_path):
    print("Background music file not found.")
else:
    pygame.mixer.music.load(background_music_path)
    pygame.mixer.music.play(-1)

backp = os.path.join(base_dir, 'assets', 'background-pic.jpg')
if not os.path.exists(backp):
    print("Background image file not found.")
else:
    back = pygame.image.load(backp)

satellitep = os.path.join(base_dir, 'pics', 'satellite-pic.png')
if not os.path.exists(satellitep):
    print("Satellite image file not found.")
else:
    quatum_quest_logo = pygame.image.load(satellitep)

screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Quantum_Circuits')
pygame.display.set_icon(quatum_quest_logo)

def print_text1(text, font_size, ypos):
    font = pygame.font.SysFont('monospace', font_size, bold=True)
    color = (255, 255, 255)
    text_surface = font.render(text, True, color)

    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, ypos))
    screen.blit(text_surface, text_rect)

def print_text2(text, font_size, ypos):
    font = pygame.font.SysFont('monospace', font_size, bold=True)
    color = (57,255,20)
    text_surface = font.render(text, True, color)

    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, ypos))
    screen.blit(text_surface, text_rect)

def draw_screen(text):
    pygame.draw.rect(screen, (255,255,255), (20, 100, screen.get_width()-40, screen.get_height()-100))
    print_text2(text, 30, 100 + screen.get_height()-100 // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(back, (0, 0))
    print_text1("Learn", 70, 70)
    draw_screen("quantum entanglement:")
    pygame.display.flip()

pygame.quit()
'''

import pygame
import os
import math
import random
import subprocess

pygame.init()
pygame.mixer.init()

# Directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

font5 = pygame.font.SysFont('monospace', 100, bold=True)  # Big bold font for "Space Socks"

# Full path to the background.wav file
background_music_path = os.path.join(base_dir, 'assets', 'background.wav')

# Check for background music file
if not os.path.exists(background_music_path):
    print("Background music file not found.")
else:
    pygame.mixer.music.load(background_music_path)
    pygame.mixer.music.play(-1)

backp = os.path.join(base_dir, 'assets', 'background-pic.jpg')
if not os.path.exists(backp):
    print("Background image file not found.")
else:
    back = pygame.image.load(backp)

satellitep = os.path.join(base_dir, 'pics', 'satellite-pic.png')
if not os.path.exists(satellitep):
    print("Satellite image file not found.")
else:
    quatum_quest_logo = pygame.image.load(satellitep)

screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Quantum_Circuits')
pygame.display.set_icon(quatum_quest_logo)

def print_text1(text, font_size, ypos):
    font = pygame.font.SysFont('monospace', font_size, bold=True)
    color = (255, 255, 255)
    text_surface = font.render(text, True, color)

    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, ypos))
    screen.blit(text_surface, text_rect)

def print_text2(text, font_size, ypos):
    font = pygame.font.SysFont('monospace', font_size, bold=True)
    color = (57, 255, 20)  # Neon green color
    text_surface = font.render(text, True, color)

    return text_surface, text_surface.get_rect(center=(screen.get_width() // 2, ypos))

def draw_screen(text):
    # Draw a black rectangle for the background of the text
    pygame.draw.rect(screen, (0, 0, 0), (20, 100, screen.get_width() - 40, screen.get_height() - 180))
    lines = wrap_text(text, 960)  # 960 is the width of the rectangle minus padding

    y_offset = 120  # Initial vertical offset for text drawing
    for line in lines:
        text_surface, text_rect = print_text2(line, 30, y_offset)
        text_rect.topleft = (40, y_offset)  # Adjust to add padding
        screen.blit(text_surface, text_rect)
        y_offset += text_rect.height  # Move down for the next line



def wrap_text(text, width):
    """Wrap text for the specified width."""
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        # Check the size of the current line with the new word
        test_line = f"{current_line} {word}".strip()
        text_surface, _ = print_text2(test_line, 30, 0)
        if text_surface.get_width() <= width:
            current_line = test_line  # Add word to current line
        else:
            lines.append(current_line)  # Add completed line to lines
            current_line = word  # Start a new line with the current word

    if current_line:  # Add any remaining text
        lines.append(current_line)

    return lines

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(back, (0, 0))
    print_text1("Learn", 70, 70)
    # Updated text with newlines inserted
    text = (
        "Quantum entanglement:"
        "Let’s say two entangled particles A and B are traveling in opposite directions. "
        "B meets a new particle C, now B and C create a new entangled space. "
        "The properties of C are transferred, almost “teleported” over to A."  
        "Quantum memory:"
        "Quantum memory refers to a physical system or device that can store and retrieve quantum information in the form of quantum states."
        "Quantum repeaters:"
        "They are devices designed to extend the range of entanglement distribution in quantum communication networks."
    )
    draw_screen(text)
    #draw_screen(" Quantum  entanglement:Let’s say two entangled particles A and B are traveling in opposite directions. B meets a new particle C, now B and C create a new entangled space. The properties of C        are transferred, almost “teleported” over to A. Quantum memory:Quantum memory refers to a physical system or device that can store and retrieve quantum information in the form of quantum states. Quantum repeaters: They are devices designed to extend the range of entanglement distribution in quantum communication networks.")

    pygame.display.flip()

pygame.quit()
