import unittest
from unittest.mock import patch, mock_open, MagicMock
from load import save_activity_data, save_body_data, save_sleep_data, load_health_data

class TestLoadMethods(unittest.TestCase):
    def setUp(self):
        # Example data to be used in tests
        self.mock_activity_data = {
            'data': [{
                'heart_rate_data': {'summary': {'avg_hr_bpm': 80}},
                'calories_data': {'BMR_calories': 1600, 'total_burned_calories': 2000},
                'metadata': {'start_time': "2023-01-01T12:00:00.000000+00:00"}
            }]
        }
        self.mock_body_data = {
            'data': [{
                'measurements_data': {'measurements': [{'estimated_fitness_age': 25, 'BMI': 22}]},
                'blood_pressure_data': {'blood_pressure_samples': [{'systolic_bp': 120}]},
                'temperature_data': {'body_temperature_samples': [{'temperature_celsius': 36.5}]},
                'metadata': {'start_time': "2023-01-01T12:00:00.000000+00:00"}
            }]
        }
        self.mock_sleep_data = {
            'data': [{
                'sleep_durations_data': {'asleep': {'num_REM_events': 5}, 'awake': {'num_wakeup_events': 2}, 'sleep_efficiency': 90},
                'metadata': {'start_time': "2023-01-01T12:00:00.000000+00:00"}
            }]
        }

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_activity_data))
    def test_save_activity_data(self, mock_file):
        activity = save_activity_data()
        # Your assertions here, e.g.:
        self.assertEqual(activity.bpm, 80)

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_body_data))
    def test_save_body_data(self, mock_file):
        body = save_body_data()
        # Your assertions here

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_sleep_data))
    def test_save_sleep_data(self, mock_file):
        sleep = save_sleep_data()
        # Your assertions here

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_activity_data))
    @patch("load.db.session.add")
    @patch("load.db.session.commit")
    @patch("load.User.query.filter_by")
    def test_load_health_data(self, mock_filter_by, mock_commit, mock_add, mock_file):
        # Mocking the return of the filter_by
        mock_user = MagicMock()
        mock_user.id = 1
        mock_filter_by.return_value.first.return_value = mock_user
        
        load_health_data("test_username")
        # Your assertions here, e.g., whether the methods were called, etc.

if __name__ == '__main__':
    unittest.main()
