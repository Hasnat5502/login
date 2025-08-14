# Greentail Kivy App

This is a Kivy implementation of the Greentail Android app, featuring a beautiful UI with horizontal scrollable card sections, a header, and footer navigation.

## Features

- **Horizontal Scrollable Cards**: Multiple sections with horizontally scrollable cards
- **Responsive Design**: Adapts to different screen sizes
- **Beautiful UI**: Rounded corners, shadows, and modern design elements
- **Navigation Footer**: Bottom navigation with icons
- **Header**: Top header with fox icon and user profile
- **CO2 Impact Tracking**: Each card shows CO2 savings and points

## Sections

1. **Recommended actions** - Tips for reducing carbon footprint
2. **Plastic Free!** - Actions to reduce plastic usage
3. **New in Greentail** - Latest features and suggestions
4. **Let's save energy** - Energy-saving recommendations

## Setup

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
python main.py
```

## File Structure

```
├── main.py              # Main Python application file
├── body.kv              # Kivy layout file
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── assets/             # Image assets (create this folder)
    ├── fox.png
    ├── search.png
    ├── progress.png
    ├── connect.png
    ├── reward.png
    ├── foxh.png
    ├── arrow.png
    ├── user.png
    ├── meal1.png
    ├── walk.png
    ├── card3.png
    ├── card41png.png
    ├── beverage2.png
    ├── card22img.png
    ├── card24shadow.png
    ├── card31shadow.png
    ├── card32img.png
    ├── card33img.png
    ├── cardgf.png
    ├── cardgf2.png
    ├── card21.png
    ├── card22.png
    ├── card31.png
    ├── card32.png
    ├── card4p1.png
    ├── card4p2.png
    ├── card2p1.png
    ├── gif22.png
    └── ... (other image files)
```

## Customization

### Adding New Cards

To add new cards to a section, modify the `HorizontalCardSection` in `body.kv`:

```kv
CardWidget:
    title: 'Your Title'
    description: 'Your description'
    co2_amount: '100g'
    points: '+10'
    small_image1: 'assets/your_image1.png'
    small_image2: 'assets/your_image2.png'
    small_image3: 'assets/your_image3.png'
    main_image: 'assets/your_main_image.png'
    size_hint: None, None
    size: '350dp', '230dp'
```

### Changing Colors

Modify the color values in `body.kv`:

```kv
Color:
    rgba: 0.95, 0.98, 0.99, 1  # Background color
```

### Adding New Sections

Create a new `HorizontalCardSection` in the main layout:

```kv
HorizontalCardSection:
    section_title: 'Your Section Title'
    # ... card properties
```

## Mobile Deployment

For mobile deployment:

1. **Android**: Use Buildozer
   ```bash
   pip install buildozer
   buildozer init
   buildozer android debug deploy run
   ```

2. **iOS**: Use Kivy-iOS
   ```bash
   pip install kivy-ios
   toolchain build kivy
   toolchain run kivy main.py
   ```

## Troubleshooting

### Missing Images
If images don't load, ensure:
- All image files are in the `assets/` folder
- Image paths in `body.kv` are correct
- Image files are valid PNG/JPG formats

### Font Issues
If custom fonts don't work:
- Install the required fonts (Poppins, Inter, Times New Roman)
- Or replace with system fonts in `body.kv`

### Performance Issues
For better performance:
- Use compressed images
- Optimize image sizes
- Consider using `Image` instead of `AsyncImage` for local assets

## License

This project is for educational purposes. Please respect the original app's licensing terms.