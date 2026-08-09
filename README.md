# Circuit breaker

A small circuit breaker with closed/open/half-open states. The clock is injected, so tests stay deterministic. No dependencies beyond the standard library.

```
circuit.py
```

Run the Python Circuitbreaker test next to the implementation for concrete examples. The whole thing is a single module, easy to drop into a project or copy-paste when you need a quick guard around flaky calls.

The trade-off here is deliberate. You could pull in a full resilience library, but for one service that's a dependency you don't control. This version keeps the logic visible and testable. If your needs grow past what this handles, swap it out then.