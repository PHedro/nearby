from nearby.geolocation import GeoLocation


class Customer:
    def __init__(self, user_id, name, latitude, longitude):
        self.user_id = user_id
        self.name = name
        self.geolocation = GeoLocation(
            latitude=float(latitude), longitude=float(longitude)
        )

    def __repr__(self):
        return "user_id: {}, name: {}".format(self.user_id, self.name)
