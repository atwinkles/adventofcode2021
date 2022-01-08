import sys, time

def main():
    start = time.time()

    diagnostics_file = open(sys.argv[1],'r')
    bits = {}
    for data in diagnostics_file:
        data_len = len(data) - 1
        if len(bits) == 0:
            bits = {key: [0,0] for key in range(0,data_len)}
        for i in range(0,data_len):
            if data[i] == "0":
                bits[i][0] += 1
            elif data[i] == "1":
                bits[i][1] += 1

    gamma_bits = ""
    epsilon_bits = ""
    
    for key in bits.keys():
        if max(bits[key]) == bits[key][0]:
            gamma_bits += "0"
            epsilon_bits += "1"
        else:
            gamma_bits += "1"
            epsilon_bits += "0"
    gamma = int(gamma_bits,2)
    epsilon = int(epsilon_bits,2)
        
    stop = (time.time() - start)*1000
    print(gamma_bits)
    print(epsilon_bits)
    print(gamma)
    print(epsilon)
    print(gamma*epsilon)
    print('Code ran in %f milliseconds' % stop)

if __name__ == "__main__":
    main()

