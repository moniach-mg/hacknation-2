import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
import pandas as pd
from spacy import displacy
from pathlib import Path
from multiprocessing import Pool

if __name__=="__main__":
    nlp = spacy.load('pl_hacknationNER')
    with open("content/data_1.txt", "r") as f:
        content = f.readlines()
    for c in content[500:505]:
        print(c)
        doc = nlp(c)
        for ent in doc.ents:
            print(ent.text, ent.label_)