import os
import unittest

from nearby.customer import Customer
from nearby.geolocation import GeoLocation


class CustomerTestCase(unittest.TestCase):
    def test_customer_initiallize_correctly(self):
        result = Customer(
            user_id=12,
            name="Christina McArdle",
            latitude="52.986375",
            longitude="-6.043701",
        )
        expected_values = {
            "user_id": 12,
            "name": "Christina McArdle",
            "latitude": 52.986375,
            "longitude": -6.043701,
        }
        self.assertEqual(expected_values["user_id"], result.user_id)
        self.assertEqual(expected_values["name"], result.name)
        self.assertEqual(expected_values["latitude"], result.geolocation.latitude)
        self.assertEqual(expected_values["longitude"], result.geolocation.longitude)

    def test_customer_repr_correctly(self):
        result = repr(
            Customer(
                user_id=12,
                name="Christina McArdle",
                latitude="52.986375",
                longitude="-6.043701",
            )
        )
        expected = "Customer user_id: 12, name: Christina McArdle, geolocation: GeoLocation Lat: 52.986375, Long: -6.043701"
        self.assertEqual(expected, result)

    def test_customer_does_not_initiallize_missing_coordinates(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12, name="Christina McArdle",
            )

    def test_customer_does_not_initiallize_missing_coordinates_none(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12, name="Christina McArdle", latitude=None, longitude=None,
            )

    def test_customer_does_not_initiallize_missing_name(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12, latitude="52.986375", longitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_name_none(self):
        with self.assertRaises(TypeError):
            Customer(
                name=None, user_id=12, latitude="52.986375", longitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_user_id(self):
        with self.assertRaises(TypeError):
            Customer(
                name="Christina McArdle", latitude="52.986375", longitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_user_id_none(self):
        with self.assertRaises(TypeError):
            Customer(
                name="Christina McArdle",
                user_id=None,
                latitude="52.986375",
                longitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_latitude(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12, name="Christina McArdle", longitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_latitude_none(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12,
                name="Christina McArdle",
                latitude=None,
                longitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_longitude(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12, name="Christina McArdle", latitude="-6.043701",
            )

    def test_customer_does_not_initiallize_missing_longitude_none(self):
        with self.assertRaises(TypeError):
            Customer(
                user_id=12,
                name="Christina McArdle",
                latitude="-6.043701",
                longitude=None,
            )


class CustomersInRangeTestCase(unittest.TestCase):
    def setUp(self):
        self.origin = GeoLocation(latitude=52.986375, longitude=-6.043701)

    def test_return_correctly_range100(self):
        expected = [
            (4, "Ian Kehoe"),
            (5, "Nora Dempsey"),
            (6, "Theresa Enright"),
            (11, "Richard Finnegan"),
            (12, "Christina McArdle"),
            (13, "Olive Ahearn"),
            (15, "Michael Ahearn"),
            (31, "Alan Behan"),
            (39, "Lisa Ahearn"),
        ]
        result = Customer.in_range_from(
            origin=self.origin, source_file_path="data/customers.txt", distance_km=100
        )
        self.assertEqual(expected, result)

    def test_return_correctly_range30(self):
        expected = [
            (5, "Nora Dempsey"),
            (6, "Theresa Enright"),
            (11, "Richard Finnegan"),
            (12, "Christina McArdle"),
            (15, "Michael Ahearn"),
            (39, "Lisa Ahearn"),
        ]
        result = Customer.in_range_from(
            origin=self.origin, source_file_path="data/customers.txt", distance_km=30
        )
        self.assertEqual(expected, result)

    def test_return_correctly_range15(self):
        expected = [
            (11, "Richard Finnegan"),
            (12, "Christina McArdle"),
        ]
        result = Customer.in_range_from(
            origin=self.origin, source_file_path="data/customers.txt", distance_km=15
        )
        self.assertEqual(expected, result)

    def test_return_correctly_range150(self):
        expected = [
            (4, "Ian Kehoe"),
            (5, "Nora Dempsey"),
            (6, "Theresa Enright"),
            (8, "Eoin Ahearn"),
            (9, "Jack Dempsey"),
            (10, "Georgina Gallagher"),
            (11, "Richard Finnegan"),
            (12, "Christina McArdle"),
            (13, "Olive Ahearn"),
            (15, "Michael Ahearn"),
            (17, "Patricia Cahill"),
            (23, "Eoin Gallagher"),
            (24, "Rose Enright"),
            (26, "Stephen McArdle"),
            (28, "Charlie Halligan"),
            (29, "Oliver Ahearn"),
            (30, "Nick Enright"),
            (31, "Alan Behan"),
            (39, "Lisa Ahearn"),
        ]
        result = Customer.in_range_from(
            origin=self.origin, source_file_path="data/customers.txt", distance_km=150
        )
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
