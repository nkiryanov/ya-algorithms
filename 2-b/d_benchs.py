def binary_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if arr[mid + 1] == x:
        return mid + 1
    if arr[mid] < x and arr[mid + 1] > x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)

def main():
    bench_length, block_num = tuple(map(int, input().split()))
    block_array = tuple(map(int, input().split()))


    if block_num == 1:
        print(block_array[0])
    
    else:
        bench_middle = bench_length // 2
        if block_num == 2:
            index = 0
        else:
            index = binary_search(block_array, bench_middle, 0, block_num)

        if bench_length % 2 == 1:
            if block_array[index] == bench_middle:
                print(block_array[index])
            elif block_array[index + 1] == bench_middle:
                print(block_array[index + 1])
            else:
                print(block_array[index], block_array[index + 1])
        else:
            if block_array[index] >= bench_middle:
                print(block_array[index - 1], block_array[index ])
            else:
                print(block_array[index], block_array[index + 1])

if __name__ == "__main__":
    main()