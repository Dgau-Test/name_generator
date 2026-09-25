from name_generator.models.name_profile import NameProfile, WeightedValue


ORC_COUNTRY = NameProfile(
    consonants=[
        WeightedValue("г", 27),
        WeightedValue("к", 25),
        WeightedValue("р", 35),
        WeightedValue("д", 20),
        WeightedValue("т", 16),
        WeightedValue("м", 12),
        WeightedValue("н", 12),
        WeightedValue("з", 7),
        WeightedValue("х", 8),
    ],

    vowels=[
        WeightedValue("а", 38),
        WeightedValue("о", 32),
        WeightedValue("у", 25),
        WeightedValue("ы", 5),
    ],

    onset_clusters=[
        WeightedValue("гр", 25),
        WeightedValue("кр", 22),
        WeightedValue("др", 18),
        WeightedValue("тр", 12),
        WeightedValue("хр", 8),
    ],

    coda_clusters=[
        WeightedValue("рг", 20),
        WeightedValue("рк", 18),
        WeightedValue("нд", 12),
        WeightedValue("нг", 12),
    ],

    start_syllables=[
        WeightedValue("Гар", 12),
        WeightedValue("Гор", 12),
        WeightedValue("Кра", 18),
        WeightedValue("Дур", 15),
        WeightedValue("Мор", 12),
        WeightedValue("Ур", 15),
        WeightedValue("Тар", 10),
        WeightedValue("Хар", 8),
    ],

    middle_syllables=[
        WeightedValue("гар", 15),
        WeightedValue("дур", 17),
        WeightedValue("рак", 15),
        WeightedValue("гор", 12),
        WeightedValue("тар", 10),
        WeightedValue("нар", 9),
        WeightedValue("мар", 7),
    ],

    end_syllables=[
        WeightedValue("ия", 8),
        WeightedValue("ар", 15),
        WeightedValue("ор", 14),
        WeightedValue("гар", 17),
        WeightedValue("дур", 14),
        WeightedValue("рак", 12),
        WeightedValue("гор", 10),
    ],

    patterns=[
        WeightedValue("SME", 55),
        WeightedValue("SMME", 30),
        WeightedValue("SE", 15),
    ],

    min_length=5,
    max_length=16,

    max_consonants_in_row=3,
    max_vowels_in_row=2,

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "рр": "р",
    },
)
