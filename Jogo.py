import pygame
from pygame.locals import *
import sys
from time import sleep
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
HEIGHT = 800
WIDTH = 800
menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0 , 0)
PURPLE = (100,0,100)

def draw_paper_button():
    # Desenho do botão "Papel"
    fonte = pygame.font.SysFont(None, 40)
    paper_text = fonte.render("Papel", True, WHITE)
    paper_button = pygame.Rect(100, HEIGHT // 2 + 100, 200, 100)
    pygame.draw.rect(menu_screen, BLUE, paper_button)
    # Centralizar o texto horizontalmente
    text_x = paper_button.centerx - paper_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = paper_button.centery - paper_text.get_height() // 2
    menu_screen.blit(paper_text, (text_x, text_y))
    return paper_button
def draw_paper_button_select():
    # Desenho do botão "Papel"
    fonte = pygame.font.SysFont(None, 40)
    paper_text = fonte.render("Papel", True, WHITE)
    paper_button = pygame.Rect(100, HEIGHT // 2 + 100, 200, 100)
    pygame.draw.rect(menu_screen, RED, paper_button)
    # Centralizar o texto horizontalmente
    text_x = paper_button.centerx - paper_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = paper_button.centery - paper_text.get_height() // 2
    menu_screen.blit(paper_text, (text_x, text_y))
    return paper_button

def draw_rock_button():
    fonte = pygame.font.SysFont(None, 40)
    rock_text = fonte.render("Pedra", True, WHITE)
    rock_button = pygame.Rect(100, HEIGHT // 2 - 50, 200, 100)
    pygame.draw.rect(menu_screen, BLUE, rock_button)
    # Centralizar o texto horizontalmente
    text_x = rock_button.centerx - rock_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = rock_button.centery - rock_text.get_height() // 2
    menu_screen.blit(rock_text, (text_x, text_y))
    return rock_button
def draw_rock_button_select():
    fonte = pygame.font.SysFont(None, 40)
    rock_text = fonte.render("Pedra", True, WHITE)
    rock_button = pygame.Rect(100, HEIGHT // 2 - 50, 200, 100)
    pygame.draw.rect(menu_screen, RED, rock_button)
    # Centralizar o texto horizontalmente
    text_x = rock_button.centerx - rock_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = rock_button.centery - rock_text.get_height() // 2
    menu_screen.blit(rock_text, (text_x, text_y))
    return rock_button
def draw_scissors_button():
    fonte = pygame.font.SysFont(None, 40)
    scissors_text = fonte.render("Tesoura", True, WHITE)
    scissors_button = pygame.Rect(100, HEIGHT // 2 + 250, 200, 100)
    pygame.draw.rect(menu_screen, BLUE, scissors_button)
    # Centralizar o texto horizontalmente
    text_x = scissors_button.centerx - scissors_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = scissors_button.centery - scissors_text.get_height() // 2
    menu_screen.blit(scissors_text, (text_x, text_y))
    return scissors_button

def draw_scissors_button_select():
    fonte = pygame.font.SysFont(None, 40)
    scissors_text = fonte.render("Tesoura", True, WHITE)
    scissors_button = pygame.Rect(100, HEIGHT // 2 + 250, 200, 100)
    pygame.draw.rect(menu_screen, RED, scissors_button)
    # Centralizar o texto horizontalmente
    text_x = scissors_button.centerx - scissors_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = scissors_button.centery - scissors_text.get_height() // 2
    menu_screen.blit(scissors_text, (text_x, text_y))
    return scissors_button

def draw_player1():
    #PLAYER 1
    fonte = pygame.font.SysFont(None, 40)
    player1_text = fonte.render("Player 1", True, BLUE)
    menu_screen.blit(player1_text, (200 - player1_text.get_width() // 2, HEIGHT // 2 - 200))

    # Desenho do botão "Pedra"
    rock_button = draw_rock_button()

    # Desenho do botão "Papel"
    paper_button = draw_paper_button()
    
    # Desenho do botão "Tesoura"
    scissors_button = draw_scissors_button()
    return paper_button, scissors_button, rock_button
def draw_computer_paper_button():
    # Desenho do botão "Papel"
    fonte = pygame.font.SysFont(None, 40)
    paper_text = fonte.render("Papel", True, WHITE)
    paper_button = pygame.Rect(500, HEIGHT // 2 + 100, 200, 100)
    pygame.draw.rect(menu_screen, BLUE, paper_button)
    # Centralizar o texto horizontalmente
    text_x = paper_button.centerx - paper_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = paper_button.centery - paper_text.get_height() // 2
    menu_screen.blit(paper_text, (text_x, text_y))
def draw_computer_paper_button_select():
    # Desenho do botão "Papel"
    fonte = pygame.font.SysFont(None, 40)
    paper_text = fonte.render("Papel", True, WHITE)
    paper_button = pygame.Rect(500, HEIGHT // 2 + 100, 200, 100)
    pygame.draw.rect(menu_screen, RED, paper_button)
    # Centralizar o texto horizontalmente
    text_x = paper_button.centerx - paper_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = paper_button.centery - paper_text.get_height() // 2
    menu_screen.blit(paper_text, (text_x, text_y))

def draw_computer_rock_button():
    # Desenho do botão "Pedra"
    fonte = pygame.font.SysFont(None, 40)
    rock_text = fonte.render("Pedra", True, WHITE)
    rock_button = pygame.Rect(500, HEIGHT // 2 - 50, 200, 100)
    pygame.draw.rect(menu_screen, BLUE, rock_button)
    # Centralizar o texto horizontalmente
    text_x = rock_button.centerx - rock_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = rock_button.centery - rock_text.get_height() // 2
    menu_screen.blit(rock_text, (text_x, text_y))
def draw_computer_rock_button_select():
    # Desenho do botão "Pedra"
    fonte = pygame.font.SysFont(None, 40)
    rock_text = fonte.render("Pedra", True, WHITE)
    rock_button = pygame.Rect(500, HEIGHT // 2 - 50, 200, 100)
    pygame.draw.rect(menu_screen, RED, rock_button)
    # Centralizar o texto horizontalmente
    text_x = rock_button.centerx - rock_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = rock_button.centery - rock_text.get_height() // 2
    menu_screen.blit(rock_text, (text_x, text_y))

def draw_computer_scissors_button():
    # Desenho do botão "Tesoura"
    fonte = pygame.font.SysFont(None, 40)
    scissors_text = fonte.render("Tesoura", True, WHITE)
    scissors_button = pygame.Rect(500, HEIGHT // 2 + 250, 200, 100)
    pygame.draw.rect(menu_screen, BLUE, scissors_button)
    # Centralizar o texto horizontalmente
    text_x = scissors_button.centerx - scissors_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = scissors_button.centery - scissors_text.get_height() // 2
    menu_screen.blit(scissors_text, (text_x, text_y))

def draw_computer_scissors_button_select():
    # Desenho do botão "Tesoura"
    fonte = pygame.font.SysFont(None, 40)
    scissors_text = fonte.render("Tesoura", True, WHITE)
    scissors_button = pygame.Rect(500, HEIGHT // 2 + 250, 200, 100)
    pygame.draw.rect(menu_screen, RED, scissors_button)
    # Centralizar o texto horizontalmente
    text_x = scissors_button.centerx - scissors_text.get_width() // 2
    # Centralizar o texto verticalmente
    text_y = scissors_button.centery - scissors_text.get_height() // 2
    menu_screen.blit(scissors_text, (text_x, text_y))
def draw_computer():
    #computer
    fonte = pygame.font.SysFont(None, 40)
    computer_text = fonte.render("Computer", True, BLUE)
    menu_screen.blit(computer_text, (600 - computer_text.get_width() // 2, HEIGHT // 2 - 200))
    draw_computer_paper_button()
    draw_computer_rock_button()
    draw_computer_scissors_button()


def draw_title():
    fonte = pygame.font.SysFont(None, 50)
    title = fonte.render("JO-KEN-PO", True, BLUE)
    menu_screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
    subtitle = fonte.render("Single Player", True, BLUE)
    menu_screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 100))
def jokenpo_animation():
    menu_screen.fill(WHITE)
    # desenhos na tela
    fonte = pygame.font.SysFont(None, 200)
    text = fonte.render("JO", True, BLUE)
    menu_screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    sleep(1)
    menu_screen.fill(WHITE)
    # desenhos na tela
    fonte = pygame.font.SysFont(None, 250)
    text = fonte.render("KEN", True, RED)
    menu_screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    sleep(1)
    menu_screen.fill(WHITE)
    # desenhos na tela
    fonte = pygame.font.SysFont(None, 225)
    text = fonte.render("PO", True, PURPLE)
    menu_screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    sleep(0.5)
    menu_screen.fill(WHITE)
    pygame.display.flip()

def computer_play():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        draw_computer_rock_button_select()
    elif computer_choice == 2:
        draw_computer_paper_button_select()
    elif computer_choice == 3:
        draw_computer_scissors_button_select()
    return computer_choice
def check_winner(player1_choice, computer_choice):
    print("player1_choice: ", player1_choice)
    print("computer_choice: ", computer_choice)
    if player1_choice == computer_choice:
        return 2 # 2 = empate
    elif player1_choice == 1: # pedra
        if computer_choice == 2: # papel
            return 0 # 0 = derrota
        else:
            return 1 # 1 = vitória
    elif player1_choice == 2: # papel
        if computer_choice == 3: # tesoura
            return 0
        else:
            return 1 # 1 = vitória
    elif player1_choice == 3: # tesoura
        if computer_choice == 1: # pedra
            return 0
        else:
            return 1 # 1 = vitória
def print_result(result):
    if result == 0:
        fonte = pygame.font.SysFont(None, 50)
        text = fonte.render("Loose!", True, RED)
        menu_screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    elif result == 1:
        fonte = pygame.font.SysFont(None, 50)
        text = fonte.render("Win!", True, BLUE)
        menu_screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    else:
        fonte = pygame.font.SysFont(None, 50)
        text = fonte.render("Draw!", True, PURPLE)
        menu_screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
# Loop principal
rodando = True

paper_button_clicked = False
scissors_button_clicked = False
rock_button_clicked = False

while rodando:
    menu_screen.fill(WHITE)
    # desenhos na tela
    draw_title()
    paper_button, scissors_button, rock_button = draw_player1()
    draw_computer()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if paper_button.collidepoint(evento.pos):
                    paper_button_clicked = True
                elif scissors_button.collidepoint(evento.pos):
                    scissors_button_clicked = True
                elif rock_button.collidepoint(evento.pos):
                    rock_button_clicked = True
    
    if paper_button_clicked:
        player_choice = 2
        draw_paper_button_select()
        pygame.display.flip()
        sleep(1)
        jokenpo_animation()
        print("paper")
        draw_title()
        draw_player1()
        draw_computer()
        draw_paper_button_select()
        computer_choice = computer_play()
        pygame.display.flip()
        result = check_winner(player_choice, computer_choice)
        print (player_choice, computer_choice, result)
        print_result(result)
        pygame.display.flip()
        sleep(3)
        paper_button_clicked = False
    elif rock_button_clicked:
        player_choice = 1
        draw_rock_button_select()
        pygame.display.flip()
        sleep(1)
        jokenpo_animation()
        draw_title()
        draw_player1()
        draw_computer()
        draw_rock_button_select()
        computer_choice = computer_play()
        pygame.display.flip()
        result = check_winner(player_choice, computer_choice)
        print (player_choice, computer_choice, result)
        print_result(result)
        pygame.display.flip()
        sleep(3)
        rock_button_clicked = False
    elif scissors_button_clicked:
        player_choice = 3
        draw_scissors_button_select()
        pygame.display.flip()
        sleep(1)
        jokenpo_animation()
        print("paper")
        draw_title()
        draw_player1()
        draw_computer()
        draw_scissors_button_select()
        computer_choice = computer_play()
        pygame.display.flip()
        result = check_winner(player_choice, computer_choice)
        print (player_choice, computer_choice, result)
        print_result(result)
        pygame.display.flip()
        sleep(3)
        scissors_button_clicked = False
    # Atualização da tela
    pygame.display.flip()

    #


# Encerramento do Pygame
pygame.quit()

# Abrir a janela do menu novamente
import main
main.janela.mainloop()

# Encerrar o programa
sys.exit()
