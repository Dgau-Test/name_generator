import pytest

from name_generator.models import WeightedValue


def test_weighted_choice_emty_list_raises_error(generator):
    with pytest.raises(ValueError, match='Список WeightedValue пуст'):
        generator.weighted_choice([])


@pytest.mark.parametrize(
    ('name', 'expected'),
    [
        ("авф", False),
        ("яччв", True),
        ("паропра", True),
        ("апрпар", True),
        ("неквпва", False),
        ("в'рп", False),
    ]
)
def test_valid_length(generator, make_profile, name, expected):
    profile = make_profile(
        min_length=4,
        max_length=6,
    )

    assert generator._valid_length(name, profile) is expected


@pytest.mark.parametrize(
    ('name', 'expected'),
    [
        ('бАра', True),
        ('лолу', True),
        ('бвГра', False),
        ('АпПпавп', False)
    ]
)
def test_valid_consonants(generator, make_profile, name, expected):
    profile = make_profile(
        max_consonants_in_row = 2
    )

    assert generator._valid_consonants(name, profile) is expected


def test_apply_replacements(generator, make_profile):
    profile = make_profile(
        replacement_rules = {
            'аа': 'а',
            'ии': 'и'
        }
    )
    name = generator._apply_replacements('Аазалиий', profile)

    assert name == 'Азалий'


@pytest.mark.parametrize(
    ('name', 'expected'),
    [
        ('бвунгд', True),
        ('арбвув', True),
        ('гзунф', True),
        ('афгзо', True),
        ('выавыа', False),
        ('гозбав', False)
    ]
)
def test_has_forbidden_combination(generator, make_profile, name, expected):
    profile = make_profile(
        forbidden_combinations = [
            'бв',
            'гз'
        ]
    )

    assert generator._has_forbidden_combination(name, profile) is expected


@pytest.mark.parametrize(
    ('name', 'random_value', 'expected'),
    [
        ('выфывф', 0.1, "вы'фывф"),
        ('выфывф', 0.9, 'выфывф'),
        ('вып', 0.1, 'вып')
    ],
)
def test_maybe_add_apostrophe(
    monkeypatch,
    make_profile,
    generator,
    name,
    random_value,
    expected,
):
    profile = make_profile(
        apostrophe_chance = 0.5
    )

    monkeypatch.setattr('random.random', lambda: random_value)
    monkeypatch.setattr('random.randint', lambda a, b: 2)

    result = generator._maybe_add_apostrophe(name, profile)

    assert result == expected


def test_generate(make_profile, generator) -> None:
    profile = make_profile(
        patterns=[
            WeightedValue("SVE"),
        ],
        start_syllables=[
            WeightedValue("эл"),
        ],
        vowels=[
            WeightedValue("а"),
        ],
        end_syllables=[
            WeightedValue("рион"),
        ],
        min_length=1,
        max_length=20,
        apostrophe_chance=0,
    )

    assert 'Эларион' == generator.generate(profile)


def test_generate_raises_error_when_generation_fails(
    monkeypatch,
    generator,
    make_profile
) -> None:
    profile = make_profile(
        patterns=[
            WeightedValue("S"),
        ],
        start_syllables=[
            WeightedValue("эль"),
        ],
        min_length=1,
        max_length=20,
        apostrophe_chance=0,
    )

    monkeypatch.setattr(
        generator,
        "_valid",
        lambda name, profile: False,
    )

    with pytest.raises(
        RuntimeError,
        match="Не удалось сгенерировать имя",
    ):
        generator.generate(profile)
