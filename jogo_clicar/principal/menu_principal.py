import pygame as pg
from Aprender.jogo_clicar.principal.objetos import *
from Aprender.jogo_clicar.principal.valores import *


class MenuPrincipal:

    def __init__(self):

        self.fundo = SpriteQualquer(Valores.todos_sprites, 1000, 1000, "assets/fundoMenu.png")
        self.titulo = CaixaDeTexto(Valores.todos_sprites, 1000, 1000, "Clicker RedSlugan", pg.Color("Red"), 55)
        self.fundoBtn = SpriteQualquer(Valores.todos_sprites, 1000, 1000, "assets/shadow.png")
        self.fundoBtn.alterarTamanho(480, 150)
        self.btnIniciar = Botao(Valores.todos_sprites, 1000, 1000, "assets/btnJogar.png")
        self.btnSair = Botao(Valores.todos_sprites, 1000, 1000, "assets/btnSair.png")
        self.txtCred = CaixaDeTexto(Valores.todos_sprites, 1000, 1000, "Hebert | Jhony | Erick", pg.Color("Black"), 30)
        self.logoSlimeInc = SpriteQualquer(Valores.todos_sprites, 1000, 1000, "assets/logoSlimeIncMenor.png")
        self.btnClicarSom = pg.mixer.Sound("assets/BOOOING_1.ogg")
        Valores.prime_menu = False

    def atualizar(self):

        self.fundo.rect.center = [Valores.LARGURA_TELA // 2, Valores.ALTURA_TELA //2]
        self.logoSlimeInc.rect.center = [55, (Valores.ALTURA_TELA // 2) + 220]
        self.titulo.rect.center = [Valores.LARGURA_TELA // 2, (Valores.ALTURA_TELA //2) - 200]
        self.fundoBtn.rect.center = [(Valores.LARGURA_TELA // 2) - 225, (Valores.ALTURA_TELA //2) + 40]
        self.btnIniciar.rect.center = [(Valores.LARGURA_TELA // 2) - 120, (Valores.ALTURA_TELA //2) + 100]
        self.btnSair.rect.center = [(Valores.LARGURA_TELA // 2) + 120, (Valores.ALTURA_TELA // 2) + 100]
        self.txtCred.rect.center = [(Valores.LARGURA_TELA // 2), (Valores.ALTURA_TELA // 2) + 250]

        if self.btnIniciar.clicou(pg.mouse.get_pos(), self.btnIniciar.rect.left, self.btnIniciar.rect.right,
                                  self.btnIniciar.rect.top,self.btnIniciar.rect.bottom):
            self.btnClicarSom.play()
            MenuPrincipal.encerrarMenu(self)
            Valores.estar_menu = False
            Valores.estar_jogo = True

        if self.btnSair.clicou(pg.mouse.get_pos(), self.btnSair.rect.left, self.btnSair.rect.right,
                                  self.btnSair.rect.top,self.btnSair.rect.bottom):
            self.btnClicarSom.play()
            Valores.rodando = False

    def encerrarMenu(self):

        self.fundo.rect.center = ([2000, 2000])
        self.logoSlimeInc.rect.center = ([1000, 1000])
        self.titulo.rect.center = ([1000, 1000])
        self.btnIniciar.rect.center = ([1000, 1000])
        self.btnSair.rect.center = ([1000, 1000])
        self.txtCred.rect.center = ([1000, 1000])
