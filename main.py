import functlib_forCNI
import funclib_forR

conjugated_names_initials_file = open('conjugated_names_initials.txt', 'w', encoding='utf-8')
respected_names_file = open('respected_names.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        ID = line.split(' ')
        surname = ID[0]
        name = ID[1]
        patronymic = ID[2]
        conjugated_names_initials_file.write(str(functlib_forCNI.conjugate_surname(surname)
                                                 + ' '
                                                 + functlib_forCNI.get_initials(name, patronymic)
                                                 + '\n'))
        respected_names_file.write(str())

source_file.close()
conjugated_names_initials_file.close()
