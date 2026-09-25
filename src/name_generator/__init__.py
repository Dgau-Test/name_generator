import random

from name_generator.models.name_profile import NameProfile, WeightedValue


class NameGenerator:
    SYMBOL_PATTERN_TO_PART = {
        'C': 'consonants',
        'V': 'vowels',
        'K': 'onset_clusters',
        'D': 'coda_clusters',
        'S': 'start_syllables',
        'M': 'middle_syllables',
        'E': 'end_syllables'
    }
    VOWELS = set('аеёиоуыэюя')

    def __init__(self, profile: NameProfile):
        self.profile = profile

    def weighted_choice(self, items: list[WeightedValue]) -> str:
        if not items:
            raise ValueError('Список WeightedValue пуст')

        return random.choices(
            population=[item.value for item in items],
            weights=[item.weight for item in items],
            k=1
        )[0]

    def _maybe_add_apostrophe(self, name: str) -> str:
        '''Возможное добавление апострофа.'''
        if (
            random.random() < self.profile.apostrophe_chance
            and len(name) >= 5
        ):
            position = random.randint(2, len(name) - 2)
            name = f"{name[:position]}'{name[position:]}"
        return name

    def _valid_consonants(self, name: str) -> bool:
        '''Хорошо ли произносится имя.'''
        consonants_in_row = 0

        for char in name.lower():
            if char in self.VOWELS:
                consonants_in_row = 0
                continue

            if char.isalpha():
                consonants_in_row += 1

                if consonants_in_row > self.profile.max_consonants_in_row:
                    return False
        return True

    def _apply_replacements(self, name: str) -> str:
        '''Применение установленных замен.'''
        for old, new in self.profile.replacement_rules.items():
            name = name.replace(old, new)
        return name

    def _has_forbidden_combination(self, name: str) -> bool:
        '''Содержит ли имя запрещенные комбинации.'''
        name = name.lower()
        return any(
            combo.lower() in name
            for combo in self.profile.forbidden_combinations 
        )

    def _valid(self, name: str) -> bool:
        '''Полная валидация имени.'''
        pure_name = name.replace("'", "")

        if not (
            self.profile.min_length
            <= len(pure_name)
            <= self.profile.max_length
        ):
            return False

        if self._has_forbidden_combination(name):
            return False

        if not self._valid_consonants(name):
            return False

        return True

    def get_persone_name(self,) -> str:
        for _ in range(500):
            pattern = self.weighted_choice(self.profile.patterns)
            name = ''.join([
                self.weighted_choice(getattr(self.profile, self.SYMBOL_PATTERN_TO_PART[s]))
                for s in pattern
            ])
            name = self._apply_replacements(name)
            name = self._maybe_add_apostrophe(name).capitalize()

            if not self._valid(name):
                continue

            return name

        raise RuntimeError('Не удалось сгенерировать имя')


__all__ = (NameGenerator,)