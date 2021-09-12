def main():
    list_elements = list(map(int, input().split()))

    set_from_list = set()
    not_unique_elements = set()

    for element in list_elements:
        if element in set_from_list:
            not_unique_elements.add(element)
        set_from_list.add(element)
    
    unique_elements = []
    
    for element in list_elements:
        if element not in not_unique_elements:
            unique_elements.append(element)
    
    print(*unique_elements)

if __name__ == "__main__":
    main()