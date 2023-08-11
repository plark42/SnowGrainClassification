import os
from skimage import io

files = os.listdir('original')
i = 0
for fName in files:
    if not 'IMG' in fName:
        continue

    fName = 'original/' + fName
    img = io.imread(fName)
    print(fName, img.shape)
    if(img.shape[0] == 3036):
        cmd = 'convert -rotate 90 -compress None %s tmp.tiff' % (fName) 
        os.system(cmd)
        fName = 'tmp.tiff'

          
    inFile = 'round_%05d.tiff' % (i)
    cmd = 'convert -resize 1024x768! -compress None %s %s' % (fName, inFile)
    os.system(cmd)
    i += 1
    
    cmd = 'convert -flip  -compress None %s round_%05d.tiff' % (inFile, i) 
    os.system(cmd)
    i += 1 

    cmd = 'convert -flop  -compress None %s round_%05d.tiff' % (inFile, i) 
    os.system(cmd)
    i += 1

    cmd = 'convert -rotate 90 -compress None %s round_%05d.tiff' % (inFile, i) 
    os.system(cmd)
    i += 1 

    cmd = 'convert -rotate 180 -compress None  %s round_%05d.tiff' % (inFile, i) 
    os.system(cmd)
    i += 1 

    cmd = 'convert -rotate 270 -compress None %s round_%05d.tiff' % (inFile, i) 
    os.system(cmd)
    i += 1 
