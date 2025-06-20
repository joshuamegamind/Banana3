import pygame

import random

import math

import sys

import json

pygame.mixer.init()
 

# Initialize

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Banana Split!")

pygame.display.set_icon(pygame.image.load("banana.png"))

clock = pygame.time.Clock()

 

# Colors
HEALTH_RED = 100, 0, 0

HEALTH_GREEN = 0, 255, 0

WHITE = (255, 255, 255)

START_COLOR = (25, 250, 25)

SELECTED_COLOR = (10, 10, 235)

UPGRADE_COLOR = (75, 200, 25)

DARK_GRAY = (100, 100, 100)

GRAY = (150, 150, 150)

BLACK = (0,0,0)

GOLD = (255, 233, 0)

ORANGE = (255, 165, 0)

SKY_BLUE = (135, 206, 235)

RED = (255, 0, 0)


 

HEALTH_BAR_SIZE = (200, 30)

HEALTH_BAR_POS = (20,20)


# Fonts

title_font = pygame.font.SysFont('Ariel', 150)

main_font = pygame.font.SysFont('Corbel', 100)

small_font = pygame.font.SysFont('Corbel', 50)

money_font = pygame.font.SysFont('Corbel', 35)

gulp_font = pygame.font.SysFont('Corbel', 40)

prestige_font = pygame.font.SysFont('Corbel', 55)

 

# Images

title_Img = pygame.transform.scale(pygame.image.load("Banansplit.png"), (500, 250))

background = pygame.image.load("background.png")

player_img = pygame.transform.scale(pygame.image.load("player.png"), (64, 64))

enemy_img = pygame.transform.scale(pygame.image.load("enemy2.png"), (64, 64))

enemy2_img = pygame.transform.scale(pygame.image.load("enemy.png"), (64, 64))

banana_img = pygame.transform.scale(pygame.image.load("BananaIMG.png"), (64, 64))

hat_player = pygame.transform.scale(pygame.image.load("hat.png"), (64, 64))

hatN_player = pygame.transform.scale(pygame.image.load("hat.png"), (100, 100))

hatPWR_original = pygame.image.load("hat_power.png").convert_alpha()

shades_player = pygame.transform.scale(pygame.image.load("cool_shades.png"), (50, 50))
shadesN_player = pygame.transform.scale(pygame.image.load("cool_shades.png"), (120, 120))




#Power Variables

angle = 0
scale = 0.1
visibleP = False
max_scale = 1

cooldown1 = 0

cooldown1_duration = 10000

last_used_time = -cooldown1_duration

power_rect = hatPWR_original.get_rect(center=(400, 300))


cool_shades_rect = shades_player.get_rect(center=(400, 300))

cool_shades_active = False
cool_shades_duration = 5000  # 5 seconds
cool_shades_cooldown = 12000  # 12 seconds
last_cool_shades_use = -cool_shades_cooldown
cool_shades_start_time = 0



#Sound Effects

banana_sound = pygame.mixer.Sound('banana_sound.wav')

explosion = pygame.mixer.Sound('enemy_death.wav')

menu_music = pygame.mixer.Sound('menu_music.wav')

game_music = pygame.mixer.Sound('game_music.wav')

upgrade_sound = pygame.mixer.Sound('upgrade_sound.wav')
 

 

# Game Variables

camera_offset_y = 0

scroll_offset = 0
 

playerX, playerY = 350, 240

player_speed = 4

player_rect = pygame.Rect(playerX + 20, playerY + 20, 60, 60)

last_damage_time = 0  # Add this near the other global variables

damage_cooldown = 1000  # 1 second




prestige1 = False


 

MAX_ENEMIES = 1

MAX_ENEMIES2 = 0

FORBIDDEN_DISTANCE = 350

MAX_BANANAS = 1

score = 0

money_score = 50

passive_income_upgrade = 0

wave = 0

banana_ONSCREEN = 0

 

last_income_time = 0

income_interval = 1000  # every 3 seconds

passive_income_amount = 1

 

multiplier = 1




max_health = 2



# Buttons

start_btn = pygame.Rect(215, 285, 375, 120)

save_btn = pygame.Rect(600, 520, 300, 75)

load_btn = pygame.Rect(-100, 520, 300, 75)

upgrade_btn = pygame.Rect(250, 420, 300, 75)

restart_btn = pygame.Rect(200, 200, 400, 150)

menu_btn = pygame.Rect(200, 415, 400, 125)

cosmetics_btn = pygame.Rect(-30, 250, 150, 80)

cos_surface = pygame.Rect(50, 200, 700, 400)


upgrade_node1_btn = pygame.Rect(250, 50, 300, 100)

upgrade_nodeM_btn = pygame.Rect(460, 250, 300, 100)

upgrade_node2_btn = pygame.Rect(60, 250, 300, 100)

upgrade_node3_btn = pygame.Rect(60, 400, 300, 100)

upgrade_node4_btn = pygame.Rect(60, 550, 300, 100)

upgrade_node5_btn = pygame.Rect(60, 700, 300, 100)

upgrade_node6_btn = pygame.Rect(60, 1000, 300, 100)

upgrade_nodeM2_btn = pygame.Rect(460, 400, 300, 100)

upgrade_nodeM3_btn = pygame.Rect(460, 550, 300, 100)

upgrade_nodeM4_btn = pygame.Rect(460, 700, 300, 100)

