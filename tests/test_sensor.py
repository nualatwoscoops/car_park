import  unittest
from sensor import EntrySensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Test Car Park", 100)
        self.sensor = EntrySensor(id="A1", car_park=self.car_park, is_active=True)

    def test_attributes_are_initialised(self):
        self.assertEqual(self.sensor.id, "A1")
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertTrue(self.sensor.is_active)

class TestSensorPlate(EntrySensor):
    def _scan_plate(self):
        return "TEST123"

    def test_detect_vehicle_updates_plate(self):
        self.car_park = CarPark("Test Car Park", 50)
        self.assertIn("TEST123", self.car_park.plates)

    def tearDown(self):
        self.sensor = None
        self.car_park = None
