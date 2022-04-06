import io

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

PATH = r"C:\geckodriver.exe"
#PATH = "C:\\Program Files (x86)\\chromedriver.exe"

def log_date():
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=PATH, options=options)
        
        driver.get("https://apod.nasa.gov/apod/archivepix.html")

        lnks= driver.find_elements_by_tag_name("a")
        # traverse list
        print(lnks[1])
        
def get_link():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=PATH, options=options)
    
    #driver = webdriver.Chrome(PATH)
    
    driver.get('https://apod.nasa.gov/apod')
    

        # https://apod.nasa.gov/apod/astropix.html

    images = driver.find_elements_by_tag_name('img')
    for image in images: #if shit abuve tab this in 
            src = image.get_attribute('src')
            print(src) #debug
            
    try: 
            image_content = requests.get(src).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)
            file_path = "nasa_pics/NasaPic.jpg"

            with open(file_path, "wb") as f:
                image.save(f, "JPEG")

            print("shit works") #debug
    except Exception as e: # and this
            print('FAILED - ', e)
    
    driver.close()
if __name__ == '__main__':
    get_link()
