"""
Program: camper_age_input.py
Author: Zachary Hayes
Last date modified: 01/22/20

Converts camper age from years to months.
"""


def main():
    print('Enter age in years: ')
    age_in_years = input()
    age_in_months = convert_to_months(age_in_years)
    print(28 * 12)


def convert_to_months(self, age_in_years):
    return age_in_years * 12


if __name__ == '__main__':
    main()
