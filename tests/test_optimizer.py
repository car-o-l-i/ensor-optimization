import unittest
from models.sensor import Sensor
from models.optimizer import SensorOptimizer

class TestSensorOptimizer(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.sensors = [
            Sensor(id=0, battery_duration=3.0, coverage_zones={0, 1}),
            Sensor(id=1, battery_duration=2.0, coverage_zones={1, 2}),
            Sensor(id=2, battery_duration=4.0, coverage_zones={0, 2}),
        ]
        self.num_zones = 3
        self.optimizer = SensorOptimizer(self.sensors, self.num_zones)
    
    def test_linear_programming_solution(self):
        """Test linear programming solution."""
        solution = self.optimizer.solve_linear_programming()
        
        # Check if solution exists
        self.assertIsNotNone(solution)
        
        # Check if all zones are covered
        covered_zones = set()
        for sensor_id, times in solution.items():
            if len(times) > 0:
                covered_zones.update(self.sensors[sensor_id].coverage_zones)
        self.assertEqual(covered_zones, set(range(self.num_zones)))
        
        # Check battery constraints
        for sensor_id, times in solution.items():
            self.assertLessEqual(len(times), self.sensors[sensor_id].battery_duration)
    
    def test_simulated_annealing_solution(self):
        """Test simulated annealing solution."""
        solution = self.optimizer.solve_simulated_annealing(iterations=100)
        
        # Check if solution exists
        self.assertIsNotNone(solution)
        
        # Check if all zones are covered
        covered_zones = set()
        for sensor_id, times in solution.items():
            if len(times) > 0:
                covered_zones.update(self.sensors[sensor_id].coverage_zones)
        self.assertEqual(covered_zones, set(range(self.num_zones)))
        
        # Check battery constraints
        for sensor_id, times in solution.items():
            self.assertLessEqual(len(times), self.sensors[sensor_id].battery_duration)

if __name__ == '__main__':
    unittest.main() 