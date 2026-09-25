from name_generator.models.name_profile import NameProfile, WeightedValue


ELF_SURNAME = NameProfile(
    consonants=[
        WeightedValue("л", 25),
        WeightedValue("р", 20),
        WeightedValue("н", 15),
        WeightedValue("с", 10),
        WeightedValue("в", 10),
    ],

    vowels=[
        WeightedValue("а", 25),
        WeightedValue("э", 20),
        WeightedValue("и", 20),
        WeightedValue("о", 15),
    ],

    start_syllables=[
        WeightedValue("Лор", 20),
        WeightedValue("Эл", 15),
        WeightedValue("Силь", 15),
        WeightedValue("Ваэ", 10),
        WeightedValue("Тал", 10),
    ],

    middle_syllables=[
        WeightedValue("ари", 15),
        WeightedValue("эли", 10),
        WeightedValue("ор", 15),
        WeightedValue("ин", 10),
    ],

    end_syllables=[
        WeightedValue("эль", 20),
        WeightedValue("ион", 15),
        WeightedValue("ир", 15),
        WeightedValue("ар", 15),
        WeightedValue("ис", 10),
    ],

    patterns=[
        WeightedValue("SE", 50),
        WeightedValue("SME", 50),
    ],

    min_length=4,
    max_length=14,
)
