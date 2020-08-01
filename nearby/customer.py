import json
import os
from decimal import Decimal

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
        return "Customer user_id: {}, name: {}, geolocation: {}".format(
            self.user_id, self.name, self.geolocation
        )

    @classmethod
    def from_file(cls, path):
        if os.path.exists(path) and os.path.isfile(path) and os.path.getsize(path) > 0:
            with open(path, "r") as data_file:
                for line in data_file:
                    yield cls(**json.loads(line))
        else:
            raise FileNotFoundError

    @classmethod
    def write_to_file(cls, data, path):
        with open(path, "w") as data_file:
            for customer in data:
                data_file.write("{}, {}\n".format(*customer))

    @classmethod
    def in_range_from(cls, origin, source_file_path, distance_km=100):
        customers = [
            (customer.user_id, customer.name)
            for customer in cls.from_file(source_file_path)
            if abs(origin.distance_to(customer.geolocation)) <= distance_km
        ]
        customers = sorted(customers, key=lambda customer: customer[0])

        return customers
