from collections import defaultdict

def runner(text):
    lines = text.splitlines()
    parties_data = defaultdict(int)

    position_in_list = 0
    voices_sum = 0
    seats_sum = 0

    for line in lines:
        if len(line) > 1:
            name, party_voices = line.rsplit(maxsplit=1)
            party_voices = int(party_voices)
            parties_data[name] = [
                position_in_list,
                party_voices,
                0,  # number of seats
                0,  # reminder of division
            ]
            voices_sum += party_voices

    electoral_quotient = voices_sum / 450

    for party in parties_data:
        party_voices = parties_data[party][1]
        bare_seats = party_voices / electoral_quotient
        seats = int(bare_seats)
        reminder = bare_seats - seats
        parties_data[party][2] = seats
        parties_data[party][3] = reminder

        seats_sum += seats
    
    if seats_sum < 450:
        sorted_parties = sorted(
            parties_data.items(),
            key=lambda item: (-item[1][3], item[1][1]),
        )
        
        i = 0
        while seats_sum < 450:
            i = i % 450
            sorted_parties[i][1][2] += 1
            seats_sum += 1
            i += 1
    
    for party_name, party_data in parties_data.items():
        print(party_name, party_data[2])

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    runner(text)
