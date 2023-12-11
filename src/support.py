

itemset_type = list[object]
dataset_type = list[list[object]]

from typing import List


itemset_type = frozenset
dataset_type = List[List[object]]

def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """
    pass
def calculate_support(dataset, itemset):
    count = 0
    total_transactions = len(dataset)

    for transaction in dataset:
        if set(itemset).issubset(transaction):
            count += 1

    support = count / total_transactions
    return support

    # initializing the counter to keep track of the occurrence in the list
    count = 0

    total_transactions = len(data_set)

    # looping through the entire dataset for occurrence of itemset
    for transaction in data_set:
        if itemsets.issubset(transaction):
            count = count + 1

    # implementing support method
    support_value = count / total_transactions

    return support_value

