from random import randint
import pygame as pg
from Aprender.jogo_clicar.principal.valores import *


class Inimigo(pg.sprite.Sprite):

    def __init__(self, grupos, x, y, caminho):
        pg.sprite.Sprite.__init__(self, grupos)
        self.image = pg.image.load(caminho)
        self.primeiraImagem = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.tempoInicial = pg.time.get_ticks()
        self.esmagar = pg.mixer.Sound("assets/Wet_splat_01.ogg")

    def atualizar_inimigo(self):

        if self.clicou(pg.mouse.get_pos(), self.rect.left, self.rect.right, self.rect.top, self.rect.bottom):
            self.esmagar.play()
            self.mover()
            self.aumentarPontos()

        elif (pg.time.get_ticks() - self.tempoInicial) > 3000:
            self.mover()

    def clicou(self, pos_mouse, xmin, xmax, ymin, ymax):
        if pg.mouse.get_pressed()[0]:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    if xmin < pos_mouse[0] < xmax and ymin < pos_mouse[1] < ymax:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

    def mover(self):

        self.rect.center = (randint(80, Valores.LARGURA_TELA - 60), randint(80, Valores.ALTURA_TELA - 60))
        self.tamanho = randint(50, 350)
        self.image = pg.transform.scale(self.primeiraImagem, (self.tamanho, self.tamanho))
        self.tempoInicial = pg.time.get_ticks()

    def aumentarPontos(self):
        Valores.pontos += 1