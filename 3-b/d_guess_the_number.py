def runner(lines):
        n = int(lines[0]) 
        guess_list_or_ask_for_help = lines[1].strip()

        beatriss_asked_help = False
        possible_variants = set([str(num) for num in range(1, n + 1)])
        impossible_variants = set()

        i = 2

        while not beatriss_asked_help:
            help_message = lines[i].strip()
            if help_message == "YES":
                possible_variants &= set(guess_list_or_ask_for_help.split())
            elif help_message == "NO":
                impossible_variants |= set(guess_list_or_ask_for_help.split())
            
            guess_list_or_ask_for_help = lines[i + 1].strip()
            if guess_list_or_ask_for_help == "HELP":
                break

            i += 2
        
        answer = possible_variants - set(impossible_variants)
        
        answer = sorted(answer)
        print(*answer)

def main():
    with open("009.file", "r") as file:
        lines = file.readlines()
    if lines:
        runner(lines)

if __name__ == "__main__":
    main()