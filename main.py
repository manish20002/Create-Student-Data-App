import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'student name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='student marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='student Gender'))
        self.s_gen = TextInput()
        self.add_widget(self.s_gen)

        self.add_widget(Label(text='student blood group'))
        self.s_bg = TextInput()
        self.add_widget(self.s_bg)

        self.press = Button(text = 'click here to save')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of the student :"+self.s_name.text)
        print("Student Marks :" + self.s_marks.text)
        print("Student Gender :" + self.s_gen.text)
        print("Student Blood Group :" + self.s_bg.text)
        print("")



class parentApp(App):
    def build(self):
        return childApp()

if __name__=="__main__":
    parentApp().run()



