itemset_type = tuple[object]
dataset_type = list[list[object]]

def support(dataset: dataset_type, itemset: itemset_type) -> float:
    """
    Calculate the support of an itemset in the dataset.
    """
    #initialising a certain count to zero
    count = 0
        #looping through the dataset(each transaction)
    for transaction in dataset:
        
        if set(itemset).issubset(transaction):
            count += 1
    return count / len(dataset)

