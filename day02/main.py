from os import environ
from typing import List
import re

def get_solution_part1(data: List[List[str]]) -> int:
    max_numbers = {"red": 12, "green": 13, "blue": 14}
    sum = 0

    for game in data:
        balls_per_game = [s.strip() for s in game[1].split(";")]
        add_game_id = True
        for round in balls_per_game:
            round_splitted = round.split(",")
            for ball_color_amount in round_splitted:
                if (ball_color_amount.find("blue") > -1
                        and int(ball_color_amount.replace("blue", "")) > max_numbers["blue"]):
                    add_game_id = False
                    break
                if (ball_color_amount.find("green") > -1
                        and int(ball_color_amount.replace("green", "")) > max_numbers["green"]):
                    add_game_id = False
                    break
                if (ball_color_amount.find("red") > -1
                        and int(ball_color_amount.replace("red", "")) > max_numbers["red"]):
                    add_game_id = False
                    break
        if add_game_id:
            sum += int(game[0].replace("Game", ""))
    return sum

def get_solution_part2(data: List[List[str]]) -> int:
    sum = 0

    for game in data:
        balls_per_game = [s.strip() for s in game[1].split(";")]
        min_amount_numbers = {"red": 0, "green": 0, "blue": 0}
        for round in balls_per_game:
            round_splitted = round.split(",")
            for ball_color_amount in round_splitted:
                if (ball_color_amount.find("blue") > -1
                        and int(ball_color_amount.replace("blue", "")) > min_amount_numbers["blue"]):
                    min_amount_numbers["blue"] = int(ball_color_amount.replace("blue", ""))
                if (ball_color_amount.find("green") > -1
                        and int(ball_color_amount.replace("green", "")) > min_amount_numbers["green"]):
                    min_amount_numbers["green"] = int(ball_color_amount.replace("green", ""))
                if (ball_color_amount.find("red") > -1
                        and int(ball_color_amount.replace("red", "")) > min_amount_numbers["red"]):
                    min_amount_numbers["red"] = int(ball_color_amount.replace("red", ""))
        sum += min_amount_numbers["red"] * min_amount_numbers["green"] * min_amount_numbers["blue"]
    return sum


if __name__ == '__main__':
    game_data = open('input.txt').read().splitlines()
    game_data_split = [s.strip().split(":") for s in game_data]
    answer = get_solution_part2(game_data_split) if environ.get('part') == 'part2'\
        else get_solution_part1(game_data_split)
    print(answer)
