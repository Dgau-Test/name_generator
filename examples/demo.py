"""Пример генерации эльфийских имён и др. наименований."""

from cultures import ELF, CultureNameGenerator

generator = CultureNameGenerator(ELF)

print('Имя:', generator.get_name())
print('Фамилия', generator.get_surname())
print('Город:', generator.get_city_name())
print('Страна', generator.get_country_name())
