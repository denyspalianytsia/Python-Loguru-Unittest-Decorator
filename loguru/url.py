from loguru import logger
import time
import requests

def contents_of_url(url):
    try:
        time_begin = time.time()
        contents = requests.get(url)
        time_after = time.time()
        finish = time_after - time_begin
        logger.info(f"Content of this URL: {contents.text}")
        logger.info(f"Response status: {contents}")
        logger.info(f"Time: {finish}")
    except:
        logger.error("Oops, something went wrong")


url = input("Input your URL: ")
contents_of_url(url)