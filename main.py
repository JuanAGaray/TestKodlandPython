import pygame as py
import os
import time

py.init()

#const

"""COLORS"""
blue_primary = (39, 125, 149)
black = (0, 0, 0)
white = (255, 255, 255)

"""FONTS"""
title_font = py.font.SysFont("Arial", 36)
button_font = py.font.SysFont("Arial", 24)
dialogue_font = py.font.SysFont("Arial", 20)

"""SPRITE"""
player_move_left_direct = os.listdir(r'assets\sprites\player\player_run_right')
player_move_jump_right = os.listdir(r'assets\sprites\player\Jumpo')
player_stand_right = os.listdir(r'assets\sprites\player\stand right')
player_sword_right = os.listdir(r'assets\sprites\player\sword')
x_pos_player, y_pos_player = 0, 0



keys=py.key.get_pressed()
# pygame setup
screen = py.display.set_mode((800 ,600))
clock = py.time.Clock()
FPS = 60 



on = True
mode='menu'
first_open_class = {"intro" : True, "lv1": True}

#Sound
sound1 = py.mixer.Sound(r'assets\sounds\menu_sound.ogg')
sound2 = py.mixer.Sound(r'assets\sounds\Frontiers.mp3')
chanel1 = py.mixer.Channel(1)
chanelVoz = py.mixer.Channel(2)

#sprites
""""PLAYER"""

def extrac_layers(dir, path, name, flip_x = False):
    ol = []
    for layer in dir:
        dir_total = path + layer
        img = py.image.load(dir_total)
        x = img.get_rect().width * 2
        y = img.get_rect().height * 2
        img = py.transform.scale(img, (x,y))
        if flip_x:
            img = py.transform.flip(img, True, False)
        ol.append(img)
    player_layers[name] = ol

player_layers = {}

extrac_layers(player_move_left_direct,'assets\\sprites\\player\\player_run_right\\','left')
extrac_layers(player_move_left_direct,'assets\\sprites\\player\\player_run_right\\','right', True)
extrac_layers(player_move_jump_right,'assets\\sprites\\player\\Jumpo\\','jump right')
extrac_layers(player_move_jump_right,'assets\\sprites\\player\\Jumpo\\','jump left', True)
extrac_layers(player_stand_right,'assets\\sprites\\player\\stand right\\','stand right')
extrac_layers(player_stand_right,'assets\\sprites\\player\\stand right\\','stand left', True)
extrac_layers(player_sword_right,'assets\\sprites\\player\\sword\\','sword right')
extrac_layers(player_sword_right,'assets\\sprites\\player\\sword\\','sword left', True)

