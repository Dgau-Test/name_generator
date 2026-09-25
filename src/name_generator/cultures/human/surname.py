from name_generator.models.name_profile import NameProfile, WeightedValue


HUMAN_SURNAME = NameProfile(
    consonants=[
        WeightedValue("б", 7),
        WeightedValue("в", 15),
        WeightedValue("д", 12),
        WeightedValue("к", 12),
        WeightedValue("л", 20),
        WeightedValue("м", 14),
        WeightedValue("н", 18),
        WeightedValue("р", 26),
        WeightedValue("с", 18),
        WeightedValue("т", 16),
    ],

    vowels=[
        WeightedValue("а", 30),
        WeightedValue("е", 22),
        WeightedValue("и", 18),
        WeightedValue("о", 22),
        WeightedValue("у", 8),
    ],

    onset_clusters=[
        WeightedValue("бр", 8),
        WeightedValue("др", 8),
        WeightedValue("кр", 8),
        WeightedValue("ст", 10),
        WeightedValue("тр", 7),
    ],

    coda_clusters=[
        WeightedValue("рд", 8),
        WeightedValue("рн", 8),
        WeightedValue("ль", 10),
        WeightedValue("ст", 10),
        WeightedValue("н", 14),
    ],

    start_syllables=[
        WeightedValue("Арден", 10),
        WeightedValue("Бел", 12),
        WeightedValue("Вар", 12),
        WeightedValue("Дор", 11),
        WeightedValue("Кел", 9),
        WeightedValue("Лор", 14),
        WeightedValue("Мар", 14),
        WeightedValue("Рен", 12),
        WeightedValue("Сар", 10),
        WeightedValue("Тер", 10),
        WeightedValue("Вел", 10),
    ],

    middle_syllables=[
        WeightedValue("ен", 15),
        WeightedValue("ар", 15),
        WeightedValue("ор", 12),
        WeightedValue("ел", 12),
        WeightedValue("ин", 10),
        WeightedValue("ер", 10),
    ],

    end_syllables=[
        WeightedValue("ар", 14),
        WeightedValue("ен", 15),
        WeightedValue("ер", 13),
        WeightedValue("ор", 12),
        WeightedValue("ин", 12),
        WeightedValue("ель", 8),
        WeightedValue("ан", 12),
        WeightedValue("ард", 7),
    ],

    patterns=[
        WeightedValue("SE", 55),
        WeightedValue("SME", 35),
        WeightedValue("SMME", 10),
    ],

    min_length=5,
    max_length=14,

    max_consonants_in_row=2,
    max_vowels_in_row=2,

    replacement_rules={
        "аа": "а",
        "ее": "е",
        "ии": "и",
        "оо": "о",
        "рр": "р",
    },
)