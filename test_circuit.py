from circuit import CircuitBreaker


def test_opens_and_recovers():
    clock = [0.0]
    cb = CircuitBreaker(2, 5, lambda: clock[0])
    cb.record(False); cb.record(False)
    assert not cb.allow()
    clock[0] = 5
    assert cb.allow()
