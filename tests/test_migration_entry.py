import unittest
from migrater import DaylioMigrationEntry
from migration_constants import FileLocationSettings


class MigrationEntryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # sample row data, contents can be adjusted as needed
        self.year = "2023"
        self.month_number = "04"
        self.month_name = "April"
        self.day = "11"
        self.full_date = f'{self.year}-{self.month_number}-{self.day}'
        self.day_of_week = "Tuesday"
        self.mood = "good"
        self.activities = ["cardio", "chest triceps"]
        self.row_data = {
            'full_date':  self.full_date,
            'date': f'{self.month_name} {self.month_number}',
            'weekday': self.day_of_week,
            'time': '08:44',
            'mood': self.mood,
            'activities': 'cardio | chest triceps',
            'note_title': '',
            'note': '- gym<br>- laundry<br>- mom chat<br><br>- taxes'
        }
        self.migration_entry = DaylioMigrationEntry(self.row_data)

    def test_content_creation(self):
        """ We expect the line separator (<br>) to be replaced by newlines (\n) in note body
        We also expect the activities separator (|) to be replaced by commas instead
        I hardcoded the expected contents to avoid making assumptions around the headers matching,
        but easy enough to change if needed in the future
        """
        expected_contents = "\n# Summary\n"
        expected_contents += "- gym\n- laundry\n- mom chat\n\n- taxes"
        expected_contents += "\n\n## Mood and Activities"
        expected_contents += f"\nMood: {self.mood}"
        expected_contents += f"\nActivities: {', '.join(self.activities)}"
        expected_contents += "\n\n# Tasks Today\n"
        actual_contents = self.migration_entry.contents
        self.assertEqual(expected_contents, actual_contents)

    def test_file_folder(self):
        expected_file_folder = f"{FileLocationSettings.MIGRATED_ENTRY_LOCATION}/" \
                               f"{self.year}/" \
                               f"{self.month_number}-{self.month_name}"
        actual_file_folder = self.migration_entry.file_folder
        self.assertEqual(expected_file_folder, actual_file_folder)

    def test_file_name(self):
        expected_file_name = f"{self.full_date}-{self.day_of_week}.md"
        actual_file_name = self.migration_entry.file_name
        self.assertEqual(expected_file_name, actual_file_name)
