from name_generator.models import Culture, Gender
from name_generator.cultures.human.city import HUMAN_CITY
from name_generator.cultures.human.country import HUMAN_COUNTRY
from name_generator.cultures.human.name import HUMAN_FEMALE, HUMAN_MALE
from name_generator.cultures.human.surname import HUMAN_SURNAME


__all__ = ('HUMAN',)


HUMAN = Culture(
    id="HUMAN",
    title="Люди",

    names=Gender(
        HUMAN_MALE, HUMAN_FEMALE
    ),

    surnames=HUMAN_SURNAME,

    cities=HUMAN_CITY,
    countries=HUMAN_COUNTRY,
)
