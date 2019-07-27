
"""
Mini Project 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


img=Image.open("Certificate.jpg")

draw=ImageDraw.Draw(img)

namefont=ImageFont.truetype("Certificate-Regular.ttf",size=40)

draw.text((285,250),"Deepak Verma",(255,255,0), font=namefont)

datefont=ImageFont.truetype("Certificate-Regular.ttf",size=20)

draw.text((100,480),"1-May-2019",(255,255,0), font=datefont)
draw.text((500,480),"30-JULY-2019",(128,255,0), font=datefont)

img.save("certi.pdf","pdf",resolution=100.0)

"""

Mini Project  2

I-Card Generation System

Write a Python code for a system that generates I-card for all studentsof Forsk
Summer Developer Program and store them in image format. 

It must take names and other required information from the user.

"""



"""
Mini Project 3

Watermarking Application

Have some pictures you want copyright protected? Add your own logo or text lightly 
across the background so that no one can simply steal your graphics off your site. 
Make a program that will add this watermark to the picture.


"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img=Image.open("DSC_0028.jpg")


draw=ImageDraw.Draw(img)

namefont=ImageFont.truetype("Certificate-Regular.ttf",size=20)

draw.text((0,0),"Made by Deepak",fill=(0,0,255),font=namefont)

img.save("watermark.jpg")






"""
Mini Project  4
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.
"""

from PIL import Image, ImageDraw
 
 
def create_image_with_ball(width, height, ball_x, ball_y, ball_size):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # draw.ellipse takes a 4-tuple (x0, y0, x1, y1) where (x0, y0) is the top-left bound of the box
    # and (x1, y1) is the lower-right bound of the box.
    draw.ellipse((ball_x, ball_y, ball_x + ball_size, ball_y + ball_size), fill='red')
    return img

# Create the frames
frames = []
x, y = 0, 0
for i in range(10):
    new_frame = create_image_with_ball(400, 400, x, y, 40)
    frames.append(new_frame)
    x += 40
    y += 40
 
# Save into a GIF file that loops forever
frames[0].save('moving_ball.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)

"""
from video to gif
"""
from moviepy.editor import VideoFileClip

clip = (VideoFileClip("Demo.mp4", audio=False)
        .subclip((1,36.0),(1,36.9))
        .resize(0.5)
        .crop(x1=189, x2=433))

clip.write_gif('sven.gif', fps=15, fuzz=2)


"""
Mini Project  5

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. 
The code should share the Horoscope on Tweeter account of the user.

"""

from selenium import webdriver
from selenium.webdriver.chrome import service
from time import sleep
url1 = "https://www.horoscope.com/us/index.aspx"
url2="https://www.ganeshaspeaks.com/horoscopes/"
url3="https://astrostyle.com/daily-horoscopes/"

webdriver_service = service.Service("C:\\Users\\Admin\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe")
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get(url1)


horoscop=[]
nextb=driver.find_element_by_xpath("//*[@id='src-hp-pisc']/img")
sleep(5)

nextb.click()

horoscop.append((driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/div[1]/p[1]")).text)

driver.get(url2)
nextb=driver.find_element_by_xpath("/html/body/main/section[1]/div/div[2]/div[2]/div[12]/div/a[1]/i/img")
nextb.click()

horoscop.append((driver.find_element_by_xpath("//*[@id='daily']/div/div[1]/div[2]/p[1]")).text)

print("Your Horoscop of today is")
for x in horoscop:
    print(x)