from ..name_profile import NameProfile


ELF = NameProfile(
    consonants=[
        "л", "р", "н", "с", "т",
        "в", "м"
    ],

    vowels=[
        "а", "э", "и", "о",
        "ае", "иа"
    ],

    start_syllables=[
        "Эл",
        "Ли",
        "Аэ",
        "Та",
        "Са",
        "Ил"
    ],

    middle_syllables=[
        "ри",
        "ла",
        "ни",
        "э",
        "ли",
        "ра"
    ],

    end_syllables=[
        "эль",
        "ион",
        "ир",
        "ан",
        "ис",
        "ор"
    ],

    patterns=[
        "SE",
        "SME",
        "SMME",
        "CVCVC"
    ],

    min_length=4,
    max_length=12,

    apostrophe_chance=0.03,
    double_vowel_chance=0.15
)