#!/usr/bin/env python
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Simple Script to convert between PW (per week) to PCM (per calendar month) rent prices. And the other way around'
    )

    parser.add_argument('rent', type=int, help='rent value')
    parser.add_argument('unit', type=str, help='pw or pcm - (default is pw)', default='pw', nargs='?')

    arguments = parser.parse_args()

    rent = arguments.rent
    unit = arguments.unit

    if unit == 'pw':
        result_rent = rent * 52 / 12
        result_unit = 'pcm'
    elif unit == 'pcm':
        result_rent = rent * 12 / 52
        result_unit = 'pw'
    else:
        raise ValueError('Unit ' + unit + ' is not supported')

    print(str(int(round(result_rent))) + ' ' + result_unit)
