from dataclasses import dataclass


@dataclass
class Route:
    name: str
    waypoints: list[str] = []  # One list for every route: refused