upgrade_nodeM5_btn = pygame.Rect(460, 1000, 300, 100)

prestige_node_btn = pygame.Rect(250, 825, 300, 100)

upgrade_nodeEXT_btn = pygame.Rect(50, 50, 100, 75)

upgrade_nodeEXT_btn2 = pygame.Rect(10, 10, 100, 75)


cosmetic_node1_btn = pygame.Rect(75, 225, 200, 150)
cosmetic_node2_btn = pygame.Rect(290, 225, 200, 150)

 

# Game State

current_screen = "start"

enemies = []

enemies2 = []

bananas = []

playerX_change = 0

playerY_change = 0

player_health = max_health

game_over = False

node1_selected = False

node2_selected = False

node3_selected = False

node4_selected = False

node5_selected = False

node6_selected = False

nodeM_selected = False

nodeM2_selected = False

nodeM3_selected = False

nodeM4_selected = False

nodeM5_selected = False

cosmetic1_selected = False

cosmetic2_selected = False




 

def apply_upgrades():

    global MAX_BANANAS, player_speed, multiplier, nodeM_selected, node3_selected, node2_selected, node4_selected, node5_selected, nodeM3_selected, nodeM4_selected, cosmetic1_selected

    MAX_BANANAS = 1

    if node2_selected:

        MAX_BANANAS = 2

    if node6_selected:

        MAX_BANANAS = 4

    player_speed = 4

    if node3_selected:

        player_speed +=1

    multiplier = 1

    if nodeM_selected:

        multiplier = 2

    if nodeM2_selected:

        multiplier = 3

    if node4_selected:

        player_health = max_health

    if node5_selected:

        score_multiplier = 2


    if nodeM3_selected:

        multiplier = 4

    if nodeM4_selected:

        multiplier = 5

    if nodeM5_selected:

        multiplier = 10




 

 

def reset_game():

    global playerX, playerY, playerX_change, playerY_change, bananas, enemies, enemies2, score, game_over, MAX_ENEMIES, wave, banana_ONSCREEN, player_health, MAX_ENEMIES2, scale, angle, max_scale, hatPWR, hatPWR_player

    playerX, playerY = 350, 240

    playerX_change = 0

    playerY_change = 0

    bananas = []

    enemies = [spawn_enemy()]

    enemies2 = [spawn_enemy2()]

    score = 0

    wave = 1

    MAX_ENEMIES = 1

    MAX_ENEMIES2 = 0

    game_over = False

    banana_ONSCREEN = len(bananas)

    player_health = max_health

    

 

def spawn_enemy():

    while True:

        x = random.randint(0, WIDTH)

        y = random.randint(0, HEIGHT)

        if math.hypot(playerX - x, playerY - y) > FORBIDDEN_DISTANCE:

            return {

                "x": x,

                "y": y,

                "visible": True,

            }

def spawn_enemy2():

    while True:

        x = random.randint(0, WIDTH)

        y = random.randint(0, HEIGHT)

        if math.hypot(playerX - x, playerY - y) > FORBIDDEN_DISTANCE:

            return {

                "x": x,

                "y": y,

                "visible2": True,

                "health2": 1

            }

 

 

def draw_text(text, font, color, x, y, surface=screen):

    rendered_text = font.render(text, True, color)

    surface.blit(rendered_text, (x, y))

 

 

def start_screen():

    global current_screen, money_score, last_income_time, node2_selected, cosmetic2_selected, node1_selected, nodeM4_selected, node6_selected, multiplier, nodeM_selected, node3_selected, nodeM2_selected, node4_selected, node5_selected, nodeM3_selected, prestige1, cosmetic1_selected

    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, START_COLOR, start_btn, border_radius=30)

    pygame.draw.rect(screen, ORANGE, cosmetics_btn, border_radius=30)

    screen.blit(hat_player, (40, 255))


    menu_music.play(-1)
    game_music.stop()

    pygame.draw.rect(screen, DARK_GRAY, save_btn, border_radius=30)

    draw_text("SAVE", small_font, WHITE, save_btn.x + 20, save_btn.y + 20)

 

    pygame.draw.rect(screen, DARK_GRAY, load_btn, border_radius=30)

    draw_text("LOAD", small_font, WHITE, load_btn.x + 150, load_btn.y + 20)

 

    screen.blit(title_Img, (160, 25))

 

    draw_text("START", main_font, WHITE, 265, 300)

 

    if node1_selected:

        current_time = pygame.time.get_ticks()

        if current_time - last_income_time > income_interval:

                money_score += passive_income_amount * multiplier

                last_income_time = current_time

 

    pygame.draw.rect(screen, UPGRADE_COLOR, upgrade_btn, border_radius=30)

    draw_text("UPGRADES", small_font, WHITE, 286, 435)

 

    pygame.display.update()

 

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if start_btn.collidepoint(event.pos):

                current_screen = "game"

                reset_game()

            if upgrade_btn.collidepoint(event.pos):

                current_screen = "upgrade"

            if cosmetics_btn.collidepoint(event.pos):

                current_screen = "cosmetics"

            if save_btn.collidepoint(event.pos):  # Save game state

                game_state = {

                    'money_score': money_score,

                    'node1_selected': node1_selected,

                    'node2_selected': node2_selected,

                    'nodeM_selected': nodeM_selected,

                    'node3_selected': node3_selected,

                    'nodeM2_selected': nodeM2_selected,

                    'nodeM3_selected': nodeM3_selected,

                    'node4_selected': node4_selected,

                    'node5_selected': node5_selected,

                    'prestige1': prestige1,

                    'nodeM4_selected': nodeM4_selected,

                    'node6_selected': node6_selected,

                    'cosmetic1_selected': cosmetic1_selected,

                    'cosmetic2_selected': cosmetic2_selected,

                }

                with open('save.json', 'w') as f:

                    json.dump(game_state, f)

 

            if load_btn.collidepoint(event.pos):  # Load game state

                with open('save.json', 'r') as f:

                    game_state = json.load(f)

                    money_score = game_state['money_score']

                    node1_selected = game_state['node1_selected']

                    node2_selected = game_state['node2_selected']

                    nodeM_selected = game_state['nodeM_selected']

                    node3_selected = game_state['node3_selected']  

                    nodeM2_selected = game_state['nodeM2_selected']

                    nodeM3_selected = game_state['nodeM3_selected']

                    node5_selected = game_state['node5_selected']

                    node6_selected = game_state['node6_selected']

                    node4_selected = game_state['node4_selected']

                    prestige1 = game_state['prestige1']

                    nodeM4_selected = game_state['nodeM4_selected']

                    node6_selected = game_state['node6_selected']

                    cosmetic1_selected = game_state['cosmetic1_selected']

                    cosmetic2_selected = game_state['cosmetic2_selected']

                    apply_upgrades()

 

