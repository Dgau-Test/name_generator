import pytest

from name_generator import CultureNameGenerator, NameGenerator
from name_generator.models import Culture, NameProfile


@pytest.fixture
def generator() -> NameGenerator:
    return NameGenerator()


@pytest.fixture
def make_profile():
    def _make_profile(**kwargs) -> NameProfile:
        defaults = {
            "min_length": 1,
            "max_length": 14,
            "max_consonants_in_row": 2,
            "max_vowels_in_row": 2,
            "apostrophe_chance": 0.0,
        }

        return NameProfile(**(defaults | kwargs))

    return _make_profile


@pytest.fixture
def culture_generator(culture: Culture) -> CultureNameGenerator:
    return CultureNameGenerator(culture)
