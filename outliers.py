import pickle
import sys
import textwrap
import os
import re
import random

import numpy as np

outliers = set()
for essay_set in range(10):
    ids, essays, y1, y2 = [], [], [], []
    for line in open('train.tsv'):
        id, set_id, score1, score2, text = line.split('\t')
        if id == 'Id' or int(set_id) - 1 != essay_set:
            continue

        ids.append(id)
        y1.append(int(score1))
        y2.append(int(score2))
        essays.append(text.lower())

    for i in range(len(y1)):
        essay = essays[i].strip()

        if y1[i] >= 2 and len(essay.split()) < 20 and\
                re.match('[a-z:]', essay[-1]) and\
                essay_set not in {9}:
            outliers.add(ids[i])

pickle.dump(outliers, open('data/outliers.pkl', 'w'), 2)

