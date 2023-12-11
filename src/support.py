from typing import List

itemset_type = frozenset
dataset_type = List[List[object]]

def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """
    count=0
    for transaction in dataset:
        if set(itemset).issubset(transaction):
             count += 1
    support_value=count/len(dataset)
    return support_value
 
if __name__==('__main__'):        
        # Mock dataset
    dataset = [
                ['top', 'milk', 'home'],
                ['top', 'fanta', 'beer', 'fish'],
                ['milk', 'fanta', 'beer', 'cola'],
                ['top', 'milk', 'fanta', 'beer'],
                ['top', 'milk', 'fanta', 'cola']
            ]
    itemset = ['milk']

    support_value = support(itemset, dataset)
    print("Support value for itemset:", support_value)
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


