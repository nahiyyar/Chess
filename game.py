import pygame
import sys
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board=Board()
        self.dragger=Dragger()
        self.next_player="white"

    def draw_board(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                color =CAMEL if (row+col)%2==0 else DARKGREEN
                rect=(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)

                pygame.draw.rect(surface,color,rect)

    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_centre = col*SQSIZE+SQSIZE//2 , row*SQSIZE+SQSIZE//2
                        piece.texture_rect = img.get_rect(center=img_centre)
                        surface.blit(img,piece.texture_rect)
    
    def show_moves(self,surface):
        if self.dragger.dragging:
            piece=self.dragger.piece
            if isinstance(piece.moves, list):
                for move in piece.moves:

                    color="#C86464" if (move.final.row+move.final.col) % 2 == 0 else "#C84646"
                    rect=(move.final.col*SQSIZE,move.final.row*SQSIZE, SQSIZE,SQSIZE)
                    pygame.draw.rect(surface,color,rect)

    def next_turn(self):
        self.next_player = "white" if self.next_player=="black" else "black"
    
    def reset(self):
        self.__init__()


