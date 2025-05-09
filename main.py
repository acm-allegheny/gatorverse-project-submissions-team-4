"""Gatorverse Main Display for On the Plane."""

import sys
import time

import pygame
from button import Button
import json 
import random

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("pictures/background.jpg")

with open("questions/questions.json", "r") as file:
    questions = json.load(file)

def def_font(size):
    """Load a font from the specified path and size."""
    return pygame.font.Font("font/font.ttf", size)

def display_text(text, font, max_width):
    """Displaying text correctly, so the user can see it on the screen"""
    words = text.split(' ')
    lines = []
    current_line = ""

    for w in words:
        test_line = current_line + w + " "
        
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = w + " "
    
    lines.append(current_line.strip())
    return lines


def gameover():
    while True:
        SCREEN.blit(BG, (0, 0))

        OVER_TEXT = def_font(90).render("GAME OVER", True, "Red")
        OVER_RECT = OVER_TEXT.get_rect(center=(640, 200))
        CLIC_TO = def_font(45).render("Click to restart", True, "White")
        CLIC_RECT = CLIC_TO.get_rect(center=(640, 400))

        SCREEN.blit(OVER_TEXT, OVER_RECT)
        SCREEN.blit(CLIC_TO, CLIC_RECT)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()
        pygame.display.update()