def upgrade_screen():

    global prestige1, max_health, player_health, btnEXT_rect, upgrade_nodeEXT_btn, nodeM5_selected, node1_selected, node6_selected, node2_selected, node3_selected, node5_selected, nodeM3_selected, nodeM4_selected, current_screen, MAX_BANANAS, money_score, last_income_time, camera_offset_y, nodeM_selected, multiplier, player_speed, nodeM_selected, nodeM2_selected, node4_selected

 

    screen.fill((0, 0, 0))

 

    # Surface for scrolling

    upgrade_surface = pygame.Surface((WIDTH, 1000))

    for y in range(0, 1000, HEIGHT):

        upgrade_surface.blit(background, (0, y))

    # Copy buttons and adjust for scrolling

    btn1_rect = upgrade_node1_btn.move(0, -camera_offset_y)

    btnM_rect = upgrade_nodeM_btn.move(0, -camera_offset_y)

    btnM2_rect = upgrade_nodeM2_btn.move(0, -camera_offset_y)

    btnM3_rect = upgrade_nodeM3_btn.move(0, -camera_offset_y)

    btnM4_rect = upgrade_nodeM4_btn.move(0, -camera_offset_y)

    btnM5_rect = upgrade_nodeM5_btn.move(0, -camera_offset_y)

    btn2_rect = upgrade_node2_btn.move(0, -camera_offset_y)

    btn3_rect = upgrade_node3_btn.move(0, -camera_offset_y)

    btn4_rect = upgrade_node4_btn.move(0, -camera_offset_y)

    btn5_rect = upgrade_node5_btn.move(0, -camera_offset_y)

    btn6_rect = upgrade_node6_btn.move(0, -camera_offset_y)
 
    btnpres_rect = prestige_node_btn.move(0, -camera_offset_y)

    btnEXT_rect = upgrade_nodeEXT_btn.move(0, -camera_offset_y)
 

    # Background box

    pygame.draw.rect(upgrade_surface, WHITE, [30, 20, 750, 950], border_radius=30)

    pygame.draw.rect(upgrade_surface, RED, btnEXT_rect, border_radius=30)

    draw_text("ESC", small_font, WHITE, btnEXT_rect.x + 9, btnEXT_rect.y + 15, upgrade_surface)



   
    

    # Connector line

    pygame.draw.line(upgrade_surface, BLACK, btn1_rect.center, btn2_rect.center, 5)

 

    pygame.draw.line(upgrade_surface, BLACK, btn2_rect.center, btn3_rect.center, 5)

 

    pygame.draw.line(upgrade_surface, BLACK, btn1_rect.center, btnM_rect.center, 5)

    

    pygame.draw.line(upgrade_surface, BLACK, btnM_rect.center, btnM2_rect.center, 5)


    pygame.draw.line(upgrade_surface, BLACK, btnM2_rect.center, btnM3_rect.center, 5)


    pygame.draw.line(upgrade_surface, BLACK, btnM3_rect.center, btnM4_rect.center, 5)


    pygame.draw.line(upgrade_surface, BLACK, btn4_rect.center, btn3_rect.center, 5)


    pygame.draw.line(upgrade_surface, BLACK, btn5_rect.center, btn4_rect.center, 5)





    pres_pos1 = (0, btn6_rect.y - 50)
    pres_pos2 = (WIDTH, btn6_rect.y - 50)
    #PRESTIGE LINE
    pygame.draw.line(upgrade_surface, GOLD, pres_pos1, pres_pos2, 5)



    pygame.draw.line(upgrade_surface, BLACK, btn6_rect.center, btn5_rect.center, 5)

    pygame.draw.line(upgrade_surface, BLACK, btnM5_rect.center, btnM4_rect.center, 5)


    # Node 1: Passive Income

    pygame.draw.rect(upgrade_surface, SELECTED_COLOR if node1_selected else START_COLOR, btn1_rect, border_radius=30)

    draw_text("Passive Income", gulp_font, WHITE, btn1_rect.x + 30, btn1_rect.y + 20, upgrade_surface)

    draw_text("$50", money_font, WHITE, btn1_rect.x + 125, btn1_rect.y + 60, upgrade_surface)

 

    color2 = SELECTED_COLOR if node2_selected else START_COLOR

    colorM = SELECTED_COLOR if nodeM_selected else START_COLOR

    colorM2 = SELECTED_COLOR if nodeM2_selected else START_COLOR

    colorM3 = SELECTED_COLOR if nodeM3_selected else START_COLOR

    colorM4 = SELECTED_COLOR if nodeM4_selected else START_COLOR

    color5 = SELECTED_COLOR if node5_selected else START_COLOR

    if prestige1:
        if node5_selected:
            color6 = SELECTED_COLOR if node6_selected else START_COLOR
        else:
            color6 = DARK_GRAY
    else:
        color6 = GOLD
    
    if prestige1:
        if nodeM4_selected:
            colorM5 = SELECTED_COLOR if nodeM5_selected else START_COLOR
        else:
            colorM5 = DARK_GRAY
    else:
        colorM5 = GOLD

    #Node Multiplier

    if node1_selected:

        pygame.draw.rect(upgrade_surface, colorM, btnM_rect, border_radius=30)

    else:

        pygame.draw.rect(upgrade_surface, DARK_GRAY, btnM_rect, border_radius=30)

    draw_text("Multiplier x2", gulp_font, WHITE, btnM_rect.x + 42.5, btnM_rect.y + 20, upgrade_surface)

    draw_text("$100", money_font, WHITE, btnM_rect.x + 125, btnM_rect.y + 60, upgrade_surface)

    if nodeM_selected:

        pygame.draw.rect(upgrade_surface, colorM2, btnM2_rect, border_radius=30)

    else:

        pygame.draw.rect(upgrade_surface, DARK_GRAY, btnM2_rect, border_radius=30)

    draw_text("Multiplier x3", gulp_font, WHITE, btnM2_rect.x + 42.5, btnM2_rect.y + 20, upgrade_surface)

    draw_text("$150", money_font, WHITE, btnM2_rect.x + 125, btnM2_rect.y + 60, upgrade_surface)


    if nodeM2_selected:

        pygame.draw.rect(upgrade_surface, colorM3, btnM3_rect, border_radius=30)

    else:

        pygame.draw.rect(upgrade_surface, DARK_GRAY, btnM3_rect, border_radius=30)

    draw_text("Multiplier x4", gulp_font, WHITE, btnM3_rect.x + 42.5, btnM3_rect.y + 20, upgrade_surface)

    draw_text("$200", money_font, WHITE, btnM3_rect.x + 125, btnM3_rect.y + 60, upgrade_surface)

    if nodeM3_selected:

        pygame.draw.rect(upgrade_surface, colorM4, btnM4_rect, border_radius=30)

    else:

        pygame.draw.rect(upgrade_surface, DARK_GRAY, btnM4_rect, border_radius=30)

    draw_text("Multiplier x5", gulp_font, WHITE, btnM4_rect.x + 42.5, btnM4_rect.y + 20, upgrade_surface)

    draw_text("$250", money_font, WHITE, btnM4_rect.x + 125, btnM4_rect.y + 60, upgrade_surface)




    

    # Node 2: +1 Bananas

    if node1_selected:

        pygame.draw.rect(upgrade_surface, color2, btn2_rect, border_radius=30)

    else:

        pygame.draw.rect(upgrade_surface, DARK_GRAY, btn2_rect, border_radius=30)

    draw_text("+1 BANANAS", small_font, WHITE, btn2_rect.x + 20, btn2_rect.y + 20, upgrade_surface)

    draw_text("$100", money_font, WHITE, btn2_rect.x + 120, btn2_rect.y + 60, upgrade_surface)

 

 

    color3 = SELECTED_COLOR if node3_selected else START_COLOR

    if node2_selected:
        pygame.draw.rect(upgrade_surface, color3, btn3_rect, border_radius=30)
    else:
        pygame.draw.rect(upgrade_surface, DARK_GRAY, btn3_rect, border_radius=30)



    draw_text("+1 SPEED", small_font, WHITE, btn3_rect.x + 50, btn3_rect.y + 20, upgrade_surface)

    draw_text("$150", money_font, WHITE, btn3_rect.x + 120, btn3_rect.y + 60, upgrade_surface)


    color4 = SELECTED_COLOR if node4_selected else START_COLOR

    if node3_selected:
        pygame.draw.rect(upgrade_surface, color4, btn4_rect, border_radius=30)
    else:
        pygame.draw.rect(upgrade_surface, DARK_GRAY, btn4_rect, border_radius=30)



    draw_text("+2 HEALTH", small_font, WHITE, btn4_rect.x + 50, btn4_rect.y + 20, upgrade_surface)

    draw_text("$250", money_font, WHITE, btn4_rect.x + 120, btn4_rect.y + 60, upgrade_surface)


    if node4_selected:
        pygame.draw.rect(upgrade_surface, color5, btn5_rect, border_radius=30)
    else:
        pygame.draw.rect(upgrade_surface, DARK_GRAY, btn5_rect, border_radius=30)

    draw_text("x2 SCORE", small_font, WHITE, btn5_rect.x + 50, btn5_rect.y + 20, upgrade_surface)

    draw_text("$300", money_font, WHITE, btn5_rect.x + 120, btn5_rect.y + 60, upgrade_surface)

    if node5_selected:
        pygame.draw.rect(upgrade_surface, color6, btn6_rect, border_radius=30)
    else:
        pygame.draw.rect(upgrade_surface, color6, btn6_rect, border_radius=30)

    draw_text("+2 BANANAS", small_font, WHITE, btn6_rect.x + 10, btn6_rect.y + 20, upgrade_surface)

    draw_text("$500", money_font, WHITE, btn6_rect.x + 110, btn6_rect.y + 55, upgrade_surface)

    if nodeM4_selected:

        pygame.draw.rect(upgrade_surface, colorM5, btnM5_rect, border_radius=30)

    else:

        pygame.draw.rect(upgrade_surface, colorM5, btnM5_rect, border_radius=30)

    draw_text("Multiplier x10", gulp_font, WHITE, btnM5_rect.x + 42.5, btnM5_rect.y + 20, upgrade_surface)

    draw_text("$600", money_font, WHITE, btnM5_rect.x + 125, btnM5_rect.y + 60, upgrade_surface)






    if prestige1:
        pygame.draw.rect(upgrade_surface, GOLD, btnpres_rect, border_radius=30)
        draw_text("PRESTIGED!", prestige_font, WHITE, btnpres_rect.x + 20, btnpres_rect.y + 30, upgrade_surface)
    else:
        pygame.draw.rect(upgrade_surface, GOLD, btnpres_rect, border_radius=30)
        draw_text("PRESTIGE", small_font, WHITE, btnpres_rect.x + 50, btnpres_rect.y + 10, upgrade_surface)
        draw_text("$750", small_font, WHITE, btnpres_rect.x + 100, btnpres_rect.y + 45, upgrade_surface)

    # Display money

    draw_text(f"${round(money_score, 1)}", small_font, BLACK, 600, 25, upgrade_surface)

 

    # Apply passive income

    if node1_selected:

        current_time = pygame.time.get_ticks()

        if current_time - last_income_time > income_interval:

            money_score += passive_income_amount * multiplier

            last_income_time = current_time

 

    # Blit upgrade surface at camera offset

    screen.blit(upgrade_surface, (0, -camera_offset_y))

    pygame.display.update()

 

    # Handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_screen = "start"
                print("gub")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # --- Handle Scroll ---
            if event.button == 4:  # Scroll up
                camera_offset_y = max(camera_offset_y - 30, 0)
            elif event.button == 5:  # Scroll down
                camera_offset_y += 30

            # --- Handle Clicks ---
            elif event.button == 1:
                adjusted_mouse_pos = (event.pos[0], event.pos[1] + camera_offset_y)

                if btn1_rect.collidepoint(adjusted_mouse_pos):
                    if not node1_selected and money_score >= 50:
                        node1_selected = True
                        money_score -= 50
                        last_income_time = pygame.time.get_ticks()

                elif node1_selected and btn2_rect.collidepoint(adjusted_mouse_pos):
                    if not node2_selected and money_score >= 100:
                        node2_selected = True
                        MAX_BANANAS = 2
                        money_score -= 100

                elif node2_selected and btn3_rect.collidepoint(adjusted_mouse_pos):
                    if not node3_selected and money_score >= 150:
                        node3_selected = True
                        player_speed += 1
                        money_score -= 150

                elif node1_selected and btnM_rect.collidepoint(adjusted_mouse_pos):
                    if not nodeM_selected and money_score >= 100:
                        nodeM_selected = True
                        multiplier = 2
                        money_score -= 100

                elif nodeM_selected and btnM2_rect.collidepoint(adjusted_mouse_pos):
                    if not nodeM2_selected and money_score >= 150:
                        nodeM2_selected = True
                        multiplier = 3
                        money_score -= 150

                elif nodeM2_selected and btnM3_rect.collidepoint(adjusted_mouse_pos):
                    if not nodeM3_selected and money_score >= 200:
                        nodeM3_selected = True
                        multiplier = 4
                        money_score -= 200

                elif nodeM3_selected and btnM4_rect.collidepoint(adjusted_mouse_pos):
                    if not nodeM4_selected and money_score >= 250:
                        nodeM4_selected = True
                        multiplier = 5
                        money_score -= 250

                elif node3_selected and not node4_selected and btn4_rect.collidepoint(adjusted_mouse_pos):
                    if money_score >= 300:
                        node4_selected = True
                        max_health = 4
                        player_health = max_health
                        money_score -= 300

                elif node4_selected and not node5_selected and btn5_rect.collidepoint(adjusted_mouse_pos):
                    if money_score >= 350:
                        node5_selected = True
                        score_multiplier = 2
                        money_score -= 350

                elif node5_selected and btn6_rect.collidepoint(adjusted_mouse_pos):
                    if not node6_selected and prestige1 and money_score >= 500:
                        node6_selected = True
                        MAX_BANANAS += 2
                        money_score -= 500

                elif nodeM4_selected and btnM5_rect.collidepoint(adjusted_mouse_pos):
                    if not nodeM5_selected and prestige1 and money_score >= 600:
                        nodeM5_selected = True
                        multiplier = 10
                        money_score -= 600


                elif not prestige1 and btnpres_rect.collidepoint(adjusted_mouse_pos) and money_score >= 750:
                        prestige1 = True

                        node1_selected = False

                        node2_selected = False
                        node3_selected = False
                        node4_selected = False
                        node5_selected = False
                        node6_selected = False
                        nodeM3_selected = False
                        nodeM4_selected = False
                        nodeM2_selected = False
                        nodeM_selected = False
                        cosmetic1_selected = False
                        cosmetic2_selected = False

                        #bullet banana
                        money_score -= money_score

        

 

 

 
