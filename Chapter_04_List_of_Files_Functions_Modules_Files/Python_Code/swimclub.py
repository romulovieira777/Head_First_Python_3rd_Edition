import statistics

FOLDER = "../swimdata/"


def read_swim_data(filename):
    """
    Return swim data from a file

    Give the name of a swimmer's file (in filename), extract all the required data, then return it to the caller as a
    tuple.
    """
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(",")

    converts = []

    for time in times:
        # The minutes value might be missing, so guard against this causing a crash.
        if ":" in time:
            minutes, rest = time.split(':')
            seconds, hundredths = rest.split('.')
        else:
            minutes = 0
            seconds, hundredths = time.split('.')
        converts.append((int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths))

    average = statistics.mean(converts)
    mins_secs, hundredths = str(round(average / 100, 2)).split('.')
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = f"{minutes}:{seconds}.{hundredths}"

    return swimmer, age, distance, stroke, times, average, converts  # Return the data as a tuple