def play():
    """Display the play screen."""
    input_text = ""
    active = False
    input_box = pygame.Rect(440, 320, 400, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    # Pick a random question
    current_q = random.choice(questions)
    question = current_q["question"]
    correct_answer = current_q["answer"].lower()

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))

        # Render question
        wrapped_lines = display_text(question, def_font(40), 1000)  # 1000px max width
        y_offset = 150
        
        for line in wrapped_lines:
            line_surf = def_font(40).render(line, True, "White")
            line_rect = line_surf.get_rect(center=(SCREEN.get_width() // 2, y_offset))
            SCREEN.blit(line_surf, line_rect)
            y_offset += 50

        # Render input box
        txt_surface = def_font(30).render(input_text, True, color)
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(SCREEN, color, input_box, 2)
        SCREEN.blit(txt_surface, (input_box.x + 5, input_box.y + 10))

        # Back Button
        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=def_font(75), base_color="White", hovering_color="Blue")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        def questions_remarks_good():
            start_time = time.time()
            while time.time() - start_time < 3:  # Run for 3 seconds
                SCREEN.blit(BG, (0, 0))  # Redraw the background to prevent overlapping
                remarks_good_text = def_font(40).render("Correct!", True, "Green")
                remarks_good_rect = remarks_good_text.get_rect(center=(640, 300))
                SCREEN.blit(remarks_good_text, remarks_good_rect)
                pygame.display.update()
                pygame.time.delay(500)  # Delay for half a second to create a flashing effect
                SCREEN.blit(BG, (0, 0))  # Clear the text
                pygame.display.update()
                pygame.time.delay(300)

        def questions_remarks_bad():
            start_time = time.time()
            while time.time() - start_time < 3:  # Run for 3 seconds
                SCREEN.blit(BG, (0, 0))  # Redraw the background to prevent overlapping
                remarks_bad_text = def_font(30).render(
                    f"Wrong! Correct answer: {correct_answer}", True, "Red"
                )
                remarks_bad_rect = remarks_bad_text.get_rect(center=(640, 300))
                SCREEN.blit(remarks_bad_text, remarks_bad_rect)
                pygame.display.update()
                pygame.time.delay(500)  # Delay for half a second to create a flashing effect
                SCREEN.blit(BG, (0, 0))  # Clear the text
                pygame.display.update()
                pygame.time.delay(300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    if input_text.lower().strip() == correct_answer:
                        questions_remarks_good()

                    else:
                        questions_remarks_bad()
                        gameover()
                        
                    input_text = ""
                    current_q = random.choice(questions)
                    question = current_q["question"]
                    correct_answer = current_q["answer"].lower()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.display.update()


def convert():
    while True:
        SCREEN.blit(BG, (0, 0))

        CONVERT_TEXT = def_font(50).render("UNFINISHED GAMEMODE", True, "Blue")
        CONVERT_RECT = CONVERT_TEXT.get_rect(center=(640, 200))
        CONVERT_TO = def_font(45).render("Click to go back!", True, "White")
        CONVERT_RECT = CONVERT_TO.get_rect(center=(640, 400))

        SCREEN.blit(CONVERT_TEXT, CONVERT_RECT)
        SCREEN.blit(CONVERT_TO, CONVERT_RECT)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()
        pygame.display.update()

def options():
    """Display the options screen."""
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))

        OPTIONS_TEXT = def_font(45).render("How to Play.", True, "WHite")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        HOW_TEXT = def_font(30).render("On the Plane gives users two options", True, "WHite")
        HOW_RECT = HOW_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(HOW_TEXT, HOW_RECT)

        TO_TEXT = def_font(30).render("of gameplay. Metric Mania and", True, "WHite")
        TO_RECT = TO_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(TO_TEXT, TO_RECT)

        PLAY_TEXT = def_font(30).render("Trivia Bonanza. Each gameplay encourages", True, "WHite")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLA_TEXT = def_font(30).render("users to put in the correct input!", True, "WHite")
        PLA_RECT = PLA_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(PLA_TEXT, PLA_RECT)

        PL_TEXT = def_font(30).render("Correct answers warrent a continuous", True, "WHite")
        PL_RECT = PL_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(PL_TEXT, PL_RECT)

        P_TEXT = def_font(30).render("play while wrong answers end the game!!", True, "WHite")
        P_RECT = P_TEXT.get_rect(center=(640, 450))
        SCREEN.blit(P_TEXT, P_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=def_font(75), base_color="White", hovering_color="Blue")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def select():
    """Display the select screen."""
    while True:
        SCREEN.blit(BG, (0, 0))

        SELECT_MOUSE_POS = pygame.mouse.get_pos()

        SELECT_TEXT = def_font(90).render("Select", True, "#b68f40")
        SELECT_RECT = SELECT_TEXT.get_rect(center=(640, 100))

        TRIVIA_BUTTON = Button(image=pygame.image.load("pictures/rectang.png"), pos=(640, 250), 
                            text_input="STREETSMART BONANZA", font=def_font(30), base_color="#5da2cf", hovering_color="White")
        CONVERT_BUTTON = Button(image=pygame.image.load("pictures/options.png"), pos=(640, 400), 
                            text_input="METRIC MANIA", font=def_font(30), base_color="#5da2cf", hovering_color="White")
        SCREEN.blit(SELECT_TEXT, SELECT_RECT)

        for button in [TRIVIA_BUTTON, CONVERT_BUTTON]:
            button.changeColor(SELECT_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TRIVIA_BUTTON.checkForInput(SELECT_MOUSE_POS):
                    play()
                if CONVERT_BUTTON.checkForInput(SELECT_MOUSE_POS):
                    convert()


        pygame.display.update()


def main_menu():
    """Display the main menu."""
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = def_font(90).render("On the Plane", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("pictures/rectang.png"), pos=(640, 250), 
                            text_input="PLAY", font=def_font(75), base_color="#5da2cf", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("pictures/options.png"), pos=(640, 400), 
                            text_input="HOW TO", font=def_font(75), base_color="#5da2cf", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("pictures/quit.png"), pos=(640, 550), 
                            text_input="QUIT", font=def_font(75), base_color="#5da2cf", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def start_screen():
    """Display the start screen."""
    while True:
        SCREEN.blit(BG, (0, 0))

        START_TEXT = def_font(90).render("On the Plane", True, "#b68f40")
        START_RECT = START_TEXT.get_rect(center=(640, 200))
        CLICK_TO = def_font(45).render("Click to start", True, "White")
        CLICK_RECT = CLICK_TO.get_rect(center=(640, 400))

        SCREEN.blit(START_TEXT, START_RECT)
        SCREEN.blit(CLICK_TO, CLICK_RECT)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()
        pygame.display.update()


start_screen()
