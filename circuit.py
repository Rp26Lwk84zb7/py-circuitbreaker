"""Minimal circuit breaker. Standard library only; clock injectable."""


class CircuitBreaker:
    def __init__(self, threshold, cooldown, now):
        self.threshold, self.cooldown, self.now = threshold, cooldown, now
        self.failures, self.opened_at, self.state = 0, 0.0, "closed"

    def allow(self):
        if self.state == "open" and self.now() - self.opened_at >= self.cooldown:
            self.state = "half-open"
        return self.state != "open"

    def record(self, ok):
        if ok:
            self.failures, self.state = 0, "closed"
        else:
            self.failures += 1
            if self.failures >= self.threshold:
                self.state, self.opened_at = "open", self.now()
