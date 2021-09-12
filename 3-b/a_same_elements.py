def main():
    set_1 = set(map(int, input().split()))
    set_2 = set(map(int, input().split()))

    print(len(set_1 & set_2))

if __name__ == "__main__":
    main()