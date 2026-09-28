from dataclasses import dataclass

from name_generator.models import NameProfile


@dataclass
class Gender[T]:
    """Хранит значения, разделённые по полу."""

    male: T
    female: T


@dataclass
class Culture:
    """Описывает набор профилей генерации для одной культуры."""

    names: Gender[NameProfile]

    surnames: NameProfile

    cities: NameProfile
    countries: NameProfile
