import math


class GeoLocation:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.latitude_rad = math.radians(self.latitude)
        self.longitude_rad = math.radians(self.longitude)

    def __repr__(self):
        return "GeoLocation Lat: %r, Long: %r" % (self.latitude, self.longitude)

    def distance_to(self, other_geolocation):
        pass
