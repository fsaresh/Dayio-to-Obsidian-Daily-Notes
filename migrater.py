from migration_constants import DailyNotesFormat, DaylioEntryKeys, FileLocationSettings, UTF_ENCODING
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
        """ Converts Daylio entry to this structure:
        # Summary
        <note body from Daylio>

        ## Mood and Activities
        Mood: <mood from Daylio>
        Activities: <activity 1 from Daylio, activity 2 from Daylio>

        ## Tasks Today
        """
        contents = DailyNotesFormat.summary_header + self.row_data[DaylioEntryKeys.NOTE_BODY].replace('<br>', '\n')
        contents += DailyNotesFormat.mood_header + DailyNotesFormat.mood_entry + self.row_data[DaylioEntryKeys.MOOD]
        contents += DailyNotesFormat.activities_entry + self.row_data[DaylioEntryKeys.ACTIVITIES].replace(' | ', ', ')
        contents += DailyNotesFormat.tasks_header
        return contents

    @property
    def file_folder(self):
        # Currently sets file folder to <MIGRATED_ENTRY_LOCATION>/YYYY/MM-<Month name>
        entry_date_parts = self.row_data[DaylioEntryKeys.FULL_DATE].split('-')
        entry_year = entry_date_parts[0]
        entry_month_numeral = entry_date_parts[1]
        entry_month_name = calendar.month_name[int(entry_month_numeral)]
        return os.path.join(
            FileLocationSettings.MIGRATED_ENTRY_LOCATION,
            f"{entry_year}/{entry_month_numeral}-{entry_month_name}"
        )

    @property
    def file_name(self):
        # Currently sets file name to YYYY-MM-DD-<Day of week>.md
        return f"{self.row_data[DaylioEntryKeys.FULL_DATE]}-{self.row_data[DaylioEntryKeys.WEEKDAY]}.md"

    def write_to_file(self):
        # Recursively creates file folder if it doesn't exist, programmatically creating year/month structure as needed
        if not os.path.exists(self.file_folder):
            os.makedirs(self.file_folder)
        with open(os.path.join(self.file_folder, self.file_name), 'w') as migrated_file:
            print(f"Writing contents to `{migrated_file.name}`")
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
