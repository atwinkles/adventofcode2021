import sys, time

def main():
    start_time = time.time()

    crab_file = open(sys.argv[1],'r')

    starting_state = [int(x) for x in crab_file.readline().strip('\n').split(',')]

    max_pos = max(starting_state)
    min_pos = min(starting_state)

    sum_vals = {}

    for i in range(min_pos,max_pos+1):
        sum_vals[i] = 0
        for position in starting_state:
            sum_vals[i] += abs(i - position)

    print(min(sum_vals.values()))
    stop_time = (time.time() - start_time)*1000
    print('Code ran in %f milliseconds' % stop_time)

if __name__ == "__main__":
    main()

