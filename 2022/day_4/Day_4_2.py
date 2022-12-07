def contains_pair(left_ids: list[str, str], right_ids: list[str, str]) -> bool:
    if int(right_ids[0]) <= int(left_ids[1]) <= int(right_ids[1]):
        return True
    if int(right_ids[0]) <= int(left_ids[0]) <= int(right_ids[1]):
        return True
    if int(left_ids[0]) <= int(right_ids[1]) <= int(left_ids[1]):
        return True
    if int(left_ids[0]) <= int(right_ids[0]) <= int(left_ids[1]):
        return True
    return False


def divide_string(init_string: str) -> [str, str]:
    temp = init_string.split(",")
    left_ids, right_ids = [numb.split("-") for numb in temp]
    return left_ids, right_ids


def parse(file) -> int:
    sum_contained = 0
    with open(f"{file}") as input_data:
        for pair in input_data:
            left_ids, right_ids = divide_string(pair)
            if contains_pair(left_ids, right_ids):
                sum_contained += 1
    return sum_contained


if __name__ == "__main__":
    f = "input.txt"
    sum_con = parse(f)
    print(sum_con)
