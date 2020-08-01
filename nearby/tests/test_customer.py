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


class CustomerFromFileTestCase(unittest.TestCase):
    def test_loads_correctly_from_base_file(self):
        result = list(Customer.from_file("data/customers.txt"))
        expected = [
            (12, "Christina McArdle", 52.986375, -6.043701),
            (1, "Alice Cahill", 51.92893, -10.27699),
            (2, "Ian McArdle", 51.8856167, -10.4240951),
            (3, "Jack Enright", 52.3191841, -8.5072391),
            (28, "Charlie Halligan", 53.807778, -7.714444),
            (7, "Frank Kehoe", 53.4692815, -9.436036),
            (8, "Eoin Ahearn", 54.0894797, -6.18671),
            (26, "Stephen McArdle", 53.038056, -7.653889),
            (27, "Enid Gallagher", 54.1225, -8.143333),
            (6, "Theresa Enright", 53.1229599, -6.2705202),
            (9, "Jack Dempsey", 52.2559432, -7.1048927),
            (10, "Georgina Gallagher", 52.240382, -6.972413),
            (4, "Ian Kehoe", 53.2451022, -6.238335),
            (5, "Nora Dempsey", 53.1302756, -6.2397222),
            (11, "Richard Finnegan", 53.008769, -6.1056711),
            (31, "Alan Behan", 53.1489345, -6.8422408),
            (13, "Olive Ahearn", 53.0, -7.0),
            (14, "Helen Cahill", 51.999447, -9.742744),
            (15, "Michael Ahearn", 52.966, -6.463),
            (16, "Ian Larkin", 52.366037, -8.179118),
            (17, "Patricia Cahill", 54.180238, -5.920898),
            (39, "Lisa Ahearn", 53.0033946, -6.3877505),
            (18, "Bob Larkin", 52.228056, -7.915833),
            (24, "Rose Enright", 54.133333, -6.433333),
            (19, "Enid Cahill", 55.033, -8.112),
            (20, "Enid Enright", 53.521111, -9.831111),
            (21, "David Ahearn", 51.802, -9.442),
            (22, "Charlie McArdle", 54.374208, -8.371639),
            (29, "Oliver Ahearn", 53.74452, -7.11167),
            (30, "Nick Enright", 53.761389, -7.2875),
            (23, "Eoin Gallagher", 54.080556, -6.361944),
            (25, "David Behan", 52.833502, -8.522366),
        ]

        for _index, _result in enumerate(result):
            self.assertEqual(_result.user_id, expected[_index][0])
            self.assertEqual(_result.name, expected[_index][1])
            self.assertEqual(_result.geolocation.latitude, expected[_index][2])
            self.assertEqual(_result.geolocation.longitude, expected[_index][3])

    def test_loads_correctly_from_short_file(self):
        result = list(Customer.from_file("data/customers_short.txt"))
        expected = [
            (12, "Christina McArdle", 52.986375, -6.043701),
            (1, "Alice Cahill", 51.92893, -10.27699),
            (2, "Ian McArdle", 51.8856167, -10.4240951),
        ]

        for _index, _result in enumerate(result):
            self.assertEqual(_result.user_id, expected[_index][0])
            self.assertEqual(_result.name, expected[_index][1])
            self.assertEqual(_result.geolocation.latitude, expected[_index][2])
            self.assertEqual(_result.geolocation.longitude, expected[_index][3])

    def test_loads_file_does_not_exists(self):
        with self.assertRaises(FileNotFoundError):
            list(Customer.from_file("data/customers_shorter.txt"))


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


class CustomerToFileTestCase(unittest.TestCase):
    OUTPUT_PATH = "data/output.txt"

    def setUp(self):
        if os.path.exists(self.OUTPUT_PATH):
            os.remove(self.OUTPUT_PATH)

    def tearDown(self):
        if os.path.exists(self.OUTPUT_PATH):
            os.remove(self.OUTPUT_PATH)

    def test_write_correctly(self):
        Customer.write_to_file(data=[(99, "John Doe")], path=self.OUTPUT_PATH)

        self.assertTrue(os.path.exists(self.OUTPUT_PATH))
        self.assertTrue(os.path.isfile(self.OUTPUT_PATH))
        self.assertTrue(os.path.getsize(self.OUTPUT_PATH) > 0)
        with open(self.OUTPUT_PATH, "r") as data_file:
            for line in data_file:
                self.assertEqual("99, John Doe\n", line)

    def test_write_correctly_range_100(self):
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
        origin = GeoLocation(latitude=52.986375, longitude=-6.043701)
        Customer.write_to_file(
            data=Customer.in_range_from(
                origin=origin, source_file_path="data/customers.txt"
            ),
            path=self.OUTPUT_PATH,
        )

        self.assertTrue(os.path.exists(self.OUTPUT_PATH))
        self.assertTrue(os.path.isfile(self.OUTPUT_PATH))
        self.assertTrue(os.path.getsize(self.OUTPUT_PATH) > 0)
        with open(self.OUTPUT_PATH, "r") as data_file:
            for _index, line in enumerate(data_file):
                self.assertEqual("{}, {}\n".format(*expected[_index]), line)


if __name__ == "__main__":
    unittest.main()
