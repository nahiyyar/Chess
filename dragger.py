from const import *
import pygame
class Dragger:
    def __init__(self):
        self.dragging=False
        self.piece=None
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self,surface):
        self.piece.set_texture(size=128)
        texture = self.piece.texture

        img= pygame.image.load(texture)
        img_centre = (self.mouseX,self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_centre)
        surface.blit(img,self.piece.texture_rect)

    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos
    
    def save_initial(self,pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] //SQSIZE
    
    def drag_piece(self,piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self,piece):
        self.piece = None
        self.dragging = False