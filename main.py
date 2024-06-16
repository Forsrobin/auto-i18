import json
from translate import Translator
import threading


def main():
    translator = Translator("messages/swe_Latn.json")
    translator.start("spa_Latn")



if __name__ == "__main__":
    main()