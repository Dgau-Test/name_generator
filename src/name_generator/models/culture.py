from dataclasses import dataclass
from name_generator.models.name_profile import NameProfile
from name_generator.models.gender import Gender


@dataclass
class Culture:
    names: Gender[NameProfile]

    surnames: NameProfile

    cities: NameProfile
    countries: NameProfile
