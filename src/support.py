itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.

    Args:
        itemsets: A dataset of itemsets represented as a list of lists of objects.
        data_set: An itemset for which the support needs to be calculated.

    Returns:
        The support value, which is the frequency of the itemset in the dataset.
    """
    count = 0
    for transaction in itemsets:
        if set(data_set).issubset(transaction):
            count += 1

    return count / len(itemsets)

if  __name__ == "__main__":

    itemsets = [
        ['A', 'B', 'C'],
        ['B', 'C', 'D'],
        ['A', 'B', 'D'],
        ['C', 'D', 'E'],
        ['A', 'C', 'E'],
    ]

data_set = ['A', 'B']

support_value = support(itemsets, data_set)

print(f"Support Value: {support_value}")

