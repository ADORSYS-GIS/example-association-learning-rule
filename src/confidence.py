from typing import List, Tuple
from support import support

dataset_type = List[List[object]]
rule_type = Tuple[List[object], List[object]]


def confidence(dataset: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.

    pass
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

    antecedent, consequent = rule
    antecedent_support = support(antecedent, dataset)
    rule_support = support(antecedent + consequent, dataset)

    if antecedent_support == 0:
        return 0  # Avoid division by zero

    confidence_value = rule_support / antecedent_support
    return confidence_value

