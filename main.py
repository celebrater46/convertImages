import glob
import os
import re
import cv2
import matplotlib.pyplot as plt

def convert():
    files = glob.glob('input/*')

    for f in files:
        # 全角文字（日本語とか）がファイル名に含まれている場合、バグになるので排除
        fname = re.sub('[^\x01-\x7E]', "", f)
        # 半角スペースの排除
        fname = re.sub(' ', "", fname)
        # ファイル名の変更
        os.rename(f, fname)

        img = cv2.imread(fname)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # .png を含んでいれば PNG を JPEG に変換、そうでなければ逆（拡張子を変えるだけで画像を自動変換してくれる模様）
        fname = fname.replace('.png', '.jpg') if '.png' in fname else fname.replace('.jpg', '.png')

        fname = fname.replace('input', 'output')
        cv2.imwrite(fname, img)


convert()