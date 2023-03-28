from loguru import logger
import subprocess
import time

def copy_file(first_path, second_path):
    try:
        time_begin = time.time()
        subprocess.run(f"cp {first_path} {second_path}")
        time_after = time.time()
        finish = time_after - time_begin
        logger.info(f"Copy informations from {first_path} to {second_path}")
        logger.info(f"Copy time: {finish}")
    except:
        logger.error("File not found or func doesn`t work as needed")

first_path = str(input("Input first path: "))
second_path = str(input("Input second path: "))

copy_file(first_path, second_path)