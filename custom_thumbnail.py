
from PIL import Image, ImageFilter
import os
#image1 = Image.open('harry.jpg')
#image1.show()
#image1.save('harry.png')

#size_300 = (300, 300)
#size_128 = (128, 128)

pixel =int(input("Enter the pixel: "))
directory = input("Enter the output directory name: ")
testfolder = input("Enter the test folder name: ")
size_custom = (pixel, pixel)

try:
    if not os.path.exists(directory):
        os.makedirs(directory)
except OSError:
    print('Error: Creating. ' + directory)

num = 0 
for f in os.listdir(testfolder):
    if f.endswith('.png') or f.endswith('.jpg') :
        i = Image.open('/home/changcw/practice/thumbnailproject/{}/{}'.format(testfolder, f))
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_custom)
        i.save('{}/{}_{}_{}'.format(directory,fn,pixel, '.png'))
        num +=1

print('Total: ', num, 'file(s)' , ' change into ' , pixel , 'pixels', ' in the ' , directory , ' folder')
#        i.thumbnail(size_128)
#        i.save('128/{}_128{}'.format(fn, fext))
