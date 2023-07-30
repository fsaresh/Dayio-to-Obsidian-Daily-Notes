import builtins
import unittest
from migrater import DaylioMigrater, DaylioMigrationEntry
from migration_constants import SAMPLE_CSV_LOCATION, UTF_ENCODING
from unittest.mock import patch


class DaylioMigraterTestCase(unittest.TestCase):
    def test_migrate_open_file(self):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            migrater = DaylioMigrater(SAMPLE_CSV_LOCATION)
            migrater.migrate()
            mock_open.assert_called_with(SAMPLE_CSV_LOCATION, newline='', encoding=UTF_ENCODING)

    def test_migrate_write_file(self):
        with patch.object(DaylioMigrationEntry, "write_to_file") as mock_write_file:
            migrater = DaylioMigrater("."+SAMPLE_CSV_LOCATION)
            migrater.migrate()
            self.assertEqual(mock_write_file.call_count, 2)
