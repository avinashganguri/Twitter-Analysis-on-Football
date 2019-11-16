# -*- coding: utf-8 -*-
import jsonpickle
import json

tweets = list(open('data1.json','rt'))

for x in tweets:
        x = json.loads(x)
        try:
                if len(x['entities']['hashtags']) != 0:
                        for p in x['entities']['hashtags']:
                                print(p['text'])
        except KeyError:
                pass

