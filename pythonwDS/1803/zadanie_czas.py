# start - godzina rozpoczęcia seansu
# playtime - ile sekund oglądaliśmy

# p = 3.5
# s = 5.6
#
# 5: 0.4 (do 6)
# 6: 1.0 (do 7)
# 7: 1.0 (do 8)
# 8: 1.0 (do 9)
# 9: 0.1 (do 10) <-- p + s
#
# 0: 0.0 - 1.00
# 1: 1.01 - 2.00
# 2: 2.01 - 3.00
# ...
# 10: 10.01 - 11.00
def time_split(start:float, playtime: float):
    start_hour = int(start)
    end = start + playtime
    end_hour = int(end) + 1

    while start <= end:
        if int(start) + 1 > end:
            print(f"{end - start:1f}")
        else:
            print(f"{(int(start))} - {(int(start) + 1) - start:.1f}")
        start = int(start) + 1

time_split(5.6, 5.3)