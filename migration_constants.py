CSV_LOCATION = "./daylio_exports/sample_daylio.csv"  # Change this to your real backup file!
SAMPLE_CSV_LOCATION = "./daylio_exports/sample_daylio.csv"
MIGRATED_ENTRY_LOCATION = "./sentence diary"
UTF_ENCODING = 'utf-8-sig'


class DailyNotesFormat:
    summary_header = "\n# Summary\n"
    mood_header = "\n\n## Mood and Activities"
    mood_entry = "\nMood: "
    activities_entry = "\nActivities: "
    tasks_header = "\n\n# Tasks Today\n"


class DaylioEntryKeys:
    FULL_DATE = 'full_date'
    WEEKDAY = 'weekday'
    MOOD = 'mood'
    ACTIVITIES = 'activities'
    NOTE_BODY = 'note'


