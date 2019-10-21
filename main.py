import functlib
import sys
import os
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender

p = Petrovich()
name = p.lastname('Алексеев', Case.GENITIVE, Gender.MALE)


conjugated_names_initials_file = open('conjugated_names_initials.txt', 'w', encoding='utf-8')
respected_names_file = open('respected_names.txt', 'w', encoding='utf-8')

required_name_of_file = sys.argv[1]

with open(functlib.get_filename(required_name_of_file), 'r', encoding='utf-8') as source_file:
    for line in source_file:
        line = line.strip()
        ID = line.split(' ')
        functlib.remove_spaces(ID)
        surname = ID[0]
        name = ID[1]
        patronymic = ID[2].translate({ord(','): None})

        info_for_first_file = functlib.write_surnames_initials(surname, name, patronymic)
        info_for_first_file =
        # conjugated_names_initials_file.write(info_for_first_file)
        conjugated_names_initials_file.write()


        info_for_second_file = functlib.write_res(name, patronymic)
        respected_names_file.write(info_for_second_file)

conjugated_names_initials_file.close()
