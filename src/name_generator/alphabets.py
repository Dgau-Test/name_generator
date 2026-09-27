from name_generator.models import Alphabet

RUSSIAN_ALPHABET = Alphabet(
    vowels=frozenset('аеёиоуыэюя'),
    consonants=frozenset('бвгджзйклмнпрстфхцчшщ'),
    modifiers=frozenset('ьъ')
)

ENGLISH_ALPHABET = Alphabet(
    vowels=frozenset("aeiouy"),
    consonants=frozenset("bcdfghjklmnpqrstvwxz")
)
