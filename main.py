import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move

class Main:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.game=Game()
    def mainloop(self):
        # running=True

        game=self.game
        screen=self.screen
        dragger=self.game.dragger
        board=self.game.board

        while True:
            
            game.draw_board(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row=dragger.mouseY//SQSIZE
                    clicked_col=dragger.mouseX//SQSIZE
                    
                    if 0<=clicked_row<8 and 0 <=clicked_col<8:
                        if board.squares[clicked_row][clicked_col].has_piece():
                            piece=board.squares[clicked_row][clicked_col].piece
                            if piece.color == game.next_player:
                                board.calculate_moves(piece,clicked_row,clicked_col)
                                dragger.save_initial(event.pos)
                                dragger.drag_piece(piece)

                                game.draw_board(screen)
                                game.show_moves(screen)
                                game.show_pieces(screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row=dragger.mouseY//SQSIZE
                        released_col=dragger.mouseX//SQSIZE

                        initial=Square(dragger.initial_row,dragger.initial_col)
                        final=Square(released_row,released_col)

                        move=Move(initial,final)

                        if board.valid_move(dragger.piece,move):
                            board.move(dragger.piece,move)

                            game.draw_board(screen)
                            game.show_pieces(screen)

                            game.next_turn()

                    dragger.undrag_piece(piece)
                    

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.draw_board(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main=Main()
main.mainloop()