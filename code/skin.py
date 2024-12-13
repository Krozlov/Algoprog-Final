import pygame
from settings import *
from support import *
from player import *

class SkinSelect:
    #current skin = Timo
    skin_path = f'{init_path}graphics/player/Timo/'
    def __init__(self,player):
        
        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.skin_number = len(player.skins)
        self.skin_names = list(player.skins.keys())
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        
        #skin display creation
        self.height = self.display_surface.get_size()[1] * 0.4
        self.width = self.display_surface.get_size()[0] // 4
        self.create_skins()
        
        #selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True
        
        #skin list path
        self.skins = {
            f'{init_path}graphics/player/Default/display.png',
            f'{init_path}graphics/player/Jude/display.png',
            f'{init_path}graphics/player/Timo/display.png'
        }
        
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.skin_number - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            
            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.skins_list[self.selection_index].trigger(self.player)
    
    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 200:
                self.can_move = True
                
    def create_skins(self):
        self.skins_list = []
        
        for skin,index in enumerate(range(self.skin_number)):
            #x pos
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.skin_number
            left = (skin * increment) + (increment - self.width) // 2
            
            #y pos
            top = self.display_surface.get_size()[1] * 0.3
            
            #create object
            skin = Skin(left,top,self.width,self.height,index,self.font)
            self.skins_list.append(skin)

    # def display_pict(self,surface,index):   
    #     #image
    #     self.image_path = self.skins[index]
    #     self.image = pygame.image.load(f'{self.image_path}').convert_alpha()
    #     image_surf = pygame.surface.Surface((65,65))
    #     image_rect = image_surf.get_rect(center = self.rect.center)
    
    # #draw
    # surface.blit(self.image,image_rect)
        
    def display(self):
        self.input()
        self.selection_cooldown()
        
        for index,skin in enumerate(self.skins_list):
            #get attributes
            name = self.skin_names[index]
            skin.display(self.display_surface,self.selection_index,name,index)
        
class Skin:
    def __init__(self,l,t,w,h,index,font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index
        self.font = font
        self.skins = {
            f'{init_path}graphics/player/Default/display.png',
            f'{init_path}graphics/player/Jude/display.png',
            f'{init_path}graphics/player/Timo/display.png'
        }
        
    def display_names(self,surface,name,selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
        
        #title
        title_surf = self.font.render(name,False,color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop)
          
        #draw
        surface.blit(title_surf,title_rect)
    
    def display_pict(self,surface,index):
        
        #image
        # self.image_path = self.skins[index]
        self.image = pygame.image.load(f'{init_path}graphics/player/Timo/display.png').convert_alpha()
        image_surf = pygame.surface.Surface((65,65))
        image_rect = image_surf.get_rect(center = self.rect.center)
        
        #draw
        surface.blit(self.image,image_rect)
    
    def trigger(self,player):       
        player.character_path = list(player.skins.values())[self.index]
        skin_path = player.character_path
        #puter balik jadi player yang ambil dari player path dan player path dikasih initial value

    def get_skin_path(self, player):
        player.character_path = list(player.skins.values())[self.index]
        return player.character_path
       
    def display(self,surface,selection_num,name,index):
        if self.index == selection_num:
            pygame.draw.rect(surface,UPGRADE_BG_COLOR_SELECTED,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        else:
            pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
                
        self.display_names(surface,name,self.index == selection_num)
        self.display_pict(surface,index)