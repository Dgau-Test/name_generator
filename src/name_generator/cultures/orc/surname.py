from name_generator.models.name_profile import NameProfile, WeightedValue


ORC_SURNAME = NameProfile(
    consonants=[
        WeightedValue("г", 28),
        WeightedValue("к", 25),
        WeightedValue("р", 32),
        WeightedValue("д", 18),
        WeightedValue("т", 14),
        WeightedValue("м", 10),
        WeightedValue("н", 10),
        WeightedValue("х", 10),
        WeightedValue("з", 6),
    ],

    vowels=[
        WeightedValue("а", 38),
        WeightedValue("о", 32),
        WeightedValue("у", 25),
        WeightedValue("ы", 5),
    ],

    onset_clusters=[
        WeightedValue("гр", 25),
        WeightedValue("кр", 25),
        WeightedValue("др", 18),
        WeightedValue("тр", 12),
        WeightedValue("хр", 10),
    ],

    coda_clusters=[
        WeightedValue("рг", 22),
        WeightedValue("рк", 20),
        WeightedValue("нд", 10),
        WeightedValue("нг", 12),
        WeightedValue("рд", 8),
    ],

    start_syllables=[
        WeightedValue("Гром", 15),
        WeightedValue("Краг", 18),
        WeightedValue("Дург", 15),
        WeightedValue("Морг", 12),
        WeightedValue("Тар", 12),
        WeightedValue("Ург", 15),
        WeightedValue("Хар", 9),
        WeightedValue("Кор", 10),
        WeightedValue("Гар", 12),
    ],

    middle_syllables=[
        WeightedValue("дур", 13),
        WeightedValue("гар", 15),
        WeightedValue("рак", 14),
        WeightedValue("гор", 12),
        WeightedValue("нар", 8),
        WeightedValue("тур", 8),
    ],

    end_syllables=[
        WeightedValue("гар", 18),
        WeightedValue("рак", 18),
        WeightedValue("дур", 15),
        WeightedValue("гор", 13),
        WeightedValue("кхар", 7),
        WeightedValue("мар", 9),
        WeightedValue("тар", 10),
    ],

    patterns=[
        WeightedValue("SE", 45),
        WeightedValue("SME", 45),
        WeightedValue("SMME", 10),
    ],

    min_length=5,
    max_length=14,

    max_consonants_in_row=3,
    max_vowels_in_row=1,

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
        "рр": "р",
    },
)
