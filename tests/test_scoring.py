from verix.detection.scoring import risk_level
def test_levels():
    assert risk_level(0, 0) == 0
    assert risk_level(1, 1) == 1
    assert risk_level(2, 1) == 2
    assert risk_level(3, 1) == 3
