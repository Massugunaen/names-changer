def get_last_letters_surname(id_surname):
    last_letters = id_surname[-2:]
    return last_letters


def get_last_letter_surname(id_surname):
    last_letters = id_surname[-1:]
    return last_letters


def conjugate_surname(id_surname):
    string_to_return = id_surname
    # Males:
    if get_last_letters_surname(id_surname) == "ов":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ев":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ев":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ун":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ин":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ик":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ич":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ап":
        string_to_return = id_surname + 'у'
    if get_last_letters_surname(id_surname) == "ой":
        id_surname = id_surname[:-1]
        string_to_return = id_surname + 'му'
    if get_last_letters_surname(id_surname) == "ий":
        id_surname = id_surname[:-2]
        string_to_return = id_surname + 'ому'

    # Females
    if get_last_letters_surname(id_surname) == "ва":
        id_surname = id_surname[:-1]
        string_to_return = id_surname + "ой"
    if get_last_letters_surname(id_surname) == "ая":
        id_surname = id_surname[:-2]
        string_to_return = id_surname + "ой"
    if get_last_letter_surname(id_surname) == "а":
        id_surname = id_surname[:-1]
        string_to_return = id_surname + "ой"
    return string_to_return


def get_initials(id_name, id_patronymic):
    name_initial = id_name[:1]
    patronymic_initial = id_patronymic[:1]
    string_to_return = name_initial.upper() + '.' + patronymic_initial.upper() + '.'
    return string_to_return


def get_introduction(id_surname):
    if get_last_letter_surname(id_surname) == "у":
        return "Уважаемый "
    else:
        return "Уважаемая "
