import functlib

conjugated_names_initials_file = open('conjugated_names_initials.txt', 'w', encoding='utf-8')
respected_names_file = open('respected_names.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        line = line.strip()
        ID = line.split(' ')
        surname = ID[0]
        name = ID[1]
        patronym = ID[2].translate({ord(','): None})
        print(ID[2])
        conjugated_names_initials_file.write(str(functlib.conjugate_surname(surname, patronym)
                                                 + ' '
                                                 + functlib.get_initials(name, patronym)
                                                 + '\n'))
        respected_names_file.write(str(functlib.get_introduction(patronym))
                                   + ' '
                                   + name
                                   + ' '
                                   + patronym
                                   + '\n')

source_file.close()
conjugated_names_initials_file.close()
