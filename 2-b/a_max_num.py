def main():
    x = -1
    max = 0
    while x != 0:
        x = int(input())
        if x == max:
            count += 1
        if x > max:
            max = x
            count = 1
    print(count)     

if __name__ == "__main__":
    main()