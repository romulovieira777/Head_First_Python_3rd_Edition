import DBcm
import os


db_details = "CoachDB.sqlite3"

FOLDER = "../swimdata/"

files = os.listdir(FOLDER)
# files.remove(".DS_Store")

SQL_SELECT_SWIMMERS = """
    SELECT * FROM swimmers WHERE name = ? AND age = ?
"""

SQL_INSERT_SWIMMERS = """
    INSERT INTO swimmers (name, age) VALUES (?, ?)
"""

SQL_SELECT_EVENTS = """
    SELECT * FROM events WHERE distance = ? AND stroke = ?
"""

SQL_INSERT_EVENTS = """
    INSERT INTO events (distance, stroke) VALUES (?, ?)
"""

SQL_GET_SWIMMER = """
    SELECT id FROM swimmers WHERE name = ? AND age = ?
"""

SQL_GET_EVENT = """
    SELECT id FROM events WHERE distance = ? AND stroke = ?
"""

SQL_INSERT_TIMES = """
    INSERT INTO times (swimmer_id, event_id, time) VALUES (?, ?, ?)
"""

with DBcm.UseDatabase(db_details) as db:
    for fn in files:
        name, age, distance, stroke = fn.removesuffix(".txt").split("-")

        db.execute(
            SQL_SELECT_SWIMMERS,
            (
                name,
                age,
            ),
        )
        if not db.fetchall():
            db.execute(
                SQL_INSERT_SWIMMERS,
                (
                    name,
                    age,
                ),
            )

        db.execute(
            SQL_SELECT_EVENTS,
            (
                distance,
                stroke,
            ),
        )
        if not db.fetchall():
            db.execute(
                SQL_INSERT_EVENTS,
                (
                    distance,
                    stroke,
                ),
            )

        db.execute(
            SQL_GET_SWIMMER,
            (
                name,
                age,
            ),
        )
        s_id = db.fetchone()[0]

        db.execute(
            SQL_GET_EVENT,
            (
                distance,
                stroke,
            ),
        )
        e_id = db.fetchone()[0]

        with open(FOLDER + fn) as sf:
            times = sf.read().strip().split(",")
            for t in times:
                db.execute(
                    SQL_INSERT_TIMES,
                    (
                        s_id,
                        e_id,
                        t,
                    ),
                )
