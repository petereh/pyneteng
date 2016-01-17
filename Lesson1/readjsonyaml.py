#! /usr/bin/env python 

import yaml
import json
import pprint


with open ('myyaml.yaml') as f :
  list2 = yaml.load(f)

pprint.pprint (list2)

with open ("myjson.json") as f :
  list3 = json.load(f)

pprint.pprint(list3)
