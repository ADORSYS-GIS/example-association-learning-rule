
sub_dataset_type = tuple[object]
support_type = float
strong_rules = list[object], list[object]
confidence_type = float


def apriori(transactions: list[list[object]], min_support: float = 0.7, min_confidence: float = 0.5) \
        -> tuple[dict[sub_dataset_type, support_type], dict[strong_rules, confidence_type]]:
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
