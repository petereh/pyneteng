#! /usr/bin/env python

from ciscoconfparse import CiscoConfParse


def main() :

    parse = CiscoConfParse("cisco_ipsec.txt")
    # Find all crypto map entries and print parent and child

    print ("The crypto maps in the parsed config are : \n" )
    crypto_objs = parse.find_objects(r"^crypto map CRYPTO")

    for obj in crypto_objs :
        print (obj.text)
        child_obj = (obj.re_search_children(r".*"))
        for obj2 in child_obj :
            print (obj2.text)
    print ("\n")

# Find crypto maps with pfs group2

    pfsg2  = parse.find_parents_w_child("crypto map CRYPTO", "set pfs group2" )

    print ("The following crypto maps have pfs set to group 2: \n")
    for obj in pfsg2 :
        print (obj)

# Find crypto maps without AES encryptions 

    print ("\n")

    trans_set = parse.find_parents_wo_child("^crypto map CRYPTO", "set transform-set AES-SHA")
    print ("The crypto maps that do not have AES-SHA transform set are : \n")

    for obj in trans_set :
        print (obj)

if __name__ == "__main__" :
    main()

