"""Содержит предопределённую культуру людей."""

from cultures.human.city import HUMAN_CITY
from cultures.human.country import HUMAN_COUNTRY
from cultures.human.name import HUMAN_FEMALE, HUMAN_MALE
from cultures.human.surname import HUMAN_SURNAME
from cultures.models import Culture, Gender

__all__ = ('HUMAN',)


HUMAN = Culture(
    names=Gender(HUMAN_MALE, HUMAN_FEMALE),
    surnames=HUMAN_SURNAME,
    cities=HUMAN_CITY,
    countries=HUMAN_COUNTRY,
)
