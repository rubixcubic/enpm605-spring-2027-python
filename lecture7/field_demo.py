"""field(default_factory=list) makes a new list for each object."""

from dataclasses import dataclass, field


@dataclass
class Route:
    name: str
    waypoints: list[str] = field(default_factory=list)


patrol = Route("patrol")
dock = Route("dock")
patrol.waypoints.append("A")
print(patrol, dock)
