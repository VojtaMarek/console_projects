"""Gets the name corresponding to an ID by simulating the so-call 'index fragmentation' ('pálení intervalů') algorithm. It works only with an orded database table."""

from random import randint
import sqlite3


PATH = "big_database.db"


def get_sql_result(query, path=PATH):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()[0]


def get_number_of_rows():
    number_of_rows = get_sql_result("SELECT COUNT(*) FROM Records;")
    return number_of_rows


def get_name_by_id(id_pointer, number_of_rows, fragmenter=2, count_from=0):
    id_search = round(number_of_rows / fragmenter) + count_from
    
    if id_pointer < id_search:
        fragmenter *= 2
        count_from += 0
    elif id_pointer > id_search:
        fragmenter *= 2
        count_from = id_search
    else:  # id_pointer == id_search:
        the_name = get_sql_result(f"SELECT name FROM Records WHERE id={str(id_pointer)}")
        output = {id_pointer: the_name}
        return output
    # print({"id_pointer": id_pointer, "number_of_rows": number_of_rows, "fragmenter": fragmenter, "count_from": count_from})
    return get_name_by_id(id_pointer, number_of_rows, fragmenter, count_from)


if __name__ == "__main__":
    id_pointer = randint(1, get_number_of_rows())
    number_of_rows = get_number_of_rows()
    print(get_name_by_id(id_pointer, number_of_rows))
