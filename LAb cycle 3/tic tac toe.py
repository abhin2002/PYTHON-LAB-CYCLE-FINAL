import pygame

pygame.init()  #initialise pygame

win = pygame.display.set_mode((550, 550))   #window for pygame

pygame.display.set_caption('Tic-Tac-Toe')   #displaying window

first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))  #drow rectangle on win with colour 255 and starting x and y and dimension of rectangle
second = pygame.draw.rect(win, (255,255,255), (200,25,150,150)) #second square with different starting position of x axis
third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))  #drow rectangle on win with colour 255 and starting x and y and dimension of rectangle
fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150)) #second square with different starting position of x axis
sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))  #drow rectangle on win with colour 255 and starting x and y and dimension of rectangle
eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150)) #second square with different starting position of x axis
ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

run = True

draw_object = 'rect'

first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

while run:

    pygame.time.delay(100)  #refresh time

    for event in pygame.event.get():        #to record the actions
        if event.type == pygame.QUIT:       #to close the window by clicking cross
            run = False

        if event.type == pygame.MOUSEBUTTONUP:  #mouse clicking event
            pos = pygame.mouse.get_pos()        #clicking position

            if first.collidepoint(pos) and first_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(50, 50, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (100,100), 50)
                    draw_object = 'rect'
                first_open = False
            if second.collidepoint(pos) and second_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(225, 50, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (275,100), 50)
                    draw_object = 'rect'
                second_open = False
            if third.collidepoint(pos) and third_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255, 0, 0),(400, 50, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (450,100), 50)
                    draw_object = 'rect'
                third_open = False
            if fourth.collidepoint(pos) and fourth_open:        #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(50, 225, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (100,275), 50)
                    draw_object = 'rect'
                fourth_open = False
            if fifth.collidepoint(pos) and fifth_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(225, 225, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (275,275), 50)
                    draw_object = 'rect'
                fifth_open = False
            if sixth.collidepoint(pos) and sixth_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255, 0, 0),(400, 225, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (450,275), 50)
                    draw_object = 'rect'
                sixth_open = False
            if seventh.collidepoint(pos) and seventh_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(50, 400, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (100,450), 50)
                    draw_object = 'rect'
                seventh_open = False
            if eighth.collidepoint(pos) and eighth_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(225, 400, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (275,450), 50)
                    draw_object = 'rect'
                eighth_open = False
            if ninth.collidepoint(pos) and ninth_open:         #if position == first position
                if draw_object == 'rect':
                    pygame.draw.rect(win, (225, 0, 0),(400, 400, 100, 100))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (450,450), 50)
                    draw_object = 'rect'
                ninth_open = False
    pygame.display.update()                 #new things brings to the friend 

pygame.quit()