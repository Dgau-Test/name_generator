from name_generator.models.name_profile import NameProfile, WeightedValue


HUMAN_MALE = NameProfile(
    consonants=[
        WeightedValue("б", 8),
        WeightedValue("в", 14),
        WeightedValue("г", 8),
        WeightedValue("д", 14),
        WeightedValue("к", 10),
        WeightedValue("л", 24),
        WeightedValue("м", 18),
        WeightedValue("н", 25),
        WeightedValue("р", 30),
        WeightedValue("с", 18),
        WeightedValue("т", 20),
        WeightedValue("ф", 4),
        WeightedValue("х", 3),
        WeightedValue("з", 7),
    ],

    vowels=[
        WeightedValue("а", 32),
        WeightedValue("е", 20),
        WeightedValue("и", 22),
        WeightedValue("о", 20),
        WeightedValue("у", 6),
    ],

    onset_clusters=[
        WeightedValue("бр", 10),
        WeightedValue("др", 12),
        WeightedValue("кр", 7),
        WeightedValue("тр", 10),
        WeightedValue("гр", 5),
        WeightedValue("ст", 10),
        WeightedValue("вар", 4),
    ],

    coda_clusters=[
        WeightedValue("рн", 8),
        WeightedValue("рт", 8),
        WeightedValue("нд", 10),
        WeightedValue("ст", 8),
        WeightedValue("ль", 10),
        WeightedValue("н", 20),
        WeightedValue("р", 20),
    ],

    start_syllables=[
        WeightedValue("Аль", 12),
        WeightedValue("Ар", 18),
        WeightedValue("Бер", 10),
        WeightedValue("Вар", 13),
        WeightedValue("Дар", 15),
        WeightedValue("Кал", 10),
        WeightedValue("Лор", 12),
        WeightedValue("Мар", 18),
        WeightedValue("Рен", 14),
        WeightedValue("Сер", 12),
        WeightedValue("Тар", 10),
        WeightedValue("Эд", 8),
        WeightedValue("Эр", 12),
        WeightedValue("Вел", 8),
    ],

    middle_syllables=[
        WeightedValue("ан", 20),
        WeightedValue("ар", 18),
        WeightedValue("ен", 15),
        WeightedValue("ер", 13),
        WeightedValue("ил", 12),
        WeightedValue("ор", 12),
        WeightedValue("ин", 15),
        WeightedValue("ел", 10),
        WeightedValue("ри", 10),
        WeightedValue("да", 5),
    ],

    end_syllables=[
        WeightedValue("ан", 22),
        WeightedValue("ар", 18),
        WeightedValue("ен", 18),
        WeightedValue("ер", 15),
        WeightedValue("ин", 16),
        WeightedValue("ор", 13),
        WeightedValue("ель", 8),
        WeightedValue("ис", 7),
        WeightedValue("он", 10),
        WeightedValue("ир", 10),
    ],

    patterns=[
        WeightedValue("SE", 28),
        WeightedValue("SME", 38),
        WeightedValue("SMME", 8),
        WeightedValue("CVCVC", 12),
        WeightedValue("KVC", 7),
        WeightedValue("CVCE", 7),
    ],

    min_length=4,
    max_length=12,

    max_consonants_in_row=2,
    max_vowels_in_row=2,

    forbidden_combinations=[
        "ааа",
        "еее",
        "иии",
        "ооо",
        "кг",
        "гк",
        "тд",
        "дт",
    ],

    replacement_rules={
        "аа": "а",
        "ее": "е",
        "ии": "и",
        "оо": "о",
        "рр": "р",
        "ннн": "нн",
    },

    apostrophe_chance=0.002,
)


HUMAN_FEMALE = NameProfile(
    consonants=[
        WeightedValue("в", 12),
        WeightedValue("д", 8),
        WeightedValue("к", 7),
        WeightedValue("л", 28),
        WeightedValue("м", 20),
        WeightedValue("н", 26),
        WeightedValue("р", 24),
        WeightedValue("с", 18),
        WeightedValue("т", 14),
        WeightedValue("з", 7),
    ],

    vowels=[
        WeightedValue("а", 38),
        WeightedValue("е", 20),
        WeightedValue("и", 24),
        WeightedValue("о", 10),
        WeightedValue("у", 3),
        WeightedValue("э", 5),
    ],

    onset_clusters=[
        WeightedValue("бр", 5),
        WeightedValue("др", 5),
        WeightedValue("ст", 8),
        WeightedValue("тр", 4),
    ],

    coda_clusters=[
        WeightedValue("ль", 12),
        WeightedValue("н", 20),
        WeightedValue("р", 12),
    ],

    start_syllables=[
        WeightedValue("Али", 15),
        WeightedValue("Ара", 12),
        WeightedValue("Эли", 17),
        WeightedValue("Ила", 9),
        WeightedValue("Ли", 13),
        WeightedValue("Мари", 18),
        WeightedValue("Са", 12),
        WeightedValue("Сели", 10),
        WeightedValue("Ве", 8),
        WeightedValue("Лора", 12),
        WeightedValue("Нари", 10),
        WeightedValue("Те", 7),
    ],

    middle_syllables=[
        WeightedValue("ли", 18),
        WeightedValue("ри", 17),
        WeightedValue("на", 20),
        WeightedValue("ла", 15),
        WeightedValue("ми", 10),
        WeightedValue("си", 8),
        WeightedValue("да", 8),
        WeightedValue("э", 5),
    ],

    end_syllables=[
        WeightedValue("а", 25),
        WeightedValue("ия", 18),
        WeightedValue("ина", 18),
        WeightedValue("ира", 17),
        WeightedValue("ела", 12),
        WeightedValue("эна", 10),
        WeightedValue("ана", 14),
        WeightedValue("ис", 5),
    ],

    patterns=[
        WeightedValue("SE", 30),
        WeightedValue("SME", 45),
        WeightedValue("SMME", 10),
        WeightedValue("CVCVCV", 10),
        WeightedValue("CVCE", 5),
    ],

    min_length=4,
    max_length=13,

    max_consonants_in_row=2,
    max_vowels_in_row=2,

    forbidden_combinations=[
        "ааа",
        "еее",
        "иии",
        "кг",
        "гк",
    ],

    replacement_rules={
        "аа": "а",
        "ее": "е",
        "ии": "и",
        "оо": "о",
        "рр": "р",
    },

    apostrophe_chance=0.0,
)
