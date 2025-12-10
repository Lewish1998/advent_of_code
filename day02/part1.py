import re


with open('puzzleInput.txt') as f:
    input: list = f.readline().split(',')

invalid_ids_list = []


def magic_regex_function(n: int, l: int):
    pattern = r'^([0-9]+)\1$'
    strint = str(n)
    if re.match(pattern, strint):
        invalid_ids_list.append(n)
        return


def invalid_ids(input: list[str]):

    for i in input:
        x, y = i.split('-')
        for j in range(int(x), int(y)):
            if len(str(j)) > 1:
                magic_regex_function(j, len(str(j)))

    print(invalid_ids_list)
    return sum(invalid_ids_list)

print(invalid_ids(input))
