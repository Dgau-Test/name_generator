from dataclasses import dataclass, field


@dataclass
class WeightedValue:
    value: str
    weight: float = 1.0


@dataclass
class NameProfile:
    # одиночные согласные
    # "к", "р", "т", "м", "н",
    consonants: list[WeightedValue] = field(default_factory=list)
    # допустимые гласные
    # "а", "о", "у", "и", "э"
    # "ае", "иа", "эи"
    vowels: list[WeightedValue] = field(default_factory=list)

    # Допустимые группы согласных
    # "кр", "гр", "тр", "др"
    onset_clusters: list[WeightedValue] = field(default_factory=list)
    coda_clusters: list[WeightedValue] = field(default_factory=list)

    # куски, которые особенно хорошо звучат в начале имени
    # "Эл", "Аэ", "Ли","Са", "Та"
    start_syllables: list[WeightedValue] = field(default_factory=list)
    # внутренние части
    # "ри","ли","на","эль","ра"
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
