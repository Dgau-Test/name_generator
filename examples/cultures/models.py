from dataclasses import dataclass
from name_generator.models import NameProfile

@dataclass
class Gender[T]:
    male: T
    female: T


@dataclass
class Culture:
    names: Gender[NameProfile]

    surnames: NameProfile

    cities: NameProfile
    countries: NameProfile

