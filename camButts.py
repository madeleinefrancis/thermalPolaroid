
import pygame, Buttons, os, numpy #,pyCam, print_image
from PIL import Image, ImageOps, ImageEnhance
from pygame.locals import *



class Button_Example:
    
    def __init__(self):

        pygame.init()

        image = 'capture.png'

        caption = os.path.dirname(os.path.realpath(__file__))

        fullPath = caption + "/" + image
        
        self.values = {'contrast': 1.0, 'brightness' : 1.0, 'sharpness' : 1.0}

        self.image = Image.open(fullPath)

        self.bg = pygame.image.load(fullPath)

        self.bg = self.grayscale(self.bg)

        self.main()

    def grayscale(self, img):
        arr = pygame.surfarray.pixels3d(img)
        #luminosity filter
        avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
        arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
        return pygame.surfarray.make_surface(arr)


    def highercon(self):

        stringy = pygame.image.tostring(self.bg, 'RGBA')

        self.image = Image.frombytes('RGBA', self.image.size, stringy)

        contrast = self.values['contrast']

        if contrast < 2.0: 

            self.values['contrast'] = contrast + 0.1

        en = ImageEnhance.Contrast(self.image)

        self.image = en.enhance(self.values['contrast'])

        stringy = self.image.tobytes()

        self.bg = pygame.image.fromstring(stringy, self.image.size, 'RGBA')

        self.update_display()

    def lowercon(self):

        stringy = pygame.image.tostring(self.bg, 'RGBA')

        self.image = Image.frombytes('RGBA', self.image.size, stringy)

        contrast = self.values['contrast']

        if contrast > 0.0: 

            self.values['contrast'] = contrast - 0.1

        en = ImageEnhance.Contrast(self.image)

        self.image = en.enhance(self.values['contrast'])

        stringy = self.image.tobytes()

        self.bg = pygame.image.fromstring(stringy, self.image.size, 'RGBA')

        self.update_display()


    def lowerbright(self):

        stringy = pygame.image.tostring(self.bg, 'RGBA')

        self.image = Image.frombytes('RGBA', self.image.size, stringy)

        brightness = self.values['brightness']

        if brightness > 0.0: 

            self.values['brightness'] = brightness - 0.1

        en = ImageEnhance.Brightness(self.image)

        self.image = en.enhance(self.values['brightness'])

        stringy = self.image.tobytes()

        self.bg = pygame.image.fromstring(stringy, self.image.size, 'RGBA')

        self.update_display()

    def higherbright(self):

        stringy = pygame.image.tostring(self.bg, 'RGBA')

        self.image = Image.frombytes('RGBA', self.image.size, stringy)

        brightness = self.values['brightness']

        if brightness < 2.0: 

            self.values['brightness'] = brightness + 0.1

        en = ImageEnhance.Brightness(self.image)

        self.image = en.enhance(self.values['brightness'])

        stringy = self.image.tobytes()

        self.bg = pygame.image.fromstring(stringy, self.image.size, 'RGBA')

        self.update_display()

    def lowersharp(self):

        stringy = pygame.image.tostring(self.bg, 'RGBA')

        self.image = Image.frombytes('RGBA', self.image.size, stringy)

        sharpness = self.values['sharpness']

        if sharpness > 0.0: 

            self.values['sharpness'] = sharpness - 0.1

        en = ImageEnhance.Sharpness(self.image)

        self.image = en.enhance(self.values['sharpness'])

        stringy = self.image.tobytes()

        self.bg = pygame.image.fromstring(stringy, self.image.size, 'RGBA')

        self.update_display()

    def highersharp(self):

        stringy = pygame.image.tostring(self.bg, 'RGBA')

        self.image = Image.frombytes('RGBA', self.image.size, stringy)

        sharpness = self.values['sharpness']

        if sharpness < 2.0: 

            self.values['sharpness'] = sharpness + 0.1

        en = ImageEnhance.Sharpness(self.image)

        self.image = en.enhance(self.values['sharpness'])

        stringy = self.image.tobytes()

        self.bg = pygame.image.fromstring(stringy, self.image.size, 'RGBA')

        self.update_display()

    # def printy(self):
    #     print_image.capture(self.image)


    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((650,370),0, 32)
        self.size = self.screen.get_size()
        x, y = self.screen.get_size()
        pygame.display.set_caption(str(x) + " X " + str(y))

        

    #Update the display and show the button
    def update_display(self):
        self.screen.fill((255,255,255))

        x, y = self.screen.get_size()

        self.screen.blit(self.bg, (0,0))

        length = (x - 100)/ 6 

        sixthX = x/6

        height = y/6



        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.ButtonLB.create_button(self.screen, (102,255,178),   0, (y-height), length,    height,    0,        "-B", (0,0,0))
        self.ButtonHB.create_button(self.screen, (255,102,102), sixthX, (y-height), length,    height,    0,        "+B", (0,0,0))

        self.ButtonLC.create_button(self.screen, (102,255,178), (2 * sixthX), (y-height), length,    height,    0,        "-C", (0,0,0))
        self.ButtonHC.create_button(self.screen, (255,102,102), (3 * sixthX), (y-height), length,    height,    0,        "+C", (0,0,0))

        self.ButtonLSh.create_button(self.screen, (102,255,178), (4 * sixthX), (y-height), length,    height,    0,        "-Sh", (0,0,0))
        self.ButtonHSh.create_button(self.screen, (255,102,102), (5 * sixthX), (y-height), length,    height,    0,        "+Sh", (0,0,0))

        self.ButtonRestore.create_button(self.screen, (255,255,102), 0, (y-(2* height) - 20), length,    height,    0,        "Return", (0,0,0))
        
        self.ButtonPrint.create_button(self.screen, (102,178,255), (5 * sixthX), (y-(2* height) - 20), length , height,    0,  "Print", (0,0,0))

        
        pygame.display.flip()


    #Run the loop
    def main(self):

        
        self.ButtonLB = Buttons.Button()
        self.ButtonHB = Buttons.Button()
        
        self.ButtonLC = Buttons.Button()
        self.ButtonHC = Buttons.Button()
        
        self.ButtonLSh = Buttons.Button()
        self.ButtonHSh = Buttons.Button()

        self.ButtonRestore = Buttons.Button()
        self.ButtonPrint = Buttons.Button()

        self.display()


        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    
                    if self.ButtonLB.pressed(pygame.mouse.get_pos()):
                        self.lowerbright()
                    elif self.ButtonHB.pressed(pygame.mouse.get_pos()):
                        self.higherbright()
                    
                    elif self.ButtonHC.pressed(pygame.mouse.get_pos()):
                        self.highercon()
                    elif self.ButtonLC.pressed(pygame.mouse.get_pos()):
                        self.lowercon()
                    
                    elif self.ButtonHSh.pressed(pygame.mouse.get_pos()):
                        self.highersharp()
                    elif self.ButtonLSh.pressed(pygame.mouse.get_pos()):
                        self.lowersharp()

                    elif self.ButtonRestore.pressed(pygame.mouse.get_pos()):
                         print "garbage"
                         #pyCam.camstream()

                    elif self.ButtonPrint.pressed(pygame.mouse.get_pos()):
                        print "garbage"
                        #self.printy()


if __name__ == '__main__':
    obj = Button_Example()
