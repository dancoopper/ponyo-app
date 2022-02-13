from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import io 
import requests

PATH = "C:\Program Files (x86)\chromedriver.exe"


def get_link():
    driver = webdriver.Chrome(PATH)

    driver.get('https://apod.nasa.gov/apod/astropix.html')


    images = driver.find_elements_by_tag_name('img')

    for image in images:
        src = image.get_attribute('src')
        print(src)
        #urllib.urlretrieve(src, "IC342Feller1024.jpg")
    try:
        image_content = requests.get(src).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = "nasa_pics/NasaPic.jpg"

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("shit works")
    except Exception as e:
        print('FAILED - ', e)
    
    driver.close()
if __name__ == '__main__':
    get_link()
