"""Предопределённые алфавиты для генерации наименований."""

from name_generator.models import Alphabet

RUSSIAN_ALPHABET = Alphabet(
    vowels=frozenset('аеёиоуыэюя'),
    consonants=frozenset('бвгджзйклмнпрстфхцчшщ'),
    modifiers=frozenset('ьъ'),
)

# 'y' считается гласной, поскольку в генерируемых наименованиях
# она может выполнять роль гласного звука.
# При необходимости это поведение можно изменить
ENGLISH_ALPHABET = Alphabet(
    vowels=frozenset('aeiouy'), consonants=frozenset('bcdfghjklmnpqrstvwxz')
)
