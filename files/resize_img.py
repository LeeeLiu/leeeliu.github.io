from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width, height):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width,height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)[0:-3]+'png'))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    parent_dir = '../data/stanfordDogs/'
    namelist = os.listdir(parent_dir)       #得到文件夹下的所有文件名称
    for name in namelist:
        for jpgfile in glob.glob(parent_dir + name +'/*.jpg'):
            convertjpg(jpgfile, "../converted_data/images0/", 64, 64)