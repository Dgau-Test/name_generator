from name_generator.models.name_profile import NameProfile, WeightedValue


ORC_CITY = NameProfile(
    consonants=[
        WeightedValue("г", 30),
        WeightedValue("к", 27),
        WeightedValue("р", 32),
        WeightedValue("д", 20),
        WeightedValue("т", 16),
        WeightedValue("м", 10),
        WeightedValue("н", 12),
        WeightedValue("х", 8),
    ],

    vowels=[
        WeightedValue("а", 40),
        WeightedValue("о", 35),
        WeightedValue("у", 20),
        WeightedValue("ы", 5),
    ],

    onset_clusters=[
        WeightedValue("гр", 27),
        WeightedValue("кр", 25),
        WeightedValue("др", 16),
        WeightedValue("тр", 12),
        WeightedValue("хр", 8),
        WeightedValue("згр", 4),
    ],

    coda_clusters=[
        WeightedValue("рг", 20),
        WeightedValue("рк", 18),
        WeightedValue("нд", 12),
        WeightedValue("нг", 12),
        WeightedValue("рт", 10),
    ],

    start_syllables=[
        WeightedValue("Гор", 15),
        WeightedValue("Гар", 13),
        WeightedValue("Краг", 18),
        WeightedValue("Дур", 15),
        WeightedValue("Мор", 11),
        WeightedValue("Ур", 14),
        WeightedValue("Торг", 12),
        WeightedValue("Хар", 9),
        WeightedValue("Грум", 8),
    ],

    middle_syllables=[
        WeightedValue("га", 12),
        WeightedValue("гор", 15),
        WeightedValue("дур", 16),
        WeightedValue("рак", 14),
        WeightedValue("тар", 10),
        WeightedValue("мар", 8),
        WeightedValue("ур", 10),
    ],

    end_syllables=[
        WeightedValue("град", 14),
        WeightedValue("гар", 15),
        WeightedValue("дор", 15),
        WeightedValue("рак", 12),
        WeightedValue("дур", 10),
        WeightedValue("гор", 10),
        WeightedValue("тар", 8),
        WeightedValue("кхар", 5),
    ],

    patterns=[
        WeightedValue("SME", 50),
        WeightedValue("SMME", 30),
        WeightedValue("SE", 20),
    ],

    min_length=5,
    max_length=16,

    max_consonants_in_row=3,
    max_vowels_in_row=1,

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "рр": "р",
    },
)
