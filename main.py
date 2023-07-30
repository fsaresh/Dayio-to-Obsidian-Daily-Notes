from migrater import DaylioMigrater
from migration_constants import CSV_LOCATION


if __name__ == '__main__':
    daylio_migrater = DaylioMigrater(CSV_LOCATION)
    daylio_migrater.migrate()
