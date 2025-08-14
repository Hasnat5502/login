from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.uix.button import Button

# Set window size for development
Window.size = (375, 812)

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
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 0
        self.spacing = 0
        
        # Left side with text content
        left_layout = BoxLayout(orientation='vertical', size_hint_x=0.6, padding=[20, 30, 10, 10])
        
        # Title
        title_label = Label(
            text=self.title,
            font_size='16sp',
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height='30dp',
            halign='left',
            valign='middle'
        )
        title_label.bind(text_size=title_label.setter('size'))
        left_layout.add_widget(title_label)
        
        # Description
        desc_label = Label(
            text=self.description,
            font_size='10sp',
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height='60dp',
            halign='left',
            valign='top'
        )
        desc_label.bind(text_size=desc_label.setter('size'))
        left_layout.add_widget(desc_label)
        
        # CO2 and points indicators
        indicators_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='30dp', spacing=10)
        
        # CO2 indicator
        co2_layout = BoxLayout(size_hint_x=None, width='60dp')
        with co2_layout.canvas.before:
            Color(0.8, 0.8, 0.8, 0.3)
            Rectangle(pos=co2_layout.pos, size=co2_layout.size)
        co2_layout.bind(pos=self._update_rect, size=self._update_rect)
        
        co2_label = Label(text=self.co2_amount, font_size='8sp', color=(0, 0, 0, 1))
        co2_layout.add_widget(co2_label)
        indicators_layout.add_widget(co2_layout)
        
        # Points indicator
        points_layout = BoxLayout(size_hint_x=None, width='40dp')
        with points_layout.canvas.before:
            Color(0.2, 0.8, 0.2, 0.3)
            Rectangle(pos=points_layout.pos, size=points_layout.size)
        points_layout.bind(pos=self._update_rect, size=self._update_rect)
        
        points_label = Label(text=self.points, font_size='8sp', color=(0, 0, 0, 1))
        points_layout.add_widget(points_label)
        indicators_layout.add_widget(points_layout)
        
        left_layout.add_widget(indicators_layout)
        
        # Small images row
        images_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp', spacing=10)
        
        # Placeholder for small images
        for i in range(3):
            placeholder = Button(
                text=f'Img{i+1}',
                size_hint=(None, None),
                size=('30dp', '30dp'),
                background_color=(0.9, 0.9, 0.9, 1)
            )
            images_layout.add_widget(placeholder)
        
        left_layout.add_widget(images_layout)
        self.add_widget(left_layout)
        
        # Right side with main image
        right_layout = BoxLayout(orientation='vertical', size_hint_x=0.4, padding=[0, 30, 20, 0])
        
        # Placeholder for main image
        main_image_placeholder = Button(
            text='Main\nImage',
            size_hint=(None, None),
            size=('80dp', '80dp'),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.8, 0.8, 0.8, 1)
        )
        right_layout.add_widget(main_image_placeholder)
        
        self.add_widget(right_layout)
    
    def _update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.8, 0.8, 0.8, 0.3)
            Rectangle(pos=instance.pos, size=instance.size)

class HorizontalCardSection(BoxLayout):
    """Horizontal scrollable section containing multiple cards"""
    section_title = StringProperty('')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = '300dp'
        self.padding = [60, 0, 60, 0]
        
        # Section title
        title_label = Label(
            text=self.section_title,
            font_size='13sp',
            color=(0.106, 0.263, 0.196, 1),
            size_hint_y=None,
            height='30dp',
            halign='left',
            valign='middle'
        )
        title_label.bind(text_size=title_label.setter('size'))
        self.add_widget(title_label)
        
        # Horizontal scroll view
        scroll_view = ScrollView(do_scroll_x=True, do_scroll_y=False, bar_width=0)
        
        # Cards container
        cards_layout = BoxLayout(
            orientation='horizontal',
            size_hint_x=None,
            width=self.minimum_width,
            spacing=60,
            padding=[0, 35, 0, 35]
        )
        
        # Add sample cards
        sample_cards = [
            {
                'title': 'Reduce food waste',
                'description': 'Saving leftovers or planning\nmeals can reduce waste\nand save up to 500g of CO₂\nper day.',
                'co2': '400g',
                'points': '+25'
            },
            {
                'title': 'Walk for short distances',
                'description': 'Choosing to walk instead\nof drive for under 3km\ncan save ~0.4kg of CO₂\nper trip.',
                'co2': '400g',
                'points': '+5'
            },
            {
                'title': 'Use energy-saving mode',
                'description': 'Lower screen brightness,\nreduce refresh rates, and\nactivate eco-mode on\nyour laptop or phone.',
                'co2': '60g',
                'points': '+5'
            },
            {
                'title': 'Educate a friend',
                'description': 'Teaching someone\ndoubles the reach of your\nactions — awareness\ndrives culture change.',
                'co2': '400g',
                'points': '+15'
            }
        ]
        
        for card_data in sample_cards:
            card = CardWidget(
                title=card_data['title'],
                description=card_data['description'],
                co2_amount=card_data['co2'],
                points=card_data['points'],
                size_hint=(None, None),
                size=('350dp', '230dp')
            )
            cards_layout.add_widget(card)
        
        scroll_view.add_widget(cards_layout)
        self.add_widget(scroll_view)