def cosmetics_screen():

    global current_screen, cosmetics_btn, cosmetic_node1_btn, node2_selected, cosmetic1_selected, screen, cos_surface, money_score, cosmetic2_selected, cosmetic_node2_btn, last_income_time, upgrade_nodeEXT_btn2

    screen.blit(background, (0,0))
    keys = pygame.key.get_pressed()

    draw_text("COSMETICS", title_font, WHITE, 100, 50)

    btnEXT_rect = upgrade_nodeEXT_btn2
    
    pygame.draw.rect(screen, WHITE, cos_surface, border_radius=30)

    color_cos1 = SELECTED_COLOR if cosmetic1_selected else ORANGE

    color_cos2 = SELECTED_COLOR if cosmetic2_selected else ORANGE

    pygame.draw.rect(screen, color_cos1, cosmetic_node1_btn, border_radius=30)

    pygame.draw.rect(screen, color_cos2, cosmetic_node2_btn, border_radius=30)

    pygame.draw.rect(screen, RED, btnEXT_rect, border_radius=30)

    draw_text("ESC", small_font, WHITE, btnEXT_rect.x + 9, btnEXT_rect.y + 15, screen)



    draw_text("$500", small_font, WHITE, cos_surface.x + 75, cos_surface.y + 120)

    draw_text("$300", small_font, WHITE, cos_surface.x + 300, cos_surface.y + 120)

    screen.blit(hatN_player, (cos_surface.x + 75, cos_surface.y + 30))

    screen.blit(shadesN_player, (cos_surface.x + 290, cos_surface.y + 30))

    if node1_selected:

        current_time = pygame.time.get_ticks()

        if current_time - last_income_time > income_interval:

                money_score += passive_income_amount * multiplier

                last_income_time = current_time

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if cosmetic_node1_btn.collidepoint(event.pos) and money_score >= 500:

                    cosmetic1_selected = True

                    money_score -= 500

                if cosmetic_node2_btn.collidepoint(event.pos) and money_score >= 300:

                    cosmetic2_selected = True

                    money_score -= 300

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_screen = "start"
                print("gub")

            
  

    pygame.display.update()


 

