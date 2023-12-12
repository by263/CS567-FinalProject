class WeatherAggregator:
    def __init__(self):
        self.weather_data = []

    def add_measurement(self, location, temperature, humidity, wind_speed):
        measurement = {
            'location': location,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
        }
        self.weather_data.append(measurement)

    def remove_measurement(self, location):
        self.weather_data = [data for data in self.weather_data if data['location'] != location]

    def get_temperature(self, location):
        for data in self.weather_data:
            if data['location'] == location:
                return data['temperature']
        return None

    def get_humidity(self, location):
        for data in self.weather_data:
            if data['location'] == location:
                return data['humidity']
        return None

    def get_wind_speed(self, location):
        for data in self.weather_data:
            if data['location'] == location:
                return data['wind_speed']
        return None

    def get_average_temperature(self):
        if not self.weather_data:
            return None
        total_temperature = sum(data['temperature'] for data in self.weather_data)
        return total_temperature / len(self.weather_data)

    def get_average_humidity(self):
        if not self.weather_data:
            return None
        total_humidity = sum(data['humidity'] for data in self.weather_data)
        return total_humidity / len(self.weather_data)

    def get_average_wind_speed(self):
        if not self.weather_data:
            return None
        total_wind_speed = sum(data['wind_speed'] for data in self.weather_data)
        return total_wind_speed / len(self.weather_data)

    def get_max_temperature(self):
        if not self.weather_data:
            return None
        max_temperature = max(data['temperature'] for data in self.weather_data)
        return max_temperature

    def get_min_temperature(self):
        if not self.weather_data:
            return None
        min_temperature = min(data['temperature'] for data in self.weather_data)
        return min_temperature

    def get_max_humidity(self):
        if not self.weather_data:
            return None
        max_humidity = max(data['humidity'] for data in self.weather_data)
        return max_humidity

    def get_min_humidity(self):
        if not self.weather_data:
            return None
        min_humidity = min(data['humidity'] for data in self.weather_data)
        return min_humidity

    def get_max_wind_speed(self):
        if not self.weather_data:
            return None
        max_wind_speed = max(data['wind_speed'] for data in self.weather_data)
        return max_wind_speed

    def get_min_wind_speed(self):
        if not self.weather_data:
            return None
        min_wind_speed = min(data['wind_speed'] for data in self.weather_data)
        return min_wind_speed

    def get_locations(self):
        return [data['location'] for data in self.weather_data]

    def count_measurements(self):
        return len(self.weather_data)

    def clear_data(self):
        self.weather_data = []

    def is_location_exist(self, location):
        return any(data['location'] == location for data in self.weather_data)

    def is_empty(self):
        return not self.weather_data
