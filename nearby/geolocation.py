from math import radians, sin, cos, asin, sqrt


class GeoLocation:
    EARTH_RADIUS_KM = 6371
    EARTH_RADIUS_MILES = 3956

    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.latitude_rad = radians(self.latitude)
        self.longitude_rad = radians(self.longitude)

    def __repr__(self):
        return "GeoLocation Lat: %r, Long: %r" % (self.latitude, self.longitude)

    def distance_to(self, other, use_metric=True):
        sin_half_delta_lat = sin((other.latitude_rad - self.latitude_rad) / 2)
        sin_half_delta_long = sin((other.longitude_rad - self.longitude_rad) / 2)

        cos_self_lat = cos(self.latitude_rad)
        cos_other_lat = cos(other.latitude_rad)

        haversine = 2 * asin(
            sqrt(
                sin_half_delta_lat ** 2
                + cos_self_lat * cos_other_lat * sin_half_delta_long ** 2
            )
        )

        multiplier = self.EARTH_RADIUS_KM if use_metric else self.EARTH_RADIUS_MILES

        return haversine * multiplier
