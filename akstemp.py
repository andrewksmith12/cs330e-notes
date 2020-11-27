def season(month):
    if month < 1 or month > 12:
        return "out of range"
    if month <= 5:
        return "spring"
    elif month <= 9:
        return "summer"
    else:
        return "fall"