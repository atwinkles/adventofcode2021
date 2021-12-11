import sys, time

def main():
    start = time.time()

    sonar_string = open(sys.argv[1],'r').read().split('\n')
    size = len(sonar_string)-1
    trios = [0 for i in range(0,size-2)]
    for i in range(0,size-2):
        trios[i] = int(sonar_string[i]) + int(sonar_string[i+1]) + int(sonar_string[i+2])
    print(trios)

    prev = None
    curr = None
    count = 0
    for sonar in trios:
        prev = curr
        if sonar != '':
            curr = sonar
            if prev != None:
                diff = curr - prev
                if diff > 0:
                    count += 1
        
    stop = (time.time() - start)*1000
    print(count)
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()
