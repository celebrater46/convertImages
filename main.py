import glob
import cv2
import matplotlib.pyplot as plt

def convert():
    files = glob.glob('input/*')

    for f in files:
        img = cv2.imread(f)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # .png を含んでいれば PNG を JPEG に変換、そうでなければ逆（拡張子を変えるだけで画像を自動変換してくれる模様）
        fname = f.replace('.png', '.jpg') if '.png' in f else f.replace('.jpg', '.png')

        fname = fname.replace('input', 'output')
        cv2.imwrite(fname, img)

convert()