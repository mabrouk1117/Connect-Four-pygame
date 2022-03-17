#auther : momen mostafa mabrouk
#id : 20210416
# game 1 (connect four) bonus game
# assignment 1 structured programming

import pygame
from pygame import mixer

pygame.init()
board = [
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"]
]

counter = 36
row = 5
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("connect four game")
pading = 80
green = (0, 255, 0)
red = (255, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 205, 0)
white = (255, 255, 255)

turn = True
clicked = False
run = True
draw = False
start = True

mixer.music.load("music_zapsplat_astro_race.mp3")
mixer.music.play(-1)

def start_game():
    global run
    screen.fill(cyan)
    header = pygame.font.Font('freesansbold.ttf', 50)
    line = header.render('Start', True, red ,blue)
    text_Rect = line.get_rect()
    text_Rect.center = (screen_width // 2, 520)

    paragraph =  pygame.font.Font('freesansbold.ttf', 25)
    content =paragraph.render('connect 4 coins to win. ', True, black)
    paragraph_rect =content.get_rect()
    paragraph_rect.center = (screen_width // 2, 100)

    screen.blit(content, paragraph_rect)
    paragraph = pygame.font.Font('freesansbold.ttf', 25)
    content = paragraph.render('RED will play first then GREEN', True, black)
    paragraph_rect = content.get_rect()
    paragraph_rect.center = (screen_width // 2, 200)

    screen.blit(content, paragraph_rect)

    paragraph = pygame.font.Font('freesansbold.ttf', 20)
    content = paragraph.render('you can connect them in row or in column or diagonally', True, black)
    paragraph_rect = content.get_rect()
    paragraph_rect.center = (screen_width // 2, 150)
    screen.blit(content, paragraph_rect)


    paragraph = pygame.font.Font('freesansbold.ttf', 25)
    content = paragraph.render('press start to start playing , good luck', True, black)
    paragraph_rect = content.get_rect()
    paragraph_rect.center = (screen_width // 2, 300)

    screen.blit(content, paragraph_rect)
    screen.blit(line, text_Rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event .type == pygame.MOUSEBUTTONDOWN :
            pressed = pygame.mouse.get_pos()
            if pressed [0] >260 and pressed[0] < 380:
                if pressed[1] >495 and pressed[1] < 545:
                    return True


def when_win():
    screen.fill(cyan)
    font = pygame.font.Font('freesansbold.ttf', 100)
    if turn:
        text = font.render('green wins', True, green, black)
    else:
        text = font.render('red wins', True, red, blue)
    win_sound = mixer.Sound("sfx-victory2.mp3")
    win_sound.play()

    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, textRect)
    pygame.display.update()
    pygame.time.wait(2500)


def update_board(board, column, row):
    global turn
    global counter
    while row >= 0:
        if board[row][column] != "-":
            row -= 1
        else:
            sound = mixer.Sound("mixkit-retro-game-notification-212.wav")
            sound.play()
            counter -= 1

            if (turn == True):
                board[row][column] = "x"
                return row
            else:
                board[row][column] = "o"
                return row
    turn = not turn
    return -1


def row_checker(board):
    for row in range(6):
        for column in range(3):
            check = []
            if board[row][column] == "x" or board[row][column] == "o":
                check.append(board[row][column])
                for col in range(column + 1, column + 4):
                    check.append(board[row][col])
                if check == ["x", "x", "x", "x"]:
                    print("player 1 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row),(120 + 80 * (column+3), 120 + 80 * row ), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True
                elif check == ["o", "o", "o", "o"]:
                    print("player 2 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row), (120 + 80 * (column+3), 120 + 80 * row ), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True


def column_checker(board):
    for column in range(6):
        for row in range(3):
            check = []
            if board[row][column] == "x" or board[row][column] == "o":
                check.append(board[row][column])
                for roww in range(row + 1, row + 4):
                    check.append(board[roww][column])
                if check == ["x", "x", "x", "x"]:
                    print("player 1 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row),(120 + 80 * column, 120 + 80 * (row + 3)), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True
                elif check == ["o", "o", "o", "o"]:
                    print("player 2 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row), (120 + 80 * column, 120 + 80 * (row + 3)), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True


def diag_checker(board):
    for row in range(3):
        for column in range(3):
            check = []
            if board[row][column] == "x" or board[row][column] == "o":
                check.append(board[row][column])
                col = column
                for roww in range(row + 1, row + 4):
                    col += 1
                    check.append(board[roww][col])
                if check == ["x", "x", "x", "x"]:
                    print("player 1 wins")

                    pygame.draw.line(screen,white, (120+80*column, 120+80*row), (120+80*col, 120+80*(row+3)), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)

                    return True
                elif check == ["o", "o", "o", "o"]:
                    print("player 2 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row), (120 + 80 * col, 120 + 80 * (row + 3)), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True

    for row in range(3):
        for column in range(3, 6):
            check = []
            if board[row][column] == "x" or board[row][column] == "o":
                check.append(board[row][column])
                col = column
                for roww in range(row + 1, row + 4):
                    col -= 1
                    check.append(board[roww][col])
                if check == ["x", "x", "x", "x"]:
                    print("player 1 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row),(120 + 80 * col, 120 + 80 * (row + 3)), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True
                elif check == ["o", "o", "o", "o"]:
                    print("player 2 wins")
                    pygame.draw.line(screen, white, (120 + 80 * column, 120 + 80 * row), (120 + 80 * col, 120 + 80 * (row + 3)), 15)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    return True


def draw_board():
    screen.fill(cyan)
    pygame.draw.rect(screen, black, pygame.Rect(80,80, screen_width-160, screen_width-160))


    for x in range(6):
        for y in range(6):
            pygame.draw.circle(screen, white, (120+80*x ,120+80*y ),35)


def convert_pos(x_pos, y_pos):
    global counter
    global turn
    if x_pos > 80 and x_pos < 560 and y_pos > 80 and y_pos < screen_height - 80:

        x_pos -= 80
        column = x_pos // 80
        update_board(board, column, row)
    else:
        turn = not turn




def draw_circles():
    for row in range(6):
        for col in range(6):
            if board[row][col] != "-":

                if board[row][col] == "x":
                    pygame.draw.circle(screen, green, ( 120 + 80 * col, 120 + 80 * row), 35)
                else:
                    pygame.draw.circle(screen, red, ( 120 + 80 * col, 120 + 80 * row), 35)


def draw_consol():
    for i in board:
        for j in i:
            print(j, end="   ")
        print()


while run:
    if start:
        if start_game():
            draw_board()
            header = pygame.font.Font('freesansbold.ttf', 40)
            line = header.render('connect 4 to win', True, black)
            text_Rect = line.get_rect()
            text_Rect.center = (screen_width // 2, 40)
            screen.blit(line, text_Rect)
            start=False
    else:
        draw_board()
    draw_circles()
    if row_checker(board) or column_checker(board) or diag_checker(board):
        when_win()
        run = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            cliked = False
            pos = pygame.mouse.get_pos()
            x_pos = pos[0]
            y_pos = pos[1]
            draw = True
            turn = not turn
            convert_pos(x_pos, y_pos)
            draw_consol()
            pygame.display.update()

    if counter == 0:
        header = pygame.font.Font('freesansbold.ttf', 40)
        line = header.render('DRAW ', True, black)
        text_Rect = line.get_rect()
        text_Rect.center = (screen_width // 2, 40)
        screen.blit(line, text_Rect)
        pygame.time.wait(2000)
        pygame.display.update()
        run = False

    pygame.display.update()

pygame.quit()
