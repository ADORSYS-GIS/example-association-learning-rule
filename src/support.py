
#defining the contents of itemset and dataset.
#itemset contains  is a tuple that takes in some objects
#dataset is a list of list that take in objects(transactions)
itemset_type = tuple[object]
dataset_type = list[list[object]]

#creating function to calculate the  support (which is the number of transactions containign an itemset / total number of transactions)
def calculate_support(dataset: dataset_type, itemset: itemset_type) -> float:
    """
    Calculate the support of an itemset in the dataset.
    """
    #initialising a certain count to zero
    count = 0
        #looping through the dataset(each transaction)
    for transaction in dataset:
        #checking if the itemset objects are subsets of the specific list(transaction) in dataset...
        #if YES , count will increment by 1
        #as count increments by 1, we take count to be our number of transactions containing an itemset 
        # the total number of transaction which is 5 in our case
        #hence count = number of itemset objects that are a subset of dataset.
        if set(itemset).issubset(transaction):
            count += 1
    return count / len(dataset)


#support function
# This function takes two arguments: dataset (a list of transactions) and itemsets (a list of itemsets).
# It creates an empty dictionary called support_values to store the support values for each itemset.
# It iterates through each itemset in the itemsets list.
# For each itemset, it calls the calculate_support function with the current dataset and itemset as arguments.
# The returned support value is then stored in the support_values dictionary with the corresponding itemset as the key.
# Finally, the function returns the dictionary with all the calculated support values.
def support(dataset: dataset_type, itemsets: list[itemset_type]) -> dict[itemset_type, float]:
    """
    Find the frequency of itemsets in the dataset.
    """

    #the support value refers to the frequency of an itemset appearing in a dataset
    support_values = {}
    for itemset in itemsets:
        support_values[itemset] = calculate_support(dataset, itemset)
    return support_values


# testing
dataset = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'eggs'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola']
]
itemsets = [('bread', 'milk'), ('diaper', 'cola'), ('milk', 'diaper'), ('bread', 'milk', 'diaper')] 

support_values = support(dataset, itemsets)
for itemset, support in support_values.items():
    print(f"Support of {itemset}: {support}")