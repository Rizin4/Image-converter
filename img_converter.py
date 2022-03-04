from PIL import Image
import sys

try:
    fullimageFileName = sys.argv[1]

    operation = sys.argv[2]

    argument = sys.argv[3]

    if operation == '-f':
        
        r = fullimageFileName.split('.')

        imageFileName = r[0]

        im = Image.open(fullimageFileName)

        converted = im.convert('RGB')

        converted.save(f'{imageFileName}t.{argument}')


    elif operation == '-r':
        im = Image.open(fullimageFileName)
        r = argument.split('x')
        r_tuple = (int(r[0]), int(r[1]))
        out = im.resize(r_tuple)
        out.save(f'output_{fullimageFileName}')

except:
    
    print('')
    print('Usage :')
    print('python img_converter.py [input file name] [operation] [argument]')
    print('')
    print('Operation: ')
    print('-f :To change format of image')
    print('1: python img_converter.py image.jpeg -f png ')
    print('2: python img_converter.py image.png -f jpeg ')
    print()
    print('-r :To resize the image')
    print('1)python img_converter.py image.jpeg -r 200x200 ')
    print('2)python img_converter.py image.jpeg -r 250x200 ')
    print('')