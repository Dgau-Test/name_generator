from name_generator.models.name_profile import NameProfile, WeightedValue


HUMAN_CITY = NameProfile(
    consonants=[
        WeightedValue("б", 8),
        WeightedValue("в", 14),
        WeightedValue("д", 15),
        WeightedValue("к", 12),
        WeightedValue("л", 20),
        WeightedValue("м", 12),
        WeightedValue("н", 18),
        WeightedValue("р", 28),
        WeightedValue("с", 16),
        WeightedValue("т", 18),
        WeightedValue("г", 9),
    ],

    vowels=[
        WeightedValue("а", 30),
        WeightedValue("е", 20),
        WeightedValue("и", 15),
        WeightedValue("о", 27),
        WeightedValue("у", 8),
    ],

    onset_clusters=[
        WeightedValue("бр", 9),
        WeightedValue("др", 10),
        WeightedValue("кр", 10),
        WeightedValue("гр", 8),
        WeightedValue("ст", 10),
        WeightedValue("тр", 8),
    ],

    coda_clusters=[
        WeightedValue("рд", 10),
        WeightedValue("рн", 8),
        WeightedValue("ст", 10),
        WeightedValue("нд", 8),
    ],

    start_syllables=[
        WeightedValue("Ард", 10),
        WeightedValue("Бел", 12),
        WeightedValue("Вар", 14),
        WeightedValue("Дор", 14),
        WeightedValue("Кал", 11),
        WeightedValue("Лор", 13),
        WeightedValue("Мар", 12),
        WeightedValue("Рен", 10),
        WeightedValue("Стар", 7),
        WeightedValue("Тар", 10),
        WeightedValue("Вел", 12),
    ],

    middle_syllables=[
        WeightedValue("ен", 12),
        WeightedValue("ар", 12),
        WeightedValue("ор", 14),
        WeightedValue("ел", 10),
        WeightedValue("ин", 8),
        WeightedValue("да", 8),
        WeightedValue("ер", 10),
    ],

    end_syllables=[
        WeightedValue("град", 8),
        WeightedValue("дор", 12),
        WeightedValue("форт", 5),
        WeightedValue("ар", 12),
        WeightedValue("ен", 12),
        WeightedValue("он", 12),
        WeightedValue("ель", 8),
        WeightedValue("ор", 12),
        WeightedValue("ин", 8),
    ],

    patterns=[
        WeightedValue("SE", 25),
        WeightedValue("SME", 50),
        WeightedValue("SMME", 20),
        WeightedValue("CVCE", 5),
    ],

    min_length=5,
    max_length=17,

    max_consonants_in_row=3,
    max_vowels_in_row=2,

    replacement_rules={
        "аа": "а",
        "ее": "е",
        "ии": "и",
        "оо": "о",
        "рр": "р",
    },
)
