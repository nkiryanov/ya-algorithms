from collections import defaultdict

def main():
    n = int(input())
    package_dict = defaultdict(int)
    for _ in range(n):
        color, value = map(int, input().split())
        package_dict[color] += value
    
    sorted_colors = sorted(package_dict)
    for key in sorted_colors:
        print(key, package_dict[key])

if __name__ == "__main__":
    main()
