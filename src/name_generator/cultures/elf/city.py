from name_generator.models.name_profile import NameProfile, WeightedValue

ELF_CITY = NameProfile(
    consonants=[
        WeightedValue("л", 25),
        WeightedValue("р", 20),
        WeightedValue("н", 20),
        WeightedValue("с", 15),
        WeightedValue("т", 10),
    ],

    vowels=[
        WeightedValue("а", 25),
        WeightedValue("э", 20),
        WeightedValue("и", 20),
        WeightedValue("о", 10),
    ],

    start_syllables=[
        WeightedValue("Эл", 20),
        WeightedValue("Лори", 15),
        WeightedValue("Аэ", 15),
        WeightedValue("Силь", 10),
        WeightedValue("Тала", 10),
        WeightedValue("Ил", 10),
    ],

    middle_syllables=[
        WeightedValue("ри", 15),
        WeightedValue("ари", 15),
        WeightedValue("ли", 15),
        WeightedValue("но", 10),
        WeightedValue("э", 10),
    ],

    end_syllables=[
        WeightedValue("ион", 20),
        WeightedValue("эль", 15),
        WeightedValue("ар", 15),
        WeightedValue("ор", 10),
        WeightedValue("илис", 10),
        WeightedValue("арион", 5),
    ],

    patterns=[
        WeightedValue("SME", 45),
        WeightedValue("SMME", 40),
        WeightedValue("SE", 15),
    ],

    min_length=5,
    max_length=18,
)
