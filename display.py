import pygame

screen = pygame.display.set_mode((800, 85)) #Will probably have to resize

image = pygame.image.load('display.bmp') #Loads the overlay

screen.blit(image,(0,0)) #Displays the overlay

