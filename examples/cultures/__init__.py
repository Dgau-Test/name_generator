"""Предоставляет lazy import к предопределённым культурам."""

from importlib import import_module
from typing import TYPE_CHECKING

from cultures.generator import CultureNameGenerator

if TYPE_CHECKING:
    from cultures.elf import ELF
    from cultures.human import HUMAN
    from cultures.orc import ORC


__all__ = ('ELF', 'ORC', 'HUMAN', 'CultureNameGenerator')

_LAZY_IMPORTS = {
    'ELF': 'cultures.elf',
    'ORC': 'cultures.orc',
    'HUMAN': 'cultures.human',
}


def __getattr__(name: str):
    """Лениво импортирует культуру при первом обращении к ней."""
    try:
        module_name = _LAZY_IMPORTS[name]
    except KeyError:
        raise AttributeError(
            f'module {__name__!r} has no attribute {name!r}'
        ) from None

    module = import_module(module_name)
    value = getattr(module, name)

    globals()[name] = value
    return value
