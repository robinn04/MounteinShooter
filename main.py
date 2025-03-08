import pygame

pygame.init()
print('setup start')
window = pygame.display.set_mode(size=(600, 480))
print('setup end')

print('loop start')
while True:
    # check free all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print'Quitting...' 
            pygame.quit()  # close window
            quit()  # and pygame
