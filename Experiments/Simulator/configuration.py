from json import load
from pyexpat import EXPAT_VERSION
import uuid

import pandas
from tqdm import tqdm

NUMBER_OF_NODES = 2
NUMBER_OF_SERVICES = 5
WINDOW_SIZE = 2

INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"
DATA = pandas.read_csv(f"{INPUT_FOLDER}/inmates_enriched_10k.csv")
EXPERIMENT_ID = None
def load_experiment_id():
    global EXPERIMENT_ID
    try:
        with open("experiment_id", "r") as f:
            EXPERIMENT_ID = int(f.read())
    except FileNotFoundError:
        pass
def increment_experiment_id():
    global EXPERIMENT_ID
    EXPERIMENT_ID += 1
    with open("experiment_id", "w") as f:
        f.write(str(EXPERIMENT_ID))

load_experiment_id()





def set_number_of_nodes(n):
    global NUMBER_OF_NODES
    NUMBER_OF_NODES = n
def set_number_of_services(n):
    global NUMBER_OF_SERVICES
    NUMBER_OF_SERVICES = n
def set_window_size(n):
    global WINDOW_SIZE
    WINDOW_SIZE = n


# pbar = tqdm(total=0)
# pbar = None
# let's use a global tqdm progress bar
def set_total_progress(total):
    pass
    # global pbar
    # pbar.total = total


def increment_progress():
    pass
    # global pbar
    # pbar.update(1)



WINDOW_ID = uuid.uuid4()
