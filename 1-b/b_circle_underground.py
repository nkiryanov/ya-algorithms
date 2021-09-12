def main():
    num_stations, home, job = map(int, input().split())

    one_side_num_stations = abs(job - home) - 1
    second_side_num_stations = num_stations - (one_side_num_stations + 2)

    result = min(one_side_num_stations, second_side_num_stations)
    
    print(result)

if __name__ == "__main__":
    main()