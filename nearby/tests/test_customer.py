import unittest

from nearby.customer import Customer


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


if __name__ == "__main__":
    unittest.main()
