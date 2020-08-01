class GeoLocation:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __repr__(self):
        return "GeoLocation Lat: %r, Long: %r" % (self.latitude, self.longitude)

    def distance_to(self, other_geolocation):
        pass
