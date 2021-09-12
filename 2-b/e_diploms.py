def main():
    n = int(input())
    folders = list(map(int, input().split()))

    max_to_look_all = sum(folders)
    max_diploms_in_folder = max(folders)

    max_to_find = max_to_look_all - max_diploms_in_folder

    print(max_to_find)

if __name__ == "__main__":
    main()