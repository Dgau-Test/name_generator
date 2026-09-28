import pytest

from name_generator.models import WeightedValue


@pytest.mark.parametrize('weight', [0, -1, -0.5])
def test_weighted_value_rejects_non_positive_weight(weight: float) -> None:
    with pytest.raises(ValueError, match='weight должен быть > 0'):
        WeightedValue('эль', weight)
