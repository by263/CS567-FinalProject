import unittest
from weather import WeatherAggregator

class TestWeatherAggregator(unittest.TestCase):
    def setUp(self):
        self.aggregator = WeatherAggregator()
        self.aggregator.add_measurement("City A", 20.0, 50, 10.0)
        self.aggregator.add_measurement("City B", 25.0, 60, 12.0)
        self.aggregator.add_measurement("City C", 18.0, 45, 8.0)

    def test_add_measurement(self):
        self.aggregator.add_measurement("City D", 22.0, 55, 11.0)
        self.assertEqual(self.aggregator.count_measurements(), 4)

    def test_remove_measurement(self):
        self.aggregator.remove_measurement("City A")
        self.assertEqual(self.aggregator.count_measurements(), 2)
        self.assertIsNone(self.aggregator.get_temperature("City A"))

    def test_get_temperature(self):
        temperature = self.aggregator.get_temperature("City B")
        self.assertEqual(temperature, 25.0)
        self.assertIsNone(self.aggregator.get_temperature("City D"))

    def test_get_humidity(self):
        humidity = self.aggregator.get_humidity("City C")
        self.assertEqual(humidity, 45)
        self.assertIsNone(self.aggregator.get_humidity("City D"))

    def test_get_wind_speed(self):
        wind_speed = self.aggregator.get_wind_speed("City A")
        self.assertEqual(wind_speed, 10.0)
        self.assertIsNone(self.aggregator.get_wind_speed("City D"))

    def test_get_average_temperature(self):
        average_temperature = self.aggregator.get_average_temperature()
        self.assertAlmostEqual(average_temperature, 21.0, places=1)

    def test_get_average_humidity(self):
        average_humidity = self.aggregator.get_average_humidity()
        self.assertAlmostEqual(average_humidity, 51.67, places=2)

    def test_get_average_wind_speed(self):
        average_wind_speed = self.aggregator.get_average_wind_speed()
        self.assertAlmostEqual(average_wind_speed, 10.0, places=1)

    def test_get_max_temperature(self):
        max_temperature = self.aggregator.get_max_temperature()
        self.assertEqual(max_temperature, 25.0)

    def test_get_min_temperature(self):
        min_temperature = self.aggregator.get_min_temperature()
        self.assertEqual(min_temperature, 18.0)

    def test_get_max_humidity(self):
        max_humidity = self.aggregator.get_max_humidity()
        self.assertEqual(max_humidity, 60)

    def test_get_min_humidity(self):
        min_humidity = self.aggregator.get_min_humidity()
        self.assertEqual(min_humidity, 45)

    def test_get_max_wind_speed(self):
        max_wind_speed = self.aggregator.get_max_wind_speed()
        self.assertEqual(max_wind_speed, 12.0)

    def test_get_min_wind_speed(self):
        min_wind_speed = self.aggregator.get_min_wind_speed()
        self.assertEqual(min_wind_speed, 8.0)

    def test_get_locations(self):
        locations = self.aggregator.get_locations()
        self.assertEqual(len(locations), 3)
        self.assertIn("City A", locations)
        self.assertIn("City B", locations)
        self.assertIn("City C", locations)

    def test_count_measurements(self):
        count = self.aggregator.count_measurements()
        self.assertEqual(count, 3)

    def test_clear_data(self):
        self.aggregator.clear_data()
        count = self.aggregator.count_measurements()
        self.assertEqual(count, 0)
        self.assertTrue(self.aggregator.is_empty())

    def test_is_location_exist(self):
        self.assertTrue(self.aggregator.is_location_exist("City A"))
        self.assertFalse(self.aggregator.is_location_exist("City D"))

    def test_is_empty(self):
        self.assertFalse(self.aggregator.is_empty())
        self.aggregator.clear_data()
        self.assertTrue(self.aggregator.is_empty())

if __name__ == '__main__':
    unittest.main()
