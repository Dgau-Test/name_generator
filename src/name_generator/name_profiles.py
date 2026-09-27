from dataclasses import dataclass

from name_generator.alphabets import ENGLISH_ALPHABET, RUSSIAN_ALPHABET
from name_generator.models import Alphabet, NameProfile


@dataclass
class RussianNameProfile(NameProfile):
    alphabet: Alphabet = RUSSIAN_ALPHABET


@dataclass
class EnglishNameProfile(NameProfile):
    alphabet: Alphabet = ENGLISH_ALPHABET
