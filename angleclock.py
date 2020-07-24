def angleClock(hour: int, minutes: int) -> float:
    HR_UNIT = 30
    MN_UNIT = 6
    if hour == 12:
        hour = 0
    HR_DEG = HR_UNIT * hour + HR_UNIT * minutes/60
    MN_DEG = MN_UNIT * minutes
    print(HR_DEG, MN_DEG)
    if HR_DEG > MN_DEG:
        return min(HR_DEG - MN_DEG, 360 - HR_DEG + MN_DEG)
    return min(MN_DEG - HR_DEG, 360 - MN_DEG + HR_DEG)


a = angleClock(1, 57)
print(a)