stand_player = player_layers['right'][0]
rect_player = stand_player.get_rect()
atk = py.image.load(r'assets\pixil-frame-0.png')
atk = py.transform.scale(atk,(248, 48))
rect_atk = atk.get_rect()
print(rect_atk.width)
background = py.image.load(r'assets\lv2.jpg')
background = py.transform.scale(background, (2000,600))
background_x = 0
background_y = 0
position_player='right'
salto = 6
jump = False
last_position = None
stand = True
first_stand = True
battle = False
count = 248
class Menu():
    
    def __init__(self):
        global first_open_class, on, mode
        screen.fill(blue_primary)
        self.closeMenu = False
        background = py.image.load(r'assets\background.png')
        background = py.transform.scale(background, (800,600))
        screen.blit(background,(0,0))
        self.buttons()
        self.sound_menu()
        self.eventMenu()
        
        
        py.display.update()
        

    def buttons(self):
        """BUTTON 1 """
        #creación del botton y texto
        button_1 = py.image.load(r'assets\button.png')
        text_button = button_font.render('Play',True, (200,200,200))
        #Centrado de button 
        self.button_rect = button_1.get_rect()
        self.button_rect.height = button_1.get_rect().height + 4
        self.button_rect.width = button_1.get_rect().width + 4
        self.button_rect.centerx = screen.get_rect().centerx
        self.button_rect.centery = (screen.get_height() / 7) * 2
        #Centrado del texto
        rec_text = text_button.get_rect()
        rec_text.centerx = screen.get_rect().centerx 
        rec_text.centery = self.button_rect.centery            
        if self.button_rect.collidepoint(py.mouse.get_pos()):
            py.draw.rect(screen, (37, 150, 190), self.button_rect, 0)
        else:
            py.draw.rect(screen, black, self.button_rect, 0)
        screen.blit(button_1, self.button_rect, )
        screen.blit(text_button, rec_text)


        """BUTTON 2 """
        button_2 = py.image.load(r'assets\button.png')
        text_button = button_font.render('Instructions ',True, (200,200,200))
        #Centrado de button 
        self.button_rect2 = button_2.get_rect()
        self.button_rect2.centerx = screen.get_rect().centerx
        self.button_rect2.height = button_2.get_rect().height + 4
        self.button_rect2.width = button_2.get_rect().width + 4
        self.button_rect2.centery = screen.get_rect().centery 
        #Centrado del texto
        rec_text = text_button.get_rect()
        rec_text.centerx = screen.get_rect().centerx 
        rec_text.centery = self.button_rect2.centery            
        if self.button_rect2.collidepoint(py.mouse.get_pos()):
            py.draw.rect(screen, (37, 150, 190), self.button_rect2, 0)
        else:
            py.draw.rect(screen, black, self.button_rect2, 0)
        screen.blit(button_2, self.button_rect2, )
        screen.blit(text_button, rec_text)


        """BUTTON 3"""
        button_3 = py.image.load(r'assets\button.png')
        text_button = button_font.render('Creditos',True, (200,200,200))
        #Centrado de button 
        self.button_rect3 = button_3.get_rect()
        self.button_rect3.height = button_3.get_rect().height + 4
        self.button_rect3.width = button_3.get_rect().width + 4
        self.button_rect3.centerx = screen.get_rect().centerx
        self.button_rect3.centery = (screen.get_height() / 7) * 5
        #Centrado del texto
        rec_text = text_button.get_rect()
        rec_text.centerx = screen.get_rect().centerx 
        rec_text.centery = self.button_rect3.centery            
        if self.button_rect3.collidepoint(py.mouse.get_pos()):
            py.draw.rect(screen, (37, 150, 190), self.button_rect3, 0)
        else:
            py.draw.rect(screen, black, self.button_rect3, 0)
        screen.blit(button_3, self.button_rect3, )
        screen.blit(text_button, rec_text)


        if self.button_rect.collidepoint(py.mouse.get_pos()) or self.button_rect2.collidepoint(py.mouse.get_pos()) or self.button_rect3.collidepoint(py.mouse.get_pos()):
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

    def sound_menu(self, close = False):
        global first_open_class
        if first_open_class["intro"] == True:
            py.mixer.Channel.play(chanel1, (sound1), -1)
            first_open_class["intro"] = False


    def eventMenu(self):
        global mode, first_open_class
        intEvent = events()
        for event in py.event.get():
            intEvent.close(event)
            if event.type == py.MOUSEBUTTONDOWN and self.button_rect.collidepoint(py.mouse.get_pos()):
                py.mixer.Channel.fadeout(chanel1,1000)
                py.mixer.Channel.play(chanel1, (sound2), -1)
                first_open_class["intro"] = True
                mode = 'game'             
                
