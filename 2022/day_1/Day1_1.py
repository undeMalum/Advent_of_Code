import sys


def parse(input_data):
    with open(f"{input_data}") as input_data:
        input_list = []
        sum_numb = 0
        for numb in input_data:
            if numb == "\n":
                input_list.append(sum_numb)
                sum_numb = 0
            else:
                sum_numb += int(numb)
        return input_list

def find_max_calories(prepared_list, elves=1):
    list_elves = []
    for elf in range(elves):
        max_elf = max(prepared_list)
        list_elves.append(max_elf)
        prepared_list.remove(max_elf)
    return list_elves


if __name__ == "__main__":
    prepared_list = parse(sys.argv[1])
    elves = find_max_calories(prepared_list, elves=3)
    print(sum(elves))
