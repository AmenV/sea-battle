import pygame
import numpy as np
import random
import time

pygame.init()                                                                  #Запуск модуля
#Подгрузка картинок для работы приложения**************************************
ship_1 = pygame.image.load('images/1_down.png')
ship_2 = [pygame.image.load('images/2_down.png'), pygame.image.load('images/2_right.png')]
ship_3 = [pygame.image.load('images/3_down.png'), pygame.image.load('images/3_right.png')]
at_zone = pygame.image.load('images/red_square.png')
font = pygame.font.Font('freesansbold.ttf', 20)
main_screen = pygame.image.load('images/main_screen.jpg')
battlefield = pygame.image.load('images/battlefield.png')
background = pygame.image.load('images/background.jpg')
#******************************************************************************
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (223,255,0)
blue = (0,0,205)
locx = 1
locy = 1
kr = 0
kd = 0
loc = 0
i = 0

step = True
battle = False
lmove = 'down'
game_pvp = False
game_pve = False
run = True
screen = pygame.display.set_mode((900, 500))                                   #Задача размеров окна
pygame.display.set_caption('Морской бой')                                      #Название окна
        

def main_menu():                                                               #создание меню
    text_1 = 'Играть против компьютера'
    text_2 = 'Играть против игрока'
    text_3 = 'Выйти'
    text = font.render(text_1, True, black, None)
    textRect = text.get_rect()
    textRect.center = (200, 150)
    text2 = font.render(text_2, True, black, None)
    text2Rect = text.get_rect()
    text2Rect.center = (230, 260) 
    text3 = font.render(text_3, True, black, None)
    text3Rect = text.get_rect()
    text3Rect.center = (300, 375)     
    screen.blit(main_screen, ((0,0)))
    if loc == 0:
        text = font.render(text_1, True, blue, None)
        textRect = text.get_rect()
        textRect.center = (200, 150)   
    elif loc == 1:
        text2 = font.render(text_2, True, blue, None)
        text2Rect = text.get_rect()
        text2Rect.center = (230, 260)         
    else:
        text3 = font.render(text_3, True, blue, None)
        text3Rect = text.get_rect()
        text3Rect.center = (300, 375)       
    screen.blit(text, textRect)                                                #Размещение кнопок меню
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    pygame.display.update()                                                    #Обновление экрана
    
