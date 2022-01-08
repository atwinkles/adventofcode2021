import sys, time

def main():
    start = time.time()

    diagnostics_file = open(sys.argv[1],'r')
    diagnostics_data = [row for row in diagnostics_file]

    oxygen_bits = recursion_diagnostics(diagnostics_data,0,'oxygen') 
    print(oxygen_bits)

    co2_bits = recursion_diagnostics(diagnostics_data,0,'co2') 
    print(co2_bits)

    oxygen = int(oxygen_bits,2)
    co2 = int(co2_bits,2)

    print(oxygen)
    print(co2)
    print(co2*oxygen)
        
    stop = (time.time() - start)*1000
    print('Code ran in %f milliseconds' % stop)

def recursion_diagnostics(data, position,lsr):

    if len(data) == 1:
        return data[0]

    bit_count = [0,0]
    zeros = []
    ones = []
    for val in data:
        if val[position] == "0":
            zeros.append(val)
            bit_count[0] += 1
        else:
            ones.append(val)
            bit_count[1] += 1

    if lsr == "oxygen":
        if position == 0:
            data = recursion_diagnostics(ones,position+1,lsr)
        elif max(bit_count) == bit_count[1]:
            data = recursion_diagnostics(ones,position+1,lsr)
        else:
            data = recursion_diagnostics(zeros,position+1,lsr)

    elif lsr == "co2":
        if position == 0:
            data = recursion_diagnostics(zeros,position+1,lsr)
        elif min(bit_count) == bit_count[0]:
            data = recursion_diagnostics(zeros,position+1,lsr)
        else:
            data = recursion_diagnostics(ones,position+1,lsr)

    return data

if __name__ == "__main__":
    main()

