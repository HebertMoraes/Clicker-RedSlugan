import pygame as pg
from Aprender.jogo_clicar.principal.menu_principal import MenuPrincipal
from Aprender.jogo_clicar.principal.jogo_principal import JogoPrincipal
from Aprender.jogo_clicar.principal.valores import Valores


class GameLoop:

    def __init__(self):

        pg.init()
        pg.mixer.init()

        while Valores.rodando:

            Valores.clock.tick(60)

            Valores.todos_sprites.update()
            # esse fill talvez deva ser retirado ao colocar um fundo correto
            Valores.tela.fill([100, 100, 100])
            Valores.todos_sprites.draw(Valores.tela)
            pg.display.update()
            pg.display.set_caption("Clicker RedSlugan")


            if Valores.estar_menu:
                if Valores.prime_menu:
                    MenuPrincipal.__init__(self)
                    Valores.prime_menu = False
                else:
                    MenuPrincipal.atualizar(self)
            if Valores.estar_jogo:
                if Valores.prime_jogo:
                    JogoPrincipal.__init__(self)
                    Valores.prime_jogo = False
                else:
                    JogoPrincipal.atualizar(self)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Valores.rodando = False

GameLoop()
