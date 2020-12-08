import json
import time
import datetime

with open("times.txt") as file:
    json_data = json.loads(file.read())

members = json_data["members"]

def solve_time_from_ts(ts, day) -> str:
    dt: datetime = datetime.datetime(2020, 12, int(day), 0, 0)
    ut: int = int(time.mktime(dt.timetuple()))
    diff: int = (int(ts) - ut)

    return str(datetime.timedelta(seconds=diff))


def format_member(member_num: int):
    member = members[str(member_num)]

    print("\nSolve times for '", member["name"], "':", sep="")

    completions = member["completion_day_level"]
    for day in range(1,25):
        try:
            parts = completions[str(day)]
        except:
            break

        for part in range(1,3):
            solve_time = parts[str(part)]["get_star_ts"]
            print("day", day, "part", part, "-> ", end="")
            print(solve_time_from_ts(solve_time, day))


for member_num in members:
    format_member(member_num)
