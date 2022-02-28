import io
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


PATH = r"C:\geckodriver.exe"
#PATH = "C:\\Program Files (x86)\\chromedriver.exe"

def get_link():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=PATH, options=options)
    
    #driver = webdriver.Chrome(PATH)
    
    driver.get('https://apod.nasa.gov/apod/astropix.html')


    images = driver.find_elements_by_tag_name('img')

    '''Check_vid = driver.switch_to.frame('YouTube video player')
    if images == False:
        for _ in Check_vid:
            V_src = Check_vid.__getattribute__('src')
        try:
            print(V_src)
        except Exception as e:
            print('FAILED - ', e)
            print("try checking out the vid")
            print("press ctrl + c to close...")
    else:'''
    for image in images: #if shit abuve tab this is 
            src = image.get_attribute('src')
            print(src)
            #urllib.urlretrieve(src, "IC342Feller1024.jpg")
    try: # and this
            image_content = requests.get(src).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)
            file_path = "nasa_pics/NasaPic.jpg"

            with open(file_path, "wb") as f:
                image.save(f, "JPEG")

            print("shit works")
    except Exception as e: # and this
            print('FAILED - ', e)
    
    driver.close()
if __name__ == '__main__':
    get_link()
