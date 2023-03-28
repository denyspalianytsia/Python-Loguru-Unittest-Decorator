from loguru import logger
import time

def sum(a, b):
    try:
        time_begin = time.time()
        sum = a + b
        logger.info(f"{a} + {b} = {sum}")
        time_after = time.time()
        finish = time_after - time_begin
        logger.info(f"Processing time: {finish} sec")
    except:
        logger.error("Oops, func doesn't work as needed")

a = int(input("Input first number: "))
b = int(input("Input second number: "))
sum(a, b)

