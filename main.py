# structure of my data base: {Surname, Name, Patronymic,\n}
import functlib

intermediary_file = open('intermediary_file.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        ID = line.split(' ')
        surname = ID[0]
        name = ID[1]
        patronymic = ID[2]
        intermediary_file.write(str(functlib.conjugate_surname(surname)
                                    + ' '
                                    + functlib.get_initials(name, patronymic)
                                    + '\n'))

source_file.close()
intermediary_file.close()
