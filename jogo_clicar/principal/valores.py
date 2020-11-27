import pygame as pg


class Valores():

    LARGURA_TELA = 800
    ALTURA_TELA = 600

    tela = pg.display.set_mode([LARGURA_TELA, ALTURA_TELA])
    pg.display.set_caption("Mate os Slugan's malvados!!")
    todos_sprites = pg.sprite.Group()

    clock = pg.time.Clock()

    estar_menu = True
    estar_jogo = False
    prime_menu = True
    prime_jogo = True
    rodando = True

    pontos = 0