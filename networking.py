# networking.py - Networking Module

class Networking:
    def __init__(self):
        self.connected_devices = []

    def connect_device(self, device_name):
        # Placeholder for connecting a device to the network
        if device_name not in self.connected_devices:
            self.connected_devices.append(device_name)
            print(f"{device_name} is now connected to the network.")
        else:
            print(f"{device_name} is already connected to the network.")

    def disconnect_device(self, device_name):
        # Placeholder for disconnecting a device from the network
        if device_name in self.connected_devices:
            self.connected_devices.remove(device_name)
            print(f"{device_name} has been disconnected from the network.")
        else:
            print(f"{device_name} is not connected to the network.")

    def list_connected_devices(self):
        # Placeholder for listing all connected devices
        if self.connected_devices:
            print("Connected Devices:")
            for device in self.connected_devices:
                print(f"- {device}")
        else:
            print("No devices are currently connected to the network.")

# Example usage:
if __name__ == "__main__":
    network = Networking()

    # Connect devices to the network
    network.connect_device("Device1")
    network.connect_device("Device2")
    network.connect_device("Device1")  # Device1 is already connected

    # List connected devices
    network.list_connected_devices()

    # Disconnect a device from the network
    network.disconnect_device("Device2")

    # List connected devices after disconnection
    network.list_connected_devices()
