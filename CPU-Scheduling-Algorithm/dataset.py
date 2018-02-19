from numpy.random import uniform, shuffle


def generate(n=60, distributions=None):
    """Return a generated list of number by given list of range and distribution tuple
        eg. spec = [(2, 8, 0.7), (20, 30, 0.2), (35, 40, 0.1)]
    """
    if distributions is None:
        distributions = [(2, 8, 0.7), (20, 30, 0.2), (35, 40, 0.1)]

    if n <= 0:
        raise Exception("n must greater than 0")

    if sum(map(lambda x: x[2], distributions)) - 1.0 > 1e-7:
        raise Exception("summation of probability must equal to 1")

    ret = []

    for distribution in distributions:
        size = int(distribution[2] * n)
        ret.extend(map(int, uniform(distribution[0], distribution[1], size)))

    shuffle(ret)

    return ret


if __name__ == '__main__':
    numbers = generate()
    print numbers
    print len(numbers)
