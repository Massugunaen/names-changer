intermediary_file = open('intermediary_file.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        intermediary_file.write(line)
        print(line)

source_file.close()
