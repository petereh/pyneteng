#! /usr/bin/env python

import yaml 
import json 

list1 = range(10)
list1.append( 'peter')
list1.append('ehiwe')
list1  = range(6)
list1.append([1,2,3,44])
list1.append ( {} )
list1[-1]['router'] =  'ciscortr'
list1[-1]['switch'] = 'junos'
list1[-1]['diction'] = {'a' :1, 'b':2 }



with open ("myyaml.yaml", "w") as f:
    f.write(yaml.dump(list1, default_flow_style=False))


with open ("myjson.json", "w") as f:
    json.dump(list1, f)
