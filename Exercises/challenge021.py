#Criar um programa que abra um arquivo mp3
import pygame
pygame.init()
pygame.mixer_music.load("raridade.mp3")
pygame.mixer_music.play()
pygame.event.wait()