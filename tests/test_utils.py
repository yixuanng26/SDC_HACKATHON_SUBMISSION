import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from utils import calculate_milestone_progress, format_user_profile, match_career_path


class TestMyFutureUtils(unittest.TestCase):
    
    def test_format_user_profile(self):
        raw_data = {"name": "Maya", "age": 19, "education": "Bachelor"}
        profile = format_user_profile(raw_data)
        
        self.assertEqual(profile["name"], "Maya")
        self.assertEqual(profile["display_title"], "Maya (Bachelor)")

    def test_calculate_milestone_progress(self):
        completed_tasks = [True, True, False, False]
        progress_percentage = calculate_milestone_progress(completed_tasks)
        
        self.assertEqual(progress_percentage, 50.0)

    def test_calculate_milestone_progress_empty(self):
        self.assertEqual(calculate_milestone_progress([]), 0.0)

    def test_match_career_path(self):
        user_skills = ["Python", "SQL", "Data Visualisation"]
        target_role = "Data Analyst"
        
        match_result = match_career_path(user_skills, target_role)
        
        self.assertIn("match_score", match_result)
        self.assertGreaterEqual(match_result["match_score"], 0)
        self.assertLessEqual(match_result["match_score"], 100)


if __name__ == "__main__":
    unittest.main()