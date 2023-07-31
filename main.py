from migrater import DaylioMigrater
from migration_constants import FileLocationSettings


if __name__ == '__main__':
    daylio_migrater = DaylioMigrater(FileLocationSettings.DAYLIO_CSV_LOCATION)
    daylio_migrater.migrate()
