possibilities = {
    "X": 0,
    "Y": 3,
    "Z": 6
    }


hand_shape = {
    "AX": 3,
    "AY": 1,
    "AZ": 2,
    "BX": 1,
    "BY": 2,
    "BZ": 3,
    "CX": 2,
    "CY": 3,
    "CZ": 1
    }


def parse(input_data):
    with open(f"{input_data}", "r") as input_data:
        battles = [line.replace(" ", "").strip() for line in input_data]
    return battles

def calculate_score(battles):
    score = 0
    for battle in battles:
        score += (possibilities[battle[1]] + hand_shape[battle])
    return score

if __name__ == "__main__":
    input_file = "input.txt"
    battles = parse(input_file)
    score = calculate_score(battles)
    print(score)
