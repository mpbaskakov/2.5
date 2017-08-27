from multiprocessing import Pool
import subprocess
import os

def find_images():
    images = os.listdir('Source')
    return images

def resize_image(link):
    input = os.path.join('Source', link)
    output = os.path.join('Result', link)
    subprocess.run(['convert', input, '-resize', '200', output])

if __name__ == '__main__':
    try:
        os.mkdir('Result')
    except FileExistsError:
        print('Папка уже существует')
    with Pool(4) as p:
        p.map(resize_image, find_images())
