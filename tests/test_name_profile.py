import pytest
from conftest import ProfileFactory

from name_generator.models import WeightedValue


@pytest.mark.parametrize(
    ('symbol', 'attribute'),
    [
        ('C', 'consonants'),
        ('V', 'vowels'),
        ('K', 'onset_clusters'),
        ('D', 'coda_clusters'),
        ('S', 'start_syllables'),
        ('M', 'middle_syllables'),
        ('E', 'end_syllables'),
    ],
)
def test_get_part(
    symbol: str,
    attribute: str,
    make_profile: ProfileFactory
) -> None:
    profile = make_profile()

    assert profile.get_part(symbol) is getattr(profile, attribute)


def test_get_part_unknown_symbol_raises(make_profile: ProfileFactory) -> None:
    profile = make_profile()

    with pytest.raises(
        ValueError,
        match='Неизвестный символ шаблона',
    ):
        profile.get_part('X')


@pytest.mark.parametrize(
    ('kwargs', 'message'),
    [
        (
            {'min_length': 0},
            'min_length должен быть >= 1',
        ),
        (
            {'min_length': 5, 'max_length': 4},
            'max_length не может быть меньше min_length',
        ),
        (
            {'max_consonants_in_row': 0},
            'max_consonants_in_row должен быть >= 1',
        ),
        (
            {'max_vowels_in_row': 0},
            'max_vowels_in_row должен быть >= 1',
        ),
        (
            {'apostrophe_chance': -0.1},
            r'apostrophe_chance должен находиться в диапазоне \[0, 1\]',
        ),
        (
            {'apostrophe_chance': 1.1},
            r'apostrophe_chance должен находиться в диапазоне \[0, 1\]',
        ),
    ],
)
def test_invalid_limits_raise(
    make_profile: ProfileFactory,
    kwargs: dict,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        make_profile(
            **kwargs,
        )


@pytest.mark.parametrize("chance", [0.0, 1.0])
def test_apostrophe_chance_boundaries_are_valid(
    make_profile: ProfileFactory,
    chance: float,
) -> None:
    profile = make_profile(apostrophe_chance=chance)

    assert profile.apostrophe_chance == chance


def test_accepts_valid_vowels(make_profile: ProfileFactory) -> None:
    profile = make_profile(
        vowels=[
            WeightedValue("а"),
            WeightedValue("ае"),
        ],
    )

    assert len(profile.vowels) == 2


def test_rejects_non_vowel_in_vowels(make_profile: ProfileFactory) -> None:
    with pytest.raises(
        ValueError,
        match="содержит негласные символы",
    ):
        make_profile(
            vowels=[
                WeightedValue("аб"),
            ],
        )


def test_vowels_validation_is_case_insensitive(
    make_profile: ProfileFactory
) -> None:
    profile = make_profile(
        vowels=[
            WeightedValue("АЕ"),
        ],
    )

    assert profile.vowels


def test_accepts_valid_consonants(make_profile: ProfileFactory) -> None:
    profile = make_profile(
        consonants=[
            WeightedValue("к"),
            WeightedValue("р"),
        ],
    )

    assert len(profile.consonants) == 2


def test_rejects_vowel_in_consonants(make_profile: ProfileFactory) -> None:
    with pytest.raises(
        ValueError,
        match="содержит несогласные символы",
    ):
        make_profile(
            consonants=[
                WeightedValue("ка"),
            ],
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "onset_clusters",
        "coda_clusters",
    ],
)
def test_accepts_valid_consonant_clusters(
    make_profile: ProfileFactory,
    field_name: str,
) -> None:
    profile = make_profile(
        **{
            field_name: [
                WeightedValue("кр"),
            ],
        },
    )

    assert getattr(profile, field_name)


@pytest.mark.parametrize(
    "field_name",
    [
        "onset_clusters",
        "coda_clusters",
    ],
)
def test_rejects_cluster_containing_vowel(
    make_profile: ProfileFactory,
    field_name: str,
) -> None:
    with pytest.raises(
        ValueError,
        match='содержит недопустимый символ',
    ):
        make_profile(
            **{
                field_name: [
                    WeightedValue("ка"),
                ],
            },
        )


def test_modifier_is_not_treated_as_consonant(
    make_profile: ProfileFactory,
) -> None:
    with pytest.raises(
        ValueError,
        match="должен содержать хотя бы одну согласную",
    ):
        make_profile(
            coda_clusters=[
                WeightedValue("ь"),
            ],
        )


def test_accepts_valid_pattern(make_profile: ProfileFactory) -> None:
    profile = make_profile(
        consonants=[
            WeightedValue("к"),
        ],
        vowels=[
            WeightedValue("а"),
        ],
        patterns=[
            WeightedValue("CVC"),
        ],
    )

    assert profile.patterns


def test_rejects_unknown_pattern_symbol(
    make_profile: ProfileFactory
) -> None:
    with pytest.raises(
        ValueError,
        match="Неизвестный символ 'X'",
    ):
        make_profile(
            consonants=[
                WeightedValue("к"),
            ],
            vowels=[
                WeightedValue("а"),
            ],
            patterns=[
                WeightedValue("CVX"),
            ],
        )


def test_rejects_pattern_using_empty_part(
    make_profile: ProfileFactory
) -> None:
    with pytest.raises(
        ValueError,
        match="'vowels' не может быть пустым",
    ):
        make_profile(
            consonants=[
                WeightedValue("к"),
            ],
            patterns=[
                WeightedValue("CV"),
            ],
        )
