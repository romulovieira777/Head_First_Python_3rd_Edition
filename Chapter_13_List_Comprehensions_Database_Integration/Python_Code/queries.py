SQL_SESSIONS = """
    SELECT DISTINCT ts 
    FROM times
"""

SQL_SWIMMERS_BY_SESSION = """
    SELECT DISTINCT swimmers.name, swimmers.age 
    FROM times, swimmers 
    WHERE DATE(times.ts) = ? AND times.swimmer_id = swimmers.id 
    ORDER BY name
"""

SQL_SWIMMERS_EVENTS_BY_SESSION = """
    SELECT DISTINCT events.distance, events.stroke
    FROM swimmers, events, times
    WHERE times.swimmer_id = swimmers.id AND
    times.event_id = events.id AND
    (swimmers.name = ? AND swimmers.age = ?) AND
    DATE(times.ts) = ?
"""

SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION = """
    SELECT times.time 
    FROM swimmers, events, times
    WHERE CAST((swimmers.name = ? AND swimmers.age = ?) AND (events.distance = ? AND events.stroke = ?) 
    AND swimmers.id = times.swimmer_id AND events.id = times.event_id AND DATE(times.ts) = ?
"""
