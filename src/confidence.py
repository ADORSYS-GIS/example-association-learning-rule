dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]


def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """
    support_of_rule = support(data_set, rule)
    support_of_antecedent = support(data_set, rule[0])
    return support_of_rule / support_of_antecedent

    pass

#this code was added
def support(data_set: dataset_type, rule: rule_type) -> float:
   
    support = 0
    for transaction in data_set:
        if rule[0] in transaction and rule[1] in transaction:
            support += 1

    return support / len(data_set)