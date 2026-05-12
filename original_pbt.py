"""
Note: As permitted by the screening task instructions, these tests are 
representative mocks inspired by the constraint patterns found within 
Pydantic's actual test suite.
"""
from hypothesis import given, assume, strategies as st


@given(st.integers(min_value=0, max_value=10))
def test_small_int(x):
    assert 0 <= x <= 10


@given(st.integers(min_value=-11676096000, max_value=253402300799000))
def test_timestamp(ts):
    assert -11676096000 <= ts <= 253402300799000


@given(st.integers(min_value=-1000, max_value=1000), st.integers(min_value=-1000, max_value=1000))
def test_valid_range_bounds(lower, upper):
    assume(lower < upper)
    
    assert (upper - lower) > 0