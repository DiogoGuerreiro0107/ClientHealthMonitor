from django.db import connections
from django.db.utils import OperationalError


def check_database_connection() -> bool:
    try:
        with connections["default"].cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchone()

        return True

    except OperationalError:
        return False