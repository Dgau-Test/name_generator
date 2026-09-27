from name_generator.models.name_profile import WeightedValue
from name_generator.name_profiles import RussianNameProfile

ORC_MALE = RussianNameProfile(
    consonants=[
        WeightedValue("г", 30),
        WeightedValue("к", 28),
        WeightedValue("р", 35),
        WeightedValue("д", 18),
        WeightedValue("т", 17),
        WeightedValue("м", 12),
        WeightedValue("н", 10),
        WeightedValue("з", 8),
        WeightedValue("б", 7),
        WeightedValue("ш", 5),
        WeightedValue("х", 7),
    ],

    vowels=[
        WeightedValue("а", 40),
        WeightedValue("о", 30),
        WeightedValue("у", 22),
        WeightedValue("ы", 6),
        WeightedValue("и", 2),
    ],

    onset_clusters=[
        WeightedValue("гр", 30),
        WeightedValue("кр", 28),
        WeightedValue("др", 18),
        WeightedValue("тр", 15),
        WeightedValue("бр", 10),
        WeightedValue("хр", 8),
        WeightedValue("згр", 4),
        WeightedValue("скр", 3),
        WeightedValue("гн", 5),
        WeightedValue("кх", 4),
    ],

    coda_clusters=[
        WeightedValue("рг", 25),
        WeightedValue("рк", 22),
        WeightedValue("рт", 15),
        WeightedValue("нг", 12),
        WeightedValue("нд", 8),
        WeightedValue("кт", 6),
        WeightedValue("рд", 10),
        WeightedValue("гд", 5),
        WeightedValue("рх", 5),
    ],

    start_syllables=[
        WeightedValue("Гар", 18),
        WeightedValue("Гор", 16),
        WeightedValue("Гру", 15),
        WeightedValue("Кра", 22),
        WeightedValue("Кро", 14),
        WeightedValue("Дра", 15),
        WeightedValue("Дур", 14),
        WeightedValue("Мор", 12),
        WeightedValue("Ур", 18),
        WeightedValue("Тар", 15),
        WeightedValue("Тор", 12),
        WeightedValue("Бра", 8),
        WeightedValue("Зар", 7),
        WeightedValue("Хар", 9),

        WeightedValue("Нарг", 8),
        WeightedValue("Грак", 9),
        WeightedValue("Кхар", 7),
        WeightedValue("Бруг", 6),
        WeightedValue("Зуг", 7),
        WeightedValue("Руг", 8),
    ],

    middle_syllables=[
        WeightedValue("га", 20),
        WeightedValue("го", 16),
        WeightedValue("ру", 18),
        WeightedValue("ра", 17),
        WeightedValue("ка", 15),
        WeightedValue("дур", 10),
        WeightedValue("гар", 12),
        WeightedValue("мор", 5),
        WeightedValue("та", 10),
        WeightedValue("ур", 12),

        WeightedValue("гу", 10),
        WeightedValue("кра", 8),
        WeightedValue("раг", 8),
        WeightedValue("дог", 6),
        WeightedValue("хар", 6),
    ],

    end_syllables=[
        WeightedValue("ак", 25),
        WeightedValue("аг", 20),
        WeightedValue("ук", 20),
        WeightedValue("уг", 12),
        WeightedValue("ар", 18),
        WeightedValue("ор", 15),
        WeightedValue("гар", 13),
        WeightedValue("дур", 10),
        WeightedValue("рак", 12),
        WeightedValue("рг", 6),

        WeightedValue("ог", 12),
        WeightedValue("ок", 10),
        WeightedValue("ург", 8),
        WeightedValue("орк", 8),
        WeightedValue("арт", 7),
        WeightedValue("гарк", 5),
    ],

    patterns=[
        # Короткие составные имена
        WeightedValue("SE", 25),
        WeightedValue("SME", 25),

        # Грубые полностью процедурные формы
        WeightedValue("KVC", 18),
        WeightedValue("CVC", 8),
        WeightedValue("CVCD", 9),
        WeightedValue("KVCD", 8),

        # Немного более длинных вариантов
        WeightedValue("KVCVC", 5),
        WeightedValue("CVCE", 2),
    ],

    min_length=3,
    max_length=11,

    max_consonants_in_row=3,
    max_vowels_in_row=1,

    forbidden_combinations=[
        "аа",
        "оо",
        "уу",
        "ыы",
        "ии",
        "ррр",
        "ггг",
        "ккк",
        "хх",
    ],

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "ыы": "ы",
        "рр": "р",
        "ггг": "гг",
        "ккк": "кк",
    },

    apostrophe_chance=0.06,
)


