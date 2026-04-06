from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# iOS Karanlık Mod Arka Planı
Window.clearcolor = (0.02, 0.02, 0.02, 1)

class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.12, 0.12, 0.14, 1) # Premium Gri
        self.color = (1, 1, 1, 1)
        self.font_size = '17sp'
        self.height = 75
        self.size_hint_y = None
        self.markup = True

class IdentityApp(App):
    def build(self):
        root = ScrollView(do_scroll_x=False)
        
        # İçerik Düzeni
        layout = BoxLayout(orientation='vertical', padding=25, spacing=12, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # Başlık (Lüks Görünüm)
        layout.add_widget(Label(
            text="[b][color=F8F8F8]AKREP1 DİJİTAL KİMLİK[/color][/b]", 
            font_size='26sp', 
            size_hint_y=None, 
            height=100, 
            markup=True
        ))
        
        # Senin Bilgilerin (Eksiksiz Liste)
        data = [
            ("👤", "İsim Soyisim", "Nebi Özkan"),
            ("🆔", "T.C. No", "10286365472"),
            ("📞", "Telefon", "0546 552 81 76"),
            ("📸", "Instagram", "ozknebi"),
            ("✈️", "Telegram", "@Ozqan_1"),
            ("🐦", "X (Twitter)", "NOzqan"),
            ("🎵", "TikTok", "ozkanebi"),
            ("📺", "YouTube Music", "@Nebiozkan1"),
            ("💳", "Enpara IBAN", "TR25 0015 7000 0000 0116 5166 50")
        ]
        
        for emoji, title, value in data:
            btn_text = f"{emoji} [b]{title}[/b]\n[size=14sp][color=A0A0A0]{value}[/color][/size]"
            layout.add_widget(StyledButton(text=btn_text))
            
        # Alt İmza
        layout.add_widget(Label(
            text="[i][color=444444]Scorpion Emperor Edition[/color][/i]", 
            size_hint_y=None, 
            height=60, 
            markup=True,
            font_size='12sp'
        ))
        
        root.add_widget(layout)
        return root

if __name__ == '__main__':
    IdentityApp().run()
