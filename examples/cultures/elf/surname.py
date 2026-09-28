from name_generator.models.name_profile import WeightedValue
from name_generator.name_profiles import RussianNameProfile


ELF_SURNAME = RussianNameProfile(
    consonants=[
        WeightedValue("л", 25),
        WeightedValue("р", 20),
        WeightedValue("н", 15),
        WeightedValue("с", 10),
        WeightedValue("в", 10),
        WeightedValue("м", 7),
        WeightedValue("т", 6),
    ],

    vowels=[
        WeightedValue("а", 25),
        WeightedValue("э", 18),
        WeightedValue("и", 20),
        WeightedValue("о", 15),
        WeightedValue("е", 10),
    ],

    onset_clusters=[
        WeightedValue("сл", 10),
        WeightedValue("тр", 6),
        WeightedValue("вр", 5),
    ],

    coda_clusters=[
        WeightedValue("ль", 12),
        WeightedValue("рн", 8),
        WeightedValue("нт", 5),
    ],

    start_syllables=[
        WeightedValue("Лор", 18),
        WeightedValue("Эл", 14),
        WeightedValue("Силь", 14),
        WeightedValue("Ваэ", 10),
        WeightedValue("Тал", 10),

        WeightedValue("Аэр", 10),
        WeightedValue("Ил", 8),
        WeightedValue("Нэр", 7),
        WeightedValue("Саэл", 7),
        WeightedValue("Лаэр", 6),
        WeightedValue("Мир", 5),
    ],

    middle_syllables=[
        WeightedValue("ари", 14),
        WeightedValue("эли", 10),
        WeightedValue("ор", 12),
        WeightedValue("ин", 9),

        WeightedValue("ри", 12),
        WeightedValue("ил", 10),
        WeightedValue("ан", 8),
        WeightedValue("эль", 6),
        WeightedValue("ла", 7),
        WeightedValue("эр", 6),
    ],

    end_syllables=[
        # Более родовые / фамильные окончания
        WeightedValue("эль", 18),
        WeightedValue("иэль", 12),
        WeightedValue("ор", 10),
        WeightedValue("ис", 10),
        WeightedValue("ан", 8),
        WeightedValue("ин", 8),
        WeightedValue("ар", 7),
        WeightedValue("ир", 6),
        WeightedValue("ион", 5),

        WeightedValue("ари", 8),
        WeightedValue("элин", 7),
        WeightedValue("орин", 7),
        WeightedValue("аэль", 6),
    ],

    patterns=[
        WeightedValue("SE", 45),
        WeightedValue("SME", 45),
        WeightedValue("SMME", 5),

        # Небольшая доля менее предсказуемых фамилий
        WeightedValue("CVCVE", 3),
        WeightedValue("KVCE", 2),
    ],

    min_length=4,
    max_length=15,

    max_consonants_in_row=2,
    max_vowels_in_row=2,

    forbidden_combinations=[
        "ааа",
        "иии",
        "эээ",
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

    apostrophe_chance=0.01
)
