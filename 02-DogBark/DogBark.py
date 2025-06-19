import pygame
import sys

def main():
    # Pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # Initialize the pygame module
    pygame.init()

    # Prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Load and scale the image
    image1 = pygame.image.load("2dogs.JPG")
    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))  # TODO 3

    # Prepare the fonts and text
    font1 = pygame.font.SysFont("times new roman", 28)  # TODO 4
    caption1 = font1.render("Two Dogs", True, BLACK)  # TODO 5

    #   DONE 7: Add a funny message on the image using a larger font
    font2 = pygame.font.SysFont("times new roman", 40)
    funny_caption = font2.render("Woof Woof!", True, WHITE)

    # Load the sound
    bark_sound = pygame.mixer.Sound("bark.wav")  # TODO 8

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()  # TODO 9

        # Clear the screen and set the background
        screen.fill(WHITE)

        # Draw the image
        screen.blit(image1, (0, 0))  # TODO 2

        # Draw the main caption at the bottom center
        caption_x = (screen.get_width() - caption1.get_width()) // 2
        caption_y = IMAGE_SIZE + 2
        screen.blit(caption1, (caption_x, caption_y))  # TODO 6

        # Draw the funny caption on top of the image
        funny_x = (IMAGE_SIZE - funny_caption.get_width()) // 2
        funny_y = 20
        screen.blit(funny_caption, (funny_x, funny_y))  # TODO 7

        # Update the screen
        pygame.display.update()

main()



