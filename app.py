import pygame as pg
import pymunk as pm
import sys

def manzanas_crear(espacio,pos):
    cuerpo = pm.Body(1,100,body_type=pm.Body.DYNAMIC)
    cuerpo.position = pos
    forma = pm.Circle(cuerpo,40)
    espacio.add(cuerpo,forma)
    return forma

    
def dibuja_manzanas(manzanas):
    for manzana in manzanas:
        pos_x = int(manzana.body.position.x)
        pos_y = int(manzana.body.position.y)
        pepe_rect = pepe.get_rect(center=(pos_x,pos_y))
        pantalla.blit(pepe,pepe_rect)

def estorbocrear(espacio,pos):
    cuerpo = pm.Body(body_type=pm.Body.STATIC)
    cuerpo.position = pos
    forma = pm.Circle(cuerpo,50)
    espacio.add(cuerpo,forma)
    return forma

def dibuja_estorbo(estorbos):
    for estorbo in estorbos:
        pos_x = int(estorbo.body.position.x)
        pos_y = int(estorbo.body.position.y)
        pg.draw.circle(pantalla,(0,0,0), (pos_x , pos_y) ,50)


pg.init()#inicia
pantalla = pg.display.set_mode((800,800))
reloj = pg.time.Clock()

espacio = pm.Space()
espacio.gravity = (0,500)
pepe = pg.image.load('pepe.png')
pepe = pg.transform.scale(pepe,(80,80))
manzanas = []
estorbos = []
run = True
while run: #loop
    for event in pg.event.get():
        if event.type == pg.QUIT: #si se sale entonces...
            pg.quit()
            sys.exit()#que se cierre
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            manzanas.append(manzanas_crear(espacio,event.pos))
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            estorbos.append(estorbocrear(espacio,event.pos))
    pantalla.fill((255,255,255))
    espacio.step(1/50)
    dibuja_manzanas(manzanas)
    dibuja_estorbo(estorbos)
    pg.display.update()#que corra
    reloj.tick(120)#120fps