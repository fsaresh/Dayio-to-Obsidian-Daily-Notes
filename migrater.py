from migration_constants import DailyNotesFormat, DaylioEntryKeys, MIGRATED_ENTRY_LOCATION, UTF_ENCODING
from typing import Dict
import calendar
import csv
import os


class DaylioMigrationEntry:
    row_data: Dict

    def __init__(self, row):
        self.row_data = row

    @property
    def contents(self):
        contents = DailyNotesFormat.summary_header + self.row_data[DaylioEntryKeys.NOTE_BODY].replace('<br>', '\n')
        contents += DailyNotesFormat.mood_header + DailyNotesFormat.mood_entry + self.row_data[DaylioEntryKeys.MOOD]
        contents += DailyNotesFormat.activities_entry + self.row_data[DaylioEntryKeys.ACTIVITIES].replace(' | ', ', ')
        contents += DailyNotesFormat.tasks_header
        return contents

    @property
    def file_folder(self):
        entry_date_parts = self.row_data[DaylioEntryKeys.FULL_DATE].split('-')
        entry_date_month_expanded = f"{entry_date_parts[1]}-{calendar.month_name[int(entry_date_parts[1])]}"
        return os.path.join(MIGRATED_ENTRY_LOCATION, f"{entry_date_parts[0]}/{entry_date_month_expanded}")

    @property
    def file_name(self):
        return f"{self.row_data[DaylioEntryKeys.FULL_DATE]}-{self.row_data[DaylioEntryKeys.WEEKDAY]}.md"

    def write_to_file(self):
        if not os.path.exists(self.file_folder):
            os.makedirs(self.file_folder)
        with open(os.path.join(self.file_folder, self.file_name), 'w') as migrated_file:
            migrated_file.write(self.contents)


class DaylioMigrater:
    def __init__(self, csv_location):
        self.csv_location = csv_location

    def migrate(self):
        with open(self.csv_location, newline='', encoding=UTF_ENCODING) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                migrated_entry = DaylioMigrationEntry(row)
                migrated_entry.write_to_file()
