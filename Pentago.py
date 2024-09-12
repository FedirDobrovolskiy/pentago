class Game():
    def __init__(self):
        self.table = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
        self.round = 0
        self.lines = [[[0, 0],[1, 0],[2, 0],[3, 0],[4, 0]], 
                 [[1, 0],[2, 0],[3, 0],[4, 0],[5, 0]],
                 [[0, 1],[1, 1],[2, 1],[3, 1],[4, 1]],
                 [[1, 1],[2, 1],[3, 1],[4, 1],[5, 1]], 
                 [[0, 2],[1, 2],[2, 2],[3, 2],[4, 2]],
                 [[1, 2],[2, 2],[3, 2],[4, 2],[5, 2]], 
                 [[0, 3],[1, 3],[2, 3],[3, 3],[4, 3]],
                 [[1, 3],[2, 3],[3, 3],[4, 3],[5, 3]],
                 [[0, 4],[1, 4],[2, 4],[3, 4],[4, 4]],
                 [[1, 4],[2, 4],[3, 4],[4, 4],[5, 4]],
                 [[0, 5],[1, 5],[2, 5],[3, 5],[4, 5]],
                 [[1, 5],[2, 5],[3, 5],[4, 5],[5, 5]],
                 [[0, 0],[0, 1],[0, 2],[0, 3],[0, 4]],
                 [[0, 1],[0, 2],[0, 3],[0, 4],[0, 5]],
                 [[1, 0],[1, 1],[1, 2],[1, 3],[1, 4]],
                 [[1, 1],[1, 2],[1, 3],[1, 4],[1, 5]],
                 [[2, 0],[2, 1],[2, 2],[2, 3],[2, 4]],
                 [[2, 1],[2, 2],[2, 3],[2, 4],[2, 5]],
                 [[3, 0],[3, 1],[3, 2],[3, 3],[3, 4]],
                 [[3, 1],[3, 2],[3, 3],[3, 4],[3, 5]],
                 [[4, 0],[4, 1],[4, 2],[4, 3],[4, 4]],
                 [[4, 1],[4, 2],[4, 3],[4, 4],[4, 5]],
                 [[5, 0],[5, 1],[5, 2],[5, 3],[5, 4]],
                 [[5, 1],[5, 2],[5, 3],[5, 4],[5, 5]],
                 [[0, 0],[1, 1],[2, 2],[3, 3],[4, 4]],
                 [[1, 1],[2, 2],[3, 3],[4, 4],[5, 5]],
                 [[0, 5],[1, 4],[2, 3],[3, 2],[4, 1]],
                 [[1, 4],[2, 3],[3, 2],[4, 1],[5, 0]],
                 [[1, 0],[2, 1],[3, 2],[4, 3],[5, 4]],
                 [[0, 1],[1, 2],[2, 3],[3, 4],[4, 5]],
                 [[0, 4],[1, 3],[2, 2],[3, 1],[4, 0]],
                 [[1, 5],[2, 4],[3, 3],[4, 2],[5, 1]]]
    def rotation_clock(self, x, y):
        table_copy = self.table
        self.table[0 + x * 3][0 + y * 3] = table_copy[0 + x * 3][2 + y * 3]
        self.table[2 + x * 3][0 + y * 3] = table_copy[0 + x * 3][0 + y * 3]
        self.table[2 + x * 3][2 + y * 3] = table_copy[2 + x * 3][0 + y * 3]
        self.table[0 + x * 3][2 + y * 3] = table_copy[2 + x * 3][2 + y * 3]
        self.table[1 + x * 3][0 + y * 3] = table_copy[0 + x * 3][1 + y * 3]
        self.table[2 + x * 3][1 + y * 3] = table_copy[1 + x * 3][0 + y * 3]
        self.table[1 + x * 3][2 + y * 3] = table_copy[2 + x * 3][1 + y * 3]
        self.table[0 + x * 3][1 + y * 3] = table_copy[1 + x * 3][2 + y * 3]
    def rotation_unclock(self, x, y):
        table_copy = self.table
        self.table[0 + x * 3][0 + y * 3] = table_copy[2 + x * 3][0 + y * 3]
        self.table[2 + x * 3][0 + y * 3] = table_copy[2 + x * 3][2 + y * 3]
        self.table[2 + x * 3][2 + y * 3] = table_copy[0 + x * 3][2 + y * 3]
        self.table[0 + x * 3][2 + y * 3] = table_copy[0 + x * 3][0 + y * 3]
        self.table[1 + x * 3][0 + y * 3] = table_copy[2 + x * 3][1 + y * 3]
        self.table[2 + x * 3][1 + y * 3] = table_copy[1 + x * 3][2 + y * 3]
        self.table[1 + x * 3][2 + y * 3] = table_copy[0 + x * 3][1 + y * 3]
        self.table[0 + x * 3][1 + y * 3] = table_copy[1 + x * 3][0 + y * 3]
    def rotate(self, x, y, a):
        if(a == 0):
            self.rotation_clock(x, y)
        elif(a == 1):
            self.rotation_unclock(x, y)
    def move(self, x, y):
        self.table[x][y] = 2 - (self.round % 2)
        self.round += 1
    def check_for_win(self):
        lines_number = 32
        i = 0
        win1 = False
        win2 = False
        while(i < lines_number):
            k = 0
            while(k < 5):
                if(self.table[self.lines[i][k][0]][self.lines[i][k][1]] == 1):
                    k += 1
                else:
                    break
            if(k == 5):
                win1 = True
            k = 0
            while(k < 5):
                if(self.table[self.lines[i][k][0]][self.lines[i][k][1]] == 2):
                    k += 1
                else:
                    break
            if(k == 5):
                win2 = True
            i += 1
            if(win1 & win2):
                return "draw"
            elif(win1):
                return "1st player wins"
            elif(win2):
                return "2nd player wins"
            else:
                return False

Pentago = Game()
while(Pentago.check_for_win() == False):
    print("rotates: enter coordinates of quarter you want to rotate, then 0 if clockwise and 1 if not clockwise\nto move you have to write x (0-5) and y (0-5) to put your ball there, then you have to write what to rotate like it was said before\nexample of move: 43010 - first we put your ball to 4th column and 3rd row. Then we rotate lower left quarter clockwise.")
    for i in range(6):
        print(Pentago.table[i][0], Pentago.table[i][1], Pentago.table[i][2], Pentago.table[i][3], Pentago.table[i][4], Pentago.table[i][5])
    print("enter your move:")
    player_move = input()
    x = int(player_move[0])
    y = int(player_move[1])
    a = int(player_move[2])
    b = int(player_move[3])
    c = int(player_move[4])
    Pentago.move(x, y)
    Pentago.rotate(a, b, c)
    for i in range(6):
        print(Pentago.table[i][0], Pentago.table[i][1], Pentago.table[i][2], Pentago.table[i][3], Pentago.table[i][4], Pentago.table[i][5])
    input()
    