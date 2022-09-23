import time
import pygame
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((575, 575))
pygame.display.set_caption('Tic Tac Toe')

grid = pygame.image.load("resources/grid.png").convert()
O = pygame.image.load("resources/o.png").convert_alpha()
X = pygame.image.load("resources/x.png").convert_alpha()
trophy = pygame.image.load("resources/trophy.png").convert_alpha()
tie = pygame.image.load("resources/tie.png").convert_alpha()
sliver = pygame.image.load("resources/sliver.png").convert()

class board():
    def __init__(self, surface):
        self.surface = surface
        self.board = [[' ']*3, [' ']*3, [' ']*3]
        self.round_count = 1
        
        self.side = 175
        self.pixel = 25
        self.len1 = len(self.board)
        self.len2 = len(self.board[0])
    
    def play(self):
        pygame.event.clear()
        while True:
            self.display()
            boln, win = self.win_check()
            if boln:
                self.exit_sequence(win)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        Board = board(surface)
                        Board.play()
                    if event.key == K_ESCAPE:
                        quit()
                if event.type == MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    self.turn(x_mouse, y_mouse)

    def display(self):
        self.surface.blit(grid, (0, 0))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == ' ':
                    continue
                if self.board[i][j] == 'X':
                    obj = X
                else:
                    obj = O
                x = (self.side + self.pixel) * j
                y = (self.side + self.pixel) * i
                self.surface.blit(obj, (x, y))
        pygame.display.flip()

    def turn(self, x, y):
        i, j = -1, -1
        temp = self.side + self.pixel
        
        if y >= 0 and y <=self.side:
            i = 0
        elif y >= temp and y <= temp + self.side:
            i = 1
        elif y >=  temp * 2 and y <= (self.side * 3) + (self.pixel * 2):
            i = 2
        
        if x >= 0 and x <=self.side:
            j = 0
        elif x >= temp and x <= temp + self.side:
            j = 1
        elif x >= temp * 2 and x <= (self.side * 3) + (self.pixel * 2):
            j = 2

        if not i == -1 and not j == -1:
            if not self.round_count % 2 == 0:
                temp = 'X'
            else:
                temp = 'O'
            if self.board[i][j] == ' ':
                self.board[i][j] = temp
                self.round_count += 1

    def win_check(self):
        nboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(self.len1):
            for j in range(self.len2):
                if self.board[i][j] == 'X':
                    nboard[i][j] = 1
                if self.board[i][j] == 'O':
                    nboard[i][j] = 4
        
        sum = 0
        for i in range(self.len1):
            sum += nboard[i][i]
        
        if sum == 3:
            return True, 'X'
        elif sum == 12:
            return True, 'O'
        
        sum, c = 0, 0
        for i in range(self.len1-1, -1, -1):
            sum += nboard[c][i]
            c += 1
        
        if sum == 3:
            return True, 'X'
        elif sum == 12:
            return True, 'O'

        for i in range(self.len1):
            sum_h, sum_v = 0, 0
            for j in range(self.len2):
                sum_h += nboard[i][j]
                sum_v += nboard[j][i]
            if sum_h == 3 or sum_v == 3:
                return True, 'X'
            elif sum_h == 12 or sum_v == 12:
                return True, 'O'
        
        if self.round_count == 10:
           return True, 'T'
        
        return False, ' '
            
    def exit_sequence(self, win):
        temp = self.side + self.pixel
        if win == 'T':
            for i in range(3):
                self.surface.blit(tie, (0, temp))
                self.flash()
        elif win == 'X':
            obj = X
        elif win == 'O':
            obj = O
        if not win == 'T':
            for i in range(3):
                self.surface.blit(sliver, (0, temp))
                self.surface.blit(trophy, (100 + temp, temp))
                self.surface.blit(obj, (100, temp))
                self.flash()
        Board = board(surface)
        Board.play()
        print('reached')

    def flash(self):
        t = 0.5
        pygame.display.flip()
        time.sleep(t+0.3)
        self.display()
        pygame.display.flip()
        time.sleep(t)

Board = board(surface)
Board.play()