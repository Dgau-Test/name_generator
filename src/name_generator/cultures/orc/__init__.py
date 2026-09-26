from name_generator.models import Culture, Gender
from name_generator.cultures.orc.city import ORC_CITY
from name_generator.cultures.orc.country import ORC_COUNTRY
from name_generator.cultures.orc.name import ORC_FEMALE, ORC_MALE
from name_generator.cultures.orc.surname import ORC_SURNAME


__all__ = ('ORC',)


ORC = Culture(
    names=Gender(
        ORC_MALE, ORC_FEMALE
    ),

    surnames=ORC_SURNAME,

    cities=ORC_CITY,
    countries=ORC_COUNTRY,
)