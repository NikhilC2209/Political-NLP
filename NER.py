# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:12:13 2022

@author: Nikhi
"""

import spacy
from spacy import displacy
import en_core_web_sm

NER = en_core_web_sm.load()

#NER = spacy.load("en_core_web_sm")

raw_text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
text = "Best wishes of Rajasthan Day to all the residents of Rajasthan, the historical land of bravery, self-respect and sacrifice. The state should move forward on the path of progress, this is the wish."
text_1 = "Come, let’s celebrate the festival of examinations. Let’s talk stress free examinations. See you on 1st April at Pariksha Pe Charcha."
text1= NER(text_1)
print(spacy.explain("GPE"))

#displacy.render(text1,style="ent",jupyter=True)

displacy.serve(text1, style="ent")