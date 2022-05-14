#!/usr/bin/env python

import argparse
import sys
from numpy import average, random, sqrt, std, sum


def generate_data(number=10):
    data = [random.randint(0, 100) for i in range(number)]
    return data


def get_standard_deviation(data, avg):
    numerator = 0.0
    denominator = 0.0

    for i in range(len(data)):
        numerator = numerator + (data[i] - avg) ** 2
    return sqrt(numerator / len(data))


def get_standard_value_list(data, avg, standard):
    standard_values = []
    for i in range(len(data)):
        standard_values.append((data[i] - avg) / standard)
    return standard_values


def get_deviation_value_list(data):
    deviation_values = []
    for i in range(len(data)):
        deviation_values.append(data[i] * 10 + 50)
    return deviation_values


def main():
    parser = argparse.ArgumentParser(description='Standard deviation tester.')
    parser.add_argument('--number',
                        metavar='NUMBER',
                        type=int,
                        help='an integer for the number of the example data')
    args = parser.parse_args()

    original_data = generate_data(args.number)
    sorted_data = sorted(original_data)
    total = sum(sorted_data)
    avg = average(sorted_data)
    standard = get_standard_deviation(sorted_data, avg)
    numpy_standard = std(sorted_data)
    standard_values = get_standard_value_list(sorted_data, avg, standard)
    deviation_values = get_deviation_value_list(standard_values)

    if(numpy_standard != standard):
        sys.stderr.write(
            f'Error: The calculated standard deviation:{standard} '
            f'does not match the numpy.std():{numpy_standard} result.'
            )
        sys.exit(1)

    print(f'サンプルデータ: {sorted_data}')
    print(f'合計: {total}')
    print(f'要素数: {args.number}')
    print(f'平均: {avg}')
    print(f'標準偏差: {standard}')
    print(f'基準値: {standard_values}')
    print(f'偏差値: {deviation_values}')


if __name__ == '__main__':
    main()

#
# EOF
#
