bf = np.array([['','','ваше ', '','', '','поле ', '', '', ''],[0,1,2,3,4,5,6,7,8,9], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [3, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ']])
bf2 = np.array([['','','ваше ', '','', '','поле ', '', '', ''],[0,1,2,3,4,5,6,7,8,9], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [3, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ']])
bf_enemy = np.array([['','','чужое', '','', '','поле', '', '', ''],[0,1,2,3,4,5,6,7,8,9], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [3, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ']])
bf_enemy_2 = np.array([['','','чужое', '','', '','поле', '', '', ''],[0,1,2,3,4,5,6,7,8,9], [1, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [2, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [3, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [5, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ']])
bf_comp = np.array([['','','чужое', '','', '','поле', '', '', ''],[0,1,2,3,4,5,6,7,8,9], [1, 'x', ' ' , 'x' , ' ', 'x' , ' ', ' ' , ' ' , ' '], [2, ' ', ' ' , ' ' , '', ' ' , ' ', ' ' , ' ' , ' '], [3, 'x', 'x' , ' ' , 'x', 'x' , ' ', ' ' , ' ' , ' '], [4, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [5, 'x', 'x' , 'x' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [6, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [7, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [8, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' '], [9, ' ', ' ' , ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ']])
game = True

class battleship:
    def show_battlefield_player1():
        
    def show_battlefield_player2():
         
    def fill_battlefield_player1():
        ship_1 = 3
        ship_2 = 4
        ship_3 = 3
        print(bf[0])
        print(bf[1])
        print(bf[2])
        print(bf[3])
        print(bf[4])
        print(bf[5])
        print(bf[6])
        print(bf[7])
        print(bf[8])
        print(bf[9])
        print(bf[10])        
        print('Расставьте корабли при помощи указания их места последовательно указав строку и столбец')
        print('Расставьте 3 однопалубных корабля')
        while ship_1 > 0:
            x = int(input())
            y = int(input())
            x += 1
            bf[x,y] = 'x'
            ship_1 -= 1
        print('Расставьте 2 двухпалубных корабля')
        while ship_2 > 0:
            x = int(input())
            y = int(input())
            x += 1
            bf[x,y] = 'x'
            t1 = x
            t2 = y
            ship_2 -= 1
            x = int(input())
            y = int(input())
            if x not in range(t1-1, t1+2) and y not in range(t2-1, t2+2):
                print('что-то пошло не так')
                print('Введите переменные снова')
                ship_2 += 1
                bf[t1,t2] = ' '
            else:
                x += 1
                bf[x,y] = 'x'
                ship_2 -= 1         
        print('Расставьте 1 трёхпалубный корабль по 2 крайним точкам')     
        while ship_3 > 0:
            x = int(input())
            y = int(input())
            x += 1
            bf[x,y] = 'x'
            t1 = x
            t2 = y
            ship_3 -= 1
            x = int(input())
            y = int(input())
            if x not in range(t1-2, t1+3) and y not in range(t2-2, t2+3):
                print('что-то пошло не так')
                print('Введите переменные снова')
                ship_3 += 1
                bf[t1,t2] = ' '
            else:
                x += 1
                bf[x,y] = 'x'
                ship_3 -= 1
            k1 = (x+t1)//2
            k2 = (y+t2)//2
            bf[k1,k2] = 'x'
            ship_3 -= 1
    def fill_battlefield_player2():
        ship_1 = 3
        ship_2 = 4
        ship_3 = 3
        print(bf2[0])
        print(bf2[1])
        print(bf2[2])
        print(bf2[3])
        print(bf2[4])
        print(bf2[5])
        print(bf2[6])
        print(bf2[7])
        print(bf2[8])
        print(bf2[9])
        print(bf2[10])        
        print('Расставьте корабли при помощи указания их места последовательно указав строку и столбец')
        print('Расставьте 3 однопалубных корабля')
        while ship_1 > 0:
            x = int(input())
            y = int(input())
            x += 1
            bf2[x,y] = 'x'
            ship_1 -= 1

        print('Расставьте 2 двухпалубных корабля')
        while ship_2 > 0:
            x = int(input())
            y = int(input())
            x += 1
            bf2[x,y] = 'x'
            t1 = x
            t2 = y
            ship_2 -= 1
            x = int(input())
            y = int(input())
            if x not in range(t1-1, t1+2) and y not in range(t2-1, t2+2):
                print('что-то пошло не так')
                print('Введите переменные снова')
                ship_2 += 1
                bf2[t1,t2] = ' '
            else:
                x += 1
                bf2[x,y] = 'x'
                ship_2 -= 1         
        print('Расставьте 1 трёхпалубный корабль по 2 крайним точкам')     
        while ship_3 > 0:
            x = int(input())
            y = int(input())
            x += 1
            bf2[x,y] = 'x'
            t1 = x
            t2 = y
            ship_3 -= 1
            x = int(input())
            y = int(input())
            if x not in range(t1-2, t1+3) and y not in range(t2-2, t2+3):
                print('что-то пошло не так')
                print('Введите переменные снова')
                ship_3 += 1
                bf2[t1,t2] = ' '
            else:
                x += 1
                bf2[x,y] = 'x'
                ship_3 -= 1
            k1 = (x+t1)//2
            k2 = (y+t2)//2
            bf2[k1,k2] = 'x'
            ship_3 -= 1    
        
    def pvp():
        match = True
        Player1 = 10
        Player2 = 10
        motion = True        
        while match:
            if motion:
                battleship.show_battlefield_player1()
                print('введите куда стрелять')
                x = int(input())
                x+=1
                y = int(input())
                if bf2[x,y] == 'x':
                    print('Попал!')
                    Player2 -= 1
                    bf_enemy[x,y] = '!'
                    bf2[x,y] = '!'
                else:
                    print('Промах!')
                    motion = False
                    bf_enemy[x,y] = '0'
                    bf2[x,y] = '0'
            else:
                battleship.show_battlefield_player2()
                print('введите куда стрелять')
                x = int(input())
                x+=1
                y = int(input())
                if bf[x,y] == 'x':
                    print('Попал!')
                    Player1 -= 1
                    bf_enemy_2[x,y] = '!'
                    bf[x,y] = '!'
                else:
                    print('Промах!')  
                    motion = True
                    bf_enemy_2[x,y] = '0'
                    bf[x,y] = '0'
            if Player1 == 0:
                print('Игрок 1 проиграл!')
                match = False
            elif Player2 == 0:
                print('Игрок 2 проиграл!')
                match = False
    def pve():
        match = True
        Player1 = 10
        PC = 10
        motion = True    
        while match:
            if motion:
                battleship.show_battlefield_player1()
                print('введите куда стрелять')
                x = int(input())
                x+=1
                y = int(input())
                if bf_comp[x,y] == 'x':
                    print('Попал!')
                    PC -= 1
                    bf_enemy[x,y] = '!'
                else:
                    print('Промах!')
                    motion = False
                    bf_enemy[x,y] = '0'   
            else:
                x = random.randint(2, 10)
                y = random.randint(1,10)
                if bf[x,y] != ' ':
                    Player1 -= 1
                    bf[x,y] = '!'
                else:
                    motion = True
                    bf[x,y] = '0'
                if Player1 == 0:
                    print('Игрок 1 !')
                    match = False
                elif PC == 0:
                    print('Компьютер не выйграл!')
                    match = False


match = False                    
                    
    
    
while game:
    print('Меню')
    print('Если вы хотите играть против компьютера, нажмите - "1"')
    print('Если вы хотите играть против человека, нажмите - "2"')
    print('Для выхода нажмите - "0"')
    k = int(input())
    if k == 0:
        break
    if k == 1:
        battleship.fill_battlefield_player1()
        battleship.pve()
    if k == 2:
        battleship.fill_battlefield_player1()
        battleship.fill_battlefield_player2()
        battleship.pvp()



    