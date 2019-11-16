from petrovich.main import Petrovich
from petrovich.enums import Case


def remove_spaces(list_of_names):
    while '' in list_of_names:
        list_of_names.remove('')
    return None


def get_initials(id_name, id_patronymic):
    name_initial = id_name[:1]
    patronymic_initial = id_patronymic[:1]
    string_to_return = name_initial.upper() + '.' + patronymic_initial.upper() + '.'
    return string_to_return


def write_surnames_initials(id_surname, id_name, id_patronymic):
    human_class = Petrovich()
    changed_surname = human_class.lastname(id_surname, Case.DATIVE)
    return str(changed_surname +
               ' ' + get_initials(id_name, id_patronymic) + '\n')


def getting_last_letters(any_string, number):
    last_letters = any_string[-number:]
    return last_letters


def get_introduction(id_patronymic):
    last_letters = getting_last_letters(id_patronymic, 3)
    if last_letters == "вич":
        return "Уважаемый"
    if last_letters == "вна":
        return "Уважаемая"


def recording_data_to_surnames_database():
    return None


def recording_data_to_patronymic_database():
    return None


def write_res(id_name, id_patronymic):
    return str(str(get_introduction(id_patronymic)) +
               ' ' + id_name + ' ' + id_patronymic + '\n')


def add_txt_extension(id_database):
    return id_database + ".txt"
