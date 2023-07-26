# extraterrestrial_resource_utilization.py - Extraterrestrial Resource Utilization Module

import time

class ExtraterrestrialResourceUtilization:
    def __init__(self, celestial_body):
        self.celestial_body = celestial_body
        self.is_mining_active = False

    def conduct_resource_survey(self):
        """Conduct a comprehensive survey of resources on the celestial body."""
        print(f"Conducting a resource survey on {self.celestial_body}...")
        time.sleep(3)
        print(f"Resource survey on {self.celestial_body} is complete.")

    def establish_resource_mineralogy_database(self):
        """Establish a mineralogy database of the resources found on the celestial body."""
        print("Establishing a mineralogy database for resource analysis...")
        time.sleep(2)
        print("Mineralogy database has been created.")

    def initiate_resource_extraction(self):
        """Initiate resource extraction operations on the celestial body."""
        if self.is_mining_active:
            print(f"Initiating resource extraction operations on {self.celestial_body}...")
            time.sleep(5)
            print(f"Resource extraction from {self.celestial_body} is ongoing.")
        else:
            print("Resource extraction is not currently active. Please activate mining operations.")

# Example usage:
if __name__ == "__main__":
    moon_resource_utilization = ExtraterrestrialResourceUtilization(celestial_body="Moon")
    moon_resource_utilization.conduct_resource_survey()
    moon_resource_utilization.establish_resource_mineralogy_database()

    # Activate mining operations on the Moon
    moon_resource_utilization.is_mining_active = True

    # Initiate resource extraction
    moon_resource_utilization.initiate_resource_extraction()
