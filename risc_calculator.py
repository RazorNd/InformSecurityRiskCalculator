#! /usr/bin/env python3
import json
from argparse import ArgumentParser
from RiskCalculator import RiskCalculator


parser = ArgumentParser()
parser.add_argument('input', help='Файл с конфигурацией угроз', type=str)
parser.add_argument('-v', help='Уровень вывода информации', action='store_true', default=False)


def load_conf(file_name):
    with open(file_name) as f:
        return json.load(f)


def main():
    arg = parser.parse_args()
    calc = RiskCalculator(load_conf(arg.input))
    if arg.v:
        for r in calc.resources:
            print(r)
            print()
        print()
    print(calc.risk_str())


if __name__ == '__main__':
    main()
