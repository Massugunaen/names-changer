# structure of my data base: {Surname, Name, Patronymic,\n}
def get_last_letters_surname():
    return None


def conjugate_surname(id_surname):
    return None


def get_initials(id_name, id_patronymic):
    name_initial = id_name[:1]
    patronymic_initial = id_patronymic[:1]
    string_to_return = name_initial.upper() + '.' + patronymic_initial + '.'
    return string_to_return


intermediary_file = open('intermediary_file.txt', 'w', encoding='utf-8')

with open('names.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        ID = line.split(' ')
        surname = ID[0]
        name = ID[1]
        patronymic = ID[2]
        last_letters = surname[-2:]
        if last_letters == "ов":
            intermediary_file.write(str(surname + 'у ' + get_initials(name, patronymic) + '\n'))


source_file.close()
intermediary_file.close()
