import clean
import img
import scaper2 as s2


def start():
    s2.get_link()
    img.image()
    clean.cleanup()

if __name__ == "__main__":
    start()
