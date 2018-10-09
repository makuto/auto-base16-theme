# AutoBase16Theme.py by Macoy Madson
# MIT License
# https://github.com/makuto/auto-base16-theme

def main():
    colorsFile = open('colors.txt', 'r')
    colorsLines = colorsFile.readlines()
    colorsFile.close()

    colors = ['#001b8c', '#0a126b', '#010e44', '#772e51', '#ca4733', '#381f4d', '#814174',
              '#90142e', '#720d21', '#28217d', '#6d2c88', '#3b0010', '#6e095b', '#827e7b',
              '#645361', '#560041']

    if colorsLines:
        colors = colorsLines
        
    for color in colors:
        print(color)

        # From https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
        rgbColor = tuple(int(color.strip('#\n')[i:i+2], 16) for i in (0, 2 ,4))
        
        print('RGB =', rgbColor)

        

if __name__ == '__main__':
    main()
