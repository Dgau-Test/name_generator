from ..name_profile import NameProfile


ORC = NameProfile(
    consonants=[
        "г", "к", "р", "д", "т",
        "гр", "кр", "др", "тр"
    ],

    vowels=[
        "а", "о", "у"
    ],

    start_syllables=[
        "Гр",
        "Кр",
        "Мор",
        "Ур",
        "Др",
        "Тар"
    ],

    middle_syllables=[
        "аг",
        "ук",
        "ог",
        "ар",
        "ур"
    ],

    end_syllables=[
        "аш",
        "ак",
        "уг",
        "ор",
        "гар"
    ],

    patterns=[
        "SE",
        "SME",
        "CVC",
        "CVCVC"
    ],

    min_length=3,
    max_length=10,

    apostrophe_chance=0.08,
    double_vowel_chance=0.0
)