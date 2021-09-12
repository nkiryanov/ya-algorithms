from collections import defaultdict

def runner(words):
    word_frequencies = defaultdict(int)
    for word in words:
        word_frequencies[word] += 1
    
    sorted_tuple_of_words = sorted(
        word_frequencies.items(),
        key=lambda item: (-item[1], item[0])
    )

    sorted_words = [item[0] for item in sorted_tuple_of_words]
    
    print("\n".join(sorted_words))

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        words = file.read().split()
    
    runner(words)
