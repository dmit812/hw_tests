stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
}


def max_sale(path):
    return f'{max(path, key = path.get)}'


ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}


def unique_geo(path):
    emp_list = []
    for use, val in ids.items():
        for num in val:
            if num not in emp_list:
                emp_list.append(num)
    return emp_list


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def visit_from_rus(path):
    vis_list = []
    for visit in geo_logs:
        if 'Россия' in list(visit.values())[0]:
            vis_list.extend(visit.items())
    return dict(vis_list)


if __name__ == '__main__':
    print(unique_geo(ids))
    print(visit_from_rus(geo_logs))
