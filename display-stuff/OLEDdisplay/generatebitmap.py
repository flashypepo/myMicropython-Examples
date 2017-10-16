# bitmap data generator to be used with oled.draw_bitmap()
# source:
# https://forum.micropython.org/viewtopic.php?t=1705&start=20
# 2017-1016 new
#   usage
#   $python generatebitmap.py<return>
#   uses font.png as bitmap input

import pygame

colors = {
    (0, 0, 0, 255): 0,
    (102, 102, 102, 255): 1,
    (204, 204, 204, 255): 2,
    (255, 255, 255, 255): 3,
}

#font.png: 16*16 image
image = pygame.image.load("font.png")
images = []

for tile_x in range(0, image.get_size()[0]/4):
    rect = (tile_x * 4, 0, 4, 6)
    images.append(image.subsurface(rect))
    
for image in images:
    print '(%s),' % ', '.join('%d' %
        sum(colors[tuple(image.get_at((x, y)))] << (x * 2)
            for x in range(4))
        for y in range(6))