from collections import defaultdict

def runner(lines):
    election_list = defaultdict(int)
    for line in lines:
        if len(line) > 1:
            name, value = line.split()
            election_list[name] += int(value)
    
    sorted_names = sorted(election_list)
    for name in sorted_names:
        print(name, election_list[name])

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
    if lines:
        runner(lines)
