def main():
    not_unique_elements = list(map(int, input().split()))
    unique_elements = set()

    for element in not_unique_elements:
        if element not in unique_elements:
            print("NO")
            unique_elements.add(element)
        else:
            print("YES")

if __name__ == "__main__":
    main()