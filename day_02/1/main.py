import sys, time

def main():
    start = time.time()

    commands_file = open(sys.argv[1],'r')
    position = [0,0]
    for command in commands_file:
        direction = command.split(' ')[0]
        distance = int(command.split(' ')[1])
        if direction == 'forward':
            position[0] += distance
        elif direction == 'down':
            position[1] += distance
        elif direction == 'up':
            position[1] -= distance
        
    stop = (time.time() - start)*1000
    print(position)
    print(position[0]*position[1])
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()
