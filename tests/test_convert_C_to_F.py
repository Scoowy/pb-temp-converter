import pytest

from pb_temp_converter.converters import C_to_F


@pytest.mark.parametrize(
    "degreesC, degreesF",
    [
        (0, 32),
        (32, 89.6),
        (64, 147.2),
        (100, 212),
    ]
)
def test_convert_C_to_F(degreesC, degreesF):
    print(C_to_F(degreesC))
    assert pytest.approx(C_to_F(degreesC), 0.01) == degreesF
