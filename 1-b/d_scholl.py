def main():
    n = int(input())
    homes_list = list(map(int, input().split()))

    mediana_num = n // 2 + 1
    school_point = homes_list[mediana_num - 1]
    print(school_point)


if __name__ == "__main__":
    main()