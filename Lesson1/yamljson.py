#! /usr/bin/env python

import yaml 
import json 


def main():
    my_dict = {
                'router' : 'cisco',
                'switch' : 'juniper',
                'os' : 'ios'
              }

    list1 = [
            0,
            1,
            2,
            3,
            "peter",
            "ehiwe",
            my_dict
            ]


    with open ("myyaml.yaml", "w") as f:
        f.write(yaml.dump(list1, default_flow_style=False))


    with open ("myjson.json", "w") as f:
        json.dump(list1, f)

if __name__ == "__main__" :
    main()
