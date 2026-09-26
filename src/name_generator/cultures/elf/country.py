from name_generator.models.name_profile import NameProfile, WeightedValue

ELF_COUNTRY = NameProfile(
    consonants=[
        WeightedValue("л", 25),
        WeightedValue("р", 20),
        WeightedValue("н", 20),
        WeightedValue("с", 10),
        WeightedValue("т", 10),
    ],

    vowels=[
        WeightedValue("а", 30),
        WeightedValue("э", 15),
        WeightedValue("и", 20),
        WeightedValue("о", 15),
    ],

    start_syllables=[
        WeightedValue("Элла", 20),
        WeightedValue("Лори", 15),
        WeightedValue("Аэла", 15),
        WeightedValue("Сари", 10),
        WeightedValue("Тала", 10),
    ],

    middle_syllables=[
        WeightedValue("ри", 15),
        WeightedValue("ни", 15),
        WeightedValue("ли", 15),
        WeightedValue("ар", 10),
    ],

    end_syllables=[
        WeightedValue("он", 20),
        WeightedValue("ия", 20),
        WeightedValue("ар", 10),
        WeightedValue("эль", 10),
        WeightedValue("ион", 15),
    ],

    patterns=[
        WeightedValue("SME", 60),
        WeightedValue("SE", 30),
        WeightedValue("SMME", 10),
    ],

    min_length=5,
    max_length=16,
)
