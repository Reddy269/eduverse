from functools import wraps
from django.db import connection, reset_queries


def print_queries(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()  # clear previous queries
        result = func(*args, **kwargs)

        queries = connection.queries
        print(f"\n--- {len(queries)} queries executed ---")
        for i, query in enumerate(queries, start=1):
            print(f"{i}. {query['sql']} ({query['time']}s)")
        print("--- end queries ---\n")

        return result

    return wrapper

