from name_generator.models.name_profile import NameProfile, WeightedValue


HUMAN_COUNTRY = NameProfile(
    consonants=[
        WeightedValue("в", 16),
        WeightedValue("д", 12),
        WeightedValue("к", 9),
        WeightedValue("л", 22),
        WeightedValue("м", 14),
        WeightedValue("н", 20),
        WeightedValue("р", 30),
        WeightedValue("с", 15),
        WeightedValue("т", 14),
        WeightedValue("г", 7),
    ],

    vowels=[
        WeightedValue("а", 34),
        WeightedValue("е", 20),
        WeightedValue("и", 18),
        WeightedValue("о", 22),
        WeightedValue("у", 6),
    ],

    onset_clusters=[
        WeightedValue("др", 8),
        WeightedValue("кр", 6),
        WeightedValue("ст", 8),
        WeightedValue("тр", 6),
        WeightedValue("вр", 4),
    ],

    coda_clusters=[
        WeightedValue("рд", 7),
        WeightedValue("рн", 8),
        WeightedValue("нд", 7),
    ],

    start_syllables=[
        WeightedValue("Аль", 10),
        WeightedValue("Ар", 12),
        WeightedValue("Вал", 14),
        WeightedValue("Вар", 12),
        WeightedValue("Дар", 10),
        WeightedValue("Кал", 10),
        WeightedValue("Лор", 14),
        WeightedValue("Мер", 10),
        WeightedValue("Рен", 10),
        WeightedValue("Сер", 8),
        WeightedValue("Тер", 9),
    ],

    middle_syllables=[
        WeightedValue("ан", 14),
        WeightedValue("ар", 12),
        WeightedValue("ен", 12),
        WeightedValue("ер", 10),
        WeightedValue("ин", 10),
        WeightedValue("ор", 12),
        WeightedValue("али", 6),
    ],

    end_syllables=[
        WeightedValue("ия", 22),
        WeightedValue("ар", 10),
        WeightedValue("ан", 12),
        WeightedValue("ор", 10),
        WeightedValue("иян", 5),
        WeightedValue("ель", 8),
        WeightedValue("ера", 10),
        WeightedValue("он", 10),
    ],

    patterns=[
        WeightedValue("SE", 30),
        WeightedValue("SME", 50),
        WeightedValue("SMME", 20),
    ],

    min_length=5,
    max_length=16,

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
