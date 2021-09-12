def main():
    code  = int(input())
    iteractor = int(input())
    checker = int(input())

    result = None

    if iteractor == 0:
        if code != 0:
            result = 3
        if code == 0:
            result = checker

    if iteractor == 1:
        result = checker

    if iteractor == 4:
        if code != 0:
            result = 3
        if code == 0:
            result = 4

    if iteractor == 6:
        result = 0

    if iteractor == 7:
        result = 1

    if result is None:
        result = iteractor

    print(result)

if __name__ == "__main__":
    main()