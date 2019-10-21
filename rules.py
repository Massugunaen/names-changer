def getting_last_letters(any_string, number):
    last_letters = any_string[-number:]
    return last_letters


def get_gender(id_patronymic):
    if getting_last_letters(id_patronymic, 3) == "вич":
        return "male"
    if getting_last_letters(id_patronymic, 3) == "вна":
        return "female"


def get_introduction(id_patronymic):
    if getting_last_letters(id_patronymic, 3) == "вич":
        return "Уважаемый"
    if getting_last_letters(id_patronymic, 3) == "вна":
        return "Уважаемая"


def conjugate_surname(id_surname, id_patronymic):
    string_to_return = id_surname
    word_ending2 = getting_last_letters(id_surname, 2)
    word_ending1 = getting_last_letters(id_surname, 1)
    gender = get_gender(id_patronymic)
    if gender == "male":
        if word_ending2 == "ов":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ев":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ев":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ун":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ин":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ик":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ич":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ыч":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ян":
            string_to_return = id_surname + 'у'
        if word_ending2 == "ца":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + 'е'
        if word_ending2 == "ой":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + 'му'
        if word_ending2 == "ий":
            id_surname = id_surname[:-2]
            string_to_return = id_surname + 'ому'

    if gender == "female":
        if word_ending2 == "ва":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + "ой"
        if word_ending2 == "ая":
            id_surname = id_surname[:-2]
            string_to_return = id_surname + "ой"
        if word_ending1 == "а":
            id_surname = id_surname[:-1]
            string_to_return = id_surname + "е"
    return string_to_return


def get_initials(id_name, id_patronymic):
    name_initial = id_name[:1]
    patronymic_initial = id_patronymic[:1]
    string_to_return = name_initial.upper() + '.' + patronymic_initial.upper() + '.'
    return string_to_return
