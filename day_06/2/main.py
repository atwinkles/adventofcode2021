import sys, time

def main():
    start_time = time.time()

    fish_file = open(sys.argv[1],'r')

    starting_state = fish_file.readline().strip('\n').split(',')

    state_list = [int(val) for val in starting_state]
    state = {}
    for i in range(0,9):
        if i not in state.keys():
            state[i] = state_list.count(i)

    #print(state)
    for i in range(1,257):
        new_fish = state[0]
        for fish in range(0,8):
            state[fish] = state[fish+1]
        state[6] += new_fish
        state[8] = new_fish
        #print(state)
    print(sum(state.values()))
    stop_time = (time.time() - start_time)*1000
    print('Code ran in %f milliseconds' % stop_time)

if __name__ == "__main__":
    main()

