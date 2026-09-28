from collections.abc import Callable

import pytest

from name_generator import NameGenerator
from name_generator.models import NameProfile
from name_generator.name_profiles import RussianNameProfile

ProfileFactory = Callable[..., NameProfile]


@pytest.fixture
def generator() -> NameGenerator:
    return NameGenerator()


@pytest.fixture
def make_profile() -> ProfileFactory:
    def _make_profile(**kwargs) -> NameProfile:
        defaults = {
            "min_length": 1,
            "max_length": 14,
            "max_consonants_in_row": 2,
            "max_vowels_in_row": 2,
            "apostrophe_chance": 0.0,
        }

        return RussianNameProfile(**(defaults | kwargs))

    return _make_profile
