import datetime

string_datetime = input()

def parse_time(s):
    year, month, day, hour, minute, second = map(int, s.split())
    dt = datetime.datetime(year, month, day, hour, minute, second)
    return dt + datetime.timedelta(days=1)

print(parse_time(string_datetime))
