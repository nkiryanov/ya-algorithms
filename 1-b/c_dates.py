def date_checker(x, y):
    if x > 12 or y > 12:
        return 1
    if x == y:
        return 1

    return 0

def main():
    x, y, year = map(int, input().split())
    result = date_checker(x, y)
    print(result)

if __name__ == "__main__":
    main()