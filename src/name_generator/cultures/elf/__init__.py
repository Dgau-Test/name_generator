from name_generator.models import Culture, Gender
from name_generator.cultures.elf.city import ELF_CITY
from name_generator.cultures.elf.country import ELF_COUNTRY
from name_generator.cultures.elf.name import ELF_FEMALE, ELF_MALE
from name_generator.cultures.elf.surname import ELF_SURNAME


__all__ = ('ELF',)


ELF = Culture(
    id="elf",
    title="Эльфы",

    names=Gender(
        ELF_MALE, ELF_FEMALE
    ),

    surnames=ELF_SURNAME,

    cities=ELF_CITY,
    countries=ELF_COUNTRY,
)