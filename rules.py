def getting_last_letters(anystring, number):
    last_letters = anystring[-number:]
    return last_letters


def get_introduction(id_patronymic):
    if getting_last_letters(id_patronymic, 3) == "вич":
        return "Уважаемый"
    if getting_last_letters(id_patronymic, 3) == "вна":
        return "Уважаемая"


def get_gender(id_patronymic):
    if getting_last_letters(id_patronymic, 3) == "вич":
        return "male"
    if getting_last_letters(id_patronymic, 3) == "вна":
        return "female"


def conjugate_surname(id_surname, id_patronymic):
    string_to_return = id_surname
    if get_gender(id_patronymic) == "male":
        if getting_last_letters(id_surname, 2) == "ов":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ев":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ев":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ун":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ин":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ик":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ич":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ыч":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ян":
            string_to_return = id_surname + 'у'
        if getting_last_letters(id_surname, 2) == "ца":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + 'е'
        if getting_last_letters(id_surname, 2) == "ой":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + 'му'
        if getting_last_letters(id_surname, 2) == "ий":
            id_surname = id_surname[:-2]
            string_to_return = id_surname + 'ому'

    if get_gender(id_patronymic) == "female":
        if getting_last_letters(id_surname, 2) == "ва":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + "ой"
        if getting_last_letters(id_surname, 2) == "ая":
            id_surname = id_surname[:-2]
            string_to_return = id_surname + "ой"
        if getting_last_letters(id_surname, 1) == "а":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + "е"
    return string_to_return
