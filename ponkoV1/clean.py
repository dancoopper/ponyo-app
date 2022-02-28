import os
import os.path
from time import sleep
import shutil



def cleanup():  # sourcery skip: hoist-statement-from-if
  
  if os.path.isdir("nasa_pics"):
    shutil.rmtree("nasa_pics")
    os.mkdir("nasa_pics")
    
if __name__ == "__main__":
    cleanup()