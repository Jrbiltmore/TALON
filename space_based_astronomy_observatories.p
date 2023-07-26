# space_based_astronomy_observatories.py - Space-Based Astronomy and Observatories Module

import time

class SpaceBasedObservatory:
    def __init__(self, name, observatory_type, location):
        self.name = name
        self.observatory_type = observatory_type
        self.location = location
        self.is_active = False

    def deploy_observatory(self):
        """Deploy the space-based observatory in its designated location."""
        print(f"Deploying {self.name}, the {self.observatory_type}, to {self.location}...")
        time.sleep(3)
        print(f"{self.name} is now operational in space.")

    def calibrate_instruments(self):
        """Calibrate the scientific instruments of the observatory."""
        print(f"Calibrating the instruments of {self.name}...")
        time.sleep(2)
        print(f"{self.name} instruments have been calibrated.")

    def observe_celestial_objects(self, target):
        """Conduct observations of celestial objects using the observatory's instruments."""
        print(f"{self.name} is observing {target}...")
        time.sleep(5)
        print(f"{self.name} has completed observations of {target}.")

# Example usage:
if __name__ == "__main__":
    hubble_space_telescope = SpaceBasedObservatory(name="Hubble Space Telescope", observatory_type="Space Telescope", location="Low Earth Orbit")
    hubble_space_telescope.deploy_observatory()

    # Calibrate instruments before observations
    hubble_space_telescope.calibrate_instruments()

    # Conduct observations of celestial objects
    hubble_space_telescope.observe_celestial_objects(target="Andromeda Galaxy")
    hubble_space_telescope.observe_celestial_objects(target="Jupiter")

    hubble_space_telescope.is_active = True

    # Perform additional observations
    if hubble_space_telescope.is_active:
        hubble_space_telescope.observe_celestial_objects(target="Crab Nebula")
        hubble_space_telescope.observe_celestial_objects(target="Orion Nebula")
