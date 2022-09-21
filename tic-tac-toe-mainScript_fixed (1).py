from tkinter import *
from tkinter import messagebox
f = [0,0,0,0,0,0,0,0,0] #fields -> f, for make my work faster
window = Tk()
import os, sys

player = True

def click():
    isDraw()
    isWinO()
    isWinX()

def winmsgbX():
    Mb = messagebox.askquestion ('The Player1 has won!','The Player1 has won!\n Do you wanna play again?')
    if Mb == 'yes':
        pass
        # must be restart func, but I didn't find any workable information
    elif Mb =='no':
        window.destroy()
def winmsgbO():
    Mb = messagebox.askquestion ('The Player2 has won!','The Player2 has won!\n Do you wanna play again?')
    if Mb == 'yes':
        pass
        # must be restart func, but I didn't find any workable information
    elif Mb =='no':
        window.destroy()
def drawmsg():
    Mb = messagebox.askquestion ('The Draw!','The Draw!\n Do you wanna play again?')
    if Mb == 'yes':
        pass
        # must be restart func, but I didn't find any workable information
    elif Mb =='no':
        window.destroy()
def click1():
    global player
    if f[0] == 0:
        if player:
            f[0] = 1
            b1['text'] = 'X'
        else:
            f[0] = -1
            b1['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player


def click2():
    global player
    if f[1] == 0:
        if player:
            f[1] = 1
            b2['text'] = 'X'
        else:
            f[1] = -1
            b2['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click3():
    global player
    if f[2] == 0:
        if player:
            f[2] = 1
            b3['text'] = 'X'
        else:
            f[2] = -1
            b3['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click4():
    global player
    if f[3] == 0:
        if player:
            f[3] = 1
            b4['text'] = 'X'
        else:
            f[3] = -1
            b4['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click5():
    global player
    if f[4] == 0:
        if player:
            f[4] = 1
            b5['text'] = 'X'
        else:
            f[4] = -1
            b5['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click6():
    global player
    if f[5] == 0:
        if player:
            f[5] = 1
            b6['text'] = 'X'
        else:
            f[5] = -1
            b6['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click7():
    global player
    if f[6] == 0:
        if player:
            f[6] = 1
            b7['text'] = 'X'
        else:
            f[6] = -1
            b7['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click8():
    global player
    if f[7] == 0:
        if player:
            f[7] = 1
            b8['text'] = 'X'
        else:
            f[7] = -1
            b8['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player
def click9():
    global player
    if f[8] == 0:
        if player:
            f[8] = 1
            b9['text'] = 'X'
        else:
            f[8] = -1
            b9['text'] = 'O'
        print(f)
        if player:
            lable_turn['text'] = f'Сейчас очередь Player2'
        else:
            lable_turn['text'] = f'Сейчас очередь Player1'
        click()
        player = not player

def isWinX():
    if(f[0] == f[1] == f[2] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[0] == f[3] == f[6] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[0] == f[4] == f[8] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[1] == f[4] == f[7] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[2] == f[5] == f[8] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[3] == f[4] == f[5] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[6] == f[7] == f[8] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
    elif (f[2] == f[4] == f[6] == 1):
        print('Player1 Win')
        label_win['text'] = 'Player1 win'
        winmsgbX()
def isWinO():
    if(f[0] == f[1] == f[2] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[0] == f[3] == f[6] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[0] == f[4] == f[8] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[1] == f[4] == f[7] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[2] == f[5] == f[8] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[3] == f[4] == f[5] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[6] == f[7] == f[8] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
    elif (f[2] == f[4] == f[6] == -1):
        print('Player2 Win')
        label_win['text'] = 'Player2 win'
        winmsgbO()
def isDraw():
    filed = 0
    for field in f:
        if field != 0:
            filed += 1
    if filed == 9:
        print('Draw')
        label_win['text'] = 'Draw'
        drawmsg()


# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - 600 / 2)
center_y = int(screen_height/2 - 600 / 2)

# set the position of the window to the center of the screen
window.geometry(f'600x600+{center_x}+{center_y}')
window.resizable(0,0)
label = Label(text='Игра "Крестики-Нолики"', font="Arial 24")
lable_turn = Label(text=f'Сейчас очередь Player1', font='Arial 10')
label_win = Label(text='')
b1 = Button(text='')
b1.config(command=click1)
b1.place(x = 185, y = 140, width = 70, height=70)


b2 = Button(text='')
b2.config(command=click2)
b2.place(x = 265, y = 140, width = 70, height=70)


b3 = Button(text='')
b3.config(command=click3)
b3.place(x = 345, y = 140, width = 70, height=70)


b4 = Button(text='')
b4.config(command=click4)
b4.place(x = 185, y = 220, width = 70, height=70)


b5 = Button(text='')
b5.config(command=click5)
b5.place(x = 265, y = 220, width = 70, height=70)


b6 = Button(text='')
b6.config(command=click6)
b6.place(x = 345, y = 220, width = 70, height=70)


b7 = Button(text='')
b7.config(command=click7)
b7.place(x = 185, y = 300, width = 70, height=70)


b8 = Button(text='', height=10, width=10)
b8.config(command=click8)
b8.place(x = 265, y = 300, width = 70, height=70)


b9 = Button(text='')
b9.config(command=click9)
b9.place(x = 345, y = 300, width = 70, height=70)


b_leave = Button(text='LEAVE')
b_leave.config(command=window.destroy)
b_leave.place(x = 250, y = 500, width = 100, height=70)


label.pack()
label_win.pack()
lable_turn.pack()
window.mainloop()