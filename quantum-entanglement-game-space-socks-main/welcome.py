
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

# Function to print text at specified positions with custom font size
def print_text1(text, font_size, ypos):
    font = pygame.font.SysFont('monospace', font_size, bold=True)
    color = (255, 255, 255)
    text_surface = font.render(text, True, color)

    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, ypos))
    screen.blit(text_surface, text_rect)

def print_text2(text, font_size, ypos):
    font = pygame.font.SysFont('monospace', font_size, bold=True)
    color = (0,0,0)
    text_surface = font.render(text, True, color)

    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, ypos))
    screen.blit(text_surface, text_rect)

satellite = pygame.image.load(satellitep)
satellite_radius = 200  # Adjust this for how far the satellite is from the center of the Earth
satellite_angle1 = 0     # Initial angle for the satellite's orbit
satellite1 = pygame.transform.scale(satellite, (70, 70))
satellite_speed1 = 0.01

satellite_angle2 = 10     # Initial angle for the satellite's orbit
satellite_speed2 = 0.02
satellite2 = pygame.transform.scale(satellite, (60, 60))

satellite_angle3 = 0     # Initial angle for the satellite's orbit
satellite_speed3 = 0.04
satellite3 = pygame.transform.scale(satellite, (80, 80))

# Load sock images
redsockp = os.path.join(base_dir, 'pics', 'redsock-pic.png')
redsock = pygame.image.load(redsockp)
redsock = pygame.transform.scale(redsock, (80, 100))

yellowsockp = os.path.join(base_dir, 'pics', 'yellowsock-pic (1).png')
yellowsock = pygame.image.load(yellowsockp)
yellowsock = pygame.transform.scale(yellowsock, (80, 100))

# Initialize sock properties
num_socks = 6
sock_positions = []
sock_speeds = []
sock_angles = []
sock_images = []

# Initialize socks (3 red and 3 yellow)
for i in range(num_socks):
    # Random initial position for each sock
    x = random.randint(50, 950)
    y = random.randint(50, 600)
    
    # Random angle and speed for each sock
    angle = random.uniform(0, 360)
    speed = random.uniform(1, 3)  # Random speed for each sock (ensures no zero speed)
    
    sock_positions.append([x, y])
    sock_speeds.append(speed)
    sock_angles.append(angle)
    
    # Assign red for first 3 and yellow for next 3
    if i < 3:
        sock_images.append(redsock)
    else:
        sock_images.append(yellowsock)

# Function to update and draw the socks
def update_and_draw_socks():
    for i in range(num_socks):
        # Update sock position based on speed and angle
        sock_positions[i][0] += int(sock_speeds[i] * math.cos(math.radians(sock_angles[i])))
        sock_positions[i][1] += int(sock_speeds[i] * math.sin(math.radians(sock_angles[i])))
        
        # Wrap the socks around the screen
        if sock_positions[i][0] > 1000:
            sock_positions[i][0] = 0
        if sock_positions[i][0] < 0:
            sock_positions[i][0] = 1000
        if sock_positions[i][1] > 650:
            sock_positions[i][1] = 0
        if sock_positions[i][1] < 0:
            sock_positions[i][1] = 650
        
        # Draw sock on screen
        screen.blit(sock_images[i], (sock_positions[i][0], sock_positions[i][1]))

def is_mouse_over_button(mfouse_pos, button_rect):
    return button_rect.collidepoint(mouse_pos)

def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    print_text2(text, 30, y + height // 2)

def launch_external_script():
    game_path = os.path.join(base_dir, 'quantum_game.py')
    try:
        subprocess.run(["python", game_path])
    except Exception as e:
        print(f"Failed to launch the game: {e}")

def launch_learn():
    course_path = os.path.join(base_dir, 'courses.py')
    try:
        subprocess.run(["python", course_path])
    except Exception as e:
        print(f"Failed to launch courses: {e}")

running = True
while running:
    
    satellite_x1 = 560 + int(satellite_radius * math.cos(math.radians(satellite_angle1)))
    satellite_y1 = 212 + int(satellite_radius * math.sin(math.radians(satellite_angle1)))
    satellite_angle1 += satellite_speed1

    satellite_x2 = 60 + int((satellite_radius+350) * math.cos(math.radians(satellite_angle2)))
    satellite_y2 = 112 + int((satellite_radius+350) * math.sin(math.radians(satellite_angle2)))
    satellite_angle2 += satellite_speed2

    satellite_x3 = 100 + int(satellite_radius * math.cos(math.radians(satellite_angle3)))
    satellite_y3 = 512 + int(satellite_radius * math.sin(math.radians(satellite_angle3)))
    satellite_angle3 -= satellite_speed3
    
    # Draw background, satellites, and socks
    screen.blit(back, (0, 0))
    print_text1("Space Socks", 100, 100)  # Title
    draw_button("Play Game", 400, 300, 200, 50, (0, 255, 0))  
    draw_button("Quit", 400, 400, 200, 50, (255, 0, 0)) 
    draw_button("Learn", 400, 500, 200, 50, (160, 32, 240)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            # Check if "Play Game" button is clicked
            if is_mouse_over_button(mouse_pos, pygame.Rect(400, 300, 200, 50)):
                pygame.mixer.music.stop()
                launch_external_script()

            # Check if "Quit" button is clicked
            elif is_mouse_over_button(mouse_pos, pygame.Rect(400, 400, 200, 50)):
                running = False
            
            elif is_mouse_over_button(mouse_pos,pygame.Rect(400,500,200,50)):
                pygame.mixer.music.stop()
                launch_learn()


    screen.blit(satellite1, (satellite_x1, satellite_y1))
    screen.blit(satellite2, (satellite_x2, satellite_y2))
    screen.blit(satellite3, (satellite_x3, satellite_y3))
    
    # Update and draw the socks
    update_and_draw_socks()
    
    pygame.display.flip()

pygame.quit()
