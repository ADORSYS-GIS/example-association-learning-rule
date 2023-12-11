from support import support
dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]


def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """
    antecedent, consequent = rule

    support_antecedent_consequent = support(data_set, antecedent + consequent)
    support_antecedent = support(data_set, antecedent)

    if support_antecedent != 0:
        confidence_value = support_antecedent_consequent / support_antecedent
    else:
        confidence_value = 0

    return confidence_value

    
