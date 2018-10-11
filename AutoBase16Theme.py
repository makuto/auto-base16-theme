# AutoBase16Theme.py by Macoy Madson
# MIT License
# https://github.com/makuto/auto-base16-theme
import random

"""
Base16 Style (from https://github.com/chriskempson/base16/blob/master/styling.md):
    base00 - Default Background
    base01 - Lighter Background (Used for status bars)
    base02 - Selection Background
    base03 - Comments, Invisibles, Line Highlighting
    base04 - Dark Foreground (Used for status bars)
    base05 - Default Foreground, Caret, Delimiters, Operators
    base06 - Light Foreground (Not often used)
    base07 - Light Background (Not often used)
    base08 - Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted
    base09 - Integers, Boolean, Constants, XML Attributes, Markup Link Url
    base0A - Classes, Markup Bold, Search Text Background
    base0B - Strings, Inherited Class, Markup Code, Diff Inserted
    base0C - Support, Regular Expressions, Escape Characters, Markup Quotes
    base0D - Functions, Methods, Attribute IDs, Headings
    base0E - Keywords, Storage, Selector, Markup Italic, Diff Changed
    base0F - Deprecated, Opening/Closing Embedded Language Tags, e.g. <?php ?>
"""

BACKGROUND_COLOR_INDEX = 0

class Base16Color:
    def __init__(self, name, selectionFunction):
        self.name = name
        self.color = None
        self.selectionFunction = selectionFunction

def rgbColorFromStringHex(colorStringHex):
    # From https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    return tuple(int(colorStringHex.strip('#')[i:i+2], 16) for i in (0, 2 ,4))

# TODO: There's probably some fancier way to do this which will give better results (e.g. convert to HSV)
def getColorAverageBrightness(color):
    rgbColor = color
    if type(color) == str:
        rgbColor = rgbColorFromStringHex(color)
        
    return sum(rgbColor) / len(rgbColor)

def colorHasBeenUsed(base16Colors, color):
    for base16Color in base16Colors:
        if base16Color.color == color:
            return True
    return False

# Pick darkest, most grey color for background. If the color is already taken, pick the next unique darkest
def pickDarkestGreyestColorUnique(base16Colors, currentBase16Color, colorPool):
    bestColor = None
    bestColorAverage = 10000
    for color in colorPool:
        rgbColorAverage = getColorAverageBrightness(color)
        if rgbColorAverage < bestColorAverage and not colorHasBeenUsed(base16Colors, color):
            bestColor = color
            bestColorAverage = rgbColorAverage

    return bestColor

# Selects the  darkest color which meets the contrast requirements and which hasn't been used yet
def pickDarkestHighContrastColorUnique(base16Colors, currentBase16Color, colorPool):
    minimumDarkContrast = 56
    viableColors = []
    for color in colorPool:
        if getColorAverageBrightness(color) - getColorAverageBrightness(base16Colors[BACKGROUND_COLOR_INDEX].color) > minimumDarkContrast:
            viableColors.append(color)

    viableColors = sorted(viableColors,
                          key=lambda color: getColorAverageBrightness(color), reverse=True)

    # We've sorted in order of brightness; pick the darkest one which is unique
    bestColor = None
    for color in viableColors:
        if not colorHasBeenUsed(base16Colors, color):
            bestColor = color
            break

    return bestColor
    
# Pick high contrast foreground (high contrast = a minimum brightness difference between this and the brightest background)
def pickHighContrastBrightColorRandom(base16Colors, currentBase16Color, colorPool):
    minimumBrightContrast = 92
    
    viableColors = []
    for color in colorPool:
        if getColorAverageBrightness(color) - getColorAverageBrightness(base16Colors[BACKGROUND_COLOR_INDEX].color) > minimumBrightContrast:
            viableColors.append(color)

    if not viableColors:
        return None
            
    return random.choice(viableColors)
    
def pickRandomColor(base16Colors, currentBase16Color, colorPool):
    return random.choice(colorPool)

def main():
    colorsFile = open('colors.txt', 'r')
    colorsLines = colorsFile.readlines()
    colorsFile.close()

    base16Colors = [
        # These go from darkest to lightest via implicit unique ordering
        # base00 - Default Background
        Base16Color('base00', pickDarkestGreyestColorUnique),
        # base01 - Lighter Background (Used for status bars)
        Base16Color('base01', pickDarkestGreyestColorUnique),
        # base02 - Selection Background
        Base16Color('base02', pickDarkestGreyestColorUnique),
        # base03 - Comments, Invisibles, Line Highlighting
        Base16Color('base03', pickDarkestHighContrastColorUnique),#pickDarkestGreyestColorUnique),
        # base04 - Dark Foreground (Used for status bars)
        Base16Color('base04', pickDarkestGreyestColorUnique),
        # base05 - Default Foreground, Caret, Delimiters, Operators
        Base16Color('base05', pickDarkestGreyestColorUnique),
        # base06 - Light Foreground (Not often used)
        Base16Color('base06', pickDarkestGreyestColorUnique),
        # base07 - Light Background (Not often used)
        Base16Color('base07', pickDarkestGreyestColorUnique),
        # base08 - Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted
        Base16Color('base08', pickHighContrastBrightColorRandom),
        # base09 - Integers, Boolean, Constants, XML Attributes, Markup Link Url
        Base16Color('base09', pickHighContrastBrightColorRandom),
        # base0A - Classes, Markup Bold, Search Text Background
        Base16Color('base0A', pickHighContrastBrightColorRandom),
        # base0B - Strings, Inherited Class, Markup Code, Diff Inserted
        Base16Color('base0B', pickHighContrastBrightColorRandom),
        # base0C - Support, Regular Expressions, Escape Characters, Markup Quotes
        Base16Color('base0C', pickHighContrastBrightColorRandom),
        # base0D - Functions, Methods, Attribute IDs, Headings
        Base16Color('base0D', pickHighContrastBrightColorRandom),
        # base0E - Keywords, Storage, Selector, Markup Italic, Diff Changed
        Base16Color('base0E', pickHighContrastBrightColorRandom),
        # base0F - Deprecated, Opening/Closing Embedded Language Tags, e.g. <?php ?>
        Base16Color('base0F', pickHighContrastBrightColorRandom)]

    # For testing
    colorPool = ['#001b8c', '#0a126b', '#010e44', '#772e51', '#ca4733', '#381f4d', '#814174',
              '#90142e', '#720d21', '#28217d', '#6d2c88', '#3b0010', '#6e095b', '#827e7b',
              '#645361', '#560041']

    if colorsLines:
        colorPool = colorsLines

    # Process color pool
    for i, color in enumerate(colorPool):
        # Remove newlines
        colorPool[i] = color.strip('\n')
        color = colorPool[i]

        # For debugging
        print(color)
        rgbColor = rgbColorFromStringHex(color)
        print('RGB =', rgbColor)

    # Select a color from the color pool for each base16 color
    for i, base16Color in enumerate(base16Colors):
        color = base16Color.selectionFunction(base16Colors, base16Color, colorPool)

        if not color:
            print('WARNING: {} could not select a color! Picking one at random'.format(base16Color.name))
            color = random.choice(colorPool)

        base16Colors[i].color = color
        
        print('Selected {} for {}'.format(base16Colors[i].color, base16Color.name))

    # Output selected colors
    # TODO: implement
        

if __name__ == '__main__':
    main()
