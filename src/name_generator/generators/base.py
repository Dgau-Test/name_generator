import random
from collections import defaultdict

from name_generator.models import NameProfile, WeightedValue


class NameGenerator:
    def __init__(self):
        self._exist_names = defaultdict(set)

    def weighted_choice(self, items: list[WeightedValue]) -> str:
        if not items:
            raise ValueError('Список WeightedValue пуст')

        return random.choices(
            population=[item.value for item in items],
            weights=[item.weight for item in items],
        )[0]

    def _maybe_add_apostrophe(self, name: str, profile: NameProfile) -> str:
        '''Возможное добавление апострофа.'''
        if (
            random.random() < profile.apostrophe_chance
            and len(name) >= 5
        ):
            position = random.randint(2, len(name) - 2)
            name = f"{name[:position]}'{name[position:]}"
        return name

    def _valid_consonants(self, name: str, profile: NameProfile) -> bool:
        '''Хорошо ли произносится имя.'''
        consonants_in_row = 0

        for char in name.lower():
            if char in profile.alphabet.vowels:
                consonants_in_row = 0
                continue

            if char.isalpha():
                consonants_in_row += 1

                if consonants_in_row > profile.max_consonants_in_row:
                    return False
        return True

    def _apply_replacements(self, name: str, profile: NameProfile) -> str:
        '''Применение установленных замен.'''
        for old, new in profile.replacement_rules.items():
            name = name.replace(old, new)
        return name

    def _has_forbidden_combination(self, name: str, profile: NameProfile) -> bool:
        '''Содержит ли имя запрещенные комбинации.'''
        name = name.lower()
        return any(
            combo.lower() in name
            for combo in profile.forbidden_combinations 
        )

    def _valid_length(self, name: str, profile: NameProfile) -> bool:
        '''Валидация длины наименования.'''
        return profile.min_length <= len(name.replace("'", "")) <= profile.max_length

    def _valid(self, name: str, profile: NameProfile) -> bool:
        '''Полная валидация наименования.'''
        if (
            not self._valid_length(name, profile)
            or not self._valid_consonants(name, profile)
            or self._has_forbidden_combination(name, profile)
        ):
            return False
        return True

    def _build(self, profile: NameProfile) -> str:
        '''Построение наименования по шаблону.'''
        pattern = self.weighted_choice(profile.patterns)

        return ''.join([
            self.weighted_choice(profile.get_part(s))
            for s in pattern
        ]).lower()

    def generate(
        self,
        profile: NameProfile,
        unique: bool = False,
        exist_key: str = 'names'
    ) -> str:
        for _ in range(500):
            name = self._build(profile)
            name = self._apply_replacements(name, profile)
            name = self._maybe_add_apostrophe(name, profile)
            name = name.capitalize()

            if not self._valid(name, profile):
                continue

            if unique:
                if name in self._exist_names[exist_key]:
                    continue
                self._exist_names[exist_key].add(name)

            return name

        raise RuntimeError('Не удалось сгенерировать наименование')
