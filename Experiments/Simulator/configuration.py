import uuid

import pandas


NUMBER_OF_NODES = 5
NUMBER_OF_SERVICES = 5
WINDOW_SIZE = 5
INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"

DATA = pandas.read_csv(f"{INPUT_FOLDER}/inmates_enriched_10k.csv")

WINDOW_ID = uuid.uuid4()
