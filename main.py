from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.lang import Builder

# Set window size for development (remove for mobile)
Window.size = (375, 812)  # iPhone X dimensions

class CardWidget(BoxLayout):
    """Individual card widget with all card properties"""
    title = StringProperty('')
    description = StringProperty('')
    co2_amount = StringProperty('')
    points = StringProperty('')
    small_image1 = StringProperty('')
    small_image2 = StringProperty('')
    small_image3 = StringProperty('')
    main_image = StringProperty('')

class HorizontalCardSection(BoxLayout):
    """Horizontal scrollable section containing multiple cards"""
    section_title = StringProperty('')
    
    # Card 1 properties
    card1_title = StringProperty('')
    card1_description = StringProperty('')
    card1_co2 = StringProperty('')
    card1_points = StringProperty('')
    card1_small1 = StringProperty('')
    card1_small2 = StringProperty('')
    card1_small3 = StringProperty('')
    card1_main = StringProperty('')
    
    # Card 2 properties
    card2_title = StringProperty('')
    card2_description = StringProperty('')
    card2_co2 = StringProperty('')
    card2_points = StringProperty('')
    card2_small1 = StringProperty('')
    card2_small2 = StringProperty('')
    card2_small3 = StringProperty('')
    card2_main = StringProperty('')
    
    # Card 3 properties
    card3_title = StringProperty('')
    card3_description = StringProperty('')
    card3_co2 = StringProperty('')
    card3_points = StringProperty('')
    card3_small1 = StringProperty('')
    card3_small2 = StringProperty('')
    card3_small3 = StringProperty('')
    card3_main = StringProperty('')
    
    # Card 4 properties
    card4_title = StringProperty('')
    card4_description = StringProperty('')
    card4_co2 = StringProperty('')
    card4_points = StringProperty('')
    card4_small1 = StringProperty('')
    card4_small2 = StringProperty('')
    card4_small3 = StringProperty('')
    card4_main = StringProperty('')

class FooterWidget(BoxLayout):
    """Footer widget with navigation icons"""
    pass

class HeaderWidget(BoxLayout):
    """Header widget with fox icon and user profile"""
    pass

class MainScreen(BoxLayout):
    """Main screen containing all sections"""
    pass

class GreentailApp(App):
    def build(self):
        # Load the KV file
        Builder.load_file('body.kv')
        return MainScreen()

if __name__ == '__main__':
    GreentailApp().run()