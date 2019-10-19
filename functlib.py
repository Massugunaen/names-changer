def filter():
    return None


def get_initials(id_name, id_patronymic):
    name_initial = id_name[:1]
    patronymic_initial = id_patronymic[:1]
    string_to_return = name_initial.upper() + '.' + patronymic_initial.upper() + '.'
    return string_to_return
