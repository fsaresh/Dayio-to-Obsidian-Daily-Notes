import os.path
import unittest
from migrater import DaylioMigrater, DaylioMigrationEntry
from migration_constants import UTF_ENCODING
from unittest.mock import patch


class DaylioMigraterTestCase(unittest.TestCase):
    # To get a test CSV, need to go up a level to root of project, then into daylio_exports, then to sample CSV
    SAMPLE_CSV_NAME = "sample_daylio.csv"
    SAMPLE_CSV_LOCATION = os.path.join(os.path.dirname(os.getcwd()), "daylio_exports", SAMPLE_CSV_NAME)

    def test_migrate_open_file(self):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            migrater = DaylioMigrater(self.SAMPLE_CSV_LOCATION)
            migrater.migrate()
            mock_open.assert_called_with(self.SAMPLE_CSV_LOCATION, newline='', encoding=UTF_ENCODING)

    def test_migrate_write_file(self):
        with patch.object(DaylioMigrationEntry, "write_to_file") as mock_write_file:
            migrater = DaylioMigrater(self.SAMPLE_CSV_LOCATION)
            migrater.migrate()
            self.assertEqual(mock_write_file.call_count, 2)
