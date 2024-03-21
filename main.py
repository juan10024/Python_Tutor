import pygame
import os
import random

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Images
# Load cat images
RUNNING = [pygame.image.load(os.path.join("Assets/Cat", "Gatito_Start.png")),
           pygame.image.load(os.path.join("Assets/Cat", "Gatito_Start.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Cat", "Gatito_Jump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Cat", "Gatito_Dead.png")),
           pygame.image.load(os.path.join("Assets/Cat", "Gatito_Dead.png"))]
GAMEOVER = [pygame.image.load(os.path.join("Assets/Other", "GameOver.png"))]




# Load cactus images
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", f"SmallCactus{i}.png")) for i in range(1, 4)]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", f"LargeCactus{i}.png")) for i in range(1, 4)]

# Load bird images
BIRD = [pygame.image.load(os.path.join("Assets/Bird", f"Bird{i}.png")) for i in range(1, 3)]

# Load cloud image
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

# Load background image
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
background_image = pygame.image.load(os.path.join("Assets/Other", "BackGround.png")).convert()


class Cat:
    # Constantes para la posición y velocidad del gato
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        # Imágenes del gato en diferentes estados
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        # Estados del gato
        self.cat_duck = False
        self.cat_run = True
        self.cat_jump = False

        # Índice para la animación del gato
        self.step_index = 0

        # Velocidad de salto y posición inicial del gato
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS

    def update(self, userInput):
        # Actualizar el estado del gato en función de la entrada del usuario

        # Comprobar si el gato está agachado, corriendo o saltando
        if self.cat_duck:
            self.duck()
        if self.cat_run:
            self.run()
        if self.cat_jump:
            self.jump()

        # Reiniciar el índice de animación si es necesario
        if self.step_index >= 10:
            self.step_index = 0

        # Controlar los movimientos del gato según la entrada del usuario
        if userInput[pygame.K_UP] and not self.cat_jump:
            self.cat_duck = False
            self.cat_run = False
            self.cat_jump = True
        elif userInput[pygame.K_DOWN] and not self.cat_jump:
            self.cat_duck = True
            self.cat_run = False
            self.cat_jump = False
        elif not (self.cat_jump or userInput[pygame.K_DOWN]):
            self.cat_duck = False
            self.cat_run = True
            self.cat_jump = False

    def duck(self):
        # Método para animar al gato agachado
        self.image = self.duck_img[self.step_index // 5]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        # Método para animar al gato corriendo
        self.image = self.run_img[self.step_index // 5]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        # Método para animar al gato saltando
        self.image = self.jump_img
        if self.cat_jump:
            self.cat_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.cat_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        # Método para dibujar al gato en la pantalla
        SCREEN.blit(self.image, (self.cat_rect.x, self.cat_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()


    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    # Variables globales necesarias para el juego
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles

    # Configuración inicial del juego
    run = True  # Variable de control del bucle principal del juego
    clock = pygame.time.Clock()  # Reloj para controlar la velocidad de fotogramas
    player = Cat()  # Crear instancia del jugador
    cloud = Cloud()  # Crear instancia de la nube
    game_speed = 20  # Velocidad inicial del juego
    x_pos_bg = 0  # Posición inicial del fondo en el eje x
    y_pos_bg = 380  # Posición inicial del fondo en el eje y
    points = 0  # Puntuación inicial del jugador
    font = pygame.font.Font('freesansbold.ttf', 20)  # Fuente para mostrar la puntuación
    obstacles = []  # Lista para almacenar los obstáculos
    death_count = 0  # Contador de muertes del jugador

    # Función para actualizar la puntuación del jugador
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Puntaje: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    # Función para gestionar el fondo en movimiento
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Bucle principal del juego
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.blit(background_image, (0, 0))  # Mostrar el fondo

        userInput = pygame.key.get_pressed()  # Obtener la entrada del usuario

        player.draw(SCREEN)  # Dibujar al jugador en la pantalla
        player.update(userInput)  # Actualizar el estado del jugador

        # Generar nuevos obstáculos si no hay ninguno en la pantalla
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        # Actualizar y dibujar los obstáculos
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            # Verificar colisión entre el jugador y los obstáculos
            if player.cat_rect.colliderect(obstacle.rect):
                pygame.time.delay(1500)  # Retraso después de una colisión
                death_count += 1  # Incrementar el contador de muertes
                menu(death_count)  # Mostrar el menú después de una muerte

        background()  # Actualizar el fondo en movimiento

        cloud.draw(SCREEN)  # Dibujar la nube en la pantalla
        cloud.update()  # Actualizar la posición de la nube

        score()  # Actualizar la puntuación del jugador

        clock.tick(30)  # Limitar la velocidad de fotogramas
        pygame.display.update()  # Actualizar la pantalla

def game_over_screen(points):
    global game_speed, background_image
    run = True
    font = pygame.font.Font('freesansbold.ttf', 30)

    while run:
        SCREEN.blit(GAMEOVER[0], (SCREEN_WIDTH // 2 - 95, SCREEN_HEIGHT // 2 - 205))
        text = font.render("GAME OVERRRRRR", True, (0, 0, 0))
        score = font.render("Tú Puntuación: " + str(points), True, (0, 0, 0))
        text_two = font.render("Presiona Enter Para Continuar", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_two_rect = text_two.get_rect()
        score_rect = score.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        text_two_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 225)
        score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(text_two, text_two_rect)
        SCREEN.blit(score, score_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Retornar True cuando el jugador desea reiniciar el juego

def menu(death_count):
    global points, game_speed, background_image
    run = True
    map_selected = False
    difficulty_selected = False

    while run:
        if death_count == 1:  # Mostrar Game Over solo si ha ocurrido una muerte
            if game_over_screen(points):  # Si el jugador desea reiniciar el juego
                death_count = 0  # Reiniciar el contador de muerte
                continue  # Volver al bucle para mostrar el menú de selección de mapa después de Game Over

        SCREEN.blit(background_image, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if not map_selected:
            # Mostrar opciones de mapa
            map_choice_text = font.render("Selecciona un mapa: (1) o (2)", True, (0, 0, 0))
            text_two = font.render("Usa las letras o números del teclado", True, (0, 0, 0))
            text_two_rect = text_two.get_rect()
            map_choice_text_rect = map_choice_text.get_rect()
            map_choice_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            text_two_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            SCREEN.blit(map_choice_text, map_choice_text_rect)
            SCREEN.blit(text_two, text_two_rect)

        elif map_selected and not difficulty_selected:
            # Mostrar opciones de dificultad
            difficulty_text = font.render("Seleccione la dificultad: (F)ácil, (M)edio o (D)ifícil", True, (0, 0, 0))
            difficulty_text_rect = difficulty_text.get_rect()
            difficulty_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            SCREEN.blit(difficulty_text, difficulty_text_rect)

        else:
            main()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if not map_selected:
                    if event.key == pygame.K_1:
                        background_image = pygame.image.load(os.path.join("Assets/Other", "BackGround.png")).convert()
                        map_selected = True
                    elif event.key == pygame.K_2:
                        background_image = pygame.image.load(os.path.join("Assets/Other", "Background_2.png")).convert()
                        map_selected = True
                elif map_selected and not difficulty_selected:
                    if event.key == pygame.K_f:
                        game_speed = 20
                        difficulty_selected = True
                    elif event.key == pygame.K_m:
                        game_speed = 30
                        difficulty_selected = True
                    elif event.key == pygame.K_d:
                        game_speed = 40
                        difficulty_selected = True

# Llamar a menu() sin pasar death_count para iniciar el juego sin una muerte previa
menu(death_count=0)

