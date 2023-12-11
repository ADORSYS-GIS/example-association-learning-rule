
itemset_type = list[object]
dataset_type = list[list[object]]


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
dataset = [
    ['A', 'B', 'C'],
    ['B', 'C', 'D'],
    ['A', 'B', 'D'],
    ['A', 'C', 'D'],
    ['A', 'C', 'E'],
]

itemset = ['A', 'C']

support = calculate_support(dataset, itemset)
print("Support:", support)
