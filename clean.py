import os
import os.path
from time import sleep
import shutil
'''
pic_1 = "C:/Users/YOUR NAME/Downloads/nasa1.jpg"
pic_2 = "C:/Users/YOUR NAME/Downloads/nasa2.jpg"
pic_3 = "C:/Users/YOUR NAME/Downloads/nasa3.jpg"
'''
def cleanup():  # sourcery skip: hoist-statement-from-if
  
  if os.path.isdir("nasa_pics"):
    shutil.rmtree("nasa_pics")
    os.mkdir("nasa_pics")
    '''
    shutil.copy(pic_1, "nasa_pics")
    shutil.copy(pic_2, "nasa_pics")
    shutil.copy(pic_3, "nasa_pics")
    '''
    
if __name__ == "__main__":
    cleanup()
