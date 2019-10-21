import rules
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender


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


def write_res(id_name, id_patronymic):
    return str(rules.get_introduction(id_patronymic) +
               ' ' + id_name + ' ' + id_patronymic + '\n')


def get_filename(id_name):
    return str(id_name) + ".txt"
