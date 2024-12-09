import pygame

pygame.init() # Inicializar Pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("INVADERS ARCADE")

# Cargar imágenes
imagen1 = pygame.image.load("alien.png")
imagen2 = pygame.image.load("alien1.png")
misil_img = pygame.image.load("misil.png")

# Colores
BLANCO = (255, 255, 255)

# Generar imágenes marcianos
class ImagenMarcianos:
    def __init__(self, imagen1, imagen2, intervalo):
        self.imagen1 = imagen1
        self.imagen2 = imagen2
        self.intervalo = intervalo
        self.tiempo_transcurrido = 0
        self.intercambio = False

    def actualizar(self, actu):
        self.tiempo_transcurrido = self.tiempo_transcurrido + actu
        if self.tiempo_transcurrido >= self.intervalo:
            self.tiempo_transcurrido = 0
            self.intercambio = not self.intercambio

    def dibujar(self, pantalla, x, y):
        if self.intercambio:
            pantalla.blit(self.imagen2, (x+20, y))
        else:
            pantalla.blit(self.imagen1, (x-20, y))

# llenar fila y hcer mas filas
intervalo = 500 # Tiempo alternar (ms) 
filas = 7 # Filas 

imagenes_marcianos = [] 
for fila in range(filas): 
    x_pos = 0 
    fila_imagenes = [] 
    while x_pos < ANCHO: 
        fila_imagenes.append(ImagenMarcianos(imagen1, imagen2, intervalo)) 
        x_pos = x_pos + imagen1.get_width() 
    imagenes_marcianos.append(fila_imagenes)

# dibujar nave y movimiento
class Misil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = misil_img
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO // 2
        self.rect.y = ALTO - 20

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x = self.rect.x - 5
        if teclas[pygame.K_RIGHT] and self.rect.x < ANCHO - self.rect.width:
            self.rect.x = self.rect.x + 5

# Crear grupos de sprites (crear rectangulos para "choques")
todos_los_sprites = pygame.sprite.Group()
marcianos = pygame.sprite.Group()

# Crear la nave y agregarla al grupo de sprites
nave = Misil()
todos_los_sprites.add(nave)
# marcianos = ImagenMarcianos()
todos_los_sprites.add(marcianos)

todos_los_sprites.add(nave)

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Bucle principal del juego
jugando = True
while jugando:
    actu = reloj.tick(30)  # Tiempo en milisegundos desde la última iteración

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    pantalla.fill(BLANCO) # Limpiar pantalla

    y_pos = 50
    for fila_imagenes in imagenes_marcianos: 
        x_pos = 0 
        for imagen in fila_imagenes: # duplicamos filas par/impar cmbiando el punto d inicio
            imagen.actualizar(actu) 
            if x_pos %2 == 0 :
                imagen.dibujar(pantalla, x_pos, y_pos) 
            else:
                imagen.dibujar(pantalla, x_pos, y_pos+20)
            x_pos = x_pos + imagen1.get_width()
            print(x_pos, y_pos)
        y_pos = y_pos + imagen2.get_height()

    
    todos_los_sprites.update()  # Actualizar sprites 
    todos_los_sprites.draw(pantalla)

    pygame.display.flip()

pygame.quit()

