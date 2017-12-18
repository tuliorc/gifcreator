import os
import imageio
from PIL import Image

images = []

size = (150, 150)

for filename in os.listdir("images"):
    # only consider the extensions below when creating the gif
    if filename.endswith(".png") or filename.endswith(
            ".jpg") or filename.endswith(".jpeg") or filename.endswith(
            ".tiff") or filename.endswith(".tif"):
        im = Image.open("images/{filename}".format(filename=filename))
        # decreases the image in quality in order to reduce gif's size
        im = im.resize((im.size[0] // 2, im.size[1] // 2),
                       Image.ANTIALIAS).rotate(-90, expand=True)
        im.save("images/temporary.jpg", optimize=True, quality=85)
        print("Appending file {filename}...".format(filename=filename))
        images.append(imageio.imread("images/temporary.jpg"))
        os.remove("images/temporary.jpg")

print("Generating GIF...")
imageio.mimsave('my.gif', images)
print("Your GIF was generated!")
