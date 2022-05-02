# -*- coding: utf-8 -*-
"""
Created on Sun May  1 01:41:47 2022

@author: Nikhi
"""

import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_dataset(*src_filenames, labels=None):
    data = []
    for filename in src_filenames:
        with open(filename) as f:
            for line in f:
                d = json.loads(line)
                if labels is None or d['gold_label'] in labels:
                    data.append(d)
    return data

r1_train_filename = os.path.join('data', 'dynasent-v1.1-round01-yelp-train.jsonl')

ternary_labels = ('positive', 'negative', 'neutral')

r1_train = load_dataset(r1_train_filename, labels=ternary_labels)

X_train, y_train = zip(*[(d['sentence'], d['gold_label']) for d in r1_train])

df=pd.DataFrame(X_train, columns=['Text'])
df["Sentiment"] = y_train
df["Sentiment"] = df["Sentiment"].astype('category')
df["Target"] = df["Sentiment"].cat.codes