# real_time_monitoring.py - Real-Time Monitoring Module

import time

class RealTimeMonitoring:
    def __init__(self):
        self.monitored_parameters = {}

    def add_parameter(self, parameter_name, initial_value):
        """
        Add a parameter to the real-time monitoring.

        Parameters:
        - parameter_name (str): The name of the parameter to monitor.
        - initial_value (float): The initial value of the parameter.
        """
        self.monitored_parameters[parameter_name] = initial_value

    def update_parameter(self, parameter_name, new_value):
        """
        Update the value of a monitored parameter.

        Parameters:
        - parameter_name (str): The name of the parameter to update.
        - new_value (float): The new value of the parameter.
        """
        if parameter_name in self.monitored_parameters:
            self.monitored_parameters[parameter_name] = new_value
        else:
            print(f"Error: Parameter '{parameter_name}' not found in real-time monitoring.")

    def get_parameter_value(self, parameter_name):
        """
        Retrieve the current value of a monitored parameter.

        Parameters:
        - parameter_name (str): The name of the parameter to retrieve.

        Returns:
        - float: The current value of the parameter.
        """
        return self.monitored_parameters.get(parameter_name, None)

    def monitor_parameters(self, interval):
        """
        Start real-time monitoring of the parameters.

        Parameters:
        - interval (int): The time interval (in seconds) between each monitoring update.
        """
        while True:
            for parameter_name, parameter_value in self.monitored_parameters.items():
                print(f"{parameter_name}: {parameter_value}")
            print("------------------------")
            time.sleep(interval)

# Example usage:
if __name__ == "__main__":
    monitoring = RealTimeMonitoring()

    # Add parameters to monitor
    monitoring.add_parameter("Temperature", 25.5)
    monitoring.add_parameter("Pressure", 1001.2)

    # Start real-time monitoring with a 2-second interval
    monitoring.monitor_parameters(2)
