from Aprender.jogo_clicar.principal.jogo_objetos import *
import pygame as pg
from random import *


# Definindo a classe inicial
class MainInicial:

    # Sempre a primeira função a ser executada
    def __init__(self):

        # definindo a constante do tamanho da tela
        self.LARGURA = 700

        # definindo a constante do tamanho da tela
        self.ALTURA = 600

        # inicializa o pygame (obrigatório para funcionar)
        pg.init()

        # definingo a janela e seu tamanho
        self.tela = pg.display.set_mode([self.LARGURA, self.ALTURA])

        # definindo o título da janela
        pg.display.set_caption("Mate os Slugan's malvados!!")

        # definingo a variável que contem o grupo de sprites
        self.todos_sprites = pg.sprite.Group()

        # instanciando a variavel sendo a classe inimigo e passando os parâmetros necessários
        self.sluganMal = Inimigo(randint(20, 680), randint(20, 580), "assets/redSlime.png")

        # instanciando a variavel sendo a classe inimigo e passando os parâmetros necessários
        self.sluganMal2 = Inimigo(randint(20, 680), randint(20, 580), "assets/redSlime.png")

        # adicionando o sluganMal no grupo dos sprites
        self.todos_sprites.add(self.sluganMal, self.sluganMal2)

        # definindo a variavel sendo a classe Titulo
        self.contador: Placar

        # instanciando a variavel sendo a classe Titulo e passando os parâmetros necessários
        self.contador = Placar(self.LARGURA // 2 - 20, self.ALTURA - 30, "PONTUAÇÃO: ")

        # adicionando o contador no grupo dos sprites
        self.todos_sprites.add(self.contador)

        # setando a variavel controladora do game looping
        self.rodando = True

        # instanciando a função game_looping
        self.game_looping()

    def game_looping(self):

        # seta a variavel clock sendo o mesmo tempo de cada clock do processador
        clock: pg.time.Clock = pg.time.Clock()

        # definindo o looping do jogo
        while self.rodando:

            # faz o looping esperar para ficar no FPS informado
            clock.tick(60)

            # instanciando o código interno de cada sprite e de todos os sprites ao mesmo
            # tempo que estão dentro desse grupo, por meio da função update de cada um
            self.todos_sprites.update()

            # pintando o interior da janela, a tela, é feito aqui dentro do looping para sobrepor o frame anterior, de
            # forma para apagar/substituir a tela anterior
            self.tela.fill([100, 100, 100])

            # atualizando INTERNAMENTE a posição do sprite na tela, que foi determinado
            # internamente por meio da função update
            self.todos_sprites.draw(self.tela)

            # desenhando tudo por cima novamente, de forma a atualizar visualmenta na tela, a camada anterior é pintada
            # e consequentimente, substituida pela pintura da pela em cinza
            pg.display.update()

            # lopping para verificar se foi clicado no evento X da janela para setar a variavel rodando em false
            # e assim, sair do looping do jogo e encerrar o jogo
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.rodando = False


# instanciando, iniciando, a classe inicial
MainInicial()