class GameIntro():
    def __init__(self):
        global first_open_class
        self.eventGame()
        py.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        self.button_battle_visible = False
        if self.button_battle_visible == False and first_open_class["intro"]:
            self.background = py.image.load(r'assets\lv2.jpg')
            self.background = py.transform.scale(self.background, (2000,600))
            self.background_x = 0
            self.background_y = 0
            screen.blit(self.background,(self.background_x, self.background_y))
            if first_open_class["intro"]  == True:
                self.move_escenary()
        py.display.update()

        

    def move_escenary(self):
        global first_open_class
        self.move_backgroun_right()
        self.escene_1()
        self.button_battle()


    def move_backgroun_right(self):
        global temporalPosx
        for i in range(5000):
            self.background_x -= i*0.00005
            screen.blit(self.background,(self.background_x, 0))
            py.display.flip()
        temporalPosx = self.background_x

    def move_backgroun_left(self):
        self.background = py.image.load(r'assets\lv2.jpg')
        self.background = py.transform.scale(self.background, (2000,600))
        self.background_x = temporalPosx
        self.background_y = 0
        for j in range(5000):
            self.background_x += j*0.00005
            screen.blit(self.background,(self.background_x, 0))
            py.display.flip()

    def escene_1(self):
        knight_escene = py.image.load(r'assets\sprites\player\rune-knight.png')
        knight_escene = py.transform.scale(knight_escene, (460,700))
        self.box_text()
        screen.blit(knight_escene, (540, 200))
        self.initial_dialogue()
    

    def box_text(self):
        dialogue_box = py.image.load(r'assets\f4c777594925773.png')
        dialogue_box = py.transform.scale(dialogue_box, (700,100))
        self.dialogue_box_rect = dialogue_box.get_rect()
        self.dialogue_box_rect.bottomleft = (0, 600)
        py.draw.rect(screen, white, self.dialogue_box_rect, 0)
        screen.blit(dialogue_box, self.dialogue_box_rect, )
        

    def initial_dialogue(self):
        global first_open_class
        first_dialogue = 'Hola novato, soy el comandante te daré tu primera misión. Tienes que acabar con todos los aprendices del gran hechicero. RECUERDA!! No te confíes. No los subestimes.'
        text_split = first_dialogue.split(' ')
        text_list_split = [] #Dividimos en texto por las palabras que se pueden ingresar en la caja de texto
        count_word = [] #Var para guardar las secciónes de palabras
        total_letter = 0 #Var pata contar la letra
        py.mixer.Channel.play(chanelVoz,py.mixer.Sound(r'assets\sounds\vocodes_f2b9a28d-d3ae-47cf-8bdc-cfde99bf93f0 (mp3cut.net).mp3'), 0)
        for i in range(len(text_split)):
            total_letter +=  len(text_split[i])
            count_word.append(text_split[i])
            if total_letter > 60 or i == (len(text_split)-1):
                text_list_split.append(count_word)
                total_letter=0
                count_word= []    
        for i in range(len(text_list_split)):
            total_word = ''
            for j in range(len(text_list_split[i])):
                total_word += (text_list_split[i][j]+ ' ')
                self.insert_text(total_word, 600+(20*i))
        first_open_class["intro"]  = False

    def insert_text(self, words,y):
        text_initial_dialogue = dialogue_font.render(words,True, black, white)
        text_initial_dialogue
        rec_text_dialogue = text_initial_dialogue.get_rect()
        rec_text_dialogue.width = (500)
        rec_text_dialogue.height = (80)
        rec_text_dialogue.bottomleft = (35,y)
        screen.blit(text_initial_dialogue, rec_text_dialogue)
        py.display.update()
        time.sleep(0.18)     

    def button_battle(self):
        button_battle = py.image.load(r'assets\button.png')
        button_battle = py.transform.scale(button_battle, (120,25))
        text_button = dialogue_font.render('[Space]',True, white)
        #Centrado de button 
        self.button_rect_battle = button_battle.get_rect()
        self.button_rect_battle.center = (625,582)
        #Centrado del texto
        rec_text = text_button.get_rect() 
        rec_text.center = self.button_rect_battle.center 
        screen.blit(button_battle, self.button_rect_battle, )
        screen.blit(text_button, rec_text)
        py.display.update()
        self.button_battle_visible == True

        
    def eventGame(self):
        global first_open_class, mode
        intEvent = events()
        for event in py.event.get():
            intEvent.close(event)
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE and first_open_class["intro"]  == False:
                    self.move_backgroun_left()
                    mode = 'first level'
   
