import rules


def remove_spaces(list_of_names):
    while '' in list_of_names:
        list_of_names.remove('')
    return None


def write_surnames_initials(surname, name, patronymic):
    return str(rules.conjugate_surname(surname, patronymic) +
               ' ' + rules.get_initials(name, patronymic) + '\n')


def write_res(name, patronymic):
    return str(rules.get_introduction(patronymic) +
               ' ' + name + ' ' + patronymic + '\n')


def get_filename(name):
    return str(name) + ".txt"
