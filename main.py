import functlib
import sys

source_database = sys.argv[1]
surnames_database = sys.argv[2]
patronymic_database = sys.argv[3]

conjugated_names_initials_file = open(functlib.add_txt_extension(surnames_database), 'w', encoding='utf-8')
respected_names_file = open(functlib.add_txt_extension(patronymic_database), 'w', encoding='utf-8')

with open(source_database + ".txt", 'r', encoding='utf-8') as source_file:
    for line in source_file:
        line = line.strip()
        ID = line.split(' ')
        functlib.remove_spaces(ID)
        surname = ID[0]
        name = ID[1]
        patronymic = ID[2].translate({ord(','): None})

        info_for_first_file = functlib.write_surnames_initials(surname, name, patronymic)
        conjugated_names_initials_file.write(info_for_first_file)

        info_for_second_file = functlib.write_res(name, patronymic)
        respected_names_file.write(info_for_second_file)

conjugated_names_initials_file.close()
respected_names_file.close()
