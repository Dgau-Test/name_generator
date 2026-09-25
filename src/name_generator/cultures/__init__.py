from importlib import import_module
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from name_generator.cultures.elf import ELF
    from name_generator.cultures.orc import ORC


__all__ = ('ELF', 'ORC')

_LAZY_IMPORTS = {
    'ELF': 'name_generator.culture.elf',
    'ORC': 'name_generator.culture.orc',
}


def __getattr__(name: str):
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
