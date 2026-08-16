# Circuit breaker

```
circuit.py
```
Look at the test file next to the implementation for concrete usage.

This gives you a basic closed, open, and half-open state machine. I injected the clock so you can test it without sleeping. Zero external dependencies.

I wrote this using only the Python standard library. When you run a solo shop, adding another pip package is just more attack surface and maintenance overhead. Keep it simple.