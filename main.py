"""""""""""""""""""""""""""""""""""""""""""""
                                             |
Made by crazybarsuk (http://t.me/crazybarsuk)|
                                             |
"""""""""""""""""""""""""""""""""""""""""""""

import os
import sys

try: from PIL import Image
except ImportError: raise ImportError('Введите в консоль следующую команду: pip3 install Pillow')

dir = input('Введите полный путь до папки с изображениями: ')

def path(*args):
        
    if sys.platform == 'win32': return '\\'.join(args)
    elif sys.platform in ['linux', 'linux2', 'darwin']: return '/'.join(('',) + args)
        
    return path


allowed_os = ['win32', 'linux', 'linux2', 'darwin']
if sys.platform not in allowed_os: exit('Платформа не поддерживается.')

extensions = ['jpg', 'jpeg', 'bmp', 'png']
images = sorted([file for file in os.listdir(dir) if os.path.isfile(path(dir, file)) and file.split('.')[-1] in extensions])

sizes = {image: map(int, input(f'{image}: X Y: ').split()) for image in images}

for image in images:
    
    IMG = Image.open(path(dir, image))
    x, y = IMG.size
    
    n_x, n_y = sizes[image]
    
    os.makedirs(path(dir, 'splitted', ''.join(image.split('.')[:-1])), exist_ok=True)
    step_x = x // n_x
    step_y = y // n_y
    N = 1
    for Y in range(0, y, step_y):
        for X in range(0, x, step_x):
            if N > n_x * n_y: break
            print(f'{image}: {N}/{n_x * n_y}')
            IMG.crop((X, Y, X + step_x, Y + step_y)).save(path(dir, 'splitted', ''.join(image.split('.')[:-1]), f'{N}.png'), quality=100)
            N += 1
