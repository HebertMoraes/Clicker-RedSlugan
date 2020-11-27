import pygame as pg
from Aprender.jogo_clicar.principal.valores import Valores


class SpriteQualquer(pg.sprite.Sprite):

    def __init__(self, grupos, x, y, caminho):
        pg.sprite.Sprite.__init__(self, grupos)
        self.image = pg.image.load(caminho)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def alterarTamanho(self, largura, altura):
        self.image = pg.transform.scale(self.image, (largura, altura))


class Botao(pg.sprite.Sprite):

    def __init__(self, grupos, x, y, caminho):
        pg.sprite.Sprite.__init__(self, grupos)
        self.image = pg.image.load(caminho)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicou(self, pos_mouse, xmin, xmax, ymin, ymax):
        if pg.mouse.get_pressed()[0]:
            if xmin < pos_mouse[0] < xmax and ymin < pos_mouse[1] < ymax:
                return True
            else:
                return False
        else:
            return False


class CaixaDeTexto(pg.sprite.Sprite):

    def __init__(self, grupos, x, y, texto, cor, tamanho):
        pg.sprite.Sprite.__init__(self, grupos)
        self.fnt = pg.font.Font(pg.font.get_default_font(), tamanho)
        self.image = self.fnt.render(texto, True, cor)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
