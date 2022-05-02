# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 02:41:03 2022

@author: Nikhi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pre_process import final_data

from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import InputExample, InputFeatures

final_df = final_data()

print(final_df.head())

model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model.summary()