def game_loop():

    global enemy_rect, last_cool_shades_use, cool_shades_active, cool_shades_cooldown, cool_shades_duration, cool_shades_start_time, enemy, enemy2, playerX, playerY, playerX_change, power_rect, power2_rect, visibleP2, last_used_time2, score_multiplier, playerY_change, game_over, hatPWR, last_used_time, scale, max_scale, angle, hatPWR_player, visibleP, current_screen, score, enemies, enemies2, spawn_enemy2, bananas, MAX_ENEMIES, MAX_ENEMIES2, wave, speed, banana_ONSCREEN, money_score, last_income_time, spawn_enemy, multiplier, player_health, last_damage_time, damage_cooldown

    if current_screen == "game_over_screen":
        game_over_screen()

    keys = pygame.key.get_pressed()

    playerX += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    playerY += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    playerX = max(-26, min(730, playerX))

    playerY = max(0, min(516, playerY))

    player_rect.topleft = (playerX + 20, playerY + 20)

    current_time = pygame.time.get_ticks()
    on_cooldown = current_time - last_used_time < cooldown1_duration
    on_cooldown2 = current_time - last_cool_shades_use < cool_shades_cooldown
    colorPWR = DARK_GRAY if on_cooldown else WHITE
    colorPWR2 = DARK_GRAY if on_cooldown2 else WHITE
    
    space_rect = (280, 510, 400, 80)

    pygame.draw.rect(screen, DARK_GRAY, space_rect, border_radius=10)


    if node5_selected:
        score_multiplier = 2
    else:
        score_multiplier = 1
    




    z_rect = (20, 490, 100, 100)

    if cosmetic1_selected:
        x_rect = (145, 490, 100, 100)
    else:
        x_rect = (20, 490, 100, 100)


   

    screen.blit(background, (0, 0))

    if cosmetic1_selected:

        pygame.draw.rect(screen, colorPWR, z_rect, border_radius=30)

        draw_text("Z", main_font, BLACK, 40, 495)

    if cosmetic2_selected:

        pygame.draw.rect(screen, colorPWR2, x_rect, border_radius=30)

        if cosmetic1_selected:
            draw_text("X", main_font, BLACK, 165, 495)

        else:
            draw_text("X", main_font, BLACK, 40, 495)



        
    time_slow_screen = False

    
    
    apply_upgrades()

    menu_music.stop()
    game_music.play()


    pygame.draw.rect(screen, DARK_GRAY, space_rect, border_radius=30)


    draw_text("SPACE", small_font, WHITE, 420, 535)

    if node1_selected:

        current_time = pygame.time.get_ticks()

        if current_time - last_income_time > income_interval:

                money_score += passive_income_amount * multiplier

                last_income_time = current_time

 

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

            if len(bananas) >= MAX_BANANAS:

                bananas.pop(0)

            bananas.append((playerX, playerY + 20))

            banana_ONSCREEN = len(bananas)


        pygame.transform.scale(hatPWR_original, (int(WIDTH * scale), int(HEIGHT * scale)))

        power_rect = hatPWR_original.get_rect(center=(400, 300))

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_z:

                current_time = pygame.time.get_ticks()
                if cosmetic1_selected and current_time - last_used_time >= cooldown1_duration:
                    visibleP = True
                    last_used_time = current_time
                    score += 5

            elif event.key == pygame.K_x:
                current_time = pygame.time.get_ticks()
                if current_time - last_cool_shades_use >= cool_shades_cooldown:
                    last_cool_shades_use = current_time
                    cool_shades_active = True
                    cool_shades_start_time = current_time


    if visibleP:
        angle += 2  # Adjust rotation speed if desired
        scale += 0.02  # Adjust scale speed if desired

    # Apply scaling and rotation
        transformed = pygame.transform.rotozoom(hatPWR_original, angle, scale)

        for enemy in enemies:
            enemy["visible"] = False
        for enemy2 in enemies2:
            enemy["visible2"] = False



    # Get new rect centered on screen
        transformed_rect = transformed.get_rect(center=(400, 300))

        screen.blit(transformed, transformed_rect)

        if scale >= max_scale:
            visibleP = False
            scale = 0.1  # Reset scale for next use
            angle = 0  # Reset angle if needed

 

    # Background

    

    


    pygame.draw.rect(screen, HEALTH_RED, (*HEALTH_BAR_POS, *HEALTH_BAR_SIZE))

    health_width = int((player_health / max_health) * HEALTH_BAR_SIZE[0])

    pygame.draw.rect(screen, HEALTH_GREEN, (HEALTH_BAR_POS[0], HEALTH_BAR_POS[1], health_width, HEALTH_BAR_SIZE[1]))

    pygame.draw.rect(screen, (0, 0, 0), (*HEALTH_BAR_POS, *HEALTH_BAR_SIZE), 2)


       

    

    



    if score < 10:

        wave = 0

        MAX_ENEMIES = 1
        MAX_ENEMIES2 = 0

 

    # Enemies

    if score >= 10:

        MAX_ENEMIES = 2

        wave = 1

        MAX_ENEMIES2 = 0
 

    if score >= 20:

        wave = 2

        speed = 2.5

        MAX_ENEMIES2 = 0 

    if score >= 30:

        wave = 3

        speed = 3

        MAX_ENEMIES = 3

        MAX_ENEMIES2 = 0 

    if score >= 40:

        wave = 4

        speed = 5

        MAX_ENEMIES2 = 0

    if score >= 50:

        wave = 5

        MAX_ENEMIES2 = 0

    if score >= 60:

        wave = 6

        speed = 4

        MAX_ENEMIES = 4

        MAX_ENEMIES2 = 0

    if score >= 70:

        wave = 7

        speed = 6

        MAX_ENEMIES = 4

        MAX_ENEMIES2 = 0

    if score >= 80:

        wave = 8

        MAX_ENEMIES2 = 0

    if score >= 90:

        wave = 9

        MAX_ENEMIES = 6

        FORBIDDEN_DISTANCE = 450

        MAX_ENEMIES2 = 0

    if score >= 100:

        wave = 10

        MAX_ENEMIES = 10

        speed = 10

        MAX_ENEMIES2 = 0

    if score >= 110:

        wave = 11

        enemy["visible"] = False

        FORBIDDEN_DISTANCE = 350

        MAX_ENEMIES2 = 2

        MAX_ENEMIES = 0

    if score >= 120:

        wave = 12

        MAX_ENEMIES2 = 3

        MAX_ENEMIES = 0

    if score >= 130:

        wave = 13

        speed2 = 3

    if score >= 140:

        enemy["visible"] = True

        wave = 14

        MAX_ENEMIES = 1

    if score >= 150:

        wave = 15

        MAX_ENEMIES2 = 4

        MAX_ENEMIES = 2

    if score >= 160:

        wave = 16

        MAX_ENEMIES2 = 5

        MAX_ENEMIES = 3

    if score >= 170:

        wave = 17

        MAX_ENEMIES = 4

        speed = 3

        speed2 = 3

    if score >= 180:

        wave = 18

        speed = 4

        speed2 = 4

    if score >= 190:

        MAX_ENEMIES2 = 7

        MAX_ENEMIES = 5

    if score >= 200:
        MAX_ENEMIES2 = 10

        MAX_ENEMIES = 0

        speed2 = 10




    

 
    if player_health <= 0:
        current_screen = "game_over_screen"
        pygame.display.update()
        return
  
    # Spawn enemies up to MAX_ENEMIES

    while len(enemies) < MAX_ENEMIES:

            enemies.append(spawn_enemy())

    while len(enemies2) < MAX_ENEMIES2:

            enemies2.append(spawn_enemy2())

 

 

    new_enemies = []

  

    for enemy in enemies:

        if not enemy["visible"]:

            new_enemies.append(spawn_enemy())

            continue

 

        # Enemy movement and logic

        speed = 2

        current_time = pygame.time.get_ticks()
        if cool_shades_active:
            if current_time - cool_shades_start_time <= cool_shades_duration:
                speed = 0.5

        dx = playerX - enemy["x"]

        dy = playerY - enemy["y"]

        dist = math.hypot(dx, dy)

        if dist:

            dx /= dist

            dy /= dist

            enemy["x"] += dx * speed

            enemy["y"] += dy * speed

 

        enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 64, 64)

 

        current_time = pygame.time.get_ticks()

        if player_rect.colliderect(enemy_rect) and current_time - last_damage_time > damage_cooldown:

            player_health -= 1

            last_damage_time = current_time



        screen.blit(enemy_img, (enemy["x"], enemy["y"]))

        new_enemies.append(enemy)







    enemies = new_enemies

    if score >= 101:
        new_enemies2 = []

      

        for enemy2 in enemies2:

            if not enemy2["visible2"]:

                new_enemies2.append(spawn_enemy2())

                continue

     

            # Enemy movement and logic

            speed2 = 1.5

            current_time = pygame.time.get_ticks()
            if cool_shades_active:
                if current_time - cool_shades_start_time <= cool_shades_duration:
                    speed2 = 0.5

            dx2 = playerX - enemy2["x"]

            dy2 = playerY - enemy2["y"]

            dist2 = math.hypot(dx2, dy2)

            if dist2:

                dx2 /= dist2

                dy2 /= dist2

                enemy2["x"] += dx2 * speed2

                enemy2["y"] += dy2 * speed2

     

            enemy2_rect = pygame.Rect(enemy2["x"] + 0, enemy2["y"] + 0, 64, 64)

     

            current_time = pygame.time.get_ticks()


            if player_rect.colliderect(enemy2_rect) and current_time - last_damage_time > damage_cooldown:

                player_health -= 2

                last_damage_time = current_time



            screen.blit(enemy2_img, (enemy2["x"], enemy2["y"]))

            new_enemies2.append(enemy2)

        enemies2 = new_enemies2
 

    # Player

    screen.blit(player_img, (playerX, playerY))

    if cosmetic1_selected:
        screen.blit(hat_player, (playerX - 1, playerY - 40))

    if cosmetic2_selected:
        screen.blit(shades_player, (playerX + 15, playerY+2.5))

    new_bananas = []

    for bx, by in bananas:

        banana_rect = banana_img.get_rect(topleft=(bx + 10, by + 10))

 

        # Check against enemies

        hit_enemy = False

        for enemy in enemies:

            if enemy["visible"]:

                enemy_rect = pygame.Rect(enemy["x"] + 12, enemy["y"] + 12, 40, 40)

                if banana_rect.colliderect(enemy_rect):

                    enemy["visible"] = False

                    score += 1 * score_multiplier

                    money_score += 1 * score_multiplier

                    hit_enemy = True



                    break  # Exit enemy loop

 



        hit_enemy2 = False
  
        for enemy2 in enemies2:

            if enemy2["visible2"]:

                enemy2_rect = pygame.Rect(enemy2["x"] + 12, enemy2["y"] + 12, 20, 20)

                if banana_rect.colliderect(enemy2_rect):

                    if enemy2["health2"] <= 0:

                        print("u")

                        enemy2["visible2"] = False

                        score += 2 * score_multiplier

                        money_score += 2 * score_multiplier

                        hit_enemy2 = True

                        break  # Exit enemy loop
                    else:
                        enemy2["health2"] -= 1
                        hit_enemy2 = True
                        break

 

        if not hit_enemy2 and not hit_enemy:

            new_bananas.append((bx, by))


    bananas = new_bananas

    banana_ONSCREEN = len(bananas)

 

 

    # Bananas

    for bx, by in bananas:

        screen.blit(banana_img, (bx, by))

    if cool_shades_active:
        time_slow_screen = True
    else:
        time_slow_screen = False

    # Disable cool shades effect after time is up
    if cool_shades_active and current_time - cool_shades_start_time > cool_shades_duration:
        cool_shades_active = False


    if time_slow_screen:
        flash_alpha = 150  # You can adjust this
        flash_surface = pygame.Surface((WIDTH, HEIGHT))
        flash_surface.set_alpha(flash_alpha)
        flash_surface.fill((135, 206, 235))  # SKY_BLUE
        screen.blit(flash_surface, (0, 0))
    

    


    # Score

    draw_text(f"Score: {score}", small_font, (0, 0, 0), 600, 10)

 

    #Banana counter

    draw_text(f"{banana_ONSCREEN}/{MAX_BANANAS}", small_font, (0, 0, 0), 700, 520)

 

    #Wave

    draw_text(f"Wave {wave}", small_font, (0, 0, 0), 300, 10)

 

    pygame.display.update()

 

def game_over_screen():

    global current_screen, last_income_time, money_score, multiplier

    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, START_COLOR, restart_btn, border_radius=30)

    draw_text("RESTART", main_font, WHITE, 215, 235)

    pygame.draw.rect(screen, START_COLOR, menu_btn, border_radius=30)

    draw_text("MENU", main_font, WHITE, 265, 435)

    pygame.display.update()


 

    if node1_selected:

        current_time = pygame.time.get_ticks()

        if current_time - last_income_time > income_interval:

            money_score += passive_income_amount * multiplier

            last_income_time = current_time

 

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if restart_btn.collidepoint(event.pos):

                current_screen = "game"

                reset_game()

            if menu_btn.collidepoint(event.pos):

                current_screen = "start"

 

# MAIN LOOP

running = True

while running:

    clock.tick(60)

    if current_screen == "start":

        start_screen()

    elif current_screen == "upgrade":

        upgrade_screen()

    elif current_screen == "cosmetics":

        cosmetics_screen()

    elif current_screen == "game":

        game_loop()

    elif current_screen == "game_over_screen":

        game_over_screen()