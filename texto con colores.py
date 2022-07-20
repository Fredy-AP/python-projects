import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
texto_estilo = Builder.load_string('''
Label:
    text:
        ('[color=00563f]texto[/color]\\n'
        '[b]con[/b]\\n'
        '[color=0098c3]colores[/color]\\n'
        '[color=088800]0.0[/color]\\n'
        '[color=8e0d0d]0.0[/color]\\n')
    markup: True
    font_size: '44pt'
    halign: 'center'
    valign: 'center'
''')
class LabelEstilo(App):
    def build(self):
        return texto_estilo
if __name__ == '__main__':
    LabelEstilo().run()
