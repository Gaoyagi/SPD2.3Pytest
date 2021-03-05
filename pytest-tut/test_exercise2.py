import math
import pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    if type(carbon_14_ratio) != float:
        raise TypeError
    if carbon_14_ratio <= 0: #can't have a negative or zero ratio of carbon
        return 0
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.

def test_get_age_carbon_14_dating():
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34, abs_tol=0.01)
    assert math.isclose(get_age_carbon_14_dating(0), 0, abs_tol=0.01)
    assert math.isclose(get_age_carbon_14_dating(-2), 0, abs_tol=0.01)
    with pytest.raises(TypeError):
            assert get_age_carbon_14_dating("A")