ORC_FEMALE = RussianNameProfile(
    consonants=[
        WeightedValue("г", 22),
        WeightedValue("к", 20),
        WeightedValue("р", 30),
        WeightedValue("д", 15),
        WeightedValue("т", 12),
        WeightedValue("м", 18),
        WeightedValue("н", 18),
        WeightedValue("з", 8),
        WeightedValue("ш", 7),
        WeightedValue("х", 5),
        WeightedValue("б", 5),
    ],

    vowels=[
        WeightedValue("а", 45),
        WeightedValue("о", 20),
        WeightedValue("у", 18),
        WeightedValue("и", 12),
        WeightedValue("ы", 5),
    ],

    onset_clusters=[
        WeightedValue("гр", 18),
        WeightedValue("кр", 15),
        WeightedValue("др", 10),
        WeightedValue("тр", 8),
        WeightedValue("бр", 7),
        WeightedValue("хр", 5),
        WeightedValue("гн", 4),
    ],

    coda_clusters=[
        WeightedValue("рг", 10),
        WeightedValue("рк", 10),
        WeightedValue("нд", 8),
        WeightedValue("нг", 8),
        WeightedValue("рт", 5),
    ],

    start_syllables=[
        WeightedValue("Гра", 15),
        WeightedValue("Кра", 15),
        WeightedValue("Дра", 10),
        WeightedValue("Ура", 15),
        WeightedValue("Мара", 12),
        WeightedValue("Гора", 10),
        WeightedValue("Зара", 9),
        WeightedValue("Тура", 10),
        WeightedValue("Хара", 7),
        WeightedValue("Нара", 8),

        WeightedValue("Гру", 8),
        WeightedValue("Кару", 8),
        WeightedValue("Мура", 10),
        WeightedValue("Рага", 8),
        WeightedValue("Бара", 6),
        WeightedValue("Дуга", 6),
        WeightedValue("Зура", 7),
    ],

    middle_syllables=[
        WeightedValue("га", 12),
        WeightedValue("ра", 20),
        WeightedValue("на", 18),
        WeightedValue("ма", 13),
        WeightedValue("ка", 12),
        WeightedValue("ру", 10),
        WeightedValue("да", 8),

        WeightedValue("гу", 8),
        WeightedValue("та", 9),
        WeightedValue("за", 6),
        WeightedValue("ша", 6),
        WeightedValue("ну", 6),
        WeightedValue("ри", 5),
    ],

    end_syllables=[
        WeightedValue("га", 16),
        WeightedValue("ра", 17),
        WeightedValue("на", 17),
        WeightedValue("ка", 13),
        WeightedValue("ша", 9),
        WeightedValue("ма", 10),
        WeightedValue("ура", 8),

        WeightedValue("да", 8),
        WeightedValue("та", 8),
        WeightedValue("ара", 7),
        WeightedValue("уга", 7),
        WeightedValue("ина", 5),
        WeightedValue("ора", 5),
    ],

    patterns=[
        WeightedValue("SE", 32),
        WeightedValue("SME", 38),
        WeightedValue("SMME", 8),

        # Процедурные имена
        WeightedValue("CVCVCV", 8),
        WeightedValue("KVCV", 7),
        WeightedValue("CVCVE", 4),
        WeightedValue("KVCE", 3),
    ],

    min_length=4,
    max_length=12,

    max_consonants_in_row=2,
    max_vowels_in_row=1,

    forbidden_combinations=[
        "аа",
        "оо",
        "уу",
        "ыы",
        "ии",
        "ррр",
        "ггг",
        "ккк",
    ],

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "ыы": "ы",
        "ии": "и",
        "рр": "р",
    },

    apostrophe_chance=0.04,
)
