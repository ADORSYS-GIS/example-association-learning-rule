import numpy as np
from itertools import combinations, chain

def count_occurences(itemset, transaction):
    count = 0
    for i in range(len(transaction)):
        if set(itemset).issubset(set(transaction[i])):
            count += 1
    return count

def join_two_itemsets(it1, it2, order):
    it1.sort(key=lambda x: order.index(x))
    it2.sort(key=lambda x: order.index(x))

    for i in range(len(it1)-1):
        if it1[i]  != it2[i]:
            return
    if order.index(it1[-1]) < order.index(it2[-1]):
        return it1 + [it2[-1]]
    return []

def join_set_itemsets(set_of_its, order):
    C = []
    for i in range(len(set_of_its)):
        for j in range(i+1, len(set_of_its)):
            it_out = join_two_itemsets(set_of_its[i], set_of_its[j], order)
            if it_out is not None and len(it_out) > 0:
                C.append(it_out)
    return C


def  load_transaction_data(path_of_data, order):
    transaction = []
    with open(path_of_data, 'r') as fid:
        for lines in fid:
            str_line = list(lines.strip().split(','))
            #raegardless of how many times an items appears it is treated as one  in a transaction
            _t = list(np.unique(str_line))
            #sorting results in list in lexical order
            _t.sort(key=lambda x: order.index(x))
            transaction.append(_t)
    return transaction


def get_frequent(itemsets, transaction, min_support, prev_discarded):
    L =[] #list of frequet itemsets
    supp_count = [] #count of the itemset
    new_discarded = []
    
    
    k = len(prev_discarded.keys())
    for s in range (len(itemsets)):
        #check if an itemset was previously discarded before checking the frequency
        discarded_before = False
        if k > 0:
            #checking for subsets of previosly discarded itemsets
            for it in prev_discarded[k]:
                if set(it).issubset(set(itemsets[s])):
                    discarded_before = True
                    break
        if not discarded_before:
            count = count_occurences(itemsets[s], transaction)
            if count/len(transaction)>= min_support:
                L.append(itemsets[s])
                supp_count.append(count)
            else:
                new_discarded.append(itemsets[s])
    return L, supp_count, new_discarded


#Generating association rules according to frequent itemsets above

#starting from frequent sets of size 2 ie (k = 1), since frequent sets of size one can't produce significant rules
def powerset(s):
   return list(chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1)))

def write_rules(X, X_S, S, conf, supp, lift, num_trans):
    out_rules = ""
    out_rules += "Freq. Itemset: {}\n".format(X)
    out_rules += " Rule: {} -> {} \n".format(list(S), list(X_S))
    out_rules += " conf: {0:2.3f}  ".format(conf)
    out_rules += " supp: {0:2.3f}  ".format(supp / num_trans)
    out_rules += " lift: {0:2.3f}  ".format(lift)
    return out_rules