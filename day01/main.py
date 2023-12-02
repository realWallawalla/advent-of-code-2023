from os import environ
from typing import List
import re

def get_solution_part1(data: List[str]) -> int:
    sum = 0
    for s in data:
        int_strings = re.findall(r"\d", s)
        cal_number = int_strings[0] + int_strings[-1]
        sum = sum + int(cal_number)
    return sum

def get_solution_part2(data: List[str]) -> int:
    sum = 0
    map_int_string = {"one": "1", "two": "2", "three": "3",
                      "four": "4", "five": "5", "six": "6",
                      "seven": "7", "eight": "8", "nine": "9"}
    for s in data:
        index_ints = {}
        for key, value in map_int_string.items():
            index_of_int_string = s.find(key)
            index_of_int = s.find(value)
            if index_of_int_string > -1:
                index_ints[index_of_int_string] = value
            if index_of_int > -1:
                index_ints[index_of_int] = value

        sorted_keys = sorted(index_ints.keys())
        cal_number = index_ints[sorted_keys[0]] + index_ints[sorted_keys[-1]]
        sum = sum + int(cal_number)
    return sum



if __name__ == '__main__':
    input = open('input.txt').read().splitlines()
    answer = get_solution_part2(input) if environ.get('part') == 'part2' else get_solution_part2(input)
    print(answer)