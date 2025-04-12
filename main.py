import pygame, sys
from button import Button
import json 
import random

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("pictures/background.png")

with open("questions/questions.json", "r") as file:
    questions = json.load(file)

def def_font(size):
    return pygame.font.Font("font/font.ttf", size)

def play():
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
        question_surf = def_font(40).render(question, True, "White")
        SCREEN.blit(question_surf, (SCREEN.get_width() // 2 - question_surf.get_width() // 2, 200))

        # Render input box
        txt_surface = def_font(30).render(input_text, True, color)
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(SCREEN, color, input_box, 2)
        SCREEN.blit(txt_surface, (input_box.x + 5, input_box.y + 10))

        # Back Button
        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=def_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

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
                        print("Correct!")
                    else:
                        print(f"Wrong. Correct answer: {correct_answer}")
                    input_text = ""
                    current_q = random.choice(questions)
                    question = current_q["question"]
                    correct_answer = current_q["answer"].lower()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))

        OPTIONS_TEXT = def_font(45).render("This is the OPTIONS screen.", True, "WHite")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=def_font(75), base_color="White", hovering_color="Green")

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

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = def_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("pictures/rectang.png"), pos=(640, 250), 
                            text_input="PLAY", font=def_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("pictures/options.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=def_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("pictures/quit.png"), pos=(640, 550), 
                            text_input="QUIT", font=def_font(75), base_color="#d7fcd4", hovering_color="White")

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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
