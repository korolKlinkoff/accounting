from tqdm import tqdm
from time import sleep


def get_employees():
    # cool progressbar for "db"
    for i in tqdm(range(10)):
        sleep(0.1)
    return ["obj1", "obj2", "obj3"]
