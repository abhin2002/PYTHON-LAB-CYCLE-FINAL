


import pygame

import sys

from pygame.locals import *

import numpy as np

# Initializing Pygame

pygame.init()

# Pygame Screen

WIDTH=450

HEIGHT=450

# Colors

w = (255, 255, 255)

b = (0, 0, 0)

g = (0, 255, 0)

gy = (200, 200, 200)

bl = (0, 0, 255)

r = (255, 0, 0)

#Tic Tac Toe Board

BOX_MARKED = (np.array([

    [0,0,0],

    [0,0,0],

    [0,0,0]

]))


DRAW=False

WINNER=None

XO='o'

window=pygame.display.set_mode((WIDTH,HEIGHT+100))

pygame.display.set_caption("Tic-Tac-Toe")

window.fill(b)



# Window and Grids

def start():

    font=pygame.font.Font(None,82)

    window.fill(gy)

    #text=font.render("Let's Play", True,bl,(gy))

    #textRect = text.get_rect()

    #textRect.center = (WIDTH // 2, HEIGHT // 2)

    #window.blit(text, textRect)

    pygame.display.update()

    pygame.time.wait(1000)

    window.fill(w)

    # Two Vertical lines

    pygame.draw.line(window,b,(WIDTH/3,0),(WIDTH/3, HEIGHT),5)

    pygame.draw.line(window,b,(WIDTH/3*2,0),(WIDTH/3*2, HEIGHT),5)

    # Two Horizontal lines

    pygame.draw.line(window,b,(0,0),(WIDTH, 0),5)

    pygame.draw.line(window,b,(0,HEIGHT/3),(WIDTH, HEIGHT/3),5)

    pygame.draw.line(window,b,(0,HEIGHT/3*2),(WIDTH, HEIGHT/3*2),5)

    pygame.draw.line(window,b,(0,HEIGHT),(WIDTH, HEIGHT),5)



#Getting Mouse coordinates

def mouse_pointing():

    global row,col

    x, y = pygame.mouse.get_pos()

    #  getting width of the box

    if(x<WIDTH/3) and (y<HEIGHT/3):

        row=0

        col=0

    elif(x>WIDTH/3 and x<WIDTH/3*2) and (y<HEIGHT/3):

        row=0

        col=1

    elif(x>WIDTH/3*2) and (y<HEIGHT/3):

        row=0

        col=2

    elif(x<WIDTH/3) and (y>HEIGHT/3 and y<HEIGHT/3*2):

        row=1

        col=0

    elif(x>WIDTH/3 and x<WIDTH/3*2) and (y>HEIGHT/3 and y<HEIGHT/3*2):

        row=1

        col=1

    elif(x>WIDTH/3*2) and (y>HEIGHT/3 and y<HEIGHT/3*2):

        row=1

        col=2

    elif(x<WIDTH/3) and (y>HEIGHT/3*2):

        row=2

        col=0

    elif(x>WIDTH/3 and x<WIDTH/3*2) and (y>HEIGHT/3*2):

        row=2

        col=1

    elif(x>WIDTH/3*2) and (y>HEIGHT/3*2):

        row=2

        col=2

    else:

        row=None

        col=None

    draw_figure(row,col)



#Drawing X and O on window

def draw_figure(row,col):

    global XO

    if(BOX_MARKED[row,col] == 0):

        global DRAW

        if row==0:

            posx = 65

        if row==1:

            posx = WIDTH/3 + 65

        if row==2:

            posx = WIDTH/3*2 + 65

        if col==0:

            posy = 65

        if col==1:

            posy = HEIGHT/3 + 65

        if col==2:

            posy = HEIGHT/3*2 + 65

        #Drawing X and O on mainscreen

        if(XO=='o'):

            pygame.draw.circle(window, g, (posy, posx ), 40,8)

            BOX_MARKED[row][col] = 1

            XO='x'

        else:

            pygame.draw.line (window,g, (posy - 30, posx - 30),

                         (posy + 30, posx + 30), 8)

            pygame.draw.line (window,g, (posy + 30, posx - 30),

                         (posy - 30, posx + 30), 8)

            BOX_MARKED[row][col] = 2

            XO='o'

        pygame.display.update()

        check_winner()

    else:

        pass

    #Show Player Message turns 

    message= XO.upper() + "'s Turn"

    font=pygame.font.Font(None,70)

    text = font.render(message, True,bl,(w))

    textRect = text.get_rect()

    textRect.center = (200,500)

    window.blit(text, textRect)

    pygame.display.update()



#This Function check winner and draw

def check_winner():

    global WINNER

    for row in range (0,3):

        if ((BOX_MARKED [row][0] == BOX_MARKED[row][1] == BOX_MARKED[row][2]) and(BOX_MARKED [row][0] != 0)):

            # this row won

            WINNER = BOX_MARKED[row][0]

            pygame.draw.line(window, b, (0, (row + 1)*HEIGHT/3 -HEIGHT/6),\

                              (WIDTH, (row + 1)*HEIGHT/3 - HEIGHT/6 ), 4)

            show_winning_message(WINNER)

            break



    # check for winning columns

    for col in range (0, 3):

        if (BOX_MARKED[0][col] == BOX_MARKED[1][col] == BOX_MARKED[2][col]) and (BOX_MARKED[0][col] != 0):

            # this column won

            WINNER = BOX_MARKED[0][col]

            #draw winning line

            pygame.draw.line (window, b,((col + 1)* WIDTH/3 - WIDTH/6, 0),\

                          ((col + 1)* WIDTH/3 - WIDTH/6, HEIGHT), 4)

            show_winning_message(WINNER)

            break



    # check for diagonal WINNERs

    if (BOX_MARKED[0][0] == BOX_MARKED[1][1] == BOX_MARKED[2][2]) and (BOX_MARKED[0][0] != 0):

        # game won diagonally left to right

        WINNER = BOX_MARKED[0][0]

        pygame.draw.line (window, b, (50, 50), (350, 350), 4)

        show_winning_message(WINNER)

       



    if (BOX_MARKED[0][2] == BOX_MARKED[1][1] == BOX_MARKED[2][0]) and (BOX_MARKED[0][2] != 0):

        # game won diagonally right to left

        WINNER = BOX_MARKED[0][2]

        pygame.draw.line (window, b, (350, 50), (50, 350), 4)

        show_winning_message(WINNER)

    

    if(all([all(row) for row in BOX_MARKED]) and WINNER is None ):

        DRAW = True

        show_winning_message('Match Draw')





def show_winning_message(winner):

    font=pygame.font.Font(None,70)

    if winner == 1:

        winner = "O is winner "

    elif winner == 2:

        winner = "X is winner"

    else:

        pass

    text=font.render(winner, True,r,(w))

    textRect = text.get_rect()

    textRect.center = (200,450)

    window.blit(text, textRect)

    

    pygame.display.update()

    pygame.time.wait(2000)

    reset_game()



def reset_game():

    global BOX_MARKED,DRAW,WINNER

    BOX_MARKED = (np.array([

        [0,0,0],

        [0,0,0],

        [0,0,0]

    ]))

    XO='x'

    DRAW=False

    WINNER=None

    start()


start()



while(True):

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

        elif event.type==MOUSEBUTTONDOWN:

            mouse_pointing()

    pygame.display.update()

    pygame.display.flip()

