def main():
    potential_palindrom = input()
    i, j = 0, len(potential_palindrom) - 1

    price = 0

    while i <= j:
        if potential_palindrom[i] != potential_palindrom[j]:
            price += 1
        i += 1
        j -= 1
    
    print(price)

if __name__ == "__main__":
    main()