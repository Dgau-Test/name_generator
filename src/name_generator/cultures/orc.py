from name_generator.models.name_profile import NameProfile, WeightedValue


ORC = NameProfile(
    consonants=[
        WeightedValue("г", 25),
        WeightedValue("к", 25),
        WeightedValue("р", 30),
        WeightedValue("д", 15),
        WeightedValue("т", 15),
        WeightedValue("м", 8),
        WeightedValue("н", 8),
        WeightedValue("з", 5),
    ],

    vowels=[
        WeightedValue("а", 40),
        WeightedValue("о", 30),
        WeightedValue("у", 20),
        WeightedValue("ы", 5),
    ],

    onset_clusters=[
        WeightedValue("гр", 30),
        WeightedValue("кр", 25),
        WeightedValue("др", 15),
        WeightedValue("тр", 10),
        WeightedValue("згр", 3),
    ],

    coda_clusters=[
        WeightedValue("рг", 20),
        WeightedValue("рк", 20),
        WeightedValue("рт", 10),
        WeightedValue("нг", 8),
    ],

    start_syllables=[
        WeightedValue("Гар", 15),
        WeightedValue("Кра", 20),
        WeightedValue("Мор", 10),
        WeightedValue("Ур", 15),
        WeightedValue("Дра", 10),
    ],

    middle_syllables=[
        WeightedValue("га", 20),
        WeightedValue("ру", 15),
        WeightedValue("ка", 15),
        WeightedValue("дор", 8),
        WeightedValue("му", 5),
    ],

    end_syllables=[
        WeightedValue("ак", 25),
        WeightedValue("гар", 20),
        WeightedValue("ук", 20),
        WeightedValue("ор", 10),
        WeightedValue("г", 10),
    ],

    patterns=[
        WeightedValue("KVC", 30),
        WeightedValue("CVCD", 25),
        WeightedValue("SME", 20),
        WeightedValue("SE", 15),
        WeightedValue("CVC", 10),
    ],

    min_length=3,
    max_length=10,

    max_consonants_in_row=3,
    max_vowels_in_row=1,

    replacement_rules={
        "аа": "а",
        "оо": "о",
        "уу": "у",
    },

    apostrophe_chance=0.05,
)
