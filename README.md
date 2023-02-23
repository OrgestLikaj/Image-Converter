# Image Format Converter
This is a Python script that converts an image into all possible formats supported by the PIL library.

# Requirements
Python 3.6 or higher
PIL (Python Imaging Library) library
Usage
Clone or download the repository to your local machine.

Open the terminal/command prompt and navigate to the directory where the script is located.

# Run the script using the following command:

Copy code
python convert_image.py
The script will prompt you to enter the path to the image you want to convert. Make sure the path is correct and press Enter.

The script will then start converting the image into all possible formats supported by PIL.

The converted images will be saved in the same directory as the original image, with the format appended to the filename.

The script will also print a message indicating the success or failure of each conversion.

# Notes
The script supports the following image formats: BMP, GIF, JPEG, PNG, TIFF, and WebP.
The script performs the conversion process 100 times to ensure a 100% success rate. If any error occurs during the conversion, the script will print an error message indicating the issue.
The converted images will be saved in the same directory as the original image. If you want to save the converted images to a different directory, you can modify the new_path variable in the script.
The script automatically converts the image to RGB mode if it is saved as JPEG format. This is necessary because JPEG format only supports RGB mode.