class firstLevel():
    def __init__(self):
        global player_layers, stand_player, rect_player, background, background_x, background_y, atk
        screen.fill((0,0,0))
        if first_open_class["lv1"]== True:
            self.char()
        
        screen.blit(background,(background_x, background_y))
        rect_player.center = (x_pos_player+27, y_pos_player+34)
        screen.blit(stand_player, (x_pos_player, y_pos_player))
        py.draw.rect(screen,"#4287f5", rect_atk)
        screen.blit(atk, (0,0))
        self.controller()
        py.display.flip()
        self.eventLeve1()
        

    def char(self):
        global first_open_class, x_pos_player, y_pos_player
        x_pos_player, y_pos_player = 80, 525
        first_open_class["lv1"]= False

    def controller(self):
        global x_pos_player, stand_player, position_player, y_pos_player, salto, jump, stand, first_stand, background_x, battle, count
        keys = py.key.get_pressed()
        #DERECHA
        if keys[py.K_RIGHT] and jump==False and battle == False:
            self.reset_sword()
            if position_player == 'left' or stand == True:
                stand_player = player_layers['right'][0]
            stand=False
            if background_x > -1189 and x_pos_player >= 500:
                background_x -=10
            else:
                if x_pos_player >= 575 and background_x < -1189:
                    pass
                else:
                    x_pos_player +=10
            py.time.delay(60)
            stand_player =  player_layers['right'][self.index_frame(player_layers['right'], stand_player)]
            position_player = 'right'
        
        #IZQUIERDA
        elif keys[py.K_LEFT] and jump==False and battle == False:
            self.reset_sword()
            if position_player == 'right' or stand == True:
                stand_player = player_layers['left'][0]
            stand=False
            if background_x <  0 and x_pos_player <= 200:
                background_x +=10
            else:
                if x_pos_player >= 80   and background_x <  1 :
                    x_pos_player -=10
            py.time.delay(60)
            stand_player =  player_layers['left'][self.index_frame(player_layers['left'], stand_player)]
            position_player = 'left'

        #ATAQUE
        elif keys[py.K_SPACE] and jump==False and count<120:
            count+=8
            rect_atk.width = rect_atk.width - 16
            if position_player == 'left' and battle ==  False :
                stand_player = player_layers['sword left'][0]
            elif position_player == 'right' and battle ==  False:
                 stand_player = player_layers['sword right'][0]
            battle = True
            stand=False

            if position_player == 'left' and battle == True:
                if background_x <  0 and x_pos_player <= 200:
                    background_x +=6
                else:
                    if x_pos_player >= 80   and background_x <  1 :
                        x_pos_player -=6
                py.time.delay(60)
                stand_player =  player_layers['sword left'][self.index_frame(player_layers['sword left'], stand_player)]
            elif position_player == 'right' and battle == True:
                if background_x > -1189 and x_pos_player >= 500:
                    background_x -=6
                else:
                    if x_pos_player >= 575 and background_x < -1189:
                        pass
                    else:
                        x_pos_player +=6
                py.time.delay(60)
                stand_player =  player_layers['sword right'][self.index_frame(player_layers['sword right'], stand_player)]
            print(count)

        #STAND
        elif stand == True and jump == False:
            self.reset_sword()
            if first_stand:
                if position_player == 'right':
                    stand_player = player_layers['stand right'][0]
                elif position_player == 'left':
                    stand_player = player_layers['stand left'][0]
                first_stand = False    
            else:
                py.time.delay(80)
            if position_player == 'right' :
                stand_player =  player_layers['stand right'][self.index_frame(player_layers['stand right'], stand_player)]
            elif position_player == 'left':
                stand_player =  player_layers['stand left'][self.index_frame(player_layers['stand left'], stand_player)]
            
        else:
            first_stand = True
            stand = True
            battle = False
            

        #SALTO
        if jump:   
            if salto >= -6:
                y_pos_player -=(salto * abs(salto))*1
                salto -=1
                if position_player == 'right':
                    stand_player =  player_layers['jump right'][self.index_frame(player_layers['jump right'], stand_player)]
                    if background_x > -1189 and x_pos_player >= 500:
                        background_x -=10
                    else:
                        if x_pos_player >= 575 and background_x < -1189:
                            pass
                        else:
                            x_pos_player +=10
                if position_player == 'left':
                    stand_player =  player_layers['jump left'][self.index_frame(player_layers['jump left'], stand_player)]
                    if background_x <  0 and x_pos_player <= 200:
                        background_x +=10
                    else:
                        if x_pos_player >= 80   and background_x <  1 :
                            x_pos_player -=10
                py.time.delay(35)
                
            else:
                stand_player = last_position
                salto=6
                jump=False
                y_pos_player = 525


    def reset_sword(self):
        global count, rect_atk
        if count>=120:
            count += 6
            rect_atk.width += 12
            if count >= 240:
                count = 0
                rect_atk.width=248

    def index_frame(self,list_, element):
        indx = list_.index(element)
        if indx == (len(list_)-1):
            return 0
        else:
            return indx +1

    def eventLeve1(self):
        global first_open_class, x_pos_player, jump, stand_player, last_position, first_stand
        intEvent = events()
        for event in py.event.get():
            intEvent.close(event)
            if event.type == py.KEYDOWN:
                if event.key == py.K_UP and jump == False:
                    jump = True
                    last_position = stand_player
                    if position_player == 'right':
                        stand_player =  player_layers['jump right'][0]
                    elif position_player == 'left':
                        stand_player =  player_layers['jump left'][0]
 
class events():
        def close(self, event_):
                if event_.type == py.QUIT:
                    py.quit()

while on:
    if mode == 'menu':
        Menu()
    elif mode == 'game':
        GameIntro()
    elif mode == 'first level':
        firstLevel()




