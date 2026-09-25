from name_generator.models.name_profile import NameProfile, WeightedValue


ORC_MALE = NameProfile(
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
        WeightedValue("згр", 4),
        WeightedValue("скр", 3),
        WeightedValue("хр", 8),
    ],

    coda_clusters=[
        WeightedValue("рг", 25),
        WeightedValue("рк", 22),
        WeightedValue("рт", 15),
        WeightedValue("нг", 12),
        WeightedValue("нд", 8),
        WeightedValue("кт", 6),
        WeightedValue("рд", 10),
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
    ],

    patterns=[
        WeightedValue("SE", 25),
        WeightedValue("SME", 30),
        WeightedValue("KVC", 20),
        WeightedValue("CVCD", 12),
        WeightedValue("CVC", 8),
        WeightedValue("KVCD", 5),
    ],

    min_length=3,
    max_length=11,

    max_consonants_in_row=3,
    max_vowels_in_row=1,

    forbidden_combinations=[
        "ааа",
        "ооо",
        "ууу",
        "ии",
        "э",
        "ю",
        "я",
    ],

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "рр": "р",
        "ггг": "гг",
        "ккк": "кк",
    },

    apostrophe_chance=0.025,
)


ORC_FEMALE = NameProfile(
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
    ],

    coda_clusters=[
        WeightedValue("рг", 10),
        WeightedValue("рк", 10),
        WeightedValue("нд", 8),
        WeightedValue("нг", 8),
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
    ],

    middle_syllables=[
        WeightedValue("га", 12),
        WeightedValue("ра", 20),
        WeightedValue("на", 18),
        WeightedValue("ма", 13),
        WeightedValue("ка", 12),
        WeightedValue("ру", 10),
        WeightedValue("да", 8),
    ],

    end_syllables=[
        WeightedValue("га", 18),
        WeightedValue("ра", 20),
        WeightedValue("на", 20),
        WeightedValue("ка", 14),
        WeightedValue("ша", 9),
        WeightedValue("ма", 10),
        WeightedValue("ура", 8),
    ],

    patterns=[
        WeightedValue("SE", 30),
        WeightedValue("SME", 45),
        WeightedValue("SMME", 12),
        WeightedValue("CVCVCV", 8),
        WeightedValue("KVCV", 5),
    ],

    min_length=4,
    max_length=12,

    max_consonants_in_row=2,
    max_vowels_in_row=1,

    forbidden_combinations=[
        "ааа",
        "ооо",
        "ууу",
        "э",
        "ю",
    ],

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "рр": "р",
    },

    apostrophe_chance=0.01,
)
