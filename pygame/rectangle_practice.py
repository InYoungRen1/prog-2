# rectangle_practice.py
# apply object/classes
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "<Rectangle>"

class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.width = 100
        self.height = 10

        self.colour = (255, 255, 0)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    rectangle = Rectangle()
    triangle = Rectangle()
    triangle.width = 100  
    # TODO: create another rectangle
    #   CHANGE ITS PROPERTIES
    #   REMINDER USE .NOTATION TO CHANGE PROPERTIES
    #    i.e. rectangle_two.x = 100

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        pygame.draw.rect(screen, rectangle.colour, (rectangle.x, rectangle.y, rectangle.width, rectangle.height))
        pygame.draw.rect(screen, triangle.colour, (triangle.x, triangle.y, triangle.width, triangle.height))
        pygame.draw.circle(screen, (0, 255, 0), (100, 100), 50)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()