from dataclasses import dataclass


@dataclass
class NameProfile:
    # согласные или согласные кластеры культуры
    # "к", "р", "т", "м", "н",
    # "кр", "гр", "тр", "др"
    consonants: list[str]
    #допустимые гласные
    # "а", "о", "у", "и", "э"
    # "ае", "иа", "эи"
    vowels: list[str]

    # куски, которые особенно хорошо звучат в начале имени
    # "Эл", "Аэ", "Ли","Са", "Та"
    start_syllables: list[str]
    # внутренние части
    # "ри","ли","на","эль","ра"
    middle_syllables: list[str]
    # окончания
    end_syllables: list[str]

    # патерн построения
    # C = согласная
    # V = гласная
    # S = начальный слог
    # M = средний слог
    # E = окончание
    patterns: list[str]

    min_length: int = 1
    max_length: int = 10

    # вероятность вставки апострофа
    apostrophe_chance: float = 0.0
    # вероятность удвоения или сочетания гласных
    double_vowel_chance: float = 0.0