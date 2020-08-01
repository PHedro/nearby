from decimal import Decimal

from nearby.file_handler import from_file
from nearby.geolocation import GeoLocation


class Customer:
    def __init__(self, user_id, name, latitude, longitude):
        self._validate_params(latitude, longitude, name, user_id)

        self.user_id = user_id
        self.name = name
        self.geolocation = GeoLocation(
            latitude=float(latitude), longitude=float(longitude)
        )

    def __repr__(self):
        return "Customer user_id: {}, name: {}, geolocation: {}".format(
            self.user_id, self.name, self.geolocation
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

    @classmethod
    def in_range_from(cls, origin, source_file_path, distance_km=100):
        customers = [
            (customer.user_id, customer.name)
            for customer in from_file(path=source_file_path, class_to_cast=cls)
            if abs(origin.distance_to(customer.geolocation)) <= distance_km
        ]
        customers = sorted(customers, key=lambda customer: customer[0])

        return customers
