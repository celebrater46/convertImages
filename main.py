import glob
import cv2
import matplotlib.pyplot as plt

def convert():
    # dst_dir = 'output'
    # os.makedirs(dst_dir, exist_ok=True)

    files = glob.glob('input/*')

    for f in files:
        img = cv2.imread(f)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        fname = f.replace('.jpg', '.png')
        fname = fname.replace('input', 'output')
        cv2.imwrite(fname, img)
        # img = Image.open(f)
        # img_resize = img.resize((img.width // 2, img.height // 2))
        # root, ext = os.path.splitext(f)
        # basename = os.path.basename(root)
        # img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))