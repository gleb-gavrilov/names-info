import json
import matplotlib.pyplot as plt


def load_children_information(gender):
    try:
        if gender == 0:
            with open('boys_children.json', encoding='windows-1251') as f:
                children = json.load(f)
        else:
            with open('girls_children.json', encoding='windows-1251') as f:
                children = json.load(f)
    except FileNotFoundError:
        children = None

    return children


def calculate_all_names():
    boys_children = load_children_information(0)
    girls_children = load_children_information(1)
    if boys_children and girls_children:
        boys = get_children_info_by_dict(boys_children)
        girls = get_children_info_by_dict(girls_children)
        if boys and girls:
            print('Информаия по мальчикам:', boys)
            get_graph(boys, 'Мальчики')

            print('Информаия по девочкам:', girls)
            get_graph(girls, 'Девочки')
    else:
        print('Не смог получить информацию о детях')


def get_children_info_by_dict(children):
    children_data = {}
    for child in children:
        year = str(child['Year'])
        if year == '2022':
            continue
        try:
            children_data[year] += child['NumberOfPersons']
        except KeyError:
            children_data[year] = child['NumberOfPersons']
    return children_data


def calculate_by_certain_name(name, gender=0):
    children = load_children_information(gender)
    if children:
        children_data = {}
        for child in children:
            if child['Name'].capitalize() == name.capitalize():
                year = str(child['Year'])
                if year == '2022':
                    continue
                try:
                    children_data[year] += child['NumberOfPersons']
                except KeyError:
                    children_data[year] = child['NumberOfPersons']
        if children_data:
            print(name, children_data)
            get_graph(children_data, name)
        else:
            print('Не нашел таких имен')
    else:
        print('Не смог получить информацию о детях')


def get_graph(children_data, title):
    plt.plot(list(children_data.keys()), list(children_data.values()))
    plt.title(f'Динамика имен {title}')
    plt.ylabel('Количество')
    plt.xlabel('Года')
    plt.savefig(f'Динамика_имен_{title}.png')
    plt.clf()


def main():
    calculate_by_certain_name('Екатерина', 1)
    calculate_all_names()


if __name__ == '__main__':
    main()
