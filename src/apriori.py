from typing import List, Tuple, Dict

sub_dataset_type = Tuple[object]
support_type = float
strong_rules_type = Tuple[List[object], List[object]]
confidence_type = float

def generate_candidates(prev_candidates: List[sub_dataset_type], k: int) -> List[sub_dataset_type]:
    """
    Generate candidate itemsets of size k from the previous candidates.
    """
    candidates = []
    for i in range(len(prev_candidates)):
        for j in range(i + 1, len(prev_candidates)):
            itemset1 = prev_candidates[i]
            itemset2 = prev_candidates[j]
            if itemset1[:k - 2] == itemset2[:k - 2]:
                candidates.append(tuple(sorted(set(itemset1) | set(itemset2))))
    return candidates

def calculate_support(dataset: List[List[object]], candidate: sub_dataset_type) -> float:
    """
    Calculate the support of a candidate itemset in the dataset.
    """
    count = sum(1 for transaction in dataset if set(candidate).issubset(transaction))
    return count / len(dataset)

def apriori(transactions: List[List[object]], min_support: float = 0.7, min_confidence: float = 0.5) \
        -> Tuple[Dict[sub_dataset_type, support_type], Dict[strong_rules_type, confidence_type]]:
    """
    Find all frequent itemsets in a dataset and generate strong association rules.
    """
    # Step 1: Find frequent 1-itemsets
    unique_items = set(item for transaction in transactions for item in transaction)
    candidates_1 = [(item,) for item in unique_items]
    frequent_1 = [(item,) for item in unique_items if calculate_support(transactions, (item,)) >= min_support]

    # Initialize variables
    k = 2
    frequent_itemsets = {1: frequent_1}
    while len(frequent_itemsets[k - 1]) > 0:
        # Generate candidate itemsets of size k
        candidates_k = generate_candidates(frequent_itemsets[k - 1], k)

        # Calculate support for each candidate and filter out infrequent itemsets
        frequent_k = [candidate for candidate in candidates_k
                      if calculate_support(transactions, candidate) >= min_support]

        # Store frequent itemsets of size k
        frequent_itemsets[k] = frequent_k
        k += 1

    # Step 2: Generate strong association rules
    strong_rules = []
    for size, itemsets in frequent_itemsets.items():
        if size > 1:
            for itemset in itemsets:
                for i in range(1, len(itemset)):
                    premise = itemset[:i]
                    conclusion = itemset[i:]
                    rule = (list(premise), list(conclusion))
                    rule_confidence = calculate_support(transactions, itemset) / calculate_support(transactions, premise)
                    if rule_confidence >= min_confidence:
                        strong_rules.append((list(premise), list(conclusion)))

    # Create dictionaries for frequent itemsets and strong rules
    frequent_itemsets_dict = {itemset: calculate_support(transactions, itemset) for size, itemsets in frequent_itemsets.items()
                              for itemset in itemsets}
    strong_rules_dict = {rule: calculate_support(transactions, rule[0] + rule[1]) / calculate_support(transactions, rule[0])
                        for rule in strong_rules}

    return frequent_itemsets_dict, strong_rules_dict

# Example Usage:
if __name__ == "__main__":
    # Example dataset
    transactions = [
        ['apple', 'banana', 'cherry'],
        ['banana', 'orange'],
        ['apple', 'banana', 'cherry', 'orange'],
        ['apple', 'cherry'],
        ['banana', 'cherry'],
    ]

    # Apriori algorithm with default parameters
    frequent_itemsets, strong_rules = apriori(transactions)

    print("Frequent Itemsets:")
    for itemset, support in frequent_itemsets.items():
        print(f"{itemset}: {support}")

    print("\nStrong Rules:")
    for rule, confidence in strong_rules.items():
        print(f"{rule[0]} -> {rule[1]} : {confidence}")
