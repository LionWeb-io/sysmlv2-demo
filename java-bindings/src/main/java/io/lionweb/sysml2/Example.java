package io.lionweb.sysml2;

/**
 * Example demonstrating SysML v2 modeling of an Electric Vehicle system.
 * Shows the use of parts, ports, attributes, requirements, and connections.
 */
public class Example {

    public static void main(String[] args) {
        Instantiator instantiator = new Instantiator();

        // Create main package for the electric vehicle system
        Package evPackage = instantiator.create(Package.class);
        evPackage.setName("ElectricVehicle");

        // Define the main vehicle part
        PartDefinition vehicleDef = instantiator.create(PartDefinition.class);
        vehicleDef.setName("Vehicle");
        evPackage.addToMember(vehicleDef);

        // Create battery subsystem
        PartUsage battery = instantiator.create(PartUsage.class);
        battery.setName("battery");
        vehicleDef.addToMember(battery);

        // Battery attributes
        AttributeUsage batteryCapacity = instantiator.create(AttributeUsage.class);
        batteryCapacity.setName("capacity");
        battery.addToMember(batteryCapacity);

        AttributeUsage batteryVoltage = instantiator.create(AttributeUsage.class);
        batteryVoltage.setName("voltage");
        battery.addToMember(batteryVoltage);

        // Create electric motor subsystem
        PartUsage motor = instantiator.create(PartUsage.class);
        motor.setName("electricMotor");
        vehicleDef.addToMember(motor);

        // Motor attributes
        AttributeUsage motorPower = instantiator.create(AttributeUsage.class);
        motorPower.setName("power");
        motor.addToMember(motorPower);

        AttributeUsage motorEfficiency = instantiator.create(AttributeUsage.class);
        motorEfficiency.setName("efficiency");
        motor.addToMember(motorEfficiency);

        // Create power port on battery
        PortUsage batteryPowerPort = instantiator.create(PortUsage.class);
        batteryPowerPort.setName("powerOutput");
        battery.addToMember(batteryPowerPort);

        // Create power port on motor
        PortUsage motorPowerPort = instantiator.create(PortUsage.class);
        motorPowerPort.setName("powerInput");
        motor.addToMember(motorPowerPort);

        // Create connection between battery and motor
        ConnectionUsage powerConnection = instantiator.create(ConnectionUsage.class);
        powerConnection.setName("powerFlow");
        vehicleDef.addToMember(powerConnection);

        // Add requirements
        RequirementUsage rangeRequirement = instantiator.create(RequirementUsage.class);
        rangeRequirement.setName("MinimumRange");
        rangeRequirement.setReqId("REQ-001");
        vehicleDef.addToMember(rangeRequirement);

        RequirementUsage performanceRequirement = instantiator.create(RequirementUsage.class);
        performanceRequirement.setName("AccelerationPerformance");
        performanceRequirement.setReqId("REQ-002");
        vehicleDef.addToMember(performanceRequirement);

        RequirementUsage efficiencyRequirement = instantiator.create(RequirementUsage.class);
        efficiencyRequirement.setName("EnergyEfficiency");
        efficiencyRequirement.setReqId("REQ-003");
        vehicleDef.addToMember(efficiencyRequirement);

        // Print summary
        System.out.println("Created Electric Vehicle System Model:");
        System.out.println("  Package: " + evPackage.getName());
        System.out.println("  Vehicle Definition: " + vehicleDef.getName());
        System.out.println("    - Parts: battery, electricMotor");
        System.out.println("    - Battery attributes: capacity, voltage");
        System.out.println("    - Motor attributes: power, efficiency");
        System.out.println("    - Ports: batteryPowerPort -> motorPowerPort");
        System.out.println("    - Connection: powerFlow");
        System.out.println("    - Requirements: 3 (range, performance, efficiency)");
    }
}
