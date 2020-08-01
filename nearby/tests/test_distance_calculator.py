import unittest

from nearby.geolocation import GeoLocation


class DistanceCalculatorTestCase(unittest.TestCase):
    def test_distance_in_km_correctly_2886_444442837984(self):
        destination = GeoLocation(latitude=36.12, longitude=-86.67)
        origin = GeoLocation(latitude=33.94, longitude=-118.40)
        expected = 2886.444442837984

        result = origin.distance_to(destination)
        self.assertEqual(expected, result)

    def test_distance_in_miles_correctly_1792_3048525925387(self):
        destination = GeoLocation(latitude=36.12, longitude=-86.67)
        origin = GeoLocation(latitude=33.94, longitude=-118.40)
        expected = 1792.3048525925387

        result = origin.distance_to(destination, use_metric=False)
        self.assertEqual(expected, result)

    def test_distance_in_km_correctly_41_768725500836176(self):
        destination = GeoLocation(latitude=53.339428, longitude=-6.257664)
        origin = GeoLocation(latitude=52.986375, longitude=-6.043701)
        expected = 41.768725500836176

        result = origin.distance_to(destination)
        self.assertEqual(expected, result)

    def test_distance_in_km_correctly_264_6531541515143(self):
        destination = GeoLocation(latitude=55.033, longitude=-8.112)
        origin = GeoLocation(latitude=52.986375, longitude=-6.043701)
        expected = 264.6531541515143

        result = origin.distance_to(destination)
        self.assertEqual(expected, result)

    def test_distance_in_km_correctly_223_6349651641532(self):
        destination = GeoLocation(latitude=55.033, longitude=-8.112)
        origin = GeoLocation(latitude=53.339428, longitude=-6.257664)
        expected = 223.6349651641532

        result = origin.distance_to(destination)
        self.assertEqual(expected, result)

    def test_distance_in_km_correctly_278_4581750754194(self):
        destination = GeoLocation(latitude=52.2296756, longitude=21.0122287)
        origin = GeoLocation(latitude=52.406374, longitude=16.9251681)
        expected = 278.4581750754194

        result = origin.distance_to(destination)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
