def return_result(d, x, y):
    if x >= 0 and y >= 0 and x + y <= d:
        return 0
    
    if x <= 0 and y <= 0:
        return 1
    
    if x < 0 and y > 0:
        if y * 2 <= d:
            return 1
        return 3
    if x > 0 and y < 0:
        if x * 2 <= d:
            return 1
        return 2
    
    if x >= y:
        return 2
    return 3

def main():
    d = int(input())
    x, y = map(int, input().split())
    result  = return_result(d, x, y)
    print(result)

if __name__ == "__main__":
    main()
