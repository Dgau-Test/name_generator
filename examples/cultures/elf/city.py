"""Профиль генерации названий для эльфийских городов."""

from name_generator.models import RussianNameProfile, WeightedValue

ELF_CITY = RussianNameProfile(
    consonants=[
        WeightedValue('л', 25),
        WeightedValue('р', 20),
        WeightedValue('н', 18),
        WeightedValue('с', 14),
        WeightedValue('т', 10),
        WeightedValue('м', 8),
        WeightedValue('в', 5),
    ],
    vowels=[
        WeightedValue('а', 25),
        WeightedValue('э', 18),
        WeightedValue('и', 22),
        WeightedValue('о', 12),
        WeightedValue('е', 10),
    ],
    onset_clusters=[
        WeightedValue('тр', 10),
        WeightedValue('ст', 8),
        WeightedValue('сл', 8),
    ],
    coda_clusters=[
        WeightedValue('ль', 15),
        WeightedValue('нт', 6),
        WeightedValue('рн', 5),
    ],
    start_syllables=[
        WeightedValue('Эл', 20),
        WeightedValue('Аэ', 16),
        WeightedValue('Ил', 14),
        WeightedValue('Ло', 12),
        WeightedValue('Лори', 8),
        WeightedValue('Силь', 10),
        WeightedValue('Тала', 8),
        WeightedValue('Эри', 8),
        WeightedValue('Нэ', 6),
        WeightedValue('Али', 6),
    ],
    middle_syllables=[
        WeightedValue('ри', 18),
        WeightedValue('ли', 18),
        WeightedValue('ра', 12),
        WeightedValue('на', 10),
        WeightedValue('но', 8),
        WeightedValue('э', 7),
        WeightedValue('ла', 10),
        WeightedValue('ми', 6),
        WeightedValue('си', 6),
    ],
    end_syllables=[
        WeightedValue('дор', 16),
        WeightedValue('тир', 14),
        WeightedValue('лон', 14),
        WeightedValue('рис', 12),
        WeightedValue('нор', 10),
        WeightedValue('эль', 10),
        WeightedValue('ар', 8),
        WeightedValue('ион', 6),
        WeightedValue('илис', 5),
        WeightedValue('тал', 5),
    ],
    patterns=[
        # Основной тип городских названий
        WeightedValue('SE', 35),
        # Более мелодичные и древние топонимы
        WeightedValue('SME', 45),
        # Длинные церемониальные названия встречаются редко
        WeightedValue('SMME', 15),
        # Немного полностью процедурных названий
        WeightedValue('KVE', 5),
    ],
    min_length=5,
    max_length=16,
    max_consonants_in_row=2,
    max_vowels_in_row=2,
    forbidden_combinations=[
        'ээ',
        'иии',
        'ааа',
        'ллл',
        'ррр',
        'ннн',
    ],
    replacement_rules={
        'ээ': 'э',
        'ии': 'и',
        'аа': 'а',
        'ллл': 'лл',
        'ррр': 'рр',
    },
    apostrophe_chance=0.005,
)
