import sys, time

def main():
    start = time.time()

    sonar_string = open(sys.argv[1],'r').read().split('\n')
    prev = None
    curr = None
    count = 0
    for sonar in sonar_string:
        prev = curr
        if sonar != '':
            curr = int(sonar)
            if prev != None:
                diff = curr - prev
                if diff > 0:
                    count += 1
        
    stop = (time.time() - start)*1000
    print(count)
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()
