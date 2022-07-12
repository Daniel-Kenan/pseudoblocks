import PIL.Image
import art
from art import text2art
from console import console
# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "\"", "*", "+", ";", ":", ",", " "]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    # print(image.size)
    ratio = height/width
    new_height = int(new_width * ratio)-40
    resized_image = image.resize((new_width, new_height ))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    path = "./images/Wnormal1.jpg"
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    # print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("./images/ascii_image.txt", "w") as f:
        f.write(ascii_image)

    with open("./images/ascii_image.txt", "r") as f:
         for line in f.readlines():
            console(line,color="BLUE")
 
# run program
print()
main()
# my_art = text2art("successfully installed",font='bulbhead',chr_ignore=True) # Return ASCII text (default font)
# print(my_art)

console("""

                                  __       _ _         _           _        _ _          _ 
                                 / _|     | | |       (_)         | |      | | |        | |
 ___ _   _  ___ ___ ___  ___ ___| |_ _   _| | |_   _   _ _ __  ___| |_ __ _| | | ___  __| |
/ __| | | |/ __/ __/ _ \/ __/ __|  _| | | | | | | | | | | '_ \/ __| __/ _` | | |/ _ \/ _` |
\__ \ |_| | (_| (_|  __/\__ \__ \ | | |_| | | | |_| | | | | | \__ \ || (_| | | |  __/ (_| |
|___/\__,_|\___\___\___||___/___/_|  \__,_|_|_|\__, | |_|_| |_|___/\__\__,_|_|_|\___|\__,_|
                                                __/ |                                      
                                               |___/                                       


""",color='GREEN')