import csv
import pygame

class csv_class:
    def __init__(self, archive, method):
        self.archive = self.read(archive, method)

    #return th matrix in the csv
    def read(self, archive, method):
        f = open(archive, method)
        data = csv.reader(f)
        data = [row for row in data]
        #Deleteth empy spaces in the matrix
        for i in data:
            if i == []:
                data.remove(i)
        return data

    #Modify th variable matrix
    def write(self, matrix):
        self.archive = matrix

    #return th matrix in the csv
    def get_matrix(self):
        return self.archive

    #Update the csv with the variable matrix
    def update_matrix(self, archive, method):
        a = self.archive
        f = open(archive, method)
        with f:
            writer = csv.writer(f)
            writer.writerows(a)

#load the csv
archive_csv = csv_class("ScoreBoard.csv","rt")
matrix_csv = archive_csv.get_matrix()

"""For write matrix in the variable"""
# archivo_csv.write("Nueva matriz")
"""For save the matrix in the csv"""
# archivo_csv.update_matriz("matriz.csv","w")
"""NOTE"""
#Firts write the variable and after save the matrix in the csv

#Class for know the position of the cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

#Class for create the buttons, require tho images for animation
class Button(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y,scale_x,scale_y):
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image_normal = pygame.transform.scale(image1,(self.scale_x,self.scale_y))
        self.image_select = pygame.transform.scale(image2,(self.scale_x,self.scale_y))
        self.image_current = self.image_normal
        self.rect = self.image_current.get_rect()
        self.rect.left, self.rect.top = (x,y)
    def update(self, screen, cursor):
        if cursor.colliderect(self.rect):
            self.image_current = self.image_select
        else:
            self.image_current = self.image_normal
        #screen.blit(pygame.transform.scale(self.image_current,(self.scale_x,self.scale_y)),self.rect)
        screen.blit(self.image_current,self.rect)
"""
class multi_line_reader():
    def __init__(self,screen, txt, x,y, font, colour=(128,128,128), justification="left"):
        self.screen = screen
        self.txt = txt
        self.x = x
        self.y = y
        self.font = font
        self.color = colour
        self.justification = justification
        self.max_width = 0
        self.text_bitmaps = []
        self.text_width = None
        self.width_diff = None
        self.bitmap = None
        self.xpos = None
    def update(self, screen,y):
        self.screen.blit(self.bitmap, (self.xpos, y))
    def funtions(self):
        self.justification = self.justification[0].upper()
        self.text = self.txt.strip().replace('\r','').split('\n')
        #Convert line a line, in bits to represent in screen
        for line in self.text:
            self.text_bit_map = self.font.render(line, True, self.color)
            self.text_width = self.text_bit_map.get_width()
            self.text_bitmaps.append((self.text_width, self.text_bit_map))
            if (self.max_width < self.text_width):
                self.max_width = self.text_width
        # Paint all the text bitmaps to the screen with justification
        for (width, self.bitmap) in self.text_bitmaps:
            self.xpos = self.x
            self.width_diff = self.max_width - width
            if (self.justification == 'R'):  # right-justify
                xpos = self.x + self.width_diff
            elif (self.justification == 'C'): # centre-justify
                self.xpos = (self.width_diff // 2)-self.x
            self.y += self.bitmap.get_height()
"""