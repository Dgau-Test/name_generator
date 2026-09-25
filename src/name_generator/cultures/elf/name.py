from name_generator.models.name_profile import NameProfile, WeightedValue


ELF_MALE = NameProfile(
    consonants=[
        WeightedValue("л", 30),
        WeightedValue("р", 25),
        WeightedValue("н", 20),
        WeightedValue("с", 10),
        WeightedValue("в", 5),
        WeightedValue("м", 5),
    ],

    vowels=[
        WeightedValue("а", 20),
        WeightedValue("э", 20),
        WeightedValue("и", 25),
        WeightedValue("е", 15),
        WeightedValue("о", 5),
    ],

    start_syllables=[
        WeightedValue("Эл", 25),
        WeightedValue("Ли", 20),
        WeightedValue("Аэ", 12),
        WeightedValue("Ил", 15),
        WeightedValue("Та", 10),
        WeightedValue("Са", 10),
    ],

    middle_syllables=[
        WeightedValue("ри", 20),
        WeightedValue("ли", 20),
        WeightedValue("ра", 15),
        WeightedValue("ни", 10),
        WeightedValue("э", 5),
    ],

    end_syllables=[
        WeightedValue("ион", 25),
        WeightedValue("ир", 25),
        WeightedValue("ор", 10),
        WeightedValue("ан", 20),
        WeightedValue("ис", 10),
    ],

    patterns=[
        WeightedValue("SME", 50),
        WeightedValue("SE", 30),
        WeightedValue("SMME", 10),
    ],

    min_length=4,
    max_length=12,

    replacement_rules={
        "ии": "и",
        "ээ": "э",
        "аа": "а",
    }
)

ELF_FEMALE = NameProfile(
    consonants=[
        WeightedValue("л", 30),
        WeightedValue("р", 20),
        WeightedValue("н", 25),
        WeightedValue("с", 15),
        WeightedValue("в", 5),
        WeightedValue("м", 10),
    ],

    vowels=[
        WeightedValue("а", 30),
        WeightedValue("э", 20),
        WeightedValue("и", 25),
        WeightedValue("е", 15),
    ],

    start_syllables=[
        WeightedValue("Эл", 20),
        WeightedValue("Ли", 25),
        WeightedValue("Аэ", 20),
        WeightedValue("Ил", 10),
        WeightedValue("Са", 15),
    ],

    middle_syllables=[
        WeightedValue("ри", 15),
        WeightedValue("ли", 25),
        WeightedValue("на", 20),
        WeightedValue("ра", 15),
        WeightedValue("э", 10),
    ],

    end_syllables=[
        WeightedValue("иэль", 20),
        WeightedValue("ара", 20),
        WeightedValue("ина", 20),
        WeightedValue("эль", 15),
        WeightedValue("ира", 20),
    ],

    patterns=[
        WeightedValue("SME", 60),
        WeightedValue("SE", 25),
        WeightedValue("SMME", 15),
    ],

    min_length=4,
    max_length=13,

    replacement_rules={
        "ии": "и",
        "ээ": "э",
        "аа": "а",
    }
)
