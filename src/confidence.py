from typing import List, Tuple

dataset_type = List[List[object]]
rule_type = Tuple[List[object], List[object]]

def confidence(dataset: dataset_type, rule: rule_type) -> float:
    """
    Calculate the confidence of a rule in the dataset.
    """
    premise, conclusion = rule
    premise_support = sum(1 for transaction in dataset if set(premise).issubset(transaction))
    rule_support = sum(1 for transaction in dataset if set(premise + conclusion).issubset(transaction))

    if premise_support == 0:
        return 0.0

    confidence_value = rule_support / premise_support
    return confidence_value

# Example Usage:
if __name__ == "__main__":
    # Example dataset
    dataset = [
        ['apple', 'banana', 'cherry'],
        ['banana', 'orange'],
        ['apple', 'banana', 'cherry', 'orange'],
        ['apple', 'cherry'],
        ['banana', 'cherry'],
    ]

    # Example rule
    rule = (['apple'], ['banana'])

    # Calculate confidence
    confidence_value = confidence(dataset, rule)

    print(f"The confidence of the rule {rule} in the dataset is: {confidence_value}")
