from pathlib import Path
import matplotlib.pyplot as plt


def display(images, count=5, is_gray=False):
    plt.figure(figsize=(20, 20))
    for i, image in enumerate(images):
        if is_gray:
            plt.subplot(1, count, i+1)
            plt.imshow(image, cmap='gray'), plt.axis('off')
        else:
            plt.subplot(1, count, i+1), plt.imshow(image), plt.axis('off')
    plt.tight_layout()


def get_path(file_name):
    path_images = '/mnt/c/data/IP_images'
    path = str(Path(path_images, file_name))
    return path
