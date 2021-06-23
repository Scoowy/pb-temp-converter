import pytest

from pb_temp_converter.converters import C_to_R


@pytest.mark.parametrize(
    "degreesC, degreesR",
    [
        (0, 491.67),
        (32, 549.27),
        (64, 606.87),
        (100, 671.67),
    ]
)
def test_convert_C_to_R(degreesC, degreesR):
    print(C_to_R(degreesC))
    assert pytest.approx(C_to_R(degreesC), 0.01) == degreesR
