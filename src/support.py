itemset_type = tuple[object]
dataset_type = list[list[object]]

def support(dataset: dataset_type, itemset: itemset_type) -> float:
    """
    Calculate the support of an itemset in the dataset.
    """
    count = 0
    for transaction in dataset:
        if set(itemset).issubset(transaction):
            count += 1
    return count / len(dataset)

