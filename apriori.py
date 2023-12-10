import numpy as np
from utils import *
from functions import load_transaction_data, get_frequent,join_set_itemsets,count_occurences,write_rules,powerset


path_to_data = 'Data.txt'
min_support = 2/9
min_confidence = 0.3 # 30 percent
order = ['I' + str(i) for i in range(1,6)]
#print(order)

with open(path_to_data, "r") as file:
    data = file.read()
transactions = data.split("\n")
num_trans = len(transactions)
#print(num_trans)

Transactions = load_transaction_data(path_to_data, order)

#innitialization
#for itemsets of 1
C = {}
L = {}
itemset_size = 1
Discarded = {itemset_size : []}
C.update({itemset_size : [ [f] for f in order ]})

#creating L1 (Frequent itemsets)
supp_cnt_L = {}
f, sup, new_discarded = get_frequent(C[itemset_size], Transactions, min_support, Discarded)
Discarded.update({ itemset_size: new_discarded}) #real discarded itemsets from first iteration
L.update({itemset_size : f})
supp_cnt_L.update({itemset_size : sup})

result = (L[1], supp_cnt_L[1])

k = itemset_size + 1
convergence = False
while not  convergence:
    C.update({k:join_set_itemsets(L[k-1], order)})
    print("Result C{} \n".format(k))
    tresult= C[k], [count_occurences(it, Transactions) for it in C[k]]
    print (result)
    print()
    f, sup, new_discarded = get_frequent(C[k],Transactions, min_support, Discarded)
    Discarded.update({k : new_discarded})
    L.update({k : f})
    supp_cnt_L.update({k : sup})
    if len(L[k]) == 0:
        convergence = True
    else:
        print("Table L{} \n".format(k))
        result = L[k], supp_cnt_L[k]
        print(result)
        print()
    k += 1

#Generating association rules according to frequent itemsets above

#starting from frequent sets of size 2 ie (k = 1), since frequent sets of size one can't produce significant rules

assoc_rules_str = ""

for i in range(1, len(L)):
    for j in range (len(L[i])):
        s = powerset(set(L[i][j]))
        s.pop() #subset containing all the elements will be gotten rid of
        for z in s:
            S = set(z)
            X = set(L[i][j])
            X_S = set(X-S)
            sup_x = count_occurences(X, Transactions)
            sup_x_s = count_occurences(X_S, Transactions)
            conf = sup_x / count_occurences(S, Transactions)
            lift = conf / (sup_x_s/num_trans)
            if conf >= min_confidence and sup_x >= min_support:
                assoc_rules_str += write_rules(X, X_S, S, conf, sup_x, lift, num_trans)

print(assoc_rules_str)
