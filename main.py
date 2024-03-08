import pygame
from objects import *

class World:
    def __init__(self, WIDTH, HEIGHT):

        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.running = True

        self.screenDims = (WIDTH, HEIGHT)
        self.point = self.pos = [WIDTH / 2, HEIGHT / 2]
        self.lines = []
        self.boxes = [Box([200,200], [500, 100], [1, 1], "03_sopie.png"),
                      Box([200, 200], [710, 100], [1, 1], "01_krish.png")]
                    #   Box([100, 100], [500, 100], [1, -0.25], "04_hana.png"), 
                    #   Box([100, 100], [500, 300], [1, -0.25], "05_ella.png"),
                    #   Box([100, 100], [300, 300], [1, -0.25], "06_rob.png")]
        pygame.display.set_icon(self.boxes[0].image)
        
    
    
    def scrUpdate(self):
        self.screen.fill((100, 100, 100))
        
            
        for i, box in enumerate(self.boxes):
            box.pos[0] += box.momtm[0]
            box.pos[1] += box.momtm[1]
            self.screen.blit(box.image, (box.pos[0], box.pos[1]))
            box.move(box.pos)
            self.colDetect(box)
        
        pygame.display.flip()
       
    def colDetect(self, object):
        for box2 in self.boxes:
            if object.colRect.colliderect(box2.colRect) and box2 != object:
                print(object.pos, box2.pos)

                # if object.pos[0] == box2.pos[0] + 200 or object.pos[0] == box2.pos[0] - 200:
                object.momtm[0] *= -1
                # else:
                object.momtm[1]  *= -1
                    

        if object.pos[0] == self.screenDims[0] - object.dims[0] or object.pos[0] == 0:
            object.momtm[0] *= -1
            

        if object.pos[1] == self.screenDims[1] - object.dims[1] or object.pos[1] == 0:
            object.momtm[1] *= -1
            #self.lineDraw(self.pos)
            
    def lineDraw(self, point):
        self.lines.append([self.point, point])
        self.point = point


world = World(1000, 500)

while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    pygame.time.wait(40)

pygame.quit()