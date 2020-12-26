from dotenv import load_dotenv, find_dotenv

from runt import api


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    api.run()
