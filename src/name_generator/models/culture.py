from dataclasses import dataclass
from name_generator.models import NameProfile


@dataclass
class Culture:
    id: str
    name: str

    male_names: NameProfile
    female_names: NameProfile

    family_names: NameProfile

    city_names: NameProfile
    country_names: NameProfile

    dynasty_names: NameProfile | None = None
    clan_names: NameProfile | None = None