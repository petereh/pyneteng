#! /usr/bin/env python 

import yaml
import json
from pprint import pprint


def output_format(my_list, my_str):
    '''
    Make the output format easier to read
    '''
    print '\n\n'
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3
    pprint(my_list)

def main() :
    with open ('myyaml.yaml') as f :
        list2 = yaml.load(f)

    with open ("myjson.json") as f :
        list3 = json.load(f)
        
        output_format(list2, 'YAML')
        output_format(list3, 'JSON')

if __name__ == "__main__" :
    main()
