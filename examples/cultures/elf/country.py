from name_generator.models import WeightedValue
from name_generator.name_profiles import RussianNameProfile

ELF_COUNTRY = RussianNameProfile(
    consonants=[
        WeightedValue("л", 25),
        WeightedValue("р", 20),
        WeightedValue("н", 20),
        WeightedValue("с", 10),
        WeightedValue("т", 10),
        WeightedValue("м", 8),
        WeightedValue("в", 5),
    ],

    vowels=[
        WeightedValue("а", 30),
        WeightedValue("э", 15),
        WeightedValue("и", 20),
        WeightedValue("о", 15),
        WeightedValue("е", 10),
    ],

    onset_clusters=[
        WeightedValue("тр", 8),
        WeightedValue("сл", 8),
        WeightedValue("ст", 6),
    ],

    coda_clusters=[
        WeightedValue("ль", 12),
        WeightedValue("рн", 6),
        WeightedValue("нт", 4),
    ],

    start_syllables=[
        WeightedValue("Элла", 18),
        WeightedValue("Лори", 14),
        WeightedValue("Аэла", 16),
        WeightedValue("Сари", 10),
        WeightedValue("Тала", 10),
        WeightedValue("Илла", 10),
        WeightedValue("Эри", 8),
        WeightedValue("Лаэ", 7),
        WeightedValue("Нэри", 7),
    ],

    middle_syllables=[
        WeightedValue("ри", 16),
        WeightedValue("ни", 14),
        WeightedValue("ли", 16),
        WeightedValue("ар", 8),
        WeightedValue("ла", 12),
        WeightedValue("ра", 10),
        WeightedValue("эль", 5),
        WeightedValue("но", 5),
    ],

    end_syllables=[
        WeightedValue("ия", 24),
        WeightedValue("ион", 18),
        WeightedValue("эль", 14),
        WeightedValue("ор", 10),
        WeightedValue("ар", 8),
        WeightedValue("он", 8),
        WeightedValue("иэль", 6),
        WeightedValue("ари", 5),
    ],

    patterns=[
        WeightedValue("SME", 50),
        WeightedValue("SE", 35),
        WeightedValue("SMME", 10),
        WeightedValue("SMME", 5),
    ],

    min_length=6,
    max_length=18,

    max_consonants_in_row=2,
    max_vowels_in_row=2,

    forbidden_combinations=[
        "ааа",
        "иии",
        "ээ",
        "ллл",
        "ррр",
        "ннн",
    ],

    replacement_rules={
        "аа": "а",
        "ии": "и",
        "ээ": "э",
        "ллл": "лл",
        "ррр": "рр",
        "ннн": "нн",
    },

    apostrophe_chance=0.003,
)
