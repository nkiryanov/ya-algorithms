def main():
    buildings_array = list(map(int, input().split()))
    home_ids = []
    market_ids = []

    for i in range(len(buildings_array)):
        if buildings_array[i] == 1:
            home_ids.append(i)
        if buildings_array[i] == 2:
            market_ids.append(i)
    
    max_distance = 0
    i = 0
        
    for home in home_ids:
        prev_market_distance = abs(home - market_ids[i])
        if i + 1 < len(market_ids):
            next_market_distance = abs(home - market_ids[i + 1])
            if next_market_distance <= prev_market_distance:
                local_max_distance = next_market_distance
                i += 1
            else:
                local_max_distance = prev_market_distance
        else:
            local_max_distance = prev_market_distance
        
        max_distance = max(max_distance, local_max_distance)

    print(max_distance)

if __name__ == "__main__":
    main()