class game:                                                                    #Основная часть игры
    def fill_battlefield_player1():                                            #Заполнение поля для игрока 1
        screen.blit(battlefield, ((150,100)))
        if ship1 > 0:
            screen.blit(ship_1, ((150 + (locx+1)*25, 90 + (locy+1)*25)))
        elif ship1 == 0 and ship2 > 0:
            screen.blit(ship_2[i], ((150 + (locx+1)*25, 90 + (locy+1)*25)))
        else:
            screen.blit(ship_3[i], ((150 + (locx+1)*25, 90 + (locy+1)*25)))
            
        
        game.draw_field_player1()                                              #Вызов функции для отрисовки поля
        pygame.display.update()
        
            
    
    def draw_field_player1():                                                  #Отрисовка поля
        for t in range(10):
            for d in range(10):
                if bf[t][d] == 'x':
                    screen.blit(ship_1, ((150 + (d+1)* 25), 90 + (t+1)*25))
                if d + 1 < 11:
                    if (bf[t][d] == 'y' or bf[t][d] == '1') and (bf[t][d+1] == 'y' or bf[t][d+1] == '1'):
                        screen.blit(ship_2[1], ((150 + (d+1)* 25, 90 + (t+1)*25)))
                elif t + 1 < 11:
                    if (bf[t][d] == 'y' or bf[t][d] == '1') and (bf[t+1][d] == 'y' or bf[t+1][d] == '1'):
                        screen.blit(ship_2[0], ((150 + (d+1)* 25, 90 + (t+1)*25)))
                
                if d + 1 < 11 and d + 2 < 11:
                    if (bf[t][d] or bf[t][d] == '1') == 'z' and bf[t][d+1] == 'z' and bf[t][d+2] == 'z':
                        screen.blit(ship_3[1], ((150 + (d+1)* 25, 90 + (t+1)*25)))
                if t + 1 < 11 and t + 2 < 11:
                    if (bf[t][d] == 'z' or bf[t][d] == '1') and bf[t+1][d] == 'z' and bf[t+2][d] == 'z':
                        screen.blit(ship_3[0], ((150 + (d+1)* 25, 90 + (t+1)*25))) 
    
    def draw_battlefield_player1():                                            #Отрисовка второго поля для 1ого игрока
        text_hit = 'X'
        text = font.render(text_hit, True, white, None)
        text_miss = 'O'       
        text2 = font.render(text_miss, True, white, None)
        for t in range(1, 10):
            for d in range(1, 10):
                if bf[t][d] == 'x':
                    screen.blit(ship_1, ((100 + (d+1)* 25), 40 + (t+1)*25))
                if d + 1 < 11:
                    if (bf[t][d] == 'y' or bf[t][d] == '1') and (bf[t][d+1] == 'y' or bf[t][d+1] == '1'):
                        screen.blit(ship_2[1], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                if t + 1 < 11:
                    if (bf[t][d] == 'y' or bf[t][d] == '1') and (bf[t+1][d] == 'y' or bf[t+1][d] == '1'):
                        screen.blit(ship_2[0], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                
                if d + 1 < 11 and d + 2 < 11:
                    if bf[t][d] == 'z' and (bf[t][d+1] == 'z' or bf[t][d+1] == '1') and (bf[t][d+2] == 'z' or bf[t][d+2] == '1'):
                        screen.blit(ship_3[1], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                if t + 1 < 11 and d + 2 < 11:
                    if bf[t][d] == 'z' and (bf[t+1][d] == 'z' or bf[t+1][d] == '1') and (bf[t+2][d] == 'z' or bf[t+2][d] == '1'):
                        screen.blit(ship_3[0], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                
                if bf[t][d] == '1':
                    texthitRect = text.get_rect()
                    texthitRect.center = (135+ (d*25), 50 + ((t+1)*25))               
                    screen.blit(text, texthitRect)
                elif bf[t][d] == '2':
                    text2Rect = text.get_rect()
                    text2Rect.center = (135 + (d * 25), 50 + ((t+1) * 25))   
                    screen.blit(text2, text2Rect)                
                
                if bf_enemy[t][d] == '1':
                    texthitRect = text.get_rect()
                    texthitRect.center = (585+ (d*25), 75 + (t*25))               
                    screen.blit(text, texthitRect)
                elif bf_enemy[t][d] == '2':
                    text2Rect = text.get_rect()
                    text2Rect.center = (585 + (d * 25), 78 + (t * 25))   
                    screen.blit(text2, text2Rect)
        
    def battle_pve():                                                          #Запуск игры против компьютера
        screen.blit(background, ((0,0))) 
        screen.blit(battlefield, ((100, 50)))
        screen.blit(battlefield, ((550, 50)))
        screen.blit(at_zone, ((575 + (locx*25), 65 + (locy*25))))
        game.draw_battlefield_player1()
        pygame.display.update()
        
        
        
    def fill_battlefield_player2():                                            #Заполнение поля для игрока 1
        screen.blit(battlefield, ((150,100)))
        if ship1 > 0:
            screen.blit(ship_1, ((150 + (locx+1)*25, 90 + (locy+1)*25)))
        elif ship1 == 0 and ship2 > 0:
            screen.blit(ship_2[i], ((150 + (locx+1)*25, 90 + (locy+1)*25)))
        else:
            screen.blit(ship_3[i], ((150 + (locx+1)*25, 90 + (locy+1)*25)))
            
        
        game.draw_field_player2()
        pygame.display.update()
        
            
    
    def draw_field_player2():                                                  #Отрисовка поля
        for t in range(10):
            for d in range(10):
                if bf2[t][d] == 'x':
                    screen.blit(ship_1, ((150 + (d+1)* 25), 90 + (t+1)*25))
                if d + 1 < 11:
                    if (bf2[t][d] == 'y' or bf2[t][d] == '1') and (bf2[t][d+1] == 'y' or bf2[t][d+1] == '1'):
                        screen.blit(ship_2[1], ((150 + (d+1)* 25, 90 + (t+1)*25)))
                elif t + 1 < 11:
                    if (bf2[t][d] == 'y' or bf2[t][d] == '1') and (bf2[t+1][d] == 'y' or bf2[t+1][d] == '1'):
                        screen.blit(ship_2[0], ((150 + (d+1)* 25, 90 + (t+1)*25)))
                
                if d + 1 < 11 and d + 2 < 11:
                    if (bf2[t][d] or bf2[t][d] == '1') == 'z' and bf2[t][d+1] == 'z' and bf2[t][d+2] == 'z':
                        screen.blit(ship_3[1], ((150 + (d+1)* 25, 90 + (t+1)*25)))
                if t + 1 < 11 and t + 2 < 11:
                    if (bf2[t][d] == 'z' or bf2[t][d] == '1') and bf2[t+1][d] == 'z' and bf2[t+2][d] == 'z':
                        screen.blit(ship_3[0], ((150 + (d+1)* 25, 90 + (t+1)*25)))   
                    
    def draw_battlefield_player2():                                            #Отрисовка второго поля для 2ого игрока
        text_hit = 'X'
        text = font.render(text_hit, True, white, None)
        text_miss = 'O'       
        text2 = font.render(text_miss, True, white, None)
        for t in range(1, 10):
            for d in range(1, 10):
                if bf2[t][d] == 'x':
                    screen.blit(ship_1, ((100 + (d+1)* 25), 40 + (t+1)*25))
                if d + 1 < 11:
                    if (bf2[t][d] == 'y' or bf2[t][d] == '1') and (bf2[t][d+1] == 'y' or bf2[t][d+1] == '1'):
                        screen.blit(ship_2[1], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                if t + 1 < 11:
                    if (bf2[t][d] == 'y' or bf2[t][d] == '1') and (bf2[t+1][d] == 'y' or bf2[t+1][d] == '1'):
                        screen.blit(ship_2[0], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                
                if d + 1 < 11 and d + 2 < 11:
                    if bf2[t][d] == 'z' and (bf2[t][d+1] == 'z' or bf2[t][d+1] == '1') and (bf2[t][d+2] == 'z' or bf2[t][d+2] == '1'):
                        screen.blit(ship_3[1], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                if t + 1 < 11 and d + 2 < 11:
                    if bf2[t][d] == 'z' and (bf2[t+1][d] == 'z' or bf2[t+1][d] == '1') and (bf2[t+2][d] == 'z' or bf2[t+2][d] == '1'):
                        screen.blit(ship_3[0], ((100 + (d+1)* 25, 40 + (t+1)*25)))
                
                if bf2[t][d] == '1':
                    texthitRect = text.get_rect()
                    texthitRect.center = (135+ (d*25), 50 + ((t+1)*25))               
                    screen.blit(text, texthitRect)
                elif bf2[t][d] == '2':
                    text2Rect = text.get_rect()
                    text2Rect.center = (135 + (d * 25), 50 + ((t+1) * 25))   
                    screen.blit(text2, text2Rect)                
                
                if bf_enemy_2[t][d] == '1':
                    texthitRect = text.get_rect()
                    texthitRect.center = (585+ (d*25), 75 + (t*25))               
                    screen.blit(text, texthitRect)
                elif bf_enemy_2[t][d] == '2':
                    text2Rect = text.get_rect()
                    text2Rect.center = (585 + (d * 25), 78 + (t * 25))   
                    screen.blit(text2, text2Rect)
                
    def battle_pvp():                                                          #Запуск игры против человека
        screen.blit(background, ((0,0))) 
        screen.blit(battlefield, ((100, 50)))
        screen.blit(battlefield, ((550, 50)))
        screen.blit(at_zone, ((575 + (locx*25), 65 + (locy*25))))
        if step == True:
            game.draw_battlefield_player1()
        elif step == False:
            game.draw_battlefield_player2()
        pygame.display.update()    
        
    
        


while run:                                                                     #Основной цикл игры
    pygame.time.delay(50)                                                      #Задача периода цикла
    
    for event in pygame.event.get():                                           #Если нажали на крест, игра закрывается
        '''выход из игры'''
        if event.type == pygame.QUIT:
            run = False  
    
    keys = pygame.key.get_pressed()                                            #Регистрация событий нажатия на кнопки
    
    main_menu()
    
    if keys[pygame.K_s]:
        time.sleep(0.1)
        if loc < 2:
            loc += 1
        elif loc == 2:
            loc = 0   
    elif keys[pygame.K_w]:
        time.sleep(0.1)
        if loc >= 1:
            loc -= 1
        elif loc == 0:
            loc = 2
    if keys[pygame.K_RETURN] and loc == 0:
        game_pve = True
    elif keys[pygame.K_RETURN] and loc == 1:
        game_pvp = True
    elif keys[pygame.K_RETURN] and loc == 2:
        run = False  
        
    if game_pve or game_pvp:
        bf = np.array([[0,1,2,3,4,5,6,7,8,9, ' ', ' '], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [3,  ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ', ' ', ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [' ', ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ']])
        bf2 = np.array([[0,1,2,3,4,5,6,7,8,9, ' ', ' '], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [3,  ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ', ' ', ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [' ', ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ']])
        bf_enemy = np.array([[0,1,2,3,4,5,6,7,8,9, ' ', ' '], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [3,  ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ', ' ', ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [' ', ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ']])
        bf_enemy_2 = np.array([[0,1,2,3,4,5,6,7,8,9, ' ', ' '], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [3,  ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ', ' ', ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [' ', ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ']])
        bf_comp = np.array([[0,1,2,3,4,5,6,7,8,9, ' ', ' '], [1, 'x', ' ' , 'x' , ' ', 'x' , ' ', ' ' , ' ' , ' ', ' ', ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [3,  ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ', ' ', ' '], [4, 'y', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [5, 'y', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [7, 'z', 'z' , 'z' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , 'y', 'y', ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' '], [' ', ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ', ' ', ' ']])
        preparation_1 = True
        preparation_2 = False
        step = True
        time.sleep(0.5)
    ship1 = 3
    ship2 = 2
    ship3 = 1    
    
    
    while game_pve:       
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            '''выход из игры'''
            if event.type == pygame.QUIT:
                run = False
                game_pve = False
        
        keys = pygame.key.get_pressed()
        if preparation_1:
            if keys[pygame.K_w]:
                if locy > 1:
                    locy -= 1
                else:
                    locy = 9-kd 
            if keys[pygame.K_s]:
                if locy < 9-kd:
                    locy += 1
                else:
                    locy = 1
                    
            if keys[pygame.K_a]:
                if locx > 1:
                    locx -= 1
                else:
                    locx = 9-kr
            if keys[pygame.K_d]:
                if locx < 9-kr:
                    locx += 1
                else:
                    locx = 1       
            if keys[pygame.K_q]:
                i -= 1
                if i < 0:
                    i = 1
                    lmove = 'right'
                else: 
                    lmove = 'down'
                time.sleep(0.2)
            if keys[pygame.K_e]:
                i += 1
                if i > 1:
                    i = 0
                    lmove = 'down'
                else:
                    lmove = 'right'
                time.sleep(0.2)
            if keys[pygame.K_RETURN]:
                time.sleep(0.2)
                if ship1 > 0:
                    bf[locy][locx] = 'x'
                    ship1 -= 1
                    kd = 0
                    kr = 0
                elif ship1 == 0 and ship2 > 0:
                    ship2 -= 1
                    bf[locy][locx] = 'y'
                    if lmove == 'down':
                        bf[locy+1][locx] = 'y'
                    elif lmove == 'right':
                        bf[locy][locx+1] = 'y'
                    if lmove == 'down':
                        kd = 2
                        kr = 0
                    elif lmove == 'right':
                        kr = 2
                        kd = 0 
                elif ship1 == 0 and ship2 == 0 and ship3 > 0:
                    ship3 -= 1
                    bf[locy][locx] = 'z'
                    if lmove == 'down':
                        bf[locy+1][locx] = 'z'
                        bf[locy+2][locx] = 'z'
                    if lmove == 'right':
                        bf[locy][locx+1] = 'z'
                        bf[locy][locx+2] = 'z' 
                    if lmove == 'down':
                        kd = 3
                        kr = 0
                    elif lmove == 'right':
                        kr = 3
                        kd = 0 
                        
            game.fill_battlefield_player1()
            
            if ship1 == 0 and ship2 == 0 and ship3 == 0:
                preparation_1 = False     
                battle = True
                hp_p1 = 10 
                hp_bot = 10
                step = True
                locx = 1
                locy = 1
                time.sleep(0.5)
        if battle:
            game.battle_pve()
            if keys[pygame.K_w]:
                if locy > 1:
                    locy -= 1
                else:
                    locy = 9
            if keys[pygame.K_s]:
                if locy < 9:
                    locy += 1
                else:
                    locy = 1
                    
            if keys[pygame.K_a]:
                if locx > 1:
                    locx -= 1
                else:
                    locx = 9
            if keys[pygame.K_d]:
                if locx < 9:
                    locx += 1
                else:
                    locx = 1  
            
            if keys[pygame.K_RETURN]:
                time.sleep(0.2) 
                if step:
                    if bf_comp[locy,locx] != ' ':
                        hp_bot -= 1
                        bf_enemy[locy, locx] = '1'
                    elif bf_comp[locy,locx] == ' ':
                        bf_enemy[locy, locx] = '2'
                        step = False
                if not step:
                    pos1 = random.randint(1, 10)
                    pos2 = random.randint(1,10)
                    if bf[pos1][pos2] != '2':
                        if bf[pos1][pos2] == 'x' or bf[pos1][pos2]== 'y' or bf[pos1][pos2] == 'z':
                            hp_p1 -= 1
                            bf[pos1][pos2] = '1'
                        elif bf[pos1][pos2] == ' ':
                            step = True
                            bf[pos1][pos2] = '2'
            if hp_bot == 0:
                text = 'You Win'
                text3 = font.render(text, True, white, None)
                text3Rect = text3.get_rect()
                text3Rect.center = (300, 375)       
                screen.blit(text3, text3Rect)      
                game_pve = False
                time.sleep(0.5)
            elif hp_p1 == 0:
                text = 'You lose'
                text3 = font.render(text, True, white, None)
                text3Rect = text3.get_rect()
                text3Rect.center = (300, 375)       
                screen.blit(text3, text3Rect) 
                game_pve = False
                time.sleep(0.5)
        
    while game_pvp:
        pygame.time.delay(50)
        
        for event in pygame.event.get():
            '''выход из игры'''
            if event.type == pygame.QUIT:
                run = False
                game_pve = False
        
        keys = pygame.key.get_pressed()

        if preparation_1:
            if keys[pygame.K_w]:
                if locy > 1:
                    locy -= 1
                else:
                    locy = 9-kd
            if keys[pygame.K_s]:
                if locy < 9-kd:
                    locy += 1
                else:
                    locy = 1
                    
            if keys[pygame.K_a]:
                if locx > 1:
                    locx -= 1
                else:
                    locx = 9-kr
            if keys[pygame.K_d]:
                if locx < 9-kr:
                    locx += 1
                else:
                    locx = 1       
            if keys[pygame.K_q]:
                i -= 1
                if i < 0:
                    i = 1
                    lmove = 'right'
                else: 
                    lmove = 'down'
                time.sleep(0.2)
            if keys[pygame.K_e]:
                i += 1
                if i > 1:
                    i = 0
                    lmove = 'down'
                else:
                    lmove = 'right'
                time.sleep(0.2)
            if keys[pygame.K_RETURN]:
                time.sleep(0.2)
                if ship1 > 0:
                    bf[locy][locx] = 'x'
                    ship1 -= 1
                    kd = 0
                    kr = 0
                elif ship1 == 0 and ship2 > 0:
                    ship2 -= 1
                    bf[locy][locx] = 'y'
                    if lmove == 'down':
                        bf[locy+1][locx] = 'y'
                    elif lmove == 'right':
                        bf[locy][locx+1] = 'y'
                    if lmove == 'down':
                        kd = 2
                        kr = 0
                    elif lmove == 'right':
                        kr = 2
                        kd = 0 
                elif ship1 == 0 and ship2 == 0 and ship3 > 0:
                    ship3 -= 1
                    bf[locy][locx] = 'z'
                    if lmove == 'down':
                        bf[locy+1][locx] = 'z'
                        bf[locy+2][locx] = 'z'
                    if lmove == 'right':
                        bf[locy][locx+1] = 'z'
                        bf[locy][locx+2] = 'z'
                    if lmove == 'down':
                        kd = 3
                        kr = 0
                    elif lmove == 'right':
                        kr = 3
                        kd = 0 

            game.fill_battlefield_player1()
            
            if ship1 == 0 and ship2 == 0 and ship3 == 0:
                preparation_1 = False
                preparation_2 = True
                ship1 = 3
                ship2 = 2
                ship3 = 1
                kd = 0
                kr = 0
        
                
        elif not preparation_1 and preparation_2:
            if keys[pygame.K_w]:
                if locy > 1:
                    locy -= 1
                else:
                    locy = 9-kd
            if keys[pygame.K_s]:
                if locy < 9-kd:
                    locy += 1
                else:
                    locy = 1
                    
            if keys[pygame.K_a]:
                if locx > 1:
                    locx -= 1
                else:
                    locx = 9-kr
            if keys[pygame.K_d]:
                if locx < 9-kr:
                    locx += 1
                else:
                    locx = 1       
            if keys[pygame.K_q]:
                i -= 1
                if i < 0:
                    i = 1
                    lmove = 'right'
                else: 
                    lmove = 'down'
                time.sleep(0.2)
            if keys[pygame.K_e]:
                i += 1
                if i > 1:
                    i = 0
                    lmove = 'down'
                else:
                    lmove = 'right'
                time.sleep(0.2)
                
            if keys[pygame.K_RETURN]:
                time.sleep(0.2)
                if ship1 > 0:
                    bf2[locy][locx] = 'x'
                    ship1 -= 1
                    kr = 0
                    kd = 0
                elif ship1 == 0 and ship2 > 0:
                    ship2 -= 1
                    bf2[locy][locx] = 'y'
                    if lmove == 'down':
                        bf2[locy+1][locx] = 'y'
                    elif lmove == 'right':
                        bf2[locy][locx+1] = 'y'
                    if lmove == 'down':
                        kd = 2
                        kr = 0
                    elif lmove == 'right':
                        kr = 2
                        kd = 0
                elif ship1 == 0 and ship2 == 0 and ship3 > 0:
                    ship3 -= 1
                    bf2[locy][locx] = 'z'
                    if lmove == 'down':
                        bf2[locy+1][locx] = 'z'
                        bf2[locy+2][locx] = 'z'
                    if lmove == 'right':
                        bf2[locy][locx+1] = 'z'
                        bf2[locy][locx+2] = 'z'
                        if lmove == 'down':
                            kd = 3
                            kr = 0
                        elif lmove == 'right':
                            kr = 3
                            kd = 0                    

            game.fill_battlefield_player2()
            
            if ship1 == 0 and ship2 == 0 and ship3 == 0:
                preparation_2 = False   
                step = 1
                hp_p1 = 10
                hp_p2 = 10
                battle = True
            
        if battle:
            game.battle_pvp()
            if keys[pygame.K_w]:
                if locy > 1:
                    locy -= 1
                else:
                    locy = 9
            if keys[pygame.K_s]:
                if locy < 9:
                    locy += 1
                else:
                    locy = 1
                    
            if keys[pygame.K_a]:
                if locx > 1:
                    locx -= 1
                else:
                    locx = 9
            if keys[pygame.K_d]:
                if locx < 9:
                    locx += 1
                else:
                    locx = 1  
            
            if keys[pygame.K_RETURN]:
                time.sleep(0.2) 
                if step:
                    if bf2[locy,locx] != ' ':
                        hp_p2 -= 1
                        bf_enemy[locy, locx] = '1'
                        bf2[locy, locx] = '1'
                    elif bf2[locy,locx] == ' ':
                        bf_enemy[locy, locx] = '2'
                        bf2[locy,locx] = '2'
                        step = False
                        time.sleep(0.5)
                if step == False:
                    if bf[locy,locx] != ' ':
                        hp_p1 -= 1
                        bf_enemy_2[locy, locx] = '1'
                        bf[locy,locx] = '1'
                    elif bf2[locy,locx] == ' ':
                        bf_enemy_2[locy, locx] = '2'
                        bf[locy,locx] = '2'
                        step = True  
                        time.sleep(1)
            if hp_p1 == 0:
                text = 'P1 wins'
                text3 = font.render(text, True, white, None)
                text3Rect = text3.get_rect()
                text3Rect.center = (300, 375)       
                screen.blit(text3, text3Rect)  
                time.sleep(1)
                game_pvp = False
            elif hp_p1 == 0:
                text = 'P2 wins'
                text3 = font.render(text, True, white, None)
                text3Rect = text3.get_rect()
                text3Rect.center = (300, 375)       
                screen.blit(text3, text3Rect) 
                game_pvp = False    
                time.sleep(1)
    
pygame.quit()
