from random import randint
import pygame as pg

# setando a variavel global
pontos: int = 0


class Placar(pg.sprite.Sprite):

    def __init__(self, x, y, texto):

        # iniciando o grupo de sprite para trabalhar com ele
        pg.sprite.Sprite.__init__(self)

        # seta a variável sendo a fonte designada, com o nome e tamanho
        fnt = pg.font.Font(pg.font.match_font("times new roman"), 42)

        # carrega o sprite e coloca dentro da variável image, só que ao invés de ser uma imagem normal, pelo
        # comando image.load(), é passado o fnt(variavel designada acima) .render, que é um simples texto:
        # texto + "" é a concatenação do placar inicial 0, True diz para não ser serrilhado e pg.Color diz a cor
        self.image = fnt.render(texto + "0", True, pg.Color("Black"))

        # criar um retangulo do tamanho da imagem
        self.rect = self.image.get_rect()

        # posicioar o retangulo no local indicado pelo parâmetro, e consequentimente, a imagem vem junto
        self.rect.center = (x, y)

        # armazenando as variaveis locais em novas variaveis da classe para ser usado posteriormente, já que aqui é
        # o __init__ e só é rodado uma vez no inicio
        self.x = x
        self.y = y
        self.texto = texto
        self.fnt = fnt
        global pontos
        self.ultimoPonto = pontos

    def update(self):
        global pontos

        # irá acontecer se foi marcado pontos
        if self.ultimoPonto != pontos:

            # atualiza o placar da mesma maneira que anteriormente no __init__ porém aqui é concatenado o texto
            # com a variavel global pontos, fazendo com que fique atualizado o texto
            self.image = self.fnt.render(self.texto + "" + str(pontos), True, pg.Color("Black"))

            # # criar um retangulo do tamanho da imagem
            self.rect = self.image.get_rect()

            # posicioar o retangulo no local indicado, e consequentimente, a imagem vem junto
            self.rect.center = (self.x, self.y)

            # atualizando a variavel ultimoPonto para a global pontos, para que possa passar pela verificação novamente
            self.ultimoPonto = pontos


# definindo a classe do inimigo que é utilizado apenas pelo SluganMal, ela herda do pg.sprite.Sprite do qual a garante
# acesso para manipular sprites
class Inimigo(pg.sprite.Sprite):

    def __init__(self, x, y, caminho):

        # iniciando o grupo de sprite para trabalhar com ele
        pg.sprite.Sprite.__init__(self)

        # carrega a imagem dada pelo caminho e a inseri em uma variavel
        self.image = pg.image.load(caminho)

        # guardando essa primeira imagem preservando a escala original do sprite
        self.primeiraImagem = self.image

        # setando uma variavel aleatóriamente para ser usada na mudança de escala do tamanho do sprite
        self.tamanho = randint(25,200)

        # mudando o tamanho e escala do sprite pela variável aleatória tamanho
        self.image = pg.transform.scale(self.image, (self.tamanho, self.tamanho))

        # criar um retangulo do tamanho da imagem
        self.rect = self.image.get_rect()

        # posicioar o retangulo no local indicado pelo parâmetro, e consequentimente, a imagem vem junto
        self.rect.center = (x, y)

        # captura o tempo atual
        self.tempoInicial = pg.time.get_ticks()

    def update(self):

        # atualiando sempre a variavel para o tempo atual
        self.tempoAtual = pg.time.get_ticks()

        # se o método clicou() retornou True, dai ele move ele mesmo (sluganInimigo) e aumenta os pontos
        if self.clicou():
            self.mover()
            self.aumentarPontos()

        # verificação se passou 3 segundos sem clicar no sluganInimigo
        elif (self.tempoAtual - self.tempoInicial) > 3000:
            self.mover()

    def mover(self):
        # reposicionando o rect e consequentimente, o sprite, para um x e y aleatório
        self.rect.center = (randint(10, 690), randint(10, 590))

        # setando uma variavel aleatóriamente para ser usada na mudança de escala do tamanho do sprite
        self.tamanho = randint(50, 100)

        # mudando o tamanho e escala do sprite pela variável aleatória tamanho
        self.image = pg.transform.scale(self.primeiraImagem, (self.tamanho, self.tamanho))

        # reiniciar a variavel inicial do tempo para voltar ao começo na contagem de 3 segundos
        self.tempoInicial = self.tempoAtual

    def clicou(self):
        # capturando a posição x e y do mouse
        posicao_mouse = pg.mouse.get_pos()

        # capturando qual dos 3 botoes do mouse foi clicado (e não scrolado), retornando como 1 se for verdadeiro,
        # na ordem: [0] = botão esquerdo, [1] = botão scroll, [2] = botão direito
        clicou = pg.mouse.get_pressed()

        # se o botão esquerdo for clicado e o mouse estiver em cima do rect do sluganInimigo
        if clicou[0] and self.rect.collidepoint(posicao_mouse):
            return True
        else:
            return False

    def aumentarPontos(self):
        # se refere a variavel pontos global, a que foi criada fora das classes aqui no jogo_objetos.py
        global pontos
        pontos += 1
