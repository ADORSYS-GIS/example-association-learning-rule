dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]


def calculate_support(data_set: dataset_type, itemset: list[object]) -> float:
    """
    To calculate the support of an itemset in a dataset.
    """
    count = sum(1 for transaction in data_set if set(itemset).issubset(transaction))
    return count / len(data_set)

def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.

    Args:
        data_set: A dataset of transactions represented as a list of lists of items.
        rule: A tuple representing an association rule, where the first list is the antecedent and the second list is the consequent.

    Returns:
        The confidence score, which is the likelihood of occurrence of the consequent given the antecedent.
    """
    antecedent, consequent = rule

    support_AB = calculate_support(data_set, antecedent + consequent)
    support_A = calculate_support(data_set, antecedent)

    if support_A != 0:
        confidence = support_AB / support_A
    else:
        confidence = 0

    return confidence

if __name__ == "__main__":
    dataset = [
        ['A', 'B', 'C'],
        ['B', 'C', 'D'],
        ['A', 'B', 'D'],
        ['C', 'D', 'E'],
        ['A', 'C', 'E'],
    ]

    rule = (['A', 'B'], ['C'])

    confidence_score = confidence(dataset, rule)

    print(f"Confidence Score: {confidence_score}")

