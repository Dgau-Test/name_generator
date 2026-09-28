import random
from collections import defaultdict

from name_generator.models import NameProfile, WeightedValue


class NameGenerator:
    def __init__(self):
        self._exist_names = defaultdict(set)

    def weighted_choice(self, items: list[WeightedValue]) -> str:
        """Возвращает случайное значение с учётом заданных весов.

        Args:
            items: Список значений и соответствующих им весов.

        Returns:
            Случайно выбранное строковое значение.

        Raises:
            ValueError: Если список значений пуст.
        """
        if not items:
            raise ValueError('Список WeightedValue пуст')

        return random.choices(
            population=[item.value for item in items],
            weights=[item.weight for item in items],
        )[0]

    def _maybe_add_apostrophe(self, name: str, profile: NameProfile) -> str:
        """Возможное добавление апострофа."""
        if random.random() < profile.apostrophe_chance and len(name) >= 5:
            position = random.randint(2, len(name) - 2)
            name = f"{name[:position]}'{name[position:]}"
        return name

    def _valid_sequence_length(
        self,
        name: str,
        chars: frozenset[str],
        max_in_row: int,
    ) -> bool:
        count = 0

        for char in name.lower():
            if char in chars:
                count += 1

                if count > max_in_row:
                    return False
            elif char.isalpha():
                count = 0

        return True

    def _valid_consonants(self, name: str, profile: NameProfile) -> bool:
        """Проверяет количество согласных, идущих подряд."""
        return self._valid_sequence_length(
            name,
            profile.alphabet.consonants,
            profile.max_consonants_in_row,
        )

    def _valid_vowels(self, name: str, profile: NameProfile) -> bool:
        """Проверяет количество гласных, идущих подряд."""
        return self._valid_sequence_length(
            name,
            profile.alphabet.vowels,
            profile.max_vowels_in_row,
        )

    def _apply_replacements(self, name: str, profile: NameProfile) -> str:
        """Применение установленных замен."""
        for old, new in profile.replacement_rules.items():
            name = name.replace(old, new)
        return name

    def _has_forbidden_combination(
        self, name: str, profile: NameProfile
    ) -> bool:
        """Содержит ли имя запрещенные комбинации."""
        name = name.lower()
        return any(
            combo.lower() in name for combo in profile.forbidden_combinations
        )

    def _valid_length(self, name: str, profile: NameProfile) -> bool:
        """Валидация длины наименования."""
        return (
            profile.min_length
            <= len(name.replace("'", ''))
            <= profile.max_length
        )

    def _valid(self, name: str, profile: NameProfile) -> bool:
        """Полная валидация наименования."""
        if (
            not self._valid_length(name, profile)
            or not self._valid_consonants(name, profile)
            or not self._valid_vowels(name, profile)
            or self._has_forbidden_combination(name, profile)
        ):
            return False
        return True

    def _build(self, profile: NameProfile) -> str:
        """Построение наименования по шаблону."""
        pattern = self.weighted_choice(profile.patterns)

        return ''.join(
            self.weighted_choice(profile.get_part(s)) for s in pattern
        ).lower()

    def generate(
        self,
        profile: NameProfile,
        *,
        unique: bool = False,
        exist_key: str = 'names',
    ) -> str:
        """Генерирует наименование в соответствии с ограничениями профиля.

        Args:
            profile: Профиль с правилами и взвешенными частями для генерации.
            unique: Требовать уникальность сгенерированного наименования.
            exist_key: Ключ области, в которой отслеживается уникальность.

        Raises:
            RuntimeError: Если не удалось сгенерировать
            корректное наименование.
        """
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
