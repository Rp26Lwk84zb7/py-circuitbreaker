# Circuit breaker

```
circuit.py
```

I keep my own circuit breaker implementation in a single file. No dependencies, no framework, just the standard library. The clock is injected so I can test timeouts without sleeping.

The state machine is the usual three states: closed, open, half-open. When the failure threshold trips, it opens. After the reset timeout, it goes half-open and lets a single probe through. If that probe succeeds, it closes again. If it fails, it reopens.

Run the Python Circuitbreaker test next to the implementation for concrete examples. The tests are plain `unittest` style, so `python -m unittest test_circuitbreaker` works.

A minimal closed/open/half-open circuit breaker — clock injected, no deps.

Python Circuitbreaker uses only the python standard library; there is no service or dependency to install. That's the point. I'd rather spend my time shipping features than babysitting infrastructure.