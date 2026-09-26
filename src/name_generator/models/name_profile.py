from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(frozen=True)
class WeightedValue:
    value: str
    weight: float = 1.0

    def __post_init__(self) -> None:
        if self.weight <= 0:
            raise ValueError("weight должен быть > 0")


@dataclass
class NameProfile:
    # одиночные согласные
    # 'к', 'р', 'т', 'м', 'н',
    consonants: list[WeightedValue] = field(default_factory=list)
    # допустимые гласные
    # 'а', 'о', 'у', 'и', 'э'
    # 'ае', 'иа', 'эи'
    vowels: list[WeightedValue] = field(default_factory=list)

    # Допустимые группы согласных
    # 'кр', 'гр', 'тр', 'др'
    onset_clusters: list[WeightedValue] = field(default_factory=list)
    coda_clusters: list[WeightedValue] = field(default_factory=list)

    # куски, которые особенно хорошо звучат в начале имени
    # 'Эл', 'Аэ', 'Ли','Са', 'Та'
    start_syllables: list[WeightedValue] = field(default_factory=list)
    # внутренние части
    # 'ри','ли','на','эль','ра'
    middle_syllables: list[WeightedValue] = field(default_factory=list)
    # окончания
    end_syllables: list[WeightedValue] = field(default_factory=list)

    prefixes: list[WeightedValue] = field(default_factory=list)
    suffixes: list[WeightedValue] = field(default_factory=list)


    # C = обычная согласная
    # V = гласная

    # K = кластер согласных в начале
    # D = кластер согласных в конце

    # S = готовое начало имени
    # M = готовая середина
    # E = готовое окончание
    patterns: list[WeightedValue] = field(default_factory=list)

    min_length: int = 1
    max_length: int = 14

    # ограничения
    max_consonants_in_row: int = 2
    max_vowels_in_row: int = 2

    # Запрещенные комбинации символов
    forbidden_combinations: list[str] = field(default_factory=list)
    # Автоматическое преобразование
    replacement_rules: dict[str, str] = field(default_factory=dict)

    # вероятность вставки апострофа
    apostrophe_chance: float = 0.0

    def get_part(self, symbol: str) -> list[WeightedValue]:
        '''Возвращает часть профиля, соответствующую переданному символу шаблона.'''
        try:
            part_name = self.SYMBOL_PATTERN_TO_PART[symbol]
        except KeyError:
            raise ValueError(
                f"Неизвестный символ шаблона: {symbol!r}"
            ) from None

        return getattr(self, part_name)

    SYMBOL_PATTERN_TO_PART: ClassVar[dict[str, str]] = {
        'C': 'consonants',
        'V': 'vowels',
        'K': 'onset_clusters',
        'D': 'coda_clusters',
        'S': 'start_syllables',
        'M': 'middle_syllables',
        'E': 'end_syllables',
    }

    def __post_init__(self) -> None:
        self._validate_lengths()
        self._validate_limits()
        self._validate_patterns()
        
    def _validate_lengths(self) -> None:
        if self.min_length < 1:
            raise ValueError('min_length должен быть >= 1')

        if self.max_length < self.min_length:
            raise ValueError(
                'max_length не может быть меньше min_length'
            )

    def _validate_limits(self) -> None:
        if self.max_consonants_in_row < 1:
            raise ValueError('max_consonants_in_row должен быть >= 1')

        if self.max_vowels_in_row < 1:
            raise ValueError('max_vowels_in_row должен быть >= 1')

        if not 0.0 <= self.apostrophe_chance <= 1.0:
            raise ValueError(
                'apostrophe_chance должен находиться в диапазоне [0, 1]'
            )

    def _validate_patterns(self) -> None:
        for weighted_pattern in self.patterns:
            pattern = weighted_pattern.value

            for symbol in pattern:
                part_name = self.SYMBOL_PATTERN_TO_PART.get(symbol)

                if part_name is None:
                    raise ValueError(
                        f'Неизвестный символ {symbol!r} '
                        f'в шаблоне {pattern!r}'
                    )

                if not getattr(self, part_name):
                    raise ValueError(
                        f'{part_name!r} не может быть пустым: '
                        f'он используется в шаблоне {pattern!r}'
                    )
