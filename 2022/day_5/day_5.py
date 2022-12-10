import parse


def create_stack_list(file_f: str) -> list[list]:
    """Creates appropriate number of sub-lists depending on number of stacks"""
    with open(f"{file_f}", "r") as input_data:
        # count how many stacks are needed
        count_stack_lines = 0
        for line in input_data:
            if line[1] == "1":
                count_stack_lines = int(line[-3])
                break
        # this will hold elements of each stack
        list_of_stacks_f = [[] for _ in range(count_stack_lines)]
    return list_of_stacks_f


def fill_stack_list(file_f: str, list_of_stacks_f: list[list]) -> list[list]:
    """Reads elements from the text file and transfers it to the list
    -> [["[A]", "[B]"], [["[A]", "[B]"]]"""
    with open(f"{file_f}", "r") as input_data:
        for line in input_data:
            if line[1] == "1":
                break

            idx = 0
            for start in range(0, len(line), 4):
                end = start + 3
                element = line[start:end]
                if element != "   ":
                    list_of_stacks_f[idx].append(element)
                idx += 1

    for idx, sub_list in enumerate(list_of_stacks_f):
        list_of_stacks_f[idx].reverse()

    return list_of_stacks_f


def fetch_instructions(file_f: str) -> list[dict]:
    """Fetch the series of instructions commanding the cargo crane"""
    pattern = parse.compile(
        "move {move_n:d} from {initial_stack:d} to {end_stack:d}"
    )
    instruction_list_f = list()

    with open(f"{file_f}", "r") as file_input:
        for line in file_input:
            if line[0] != "m":
                continue
            obtain_instruction_dict = pattern.search(f"{line}")
            instruction_list_f.append(obtain_instruction_dict.named)
    return instruction_list_f


def parse_input(file_f: str) -> (list[str], list[dict]):
    # input file consists of both instructions and stacks
    # this should be managed somehow

    list_of_stacks_f = create_stack_list(file_f)
    list_of_stacks_f = fill_stack_list(file_f, list_of_stacks_f)
    instruction_list_f = fetch_instructions(file_f)

    return list_of_stacks_f, instruction_list_f


def solve_1(list_of_stacks_f: list[list], instruction_list_f: list[dict]) -> str:
    for instruction in instruction_list_f:
        for _ in range(instruction["move_n"]):
            crate = list_of_stacks_f[instruction["initial_stack"] - 1].pop()
            list_of_stacks_f[instruction["end_stack"] - 1].append(crate)

    # read the content of top crates
    final_str = ""
    for sub_list in list_of_stacks_f:
        final_str += sub_list[-1][1]

    return final_str


def solve_2(list_of_stacks_f: list[list], instruction_list_f: list[dict]) -> str:
    for instruction in instruction_list_f:
        temp = list()
        for _ in range(instruction["move_n"]):
            crate_1 = list_of_stacks_f[instruction["initial_stack"] - 1].pop()
            temp.append(crate_1)
        temp.reverse()
        for crate_2 in temp:
            list_of_stacks_f[instruction["end_stack"] - 1].append(crate_2)

    # read the content of top crates
    final_str = ""
    for sub_list in list_of_stacks_f:
        final_str += sub_list[-1][1]

    return final_str


if __name__ == "__main__":
    f = "input.txt"
    list_of_stacks, instruction_list = parse_input(f)
    final_1 = solve_1(list_of_stacks, instruction_list)
    list_of_stacks, instruction_list = parse_input(f)
    final_2 = solve_2(list_of_stacks, instruction_list)
    print(final_1, final_2)
