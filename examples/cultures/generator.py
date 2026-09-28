from cultures.models import Culture

from name_generator import NameGenerator


class CultureNameGenerator(NameGenerator):
    def __init__(self, culture: Culture):
        super().__init__()
        self.culture = culture

    def get_name(self, sex: bool = True, unique: bool = False) -> str:
        '''Сгенерировать имя.'''
        gender = 'male' if sex else 'female'
        return self.generate(
            getattr(self.culture.names, gender),
            unique,
            'names'
        )

    def get_surname(self, unique: bool = False) -> str:
        '''Сгенерировать фамилию.'''
        return self.generate(
            self.culture.surnames,
            unique,
            'surnames'
        )

    def get_city_name(self, unique: bool = True) -> str:
        '''Сгенерировать наименование города.'''
        return self.generate(
            self.culture.cities,
            unique,
            'cities'
        )

    def get_country_name(self, unique: bool = True) -> str:
        '''Сгенерировать наименование страны.'''
        return self.generate(
            self.culture.countries,
            unique,
            'countries'
        )
