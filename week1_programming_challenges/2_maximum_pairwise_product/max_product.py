# python3


def max_pairwise_product(numbers):
    first = max(numbers)
    numbers.remove(first)
    second = max(numbers)
    return first * second


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
