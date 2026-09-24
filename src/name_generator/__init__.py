import random

from app.core.name_generator.name_profile import NameProfile


__all__ = (NameProfile,)


class NameGenerator:
    SYMBOL_PATTERN_TO_PART = {
        'C': 'consonants',
        'V': 'vowels',
        'S': 'start_syllables',
        'M': 'middle_syllables',
        'E': 'end_syllables'
    }

    def __init__(self, profile: NameProfile):
        self.profile = profile


    def _mutate_person_name(self, name: str) -> str:
        if (
            random.random() < self.profile.apostrophe_chance
            and len(name) >= 5
        ):
            position = random.randint(2, len(name) - 2)
            name = f"{name[:position]}'{name[position:]}"
        return name

    def _valid_length(self, name: str) -> bool:
        return self.profile.min_length <= len(name) <= self.profile.max_length

    def _pronounceable(self, name: str) -> bool:
        """Хорошо ли произносится имя."""
        vowels = set('аеёиоуыэюя')
        consonants_in_row = 0

        for char in name.lower():
            if char in vowels:
                consonants_in_row = 0
                continue

            if char.isalpha():
                consonants_in_row += 1

                if consonants_in_row > 3:
                    return False
        return True


    def get_persone_name(self, pattern: None | str = None) -> str:

        for _ in range(500):
            pattern = pattern or random.choice(self.profile.patterns)
            name = ''.join([
                random.choice(getattr(self.profile, self.SYMBOL_PATTERN_TO_PART[s]))
                for s in pattern
            ])

            name = self._mutate_person_name(name).capitalize()

            if (
                not self._valid_length(name)
                or not self._pronounceable(name)
            ):
                continue

            return name

        raise RuntimeError('Не удалось сгенерировать имя')