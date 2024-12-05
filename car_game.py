import pygame
import sys
import random

# Initialize pygame

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame prueba")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Vehicle class
class Vehicle:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 80))  # Resize the image
        self.rect = pygame.Rect(x, y, 100, 100)
        self.x = x
        self.y = y

    def drive(self, dx, dy):
        """Mover el coche """
        self.x += dx
        self.y += dy
        self.rect.topleft= (self.x, self.y)

    def draw(self, surface):
        """Dibujar el coche """
        surface.blit(self.image, (self.x, self.y))
        pygame.draw.rect(surface, (0, 0, 0), self.rect)

 

# Obstaculo Class
class Obstaculo:
    def __init__(self, name, image_path1, x, y):
        self.name = name
        self.image = pygame.image.load(image_path1)
        self.image = pygame.transform.scale(self.image, (100, 80))  # Resize the image
        self.rect = pygame.Rect(x, y, 100, 100)
        self.x = x
        self.y = y

    # def drive(self, dx, dy):
        # """Mover el obstaculo """
        # self.x += dx
        # self.y += dy

    def draw(self, surface):
        """Dibujar el obstaculo """
        surface.blit(self.image, (self.x, self.y))

CAR_IMAGE_PATH = "car.png" 
OBSTACULO_IMAGE_PATH1 = "obstaculo.png"  

# Create a vehicle object
car = Vehicle("Car 1", CAR_IMAGE_PATH, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
obstaculo1 = Obstaculo("Obstaculo1",OBSTACULO_IMAGE_PATH1, random.randint(0, SCREEN_WIDTH), random.randint(0,SCREEN_HEIGHT))
obstaculo2 = Obstaculo("Obstaculo2",OBSTACULO_IMAGE_PATH1, random.randint(0, SCREEN_WIDTH), random.randint(0,SCREEN_HEIGHT))
obstaculo3 = Obstaculo("Obstaculo3",OBSTACULO_IMAGE_PATH1, random.randint(0, SCREEN_WIDTH), random.randint(0,SCREEN_HEIGHT))
obstaculo4 = Obstaculo("Obstaculo4",OBSTACULO_IMAGE_PATH1, random.randint(0, SCREEN_WIDTH), random.randint(0,SCREEN_HEIGHT))
obstaculos=[obstaculo1,obstaculo2,obstaculo3,obstaculo4]




# Main game loop
score=0
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle keys for car movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            car.drive(0, -5)  # Move up
        if keys[pygame.K_DOWN]:
            car.drive(0, 5)  # Move down
        if keys[pygame.K_LEFT]:
            car.drive(-5, 0)  # Move left
        if keys[pygame.K_RIGHT]:
            car.drive(5, 0)  # Move right

        # Borrar el screen
        screen.fill(WHITE)

        # Dibujar el coche
        car.draw(screen)
        
        # Dibujar el obstaculo
        for o in obstaculos :
            o.draw(screen)
        
        # Atencion Colision
        for o in obstaculos:
            if car.rect.colliderect(o.rect):
                print("collision")
                score +=1
                print(score)
            o.draw(screen)

        # Actualizar todo que has sido dibujado
        pygame.display.flip()

        # Mantener el FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()