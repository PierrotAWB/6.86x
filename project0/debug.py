import pdb

def get_sum_metrics(predictions, metrics=[]):
    #pdb.set_trace()
#    metrics.append(lambda x : x)
#    metrics.append(lambda x : x + 1)
#    metrics.append(lambda x : x + 2)
#
    #pdb.set_trace()
    metrics += list(map(lambda x: (lambda y: y + x), range(3))) 

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    del metrics[:]

    return sum_metrics

def main():
    # pdb.set_trace()
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9

if __name__ == "__main__":
    main()
