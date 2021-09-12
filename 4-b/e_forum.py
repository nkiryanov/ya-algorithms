from collections import defaultdict

def runner(lines):
    n = int(lines[0].strip())
    topics = defaultdict(list)
    messages = defaultdict(int)

    line_i = 1

    for i in range(1, n + 1):
        message_header = int(lines[line_i].strip())
        if message_header == 0:
            topic_name = lines[line_i + 1].strip()
            line_i += 3

            topics[topic_name] = [1, i]
        else:
            topic_name = messages[message_header]
            topics[topic_name][0] += 1
            line_i += 2
        
        messages[i] = topic_name
        i += 1
    
    topic = max(topics.items(), key=lambda item: (item[1][0], -item[1][1]))
    print(topic[0])

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    runner(lines)
