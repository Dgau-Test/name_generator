from dataclasses import dataclass


@dataclass(frozen=True)
class WeightedValue:
    value: str
    weight: float = 1.0

    def __post_init__(self) -> None:
        if self.weight <= 0:
            raise ValueError('weight должен быть > 0')
