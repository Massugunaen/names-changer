def get_last_letters_surname(id_surname):
    last_letters = id_surname[-2:]
    return last_letters


def conjugate_surname(id_surname):
    string_to_return = id_surname
    if get_last_letters_surname(id_surname) == "ов":
        string_to_return = id_surname + 'у'
    return string_to_return


def get_initials(id_name, id_patronymic):
    name_initial = id_name[:1]
    patronymic_initial = id_patronymic[:1]
    string_to_return = name_initial.upper() + '.' + patronymic_initial.upper() + '.'
    return string_to_return
