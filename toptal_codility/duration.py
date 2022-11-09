import math


def duration(X):
    # X is less than 60s
    if X < 60:
        return f'{X}s'

    # X is greater than or equal 1 min and less than 1 hour
    if X >= 60 and X < 3600:
        # change seconds into min
        minutes = X / 60

        # if result is a whole number return result
        if minutes.is_integer():
            return f'{math.floor(minutes)}m'

        full_min = math.trunc(minutes)  # get the full minute
        # convert the decimal into seconds
        rem_min = minutes - math.floor(minutes)
        seconds = math.floor(rem_min * 60)

        return f'{full_min}m{seconds}s'

    # X is greater than or equal to 1 hr and less than 1 day
    if X >= 3600 and X < 86400:
        # change seconds into hr
        hours = X / 3600

        # if result is a whole number return result
        if hours.is_integer():
            return f'{math.floor(hours)}h'

        full_hr = math.trunc(hours)  # get the full hr
        # convert the decimal into min
        rem_hr = hours - math.floor(hours)
        minutes = rem_hr * 60

        return f'{full_hr}h{duration(minutes * 60)}'


if __name__ == "__main__":
    print(duration(100))
    print(duration(60))
    print(duration(7263))
