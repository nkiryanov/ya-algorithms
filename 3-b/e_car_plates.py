def main():
    m = int(input())
    testimonies = [set()] * m
    for i in range(m):
        testimonies[i] = set(input())

    n = int(input())

    suspicion_plates = []
    max = 0

    for _ in range(n):
        plate = input()
        plate_set = set(plate)
        suspicions = 0
        for testimony in testimonies:
            if testimony.issubset(plate_set):
                suspicions += 1

        if suspicions == max:
            suspicion_plates.append(plate)
        if suspicions > max:
            suspicion_plates = [plate]
            max = suspicions
    
    [print(plate) for plate in suspicion_plates]

if __name__ == "__main__":
    main()
            