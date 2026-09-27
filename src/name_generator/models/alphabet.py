from dataclasses import dataclass, field


@dataclass(frozen=True)
class Alphabet:
    vowels: frozenset[str]
    consonants: frozenset[str]

    # Буквенные символы, которые не являются
    # ни гласными, ни согласными
    modifiers: frozenset[str] = field(
        default_factory=frozenset
    )