from PIL import Image
import os

# specify the path of the image you want to convert
image_path = 'path/to/your/image.png'

# create a list of all possible formats that are compatible with each other
formats = ['bmp', 'gif', 'jpeg', 'png', 'tiff', 'webp']

# loop through the formats list and save the image in each format 100 times
for i in range(100):
    for format in formats:
        try:
            new_path = os.path.splitext(image_path)[0] + '_' + str(i) + '.' + format
            if format == 'jpeg':
                # convert to RGB mode if saving as JPEG
                img = Image.open(image_path).convert('RGB')
            else:
                img = Image.open(image_path)
            img.save(new_path, format=format)
            print(f"Image {i}: saved as {format}")
        except Exception as e:
            print(f"Error saving image {i} as {format}: {e}")
