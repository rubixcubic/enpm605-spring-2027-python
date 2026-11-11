"""Callbacks: functions that other code calls when something happens."""

from collections.abc import Callable
from functools import partial

subscribers: dict[str, list[Callable]] = {}  # Topic -> callbacks


def subscribe(topic: str, callback: Callable) -> None:
    """Call callback(msg) for each message published on topic."""
    if topic not in subscribers:
        subscribers[topic] = []
    subscribers[topic].append(callback)


def publish(topic: str, msg) -> None:
    """Call every callback subscribed to topic, in order."""
    for callback in subscribers.get(topic, []):
        callback(msg)


def on_scan(ranges_m: list[float]) -> None:
    print(f"on_scan: nearest {min(ranges_m)} m")


def on_battery(pct: int) -> None:
    print(f"on_battery: {pct}%")


subscribe("/scan", on_scan)
subscribe("/battery", on_battery)
publish("/scan", [2.5, 0.9, 3.1])
publish("/battery", 87)  # 87%: chosen for this example
publish("/scan", [0.4, 1.2])
publish("/odom", (1.0, 2.0))  # No subscriber: nothing happens


# A timer calls its callback once per period (simulated time)
def run_timer(period_s: float, callback: Callable, ticks: int) -> None:
    for k in range(1, ticks + 1):
        callback(k * period_s)


def on_tick(t: float) -> None:
    print(f"tick at t = {t:.1f} s")


run_timer(0.5, on_tick, 3)  # 0.5 s and 3 ticks: chosen


# A callback that needs more than the message
def log_scan(robot: str, ranges_m: list[float]) -> None:
    print(f"{robot}: {len(ranges_m)} readings")


subscribe("/scan", partial(log_scan, "waffle_01"))
subscribe("/scan", lambda msg: log_scan("burger_02", msg))
publish("/scan", [1.5, 2.0])
