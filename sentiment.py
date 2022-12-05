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
from dynasent import load_dynasent 

from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import InputExample, InputFeatures
import tensorflow as tf

from sklearn.model_selection import train_test_split

# final_df = final_data()

# print(final_df.head())

model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model.summary()

dyna_df = load_dynasent()
print(dyna_df.head())

dyna_df = dyna_df.iloc[:1000,:]

# X = dyna_df["Text"]
# y = dyna_df["Target"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

train_split = (int)(0.8*(len(dyna_df)))
#test_split = (int)(0.2*(len(dyna_df)))

train_df = dyna_df.iloc[:train_split,:]
test_df = dyna_df.iloc[train_split:,:]

# ex = InputExample(guid=None,
#              text_a = "Hello, world",
#              label = 1)

# print(ex.text_b)

def convert_data_to_examples(train, test, DATA_COLUMN, LABEL_COLUMN): 
  train_InputExamples = train.apply(lambda x: InputExample(guid=None, # Globally unique ID for bookkeeping, unused in this case
                                                          text_a = x[DATA_COLUMN], 
                                                          label = x[LABEL_COLUMN]), axis = 1)

  validation_InputExamples = test.apply(lambda x: InputExample(guid=None, # Globally unique ID for bookkeeping, unused in this case
                                                          text_a = x[DATA_COLUMN], 
                                                          label = x[LABEL_COLUMN]), axis = 1)
  
  return train_InputExamples, validation_InputExamples

  train_InputExamples, validation_InputExamples = convert_data_to_examples(train, 
                                                                           test, 
                                                                           'DATA_COLUMN', 
                                                                           'LABEL_COLUMN')
  
def convert_examples_to_tf_dataset(examples, tokenizer, max_length=128):
    features = [] # -> will hold InputFeatures to be converted later

    for e in examples:
        # Documentation is really strong for this method, so please take a look at it
        input_dict = tokenizer.encode_plus(
            e.text_a,
            add_special_tokens=True,
            max_length=max_length, # truncates if len(s) > max_length
            return_token_type_ids=True,
            return_attention_mask=True,
            pad_to_max_length=True, # pads to the right by default # CHECK THIS for pad_to_max_length
            truncation=True
        )

        input_ids, token_type_ids, attention_mask = (input_dict["input_ids"],
            input_dict["token_type_ids"], input_dict['attention_mask'])

        features.append(
            InputFeatures(
                input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids, label=e.label
            )
        )

    def gen():
        for f in features:
            yield (
                {
                    "input_ids": f.input_ids,
                    "attention_mask": f.attention_mask,
                    "token_type_ids": f.token_type_ids,
                },
                f.label,
            )

    return tf.data.Dataset.from_generator(
        gen,
        ({"input_ids": tf.int32, "attention_mask": tf.int32, "token_type_ids": tf.int32}, tf.int64),
        (
            {
                "input_ids": tf.TensorShape([None]),
                "attention_mask": tf.TensorShape([None]),
                "token_type_ids": tf.TensorShape([None]),
            },
            tf.TensorShape([]),
        ),
    )


DATA_COLUMN = 'Text'
LABEL_COLUMN = 'Target'

train_InputExamples, validation_InputExamples = convert_data_to_examples(train_df, test_df, DATA_COLUMN, LABEL_COLUMN)

train_data = convert_examples_to_tf_dataset(list(train_InputExamples), tokenizer)
# train_data = train_data.shuffle(100).batch(32).repeat(2)
train_data = train_data.shuffle(100).batch(8)

validation_data = convert_examples_to_tf_dataset(list(validation_InputExamples), tokenizer)
validation_data = validation_data.batch(8)

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy('accuracy')])

model.fit(train_data, epochs=20, validation_data=validation_data)

# def convert_example_to_feature(review):
#   return tokenizer.encode_plus(review,
#                 add_special_tokens = True, # add [CLS], [SEP]
#                 max_length = max_length, # max length of the text that can go to BERT
#                 pad_to_max_length = True, # add [PAD] tokens
#                 return_attention_mask = True, # add attention mask to not focus on pad tokens
#               )

# # can be up to 512 for BERT
# max_length = 512
# batch_size = 6

# def map_example_to_dict(input_ids, attention_masks, token_type_ids, label):
#   return {
#       "input_ids": input_ids,
#       "token_type_ids": token_type_ids,
#       "attention_mask": attention_masks,
#   }, label

# def encode_examples(ds, limit=-1):
#   # prepare list, so that we can build up final TensorFlow dataset from slices.
#   input_ids_list = []
#   token_type_ids_list = []
#   attention_mask_list = []
#   label_list = []
#   if (limit > 0):
#       ds = ds.take(limit)
#   for review, label in tfds.as_numpy(ds):
#     bert_input = convert_example_to_feature(review.decode())
#     input_ids_list.append(bert_input['input_ids'])
#     token_type_ids_list.append(bert_input['token_type_ids'])
#     attention_mask_list.append(bert_input['attention_mask'])
#     label_list.append([label])
#   return tf.data.Dataset.from_tensor_slices((input_ids_list, attention_mask_list, token_type_ids_list, label_list)).map(map_example_to_dict)

# # train dataset
# ds_train_encoded = encode_examples(ds_train).shuffle(10000).batch(batch_size)
# # test dataset
# ds_test_encoded = encode_examples(ds_test).batch(batch_size)