import pytest

from pb_temp_converter.converters import F_to_K


@pytest.mark.parametrize(
    "degreesF, degreesK",
    [
        (0, 255.372),
        (32, 273.15),
        (64, 290.928),
        (100, 310.928),
    ]
)
def test_convert_F_to_K(degreesF, degreesK):
    print(F_to_K(degreesF))
    assert pytest.approx(F_to_K(degreesF), 0.01) == degreesK
