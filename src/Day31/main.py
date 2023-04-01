from wndroot import FlashCardWnd
import os


DIR = os.path.dirname(__file__)

flash_cards = FlashCardWnd("French with Flash Cards!", os.path.join(DIR, "data/french_words.csv"))
