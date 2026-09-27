from name_generator.models.name_profile import WeightedValue
from name_generator.name_profiles import RussianNameProfile

HUMAN_COUNTRY = RussianNameProfile(
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
        WeightedValue("б", 6),
        WeightedValue("п", 5),
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
        WeightedValue("бр", 5),
        WeightedValue("гр", 5),
    ],

    coda_clusters=[
        WeightedValue("рд", 7),
        WeightedValue("рн", 8),
        WeightedValue("нд", 7),
        WeightedValue("рт", 5),
        WeightedValue("ль", 5),
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

        WeightedValue("Бел", 8),
        WeightedValue("Гар", 8),
        WeightedValue("Нор", 10),
        WeightedValue("Вер", 8),
        WeightedValue("Рав", 7),
        WeightedValue("Дал", 7),
        WeightedValue("Кор", 7),
    ],

    middle_syllables=[
        WeightedValue("ан", 14),
        WeightedValue("ар", 12),
        WeightedValue("ен", 12),
        WeightedValue("ер", 10),
        WeightedValue("ин", 10),
        WeightedValue("ор", 12),
        WeightedValue("али", 6),

        WeightedValue("ов", 8),
        WeightedValue("ев", 6),
        WeightedValue("он", 7),
        WeightedValue("ел", 7),
        WeightedValue("ра", 6),
        WeightedValue("да", 5),
    ],

    end_syllables=[
        # Наиболее характерные окончания стран
        WeightedValue("ия", 24),
        WeightedValue("ея", 8),
        WeightedValue("ера", 10),
        WeightedValue("ана", 9),
        WeightedValue("ания", 8),

        # Нейтральные фэнтезийные окончания
        WeightedValue("ан", 11),
        WeightedValue("ар", 8),
        WeightedValue("ор", 9),
        WeightedValue("ель", 8),
        WeightedValue("он", 9),

        # Более жёсткие региональные формы
        WeightedValue("ланд", 5),
        WeightedValue("ария", 6),
        WeightedValue("ория", 6),
    ],

    patterns=[
        WeightedValue("SE", 35),
        WeightedValue("SME", 50),
        WeightedValue("SMME", 10),

        # Редкие названия, построенные непосредственно
        # из фонологии культуры.
        WeightedValue("CVCE", 3),
        WeightedValue("KVCE", 2),
    ],

    min_length=5,
    max_length=17,

    max_consonants_in_row=2,
    max_vowels_in_row=2,

    forbidden_combinations=[
        "ааа",
        "еее",
        "иии",
        "ооо",
        "ууу",
        "ррр",
        "ллл",
        "ннн",
    ],

    replacement_rules={
        "аа": "а",
        "ее": "е",
        "ии": "и",
        "оо": "о",
        "уу": "у",
        "рр": "р",
        "ллл": "лл",
        "ннн": "нн",
    },

    apostrophe_chance=0.0,
)
