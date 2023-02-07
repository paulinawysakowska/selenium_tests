import os


def get_config():
    return {
        "first_url": os.environ.get("FIRST_URL", "https://google.com"),
        "searching_phrase": os.environ.get("SEARCHING_PHRASE", "Allegro"),


    }
