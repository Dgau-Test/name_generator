from dataclasses import dataclass


@dataclass(frozen=True)
class WeightedValue:
    """Хранит значение и его вес для взвешенного случайного выбора."""

    value: str
    weight: float = 1.0

    def __post_init__(self) -> None:
        if self.weight <= 0:
            raise ValueError('weight должен быть > 0')
