# biodegradable_satellites.py - Biodegradable Satellites Module

class BiodegradableSatellite:
    def __init__(self, satellite_id, lifespan):
        self.satellite_id = satellite_id
        self.lifespan = lifespan
        self.is_active = False

    def activate(self):
        """Activate the biodegradable satellite."""
        self.is_active = True

    def deactivate(self):
        """Deactivate the biodegradable satellite."""
        self.is_active = False

    def decompose(self):
        """Simulate the biodegradation of the satellite after its lifespan."""
        if self.is_active:
            print(f"Satellite {self.satellite_id} is still active. Decomposition postponed.")
        else:
            print(f"Satellite {self.satellite_id} is decomposing. Environmental impact being monitored.")
            # Placeholder for environmental impact monitoring (to be implemented)

# Example usage:
if __name__ == "__main__":
    satellite_1 = BiodegradableSatellite("TALON-1", lifespan=5)
    satellite_2 = BiodegradableSatellite("TALON-2", lifespan=7)

    satellite_1.activate()
    satellite_1.decompose()  # Decomposition postponed as it is still active
    satellite_1.deactivate()
    satellite_1.decompose()  # Satellite is decomposing

    satellite_2.decompose()  # Satellite is decomposing
