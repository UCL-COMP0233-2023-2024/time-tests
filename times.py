import datetime
debug = False

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    if start_time_s>end_time_s:
        raise ValueError("you need to swap the two dates around")
    else:
        d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
        sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                    start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                    for i in range(number_of_intervals)]
        return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1:list, range2:list):

    overlap_time = []
    if debug: print("\n### for loop A ###")
    for start1, end1 in range1:
        if debug: print(f"start1: {start1}\nend1: {end1}\noverlap_time: {overlap_time}\n\n    ### for loop B ###")
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
            if debug: print(f"    start2: {start2}\n    end2: {end2} \n    low: {low}\n    high: {high}\n    overlap_time: {overlap_time}\n")
    return overlap_time

if __name__ == "__main__":
    debug = True
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))