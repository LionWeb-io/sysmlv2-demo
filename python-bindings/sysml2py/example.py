from sysml2py.sysml.node_classes import Package, PartDefinition, PartUsage, AttributeUsage, PortUsage, ConnectionUsage, RequirementUsage

import inspect

class Instantiator:
    def __init__(self):
        self._id = 0

    def next_id(self) -> str:
        self._id += 1
        return f"id{self._id}"

    def create(self, clazz):
        sig = inspect.signature(clazz)  # for classes, this reflects __call__/__init__
        params = list(sig.parameters.values())

        # We want: callable(id) to be valid (one positional argument).
        try:
            sig.bind(self.next_id())
        except TypeError as e:
            raise RuntimeError(f"{clazz} cannot be called with a single 'id' argument: {sig}") from e

        try:
            return clazz(self.next_id())
        except Exception as e:
            raise RuntimeError(e) from e

if __name__ == '__main__':
    inst = Instantiator()

    # Create main package for the electric vehicle system
    ev_package = inst.create(Package)
    ev_package.name = "ElectricVehicleSystem"

    # Define the main vehicle part
    vehicle_def = inst.create(PartDefinition)
    vehicle_def.name = "Vehicle"
    ev_package.add_to_member(vehicle_def)

    # Create battery subsystem
    battery = inst.create(PartUsage)
    battery.name = "battery"
    vehicle_def.add_to_member(battery)

    # Battery attributes
    battery_capacity = inst.create(AttributeUsage)
    battery_capacity.name = "capacity"
    battery.add_to_member(battery_capacity)

    battery_voltage = inst.create(AttributeUsage)
    battery_voltage.name = "voltage"
    battery.add_to_member(battery_voltage)

    # Create electric motor subsystem
    motor = inst.create(PartUsage)
    motor.name = "electricMotor"
    vehicle_def.add_to_member(motor)

    # Motor attributes
    motor_power = inst.create(AttributeUsage)
    motor_power.name = "power"
    motor.add_to_member(motor_power)

    motor_efficiency = inst.create(AttributeUsage)
    motor_efficiency.name = "efficiency"
    motor.add_to_member(motor_efficiency)

    # Create power port on battery
    battery_power_port = inst.create(PortUsage)
    battery_power_port.name = "powerOutput"
    battery.add_to_member(battery_power_port)

    # Create power port on motor
    motor_power_port = inst.create(PortUsage)
    motor_power_port.name = "powerInput"
    motor.add_to_member(motor_power_port)

    # Create connection between battery and motor
    power_connection = inst.create(ConnectionUsage)
    power_connection.name = "powerFlow"
    vehicle_def.add_to_member(power_connection)

    # Add requirements
    range_requirement = inst.create(RequirementUsage)
    range_requirement.name = "MinimumRange"
    range_requirement.req_id = "REQ-001"
    vehicle_def.add_to_member(range_requirement)

    performance_requirement = inst.create(RequirementUsage)
    performance_requirement.name = "AccelerationPerformance"
    performance_requirement.req_id = "REQ-002"
    vehicle_def.add_to_member(performance_requirement)

    efficiency_requirement = inst.create(RequirementUsage)
    efficiency_requirement.name = "EnergyEfficiency"
    efficiency_requirement.req_id = "REQ-003"
    vehicle_def.add_to_member(efficiency_requirement)

    # Print summary
    print("Created Electric Vehicle System Model:")
    print("  Package: " + ev_package.name)
    print("  Vehicle Definition: " + vehicle_def.name)
    print("    - Parts: battery, electricMotor")
    print("    - Battery attributes: capacity, voltage")
    print("    - Motor attributes: power, efficiency")
    print("    - Ports: batteryPowerPort -> motorPowerPort")
    print("    - Connection: powerFlow")
    print("    - Requirements: 3 (range, performance, efficiency)")    