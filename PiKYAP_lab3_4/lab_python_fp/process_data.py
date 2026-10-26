import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
import random

path = 'data_light.json'

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(arg):
    return list(Unique(sorted([i["job-name"] for i in arg], key=lambda i: i.lower()), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda a: a.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda a: a + " с опытом Python", arg))


@print_result
def f4(arg):
    return [f"{i}{j}" for i, j in zip(arg, [f", зарплата {random.randint(100000, 200000)} руб." for _ in range(len(arg))])]



if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))