class FooterWidget(BoxLayout):
    """Footer widget with navigation icons"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = [30, 0, 30, 0]
        self.size_hint_y = None
        self.height = '77dp'
        
        # Add spacing
        self.add_widget(Widget(size_hint_x=0.15))
        
        # Navigation icons
        icons = ['Home', 'Search', 'Progress', 'Connect', 'Reward']
        for i, icon_name in enumerate(icons):
            # Icon container
            icon_container = BoxLayout(size_hint_x=None, width='43dp')
            with icon_container.canvas.before:
                Color(0.9, 0.9, 0.9, 1)
                Rectangle(pos=icon_container.pos, size=icon_container.size)
            icon_container.bind(pos=self._update_rect, size=self._update_rect)
            
            # Icon button
            icon_button = Button(
                text=icon_name,
                size_hint=(None, None),
                size=('30dp', '30dp'),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                background_color=(0.8, 0.8, 0.8, 1)
            )
            icon_container.add_widget(icon_button)
            self.add_widget(icon_container)
            
            # Add spacing between icons
            if i < len(icons) - 1:
                self.add_widget(Widget(size_hint_x=0.1))
        
        # Add final spacing
        self.add_widget(Widget(size_hint_x=0.15))
    
    def _update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            Rectangle(pos=instance.pos, size=instance.size)

class HeaderWidget(BoxLayout):
    """Header widget with fox icon and user profile"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = [30, 0, 30, 0]
        self.size_hint_y = None
        self.height = '107dp'
        
        # Left side with fox icon and text
        left_layout = BoxLayout(orientation='horizontal', size_hint_x=0.7)
        with left_layout.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=left_layout.pos, size=left_layout.size)
        left_layout.bind(pos=self._update_rect, size=self._update_rect)
        
        # Fox icon placeholder
        fox_icon = Button(
            text='🦊',
            size_hint=(None, None),
            size=('30dp', '30dp'),
            pos_hint={'center_y': 0.5},
            background_color=(0.9, 0.9, 0.9, 1)
        )
        left_layout.add_widget(fox_icon)
        
        # Text
        text_label = Label(
            text='Calculate Your Footprint',
            font_size='14sp',
            color=(0, 0, 0, 1),
            size_hint_x=0.7
        )
        left_layout.add_widget(text_label)
        
        # Arrow icon placeholder
        arrow_icon = Button(
            text='→',
            size_hint=(None, None),
            size=('20dp', '20dp'),
            pos_hint={'center_y': 0.5},
            background_color=(0.9, 0.9, 0.9, 1)
        )
        left_layout.add_widget(arrow_icon)
        
        self.add_widget(left_layout)
        
        # Spacing
        self.add_widget(Widget(size_hint_x=0.1))
        
        # User profile image placeholder
        user_icon = Button(
            text='👤',
            size_hint=(None, None),
            size=('50dp', '50dp'),
            pos_hint={'center_y': 0.5},
            background_color=(0.9, 0.9, 0.9, 1)
        )
        self.add_widget(user_icon)
    
    def _update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=instance.pos, size=instance.size)

class MainScreen(BoxLayout):
    """Main screen containing all sections"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Header
        header = HeaderWidget()
        self.add_widget(header)
        
        # Main scrollable content
        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        content_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=self.minimum_height,
            padding=[0, 50, 0, 70]
        )
        
        # Intro text
        intro_label = Label(
            text="It's your chance to\ntake action, Shihab.",
            font_size='32sp',
            color=(0.106, 0.263, 0.196, 1),
            size_hint_y=None,
            height='100dp',
            halign='left',
            valign='middle'
        )
        intro_label.bind(text_size=intro_label.setter('size'))
        content_layout.add_widget(intro_label)
        
        # Add sections
        sections = ['Recommended actions', 'Plastic Free!', 'New in Greentail', "Let's save energy"]
        for section_title in sections:
            section = HorizontalCardSection(section_title=section_title)
            content_layout.add_widget(section)
        
        scroll_view.add_widget(content_layout)
        self.add_widget(scroll_view)
        
        # Footer
        footer = FooterWidget()
        self.add_widget(footer)

class GreentailApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    GreentailApp().run()