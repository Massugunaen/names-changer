intermediary_file = open('intermediary_file.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        name = line.split(' ')
        # intermediary_file.write(str(name))  # checking what type of variable
        intermediary_file.write(str(name[0] + '\n'))

source_file.close()
intermediary_file.close()
