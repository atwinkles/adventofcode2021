import sys, time

def main():
    start_time = time.time()

    line_file = open(sys.argv[1],'r')

    cover = {}

    with line_file as f:
        for line in f:
            data = line.split(' -> ')  
            start_val = data[0].split(',')
            start = (int(start_val[0]),int(start_val[1]))
            stop_val = data[1].split(',')
            stop = (int(stop_val[0]),int(stop_val[1]))
            if start[0] == stop[0]:
                max_val = max(start[1],stop[1])
                min_val = min(start[1],stop[1])
                for i in range(min_val,max_val+1):
                    point = (start[0],i)
                    if point in cover:
                        cover[point] += 1
                    else:
                        cover[point] = 1
            elif start[1] == stop[1]:
                max_val = max(start[0],stop[0])
                min_val = min(start[0],stop[0])
                for i in range(min_val,max_val+1):
                    point = (i,start[1])
                    if point in cover:
                        cover[point] += 1
                    else:
                        cover[point] = 1

    total = 0
    for count in cover.values():
        if count >= 2:
            total += 1

    print(total)
    stop_time = (time.time() - start_time)*1000
    print('Code ran in %f milliseconds' % stop_time)

if __name__ == "__main__":
    main()

