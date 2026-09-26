from collections import defaultdict
from operator import attrgetter

from name_generator.generators.base import NameGenerator
from name_generator.models import Culture


class CultureNameGenerator(NameGenerator):
    def __init__(self, culture: Culture):
        super().__init__()
        self.culture = culture
        self.exist_objects = defaultdict(set)

    def _generate(
        self,
        key_profile: str,
        exist_key: str | None = None,
        unique: bool = False
    ):
        profile = attrgetter(key_profile)(self.culture)
        exist_key = exist_key or key_profile
        for _ in range(500):
            name = self.generate(profile)
            
            if unique:
                if name in self.exist_objects[exist_key]:
                    continue
                self.exist_objects[exist_key].add(name)
            
            return name
        raise RuntimeError('Не удалось сгенерировать наименование')

    def get_name(self, sex: bool = True, unique: bool = False) -> str:
        '''Сгенерировать имя.'''
        gender = 'male' if sex else 'female'
        return self._generate(
            f'names.{gender}',
            exist_key='names',
            unique=unique
        )

    def get_surname(self, unique: bool = False):
        '''Сгенерировать фамилию.'''
        return self._generate('surnames', unique=unique)

    def get_city_name(self, unique: bool = True):
        '''Сгенерировать наименование города.'''
        return self._generate('cities', unique = unique)

    def get_contry_name(self, unique: bool = True):
        '''Сгенерировать наименование страны.'''
        return self._generate('countries', unique=unique)
