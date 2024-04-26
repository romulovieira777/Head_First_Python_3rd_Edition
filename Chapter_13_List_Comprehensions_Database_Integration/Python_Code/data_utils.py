import DBcm


db_details = "CoachDB.sqlite3"


from Chapter_13_List_Comprehensions_Database_Integration.Python_Code.queries import *


def get_swimmers_events(name, age, date):
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_EVENTS_BY_SESSION, (name, age, date))
        results = db.fetchall()
    return results