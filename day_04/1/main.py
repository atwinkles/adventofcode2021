import sys, time

class Bingo:
    def __init__(self,data):
        self.rows = data

    def check_bingo(self):
        row_check = ['X','X','X','X','X'] in self.rows
        col_check = False
        for j in range(0,5):
            if self.rows[0][j] == 'X' and self.rows[1][j] == 'X' and self.rows[2][j] == 'X' and self.rows[3][j] == 'X' and self.rows[4][j] == 'X':
                col_check = False

        if row_check or col_check:
            return True
        else:
            return False

    def play_round(self,value):
        for i in range(0,5):
            if value in self.rows[i]:
                index = self.rows[i].index(value)
                self.rows[i][index] = 'X'
                return True
        return False
        
    def amount(self):
        total = 0
        for row in self.rows:
            for value in row:
                if value != 'X':
                    total += int(value)
        return total

    def __str__(self):
        stringval = ''
        for row in self.rows:
            for val in row:
                if len(val) == 1:
                    stringval += val + '  ' 
                else:
                    stringval += val + ' ' 
            stringval += '\n'
        return stringval

def main():
    start = time.time()

    bingo_file = open(sys.argv[1],'r')
    
    chosen = bingo_file.readline().strip('\n').split(',')

    board_data = []

    with bingo_file as f:
        for line in f:
            if line == "\n":
                board_data.append([])
            elif line != '':
                data = line.strip('\n').split(' ')
                data = list(filter(lambda a: a != '',data))
                size = len(board_data)
                board_data[size-1].append(data)
    boards = []

    for board in board_data:
        boards.append(Bingo(board))

    for num in chosen:
        #print('Round {}: {}'.format(chosen.index(num),num))
        for board in boards:
            if board.play_round(num):
                result = board.check_bingo()
                if result:
                    print('Winning board is number {}'.format(boards.index(board)))
                    print(board)
                    amount = int(board.amount()) * int(num)
                    print(amount)
                    stop = (time.time() - start)*1000
                    print('Code ran in %f milliseconds' % stop)
                    return 0

if __name__ == "__main__":
    main()

