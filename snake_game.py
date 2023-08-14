
# coding: iso-8859-1 -*- 

import math                     #realizar opera��es matem�ticas
import random                   #gerar n�meros rand�micos
import pygame                   #principal m�dulo para jogos
import tkinter as tk            #interface gr�fica
from tkinter import messagebox  #interface gr�fica

pygame.init()                   #inicializa o m�dulo

#classe utilizada para desenhar os cubos na tela
class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1             #inicializa com o movimento na horizontal
        self.dirny = 0
        self.color = color


    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)     #atualiza o movimento
                                                                            #os movimentos s�o baseados no grid da tela e n�o na posi��o da tela

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows                                           #encontra a dist�ncia entre cada uma das linhas do grid
        i = self.pos[0]                                                     #posi��o das linhas (grid)
        j = self.pos[1]                                                     #posi��o das colunas (grid)

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2)) #desenha o ret�ngulo que representa o "cubo" definido
                                                                            # os valores de +1 e -2 s�o utilizados para n�o desenhar sobre as linhas 
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)



# classe utilizada para desenhar e movimentar o snake na tela
# essa classe recebe constroi a snake utilizando a classe cubo
class snake(object):
    body = []                           #lista que cont�m o corpo de cubos do snake
    turns = {}                          #dicion�rio utilizado para manter o movimento da snake
    def __init__(self, color, pos):
        self.color = color              #cor da snake
        self.head = cube(pos)           #cubo principal (cabe�a da snake)
        self.body.append(self.head)     #inicializa��o da lista com a cabe�a 
        self.dirnx = 0                  #movimento no eixo x
        self.dirny = 1                  #movimento no eixo y

#m�todo utilizado para realizar os movimentos da snake
    def move(self):
        #loop para tratar os eventos que ocorrem durante uma partida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                           #evento de fechar a tela
                pygame.quit()

            keys = pygame.key.get_pressed()                         #captura as teclas pressionadas

            #identifica qual � a tecla pressionada
            for key in keys:
                #tecla para a esquerda
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1                                             #movimenta 1 quadro para a esquerda
                    self.dirny = 0                                              #garante que n�o existe moviemento vertical
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]     #lista rastrear as posi��es do movimento

                #tecla para a direita
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1                                              #movimenta um quadrado para a direita
                    self.dirny = 0                                              #garante apenas o movimento na horizontal
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]     #rastrea os movimentos

                #tecla para cima
                elif keys[pygame.K_UP]:
                    self.dirnx = 0                                              #garante apenas o movimento na vertical
                    self.dirny = -1                                             #movimento para cima (inico da tela no corner superior esquerdo)
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]     #rastrea a mudan�a de dire��o

                #tecla para baixo
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0                                              #garante o movimento apenas na vertical
                    self.dirny = 1                                              #movimenta um quadro para baixo
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]     #rastrea o movimento

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                #verifica se o snake atingiu as bordas da tela
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)                                       #se n�o atingiu as bordas, movimenta normal


    #quando o jogo "termina"
    #reseta as vari�veis (reinicializa)
    #mesma do construtor da classe snake
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1


    #adiciona um novo cubo para a cauda da snake
    def addCube(self):
        tail = self.body[-1]                                        # a cauda como sendo a �ltima da lista de cubos da snake
        dx, dy = tail.dirnx, tail.dirny                             # dire��o 

        #identifica em qual dire��o est� se movendo para adicionar o cubo � cauda
        if dx == 1 and dy == 0:                                      #movimentando para a direita
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))      #adiciona o cubo � esquerda
        elif dx == -1 and dy == 0:                                   #movimentando para a esquerda
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))      #adiciona para a direita
        elif dx == 0 and dy == 1:                                    #movimentando para baixo
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))      #adiciona para a cima
        elif dx == 0 and dy == -1:                                   #movimentando para cima
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))      #adiciona para baixo

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

        
    #constroi a snake
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:                                   #verifica se � a cabe�a da snake para adicionar os olhos
                c.draw(surface, True)
            else:
                c.draw(surface)

#utilizada para desenhar o grid na tela (as linhas)
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  #define a dist�ncia entre cada uma das linhas presentes na tela

    x = 0
    y = 0
    
    #divide a tela em pontos para desenhar as linhas
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        #desenha as linhas para a tela (grid)
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))  #linhas horizontais
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))  #linhas verticais


#utilizada para desenhar todos os elementos na tela a cada no frame
def redrawWindow(surface):
    global rows, width, s, snack    #vari�veis globais que s�o atualizadas a cada novo frame
    surface.fill((0,0,0))           # preenche a tela com o fundo preto
    s.draw(surface)                 #desenha a snake na tela
    snack.draw(surface)             #desenha os quadros (comida) na tela
    drawGrid(width,rows, surface)   #desenha as linhas (grid) na tela
    pygame.display.update()         #atualiza o frame na tela

#adiciona a comida (cubos) para o jogo
def randomSnack(rows, item):

    positions = item.body                                               #posi��es do snake 

    while True:
        x = random.randrange(rows)                                      #verifica uma posi��o rand�mica para desenhar a "comida"
        y = random.randrange(rows)                                      #verifica uma posi��o rand�mica para desenhar a "comida"
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:   #verifica se a posi��o da snake (cabe�a) � a mesma que vamos desenhar a comida (lista de uma lista filtrada)
            continue
        else:
            break

    return (x,y)


#utilizada para enviar a mensagem ap�s o erro do jogador
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)       #adiciona a mensagem ao topo
    root.withdraw()
    messagebox.showinfo(subject, content)   #adiciona a mensagem ao box
    try:
        root.destroy()
    except:
        pass


#fun��o principal para o jogo
def main():
    global width, rows, s, snack                                #vari�veis globais para o funcionamento do jogo
    width = 500                                                 #dimens�o da tela
    rows = 20                                                   #n�mero de linhas e colunas da matriz (grid)
    win = pygame.display.set_mode((width, width))               #define as dimens�es da tela
    s = snake((255,0,0), (10,10))                               #define a cor e a posi��o inicial da snake na tela
    snack = cube(randomSnack(rows, s), color=(0,255,0))         #define a cor para os quadros que representam a comida do snake
    flag = True                                                 #flag para indicar se o jogo foi finalizado

    clock = pygame.time.Clock()                                 #instancia o objeto clock que � utilizado para ajustar a velocidade do jogo

    #loop principal do jogo
    while flag:
        pygame.time.delay(50)                                   #delay utilizado para deixar o jogo um pouco mais lento
        clock.tick(10)                                          #define a taxa m�xima de atualiza��o do jogo (frame rate)
        s.move()                                                #captura os movimentos (teclas) e realiza a atualiza��o da posi��o do snake
        if s.body[0].pos == snack.pos:                          #verifica se a snake "se alimentou"
            s.addCube()                                         #adiciona o novo cubo para o corpo da snake    
            snack = cube(randomSnack(rows, s), color=(0,255,0)) #desenha um novo cubo (alimento) para a snake

        #evrifica se o usu�rio perdeu 
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):         #caso a cabe�a encontre uma parte do corpo
                print("\'Pontua��o: \'", len(s.body))                           #realiza o print da pontua��o final 
                message_box("\'Ixi, voc� perdeu!\'", "\'Tente novamente.\'")    #apresenta a mensagem para a tela
                s.reset((10,10))                                                #coloca a snake na posi��o inicial
                break


        redrawWindow(win)                                       #desenha toda a tela




#inicializa o jogo
main()