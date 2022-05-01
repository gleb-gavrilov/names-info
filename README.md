# Анализ имен/рождаемости

## Описание
Скрипт позволяет узнать сколько детей назвали тем или другим именем
в Москве, а следовательно и рождаемость. Все данные были взяты из https://data.mos.ru/.
Итоговые данные будут 

## Требования к окружению
Python 3.8.9

## Как установить
Скачайте проект и установите зависимости

 `pip install requirements.txt`
 
## Запуск
> calculate_by_certain_name(name, gender) - показывает статистику по определенному имени.
> Второй аругмент это пол. Мужчина - 0, женщина - 1. По дефолту стоит 0.

> calculate_all_names() - строит графики по всем именам. Отдельный график для мужчин, отдельный для женщин
> 