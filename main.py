from src.apriori import apriori
# from src.confidence import confidence
# from src.support import support

if __name__ == '__main__':
    result = apriori([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0.3, 0.7)
    print(result)
