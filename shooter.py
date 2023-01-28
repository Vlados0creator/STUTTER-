import pygame 
import os
pygame.init()

WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 40

def file_path(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path,file_name)
    return path

image_background = pygame.image.load(file_path("fon.jpg"))
image_background = pygame.transform.scale(image_background,(WIN_WIDTH, WIN_HEIGHT))

Player_image = pygame.image.load(file_path("fon.jpg"))
Player_image = pygame.transform.scale(Player_image,(50, 50))

enemy_image = pygame.image.load(file_path("fon.jpg"))
enemy_image = pygame.transform.scale(enemy_image,(50, 50))

window = pygame.display.set_mode([WIN_WIDTH,WIN_HEIGHT])
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__ (self,x,y,width,height,img,speed):
        super().__init__()
        self.image = pygame.image.load(file_path(img))
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,x,y,width,height,img,speed):
        super().__init__(x,y,width , height , img,speed)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def fire(self):
        pass

player = Player(300,400,70,70,"Player.jpg",5)

play = True 
game = True 

while game == True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game = False

    if play ==True:
        window.blit(image_background,(0,0))

        player.reset()
        player.update()

    clock.tick(FPS)
    pygame.display.update()