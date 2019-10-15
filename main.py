intermediary_file = open('intermediary_file.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        name = line.split(' ')
        writedown_name = name[0]
        last_letters = writedown_name[-2:]
        if last_letters == "ов":
            intermediary_file.write(str(writedown_name + 'у' + '\n'))
        

source_file.close()
intermediary_file.close()
