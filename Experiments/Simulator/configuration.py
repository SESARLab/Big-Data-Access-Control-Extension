import uuid

import pandas


NUMBER_OF_NODES = 6
NUMBER_OF_SERVICES = 3
WINDOW_SIZE = NUMBER_OF_NODES
INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"
DATA = pandas.read_csv(f"{INPUT_FOLDER}/inmates_enriched_10k.csv")
WINDOW_ID = uuid.uuid4()
