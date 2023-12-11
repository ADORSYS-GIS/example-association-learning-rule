

sub_dataset_type = tuple[object]

from typing import List, Tuple, Dict
from itertools import chain, combinations

# Importing support and confidence functions
from support import support
from confidence import confidence

sub_dataset_type = Tuple[object]

support_type = float
strong_rules_type = Tuple[List[object], List[object]]
confidence_type = float


def apriori(transactions: List[List[object]], min_support: float = 0.7, min_confidence: float = 0.5) \
        -> Tuple[Dict[sub_dataset_type, support_type], Dict[strong_rules_type, confidence_type]]:
    """
    To find all frequent itemsets in a dataset and generate strong association rules.
    """

    return {}, {}
from itertools import combinations

def calculate_support(dataset, itemset):
    count = 0
    total_transactions = len(dataset)

    for transaction in dataset:
        if set(itemset).issubset(transaction):
            count += 1

    support = count / total_transactions
    return support


def calculate_confidence(dataset, rule):
    premise = rule[0]
    conclusion = rule[1]

    support_AB = calculate_support(dataset, premise + conclusion)
    support_A = calculate_support(dataset, premise)

    if support_A != 0:
        confidence = support_AB / support_A
    else:
        confidence = 0

    return confidence


def find_frequent_1_itemsets(dataset, min_support):
    item_counts = {}

    for transaction in dataset:
        for item in transaction:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

    frequent_1_itemsets = []
    total_transactions = len(dataset)

    for item, count in item_counts.items():
        support = count / total_transactions
        if support >= min_support:
            frequent_1_itemsets.append([item])

    return frequent_1_itemsets


def generate_candidate_itemsets(Lk, k):
    Ck = []
    for i in range(len(Lk)):
        for j in range(i + 1, len(Lk)):
            L1 = Lk[i]
            L2 = Lk[j]
            if L1[:-1] == L2[:-1]:
                candidate = L1 + [L2[-1]]
                Ck.append(candidate)
    return Ck


def count_support(dataset, Ck):
    support_counts = {}

    for transaction in dataset:
        for candidate in Ck:
            if set(candidate).issubset(transaction):
                if tuple(candidate) in support_counts:
                    support_counts[tuple(candidate)] += 1
                else:
                    support_counts[tuple(candidate)] = 1

    return support_counts


def prune_candidates(support_counts, min_support):
    Lk = []

    total_transactions = len(dataset)

    for candidate, count in support_counts.items():
        support = count / total_transactions
        if support >= min_support:
            Lk.append(list(candidate))

    return Lk


def generate_non_empty_subsets(itemset):
    subsets = []
    for r in range(1, len(itemset)):
        subsets.extend(combinations(itemset, r))
    return subsets


def apriori(dataset, min_support, min_confidence):
    L1 = find_frequent_1_itemsets(dataset, min_support)

    frequent_itemsets = []
    strong_rules = []

    k = 2
    while L1:
        Ck = generate_candidate_itemsets(L1, k)

        support_counts = count_support(dataset, Ck)

        Lk = prune_candidates(support_counts, min_support)

        frequent_itemsets.extend(Lk)

        for itemset in Lk:
            subsets = generate_non_empty_subsets(itemset)
            for subset in subsets:
                rule = (list(subset), list(set(itemset) - set(subset)))
                confidence = calculate_confidence(dataset, rule)
                if confidence >= min_confidence:
                    strong_rules.append((rule, confidence))

        k += 1
        L1 = Lk

    return frequent_itemsets, strong_rules


    # Initializes dictionaries to store frequent itemsets and strong rules.
    frequent_itemsets = {}
    strong_rules = {}

    # Creates unique 1-itemsets and calculates their support using the support function.
    # Initialize L1 = {frequent 1-itemsets}
    unique_items = set(item for transaction in transactions for item in transaction)
    candidates_1 = [frozenset([item]) for item in unique_items]
    frequent_itemsets[1] = {candidate: support(transactions, [list(candidate)]) for candidate in candidates_1}

    # Iterates over the levels of itemsets (k) until no more frequent itemsets are found and generating candidate sets
    # For (k = 2; Lk-1 is not empty; k++):
    k = 2
    while len(frequent_itemsets[k - 1]) > 0:
        # Generating Ck, candidate k-itemsets, from Lk-1
        candidates_k = generate_candidates(list(frequent_itemsets[k - 1]), k)

        # For each transaction t in D:
        for transaction in transactions:
            # Increment count of all candidates in Ck that are contained in t
            for candidate in candidates_k:
                if set(candidate).issubset(transaction):
                    frequent_itemsets[k - 1][frozenset(candidate)] += 1

        # Lk = {c in Ck | support(c) >= min_support}
        frequent_itemsets[k] = {candidate: support_value for candidate, support_value in
                                frequent_itemsets[k - 1].items()
                                if support_value / len(transactions) >= min_support}

        k += 1

    # Frequent Itemsets = Union of all Lk
    frequent_itemsets = {itemset: support_value for itemsets in frequent_itemsets.values() for itemset, support_value in
                         itemsets.items()}

    # For each frequent itemset l in Frequent Itemsets:
    for itemset in frequent_itemsets.keys():

        # Generate all non-empty subsets of l
        subsets = get_subsets(itemset)

        # For every non-empty subset s of l:
        for subset in subsets:
            # Rule = s -> (l - s)
            rule = (subset, list(set(itemset) - set(subset)))

            # If Calculate_Confidence(D, Rule) >= min_confidence:
            confidence_value = confidence(transactions, rule)
            if confidence_value >= min_confidence:
                # Add Rule to Strong Rules
                strong_rules[tuple(rule)] = confidence_value

    # Return Frequent Itemsets, Strong Rules
    return frequent_itemsets, strong_rules


def generate_candidates(frequent_itemsets: List[frozenset], k: int) -> List[frozenset]:
    """
    Generate candidate k-itemsets from frequent (k-1)-itemsets.
    """
    candidates = []
    n = len(frequent_itemsets)

    for i in range(n):
        for j in range(i + 1, n):
            # Merging the frequent (k-1)-itemsets to generate candidates
            candidate = frozenset(sorted(set(frequent_itemsets[i]).union(frequent_itemsets[j])))

            # Check if the candidate has length k
            if len(candidate) == k:
                candidates.append(candidate)

    return candidates



def get_subsets(itemset: List[object]) -> List[List[object]]:
    """
    Generate all non-empty subsets of a set.
    """
    return [list(subset) for subset in chain.from_iterable(combinations(itemset, r) for r in range(1, len(itemset)))]








    
