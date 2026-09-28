from name_generator.models.name_profile import WeightedValue
from name_generator.name_profiles import RussianNameProfile

HUMAN_CITY = RussianNameProfile(
    consonants=[
        WeightedValue("б", 8),
        WeightedValue("в", 14),
        WeightedValue("д", 15),
        WeightedValue("к", 12),
        WeightedValue("л", 20),
        WeightedValue("м", 12),
        WeightedValue("н", 18),
        WeightedValue("р", 28),
        WeightedValue("с", 16),
        WeightedValue("т", 18),
        WeightedValue("г", 9),
        WeightedValue("п", 7),
        WeightedValue("з", 6),
    ],

    vowels=[
        WeightedValue("а", 30),
        WeightedValue("е", 20),
        WeightedValue("и", 15),
        WeightedValue("о", 27),
        WeightedValue("у", 8),
    ],

    onset_clusters=[
        WeightedValue("бр", 9),
        WeightedValue("др", 10),
        WeightedValue("кр", 10),
        WeightedValue("гр", 8),
        WeightedValue("ст", 10),
        WeightedValue("тр", 8),
        WeightedValue("пр", 7),
        WeightedValue("ск", 7),
        WeightedValue("кл", 5),
    ],

    coda_clusters=[
        WeightedValue("рд", 10),
        WeightedValue("рн", 8),
        WeightedValue("ст", 10),
        WeightedValue("нд", 8),
        WeightedValue("рт", 7),
        WeightedValue("ль", 6),
        WeightedValue("ск", 6),
    ],

    start_syllables=[
        WeightedValue("Ард", 10),
        WeightedValue("Бел", 12),
        WeightedValue("Вар", 14),
        WeightedValue("Дор", 14),
        WeightedValue("Кал", 11),
        WeightedValue("Лор", 13),
        WeightedValue("Мар", 12),
        WeightedValue("Рен", 10),
        WeightedValue("Стар", 7),
        WeightedValue("Тар", 10),
        WeightedValue("Вел", 12),

        WeightedValue("Бран", 9),
        WeightedValue("Гар", 9),
        WeightedValue("Крон", 7),
        WeightedValue("Нор", 10),
        WeightedValue("Ост", 7),
        WeightedValue("Рав", 8),
        WeightedValue("Бер", 9),
        WeightedValue("Дал", 8),
    ],

    middle_syllables=[
        WeightedValue("ен", 12),
        WeightedValue("ар", 12),
        WeightedValue("ор", 14),
        WeightedValue("ел", 10),
        WeightedValue("ин", 8),
        WeightedValue("да", 8),
        WeightedValue("ер", 10),

        WeightedValue("ов", 10),
        WeightedValue("ан", 9),
        WeightedValue("ев", 7),
        WeightedValue("ол", 7),
        WeightedValue("ра", 6),
        WeightedValue("бург", 3),
    ],

    end_syllables=[
        # Явно городские окончания
        WeightedValue("град", 10),
        WeightedValue("дор", 10),
        WeightedValue("форт", 5),
        WeightedValue("бург", 8),
        WeightedValue("ск", 8),
        WeightedValue("ово", 7),
        WeightedValue("ино", 6),

        # Нейтральные топонимические окончания
        WeightedValue("ар", 9),
        WeightedValue("ен", 10),
        WeightedValue("он", 10),
        WeightedValue("ель", 7),
        WeightedValue("ор", 10),
        WeightedValue("ин", 8),
        WeightedValue("ан", 7),
        WeightedValue("ов", 8),
    ],

    patterns=[
        WeightedValue("SE", 35),
        WeightedValue("SME", 45),
        WeightedValue("SMME", 12),

        # Полностью процедурные формы
        WeightedValue("CVCE", 5),
        WeightedValue("KVCE", 3),
    ],

    min_length=5,
    max_length=17,

    max_consonants_in_row=3,
    max_vowels_in_row=2,

    forbidden_combinations=[
        "ааа",
        "еее",
        "иии",
        "ооо",
        "ууу",
        "ррр",
        "ннн",
        "ллл",
        "ттт",
    ],

    replacement_rules={
        "аа": "а",
        "ее": "е",
        "ии": "и",
        "оо": "о",
        "уу": "у",
        "рр": "р",
        "ннн": "нн",
        "ллл": "лл",
        "ттт": "тт",
    },

    apostrophe_chance=0.0,
)
