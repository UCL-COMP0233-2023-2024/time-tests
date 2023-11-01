import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    # print("overlap_time = " + overlap_time)
    if overlap_time[0][0] > overlap_time[0][1]:
        raise ValueError("There is no overlap.")
    elif overlap_time[0][0] == overlap_time[0][1]:
        return str(overlap_time[0][0]) # not a list-how to transform
    else:
        return overlap_time
    # return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))


    # test for no overlap ranges
    range0 = time_range("2010-01-12 09:00:00", "2010-01-12 09:59:59")
    # print(compute_overlap_time(range0, large))
 
    # test for a point overlap
    range1 = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00")
    print(compute_overlap_time(range1, large)) # 不是一个list
    
    # test for partial overlap
    range2 = time_range("2010-01-12 09:30:00", "2010-01-12 10:40:00")
    print(compute_overlap_time(short, range2))
    # if range2 has some intervals, the test would fail



    # test for full overlap
    # print(compute_overlap_time(large, short))



