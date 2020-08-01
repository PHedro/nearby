import unittest
from decimal import Decimal

from nearby.geolocation import GeoLocation


class GeoLocationTestCase(unittest.TestCase):
    def test_geo_location_initiallizes_with_strings_correctly(self):
        result = GeoLocation(
            latitude="52.986375",
            longitude="-6.043701",
        )

        self.assertEqual(float("52.986375"), result.latitude)
        self.assertEqual(float("-6.043701"), result.longitude)

    def test_geo_location_initiallizes_with_floats_correctly(self):
        result = GeoLocation(
            latitude=52.986375,
            longitude=-6.043701,
        )

        self.assertEqual(float("52.986375"), result.latitude)
        self.assertEqual(float("-6.043701"), result.longitude)

    def test_geo_location_initiallizes_with_floats_correctly_decimal(self):
        result = GeoLocation(
            latitude=Decimal(52.986375),
            longitude=Decimal(-6.043701),
        )

        self.assertEqual(float("52.986375"), result.latitude)
        self.assertEqual(float("-6.043701"), result.longitude)

    def test_geo_location_initiallizes_with_int_correctly(self):
        result = GeoLocation(
            latitude=52,
            longitude=-6,
        )

        self.assertEqual(52, result.latitude)
        self.assertEqual(-6, result.longitude)

    def test_geo_location_initiallizes_with_int_correctly_zeroes(self):
        result = GeoLocation(
            latitude=0,
            longitude=0,
        )

        self.assertEqual(0, result.latitude)
        self.assertEqual(0, result.longitude)

    def test_geo_location_initiallizes_with_int_correctly_zeroes_decimal(self):
        result = GeoLocation(
            latitude=Decimal(0),
            longitude=Decimal(0),
        )

        self.assertEqual(0, result.latitude)
        self.assertEqual(0, result.longitude)

    def test_geo_location_does_not_initiallizes_with_invalid_string_lat(self):
        with self.assertRaises(ValueError):
            GeoLocation(latitude="52A986375", longitude=-6,)

    def test_geo_location_does_not_initiallizes_with_invalid_string_long(self):
        with self.assertRaises(ValueError):
            GeoLocation(latitude=52, longitude="-6f",)

    def test_geo_location_does_not_initiallizes_with_invalid_string_both(self):
        with self.assertRaises(ValueError):
            GeoLocation(latitude="52A986375", longitude="-6f",)


if __name__ == "__main__":
    unittest.main()
