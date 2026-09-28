from cultures.models import Culture
from name_generator import NameGenerator


class CultureNameGenerator(NameGenerator):
    """Генерирует имена и др. наименования на основе профилей культуры."""

    def __init__(self, culture: Culture):
        super().__init__()
        self.culture = culture

    def get_name(self, sex: bool = True, unique: bool = False) -> str:
        """Генерирует имя."""
        gender = 'male' if sex else 'female'
        return self.generate(
            profile=getattr(self.culture.names, gender),
            unique=unique,
            exist_key='names',
        )

    def get_surname(self, unique: bool = False) -> str:
        """Генерирует фамилию."""
        return self.generate(
            profile=self.culture.surnames, unique=unique, exist_key='surnames'
        )

    def get_city_name(self, unique: bool = True) -> str:
        """Генерирует наименование города."""
        return self.generate(
            profile=self.culture.cities, unique=unique, exist_key='cities'
        )

    def get_country_name(self, unique: bool = True) -> str:
        """Генерирует наименование страны."""
        return self.generate(
            profile=self.culture.countries,
            unique=unique,
            exist_key='countries',
        )
