import pygame as pg
from Aprender.jogo_clicar.principal.inimigo import Inimigo
from Aprender.jogo_clicar.principal.objetos import *
from Aprender.jogo_clicar.principal.valores import *
import random


class JogoPrincipal:

    def __init__(self):

        self.fundoJogo = SpriteQualquer(Valores.todos_sprites, 400, 300, "assets/fundoGameplay.png")
        self.inimigo1 = Inimigo(Valores.todos_sprites, random.randint(20, Valores.LARGURA_TELA - 20),
                                random.randint(20, Valores.ALTURA_TELA - 20), "assets/redSlime.png")
        self.placar = CaixaDeTexto(Valores.todos_sprites, Valores.LARGURA_TELA // 2, Valores.ALTURA_TELA - 50,
                                   "Placar: " + str(Valores.pontos), pg.Color("Red"), 40)
        Valores.prime_jogo = False

    def atualizar(self):

        self.inimigo1.atualizar_inimigo()
        self.placar.image = self.placar.fnt.render("Placar: " + str(Valores.pontos), True, pg.Color("Red"))

    def encerrarJogo(self):
        pass
