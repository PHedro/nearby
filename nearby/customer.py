from nearby.geolocation import GeoLocation


class Customer:
    def __init__(self, user_id, name, latitude, longitude):
        self._validate_params(latitude, longitude, name, user_id)

        self.user_id = user_id
        self.name = name
        self.geolocation = GeoLocation(
            latitude=float(latitude), longitude=float(longitude)
        )

    @staticmethod
    def _validate_params(latitude, longitude, name, user_id):
        all_fields_present = all(
            (
                user_id and isinstance(user_id, int),
                name and isinstance(name, str),
                Customer._valdidate_coordinate(latitude),
                Customer._valdidate_coordinate(longitude),
            )
        )
        if not all_fields_present:
            raise TypeError

    @staticmethod
    def _valdidate_coordinate(coordinate):
        return coordinate not in {None, ""} and isinstance(
            coordinate, (int, float, Decimal, str)
        )

    def __repr__(self):
        return "user_id: {}, name: {}".format(self.user_id, self.name)
