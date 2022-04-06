import clean
import img2
import scaper2 as s2


def start():
    s2.get_link()
    img2.MyApp().run()
    clean.cleanup()

if __name__ == "__main__":
    start()
