import string

def obtain_priorities():
    priorities = dict()

    for priority, item_type in enumerate(string.ascii_letters):
        priorities[f"{item_type}"] = priority + 1

    return priorities

def divide_str(init_str):
    length = len(init_str)
    str_a, str_b = [init_str[:length//2], init_str[length//2:]]
    return str_a, str_b

def parse(file, priorities):
    with open(f"{file}", "r") as data:
        sum_pro = 0
        for items in data:
            l_com, r_com = divide_str(items)

            for item in l_com:
                if item in r_com:
                    sum_pro += priorities[item]
                    break

    return sum_pro

if __name__ == "__main__":
    file = "input.txt"
    priorities = obtain_priorities()
    out = parse(file, priorities)
    print(out)
