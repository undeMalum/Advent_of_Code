hand_shape = {
    "X": 1,
    "Y": 2,
    "Z": 3
    }


possibilities = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
    }


def parse(input_data):
    with open(f"{input_data}", "r") as input_data:
        battles = [line.replace(" ", "").strip() for line in input_data]
    return battles

def calculate_score(battles):
    score = 0
    for battle in battles:
        score += possibilities[battle] + hand_shape[battle[1]]
    return score

if __name__ == "__main__":
    input_file = "input.txt"
    battles = parse(input_file)
    score = calculate_score(battles)
    print(score)
