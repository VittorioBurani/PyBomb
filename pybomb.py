import numpy as np
from random import randrange
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,disable_multitouch')

class RLButton(Button):
    def __init__(self, **kwargs):
        super(RLButton,self).__init__(**kwargs)
        self.clicked=False
        self.rightclicked=False
        self.mouse_click: str
        self.bind(on_touch_down=self.click)
    def click(self, instance, touch):
        self.mouse_click=touch.button

class Grid(RelativeLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.entry()

    def entry(self):
        self.add_widget(Image(source='imgs/enter.png'))
        self.add_widget(Button(text="[b][u][font=fonts/ScriptsoftRegular][size=100]PyBomb[/size][/font][/u][/b]", markup=True, background_color=(1,1,1,0.5), color=(1,0.6,0.4,1), size_hint=(0.5, 0.3), pos_hint={'x': 0.25, 'y': 0.35}, on_press=self.setlay))

    def setlay(self, button):
        self.clear_widgets()
        self.add_widget(Label(text="[b][size=20][font=fonts/ScriptsoftRegular]INSERT THE DIMENSION OF THE\nMINEFIELD (Default: 20):[/font][/size][/b]", markup=True, color=(1,0.6,0.4,1), pos_hint={'x': 0, 'y': 0.20}))
        self.add_widget(Label(text="[b][size=20][font=fonts/ScriptsoftRegular]INSERT THE NUMBER OF BOMBS\nAND MINES (Default: 32):[/font][/size][/b]", markup=True, color=(1,0.6,0.4,1), pos_hint={'x': 0, 'y': 0.05}))
        self.txt1 = TextInput(background_color=(1,0.6,0.4,1), multiline=False, size_hint=(0.05,0.05), pos_hint={'x': 0.7, 'top': 0.7})
        self.add_widget(self.txt1)
        self.txt2 = TextInput(background_color=(1,0.6,0.4,1), multiline=False, size_hint=(0.05,0.05), pos_hint={'x': 0.7, 'top': 0.55})
        self.add_widget(self.txt2)
        b = Button(text="[b][size=40][font=fonts/ScriptsoftRegular]GO SWEEP![/font][/size][/b]", markup=True, color=(1,0.6,0.4,1), background_color=(1,1,1,0.5), size_hint=(0.4,0.2), pos_hint={'x': 0.3, 'y': 0.2})
        b.bind(on_press=self.setdim)
        self.add_widget(b)

    def setdim(self, button):
        if self.txt1.text and int(self.txt1.text)>9:
            self.grid_dimension = int(self.txt1.text)
        else:
            self.grid_dimension = 20
        if self.txt2.text and (int(self.txt2.text)<(self.grid_dimension*self.grid_dimension)):
            self.bomb_num = int(self.txt2.text)
        else:
            self.bomb_num = 32
        self.set()

    def set(self):
        self.clear_widgets()
        self.grid = np.zeros((self.grid_dimension,self.grid_dimension))
        self.act_bomb = self.bomb_num
        self.bomb_pos = []
        while self.act_bomb:
            i=randrange(0,self.grid_dimension-1)
            j=randrange(0,self.grid_dimension-1)
            if self.grid[i][j]==0:
                self.grid[i][j]=-1
                self.act_bomb-=1
                self.bomb_pos.append((i,j))
        del self.act_bomb
        for i in range(self.grid_dimension):
            for j in range(self.grid_dimension):
                if self.grid[i][j]!=-1:
                    if i==0 and j==0:
                        if self.grid[i][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j+1]==-1:
                            self.grid[i][j]+=1
                    elif i==(self.grid_dimension-1) and j==0:
                        if self.grid[i-1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j+1]==-1:
                            self.grid[i][j]+=1
                    elif i==0 and j==(self.grid_dimension-1):
                        if self.grid[i][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j]==-1:
                            self.grid[i][j]+=1
                    elif i==(self.grid_dimension-1) and j==(self.grid_dimension-1):
                        if self.grid[i-1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j-1]==-1:
                            self.grid[i][j]+=1
                    elif i==0:
                        if self.grid[i][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j+1]==-1:
                            self.grid[i][j]+=1
                    elif j==0:
                        if self.grid[i-1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j+1]==-1:
                            self.grid[i][j]+=1
                    elif i==(self.grid_dimension-1):
                        if self.grid[i-1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j+1]==-1:
                            self.grid[i][j]+=1
                    elif j==(self.grid_dimension-1):
                        if self.grid[i-1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j]==-1:
                            self.grid[i][j]+=1
                    else:
                        if self.grid[i-1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i-1][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i][j+1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j-1]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j]==-1:
                            self.grid[i][j]+=1
                        if self.grid[i+1][j+1]==-1:
                            self.grid[i][j]+=1
        if self.grid_dimension<36:
            self.fontsize = 40-self.grid_dimension
        else:
            self.fontsize = 5
        for i in range(0,self.grid_dimension):
            for j in range(0,self.grid_dimension):
                if self.grid[i][j]==-1:
                    self.add_widget(Image(source='imgs/orangebomb.png', allow_stretch=True, size_hint=(1/self.grid_dimension, 1/self.grid_dimension), pos_hint= {'x': (1/self.grid_dimension)*i, 'top': 1-(1/self.grid_dimension)*j}))
                else:
                    self.add_widget(Label(text=str(int(self.grid[i][j])), font_size=self.fontsize, color=(1,0.6,0.4,1), size_hint= (1/self.grid_dimension, 1/self.grid_dimension), pos_hint= {'x': (1/self.grid_dimension)*i, 'top': 1-(1/self.grid_dimension)*j}))
        self.fill()

    def bomb_click(self, button):
        if button.mouse_click=='right':
            if button.rightclicked==True:
                button.background_color=(1,0.6,0.4,2)
                button.rightclicked=False
                self.bomb_pos.append((button.i, button.j))
            else:
                button.background_color=(0,1,0,1)
                button.rightclicked=True
                self.bomb_pos.remove((button.i, button.j))
                if not self.bomb_pos:
                    self.add_widget(Popup(title="WOW! You won!", content=Image(source="imgs/wow.png", allow_stretch=True), size_hint=(0.4,0.4), pos_hint={'x': 0.3, 'y': 0.4}))
                    b = Button(text="[b][size=48][font=fonts/ScriptsoftRegular]Play![/font][/size][/b]", markup=True, color=(1,0.6,0.4,1), background_color=(1,1,1,0.5),  size_hint=(0.4,0.2), pos_hint={'x': 0.3, 'y': 0.2})
                    b.bind(on_press=self.setlay)
                    self.add_widget(b)
        else:
            button.background_color=(0,0,0,0)
            img = Image(allow_stretch=True)
            n = randrange(1,8)
            if n==1:
                img.source="imgs/boom.png"
            elif n==2:
                img.source="imgs/kaboom.png"
            elif n==3:
                img.source="imgs/pow.png"
            elif n==4:
                img.source="imgs/kapow.png"
            elif n==5:
                img.source="imgs/kapowboom.png"
            elif n==6:
                img.source="imgs/nuke.png"
            elif n==7:
                img.source="imgs/zap.png"
            else:
                img.source="imgs/splat.png"
            del n
            self.add_widget(Popup(title="DAMN! You lost!", content=img, size_hint=(0.4,0.4), pos_hint={'x': 0.3, 'y': 0.4}))
            b = Button(text="[b][size=48][font=fonts/ScriptsoftRegular]Retry![/font][/size][/b]", markup=True, color=(1,0.6,0.4,1), background_color=(1,1,1,0.5), size_hint=(0.4,0.2), pos_hint={'x': 0.3, 'y': 0.2})
            b.bind(on_press=self.setlay)
            self.add_widget(b)

    def norm_click(self, button):
        if button.mouse_click=='right':
            if button.rightclicked==True:
                if button.clicked:
                    button.background_color=(0,0,0,0)
                else:
                    button.background_color=(1,0.6,0.4,2)
                    button.rightclicked=False
            else:
                if button.clicked:
                    button.background_color=(0,0,0,0)
                else:
                    button.background_color=(0,1,0,1)
                    button.rightclicked=True
        else:
            button.background_color=(0,0,0,0)
            button.clicked=True

    def fill(self):
        for i in range(self.grid_dimension):
            for j in range(self.grid_dimension):
                if self.grid[i][j]==-1:
                    b = RLButton(background_color=(1,0.6,0.4,2), size_hint=(1/self.grid_dimension, 1/self.grid_dimension), pos_hint={'x': (1/self.grid_dimension)*i, 'top': 1-(1/self.grid_dimension)*j})
                    b.bind(on_press=self.bomb_click)
                    b.i = i
                    b.j = j
                    self.add_widget(b)
                else:
                    b = RLButton(background_color=(1,0.6,0.4,2), size_hint=(1/self.grid_dimension, 1/self.grid_dimension), pos_hint={'x': (1/self.grid_dimension)*i, 'top': 1-(1/self.grid_dimension)*j})
                    b.bind(on_press=self.norm_click)
                    self.add_widget(b)



class PyBomb(App):
    def build(self):
        self.map = Grid()
        return self.map


if __name__=='__main__':
    PyBomb().run()
