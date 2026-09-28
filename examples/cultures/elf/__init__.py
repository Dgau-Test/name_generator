from cultures.elf.city import ELF_CITY
from cultures.elf.country import ELF_COUNTRY
from cultures.elf.name import ELF_FEMALE, ELF_MALE
from cultures.elf.surname import ELF_SURNAME
from cultures.models import Culture, Gender

__all__ = ('ELF',)


ELF = Culture(
    names=Gender(
        ELF_MALE, ELF_FEMALE
    ),

    surnames=ELF_SURNAME,

    cities=ELF_CITY,
    countries=ELF_COUNTRY,
)