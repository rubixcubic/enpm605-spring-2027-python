"""Business rules 3 and 4, enforced by the Robot class."""

from robotics_competition.robot import Robot

hauler = Robot("Hauler", 30)  # 30%: chosen for this example
for minutes in [5, 6, 3]:  # Task lengths, chosen for this example
    done = hauler.perform_task("carry crate", minutes)
    print(f"{minutes} min: done={done}, {hauler}")
hauler.recharge()
print(hauler, Robot.total_robots)
print(hauler.perform_task("long haul", 60), hauler)  # Needs 120%
