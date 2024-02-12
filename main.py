'''from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor=(1,1,1,1)
class myapp(App):
    def build(self):
        return Label(text='Alhamdulillah i have done',font_size="30sp",bold=True,italic=True,color=(1,0,0,1))
myapp().run()'''




'''
from kivy.app import App
from kivy.uix.button import Button
class buttonapp(App):
    def build(self):
        btn=Button(text="click me",size_hint=(0.8,0.4),pos_hint={"center_x":0.5,"center_y":0.5},font_size='90sp',on_release=self.btn_click,color=(0,0,0))
        return btn
    def btn_click(self,btn):
        print("hello")
buttonapp().run()

'''



'''
from kivy.app import App
from kivy.uix.image import Image
class ImageShow(App):
    def build(self):
        Img=Image(source='20221025_173228',size_hint=(None,None),width=500,height=500,pos_hint={"center_x":0.5,"center_y":0.5})
        return Img
ImageShow().run()


'''




''' 
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.clearcolor=(0,1,1,1)
Window.size=(500,700)
class MyApp(App):
    def build(self):
        layout=BoxLayout(orientation='vertical',spacing=20,padding=50,pos_hint={"center_x":0.5,"center_y":0.5})
        button1=Button(text="button 1")
        button2=Button(text="button 2")
        button3=Button(text="button 3")
        button4=Button(text="button 4")
        
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        return layout
MyApp().run()


'''

'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
class MyApp(App):
    def build(self):
        layout=GridLayout(rows=2)
        btn1=Button(text='Hello  ',font_size="20sp")
        btn2=Button(text='Hello  ',font_size="20sp")
        btn3=Button(text='Hello  ',font_size="20sp")
        btn4=Button(text='Hello  ',font_size="20sp")
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout
MyApp().run()


'''
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout=BoxLayout(orientation="horizontal",spacing=222,padding=23)
        
        btn1=Button(text='1st stage')
        btn2=Button(text='2nd stage')
        
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout
MyApp().run()