import uuid

import pandas
from tqdm import tqdm

NUMBER_OF_NODES = 5
NUMBER_OF_SERVICES = 5
WINDOW_SIZE = 2
INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"

DATA = pandas.read_csv(f"{INPUT_FOLDER}/inmates_enriched_10k.csv")

WINDOW_ID = uuid.uuid4()
pbar = None
def set_total_combinations(total):
    global pbar
    pbar = tqdm(total=total)

def update_progress():
    global pbar
    pbar.update(1)
