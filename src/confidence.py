dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]


def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
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
dataset = [
    ['A', 'B', 'C'],
    ['B', 'C', 'D'],
    ['A', 'B', 'D'],
    ['A', 'C', 'D'],
    ['A', 'C', 'E'],
]

rule = (['A'], ['C'])

confidence = calculate_confidence(dataset, rule)
print("Confidence:", confidence)