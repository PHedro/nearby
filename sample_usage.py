from nearby.customer import Customer
from nearby.file_handler import write_to_file
from nearby.geolocation import GeoLocation


def export_to_file():
    origin = GeoLocation(latitude=53.339428, longitude=-6.257664)
    data = Customer.in_range_from(
        origin=origin, source_file_path="nearby/tests/data/customers.txt"
    )
    write_to_file(data=data, path="export.txt")


if __name__ == "__main__":
    export_to_file()
