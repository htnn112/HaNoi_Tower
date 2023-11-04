#Python 3.7.4

visual_tower = [
['          _          ','          _          ','          _          '],#0 - 012
['         | |         ','         | |         ','         | |         '],#1 - 012
['         | |         ','         | |         ','         | |         '],#2 - 012
['         | |         ','         | |         ','         | |         '],#3 - 012
['         | |         ','         | |         ','         | |         '],#4 - 012
['         | |         ','         | |         ','         | |         '],#5 - 012
['         | |         ','         | |         ','         | |         '],#6 - 012
['(======TOWER=1======)','(======TOWER=2======)','(======TOWER=3======)'] #7 - 012
]

disk = ['      (DISK==1)      ',
        '     (=DISK==2=)     ',
        '    (==DISK==3==)    ',
        '   (===DISK==4===)   ',
        '  (====DISK==5====)  ',
        '         | |         ',]


class TowerOfHanoi():
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.towers = [[], [], []]
        self.moves = 0

        for i in range(num_floors, 0, -1):
            self.towers[0].append(i)

    def you_win(self):
        print("               \!!\      ////     !!!!!!!!!     !!!!       !!!!", end="\n")
        print("                \!!\    ////    !!!!!!!!!!!!!   !!!!       !!!!", end="\n")
        print("                 \!!\  ////    !!!!       !!!!  !!!!       !!!!", end="\n")
        print("                  \!!\////     !!!!       !!!!  !!!!       !!!!", end="\n")
        print("                   \!!!!/      !!!!       !!!!  !!!!       !!!!", end="\n")
        print("                    !!!!       !!!!       !!!!  !!!!       !!!!", end="\n")
        print("                    !!!!       !!!!       !!!!  !!!!       !!!!", end="\n")
        print("                    !!!!       !!!!       !!!!  !!!!       !!!!", end="\n")
        print("                    !!!!        !!!!!!!!!!!!!    !!!!!!!!!!!!!", end="\n")
        print("                    !!!!          !!!!!!!!!        !!!!!!!!!", end="\n")
        print(" \n ")
        print("        \!!!\                              ///!/  !!!!    !!!!\      !!!!", end="\n")
        print("         \!!!\                            ///!/   !!!!    !!!!!\     !!!!", end="\n")
        print("          \!!!\                          ///!/    !!!!    !!!!!!\    !!!!", end="\n")
        print("           \!!!\                        ///!/     !!!!    !!!!\!!\   !!!!", end="\n")
        print("            \!!!\                      ///!/      !!!!    !!!! \!!\  !!!!", end="\n")
        print("             \!!!\       !!!!!        ///!/       !!!!    !!!!  \!!\ !!!!", end="\n")
        print("              \!!!\     ///!!!!\     ///!/        !!!!    !!!!   \!!\!!!!", end="\n")
        print("               \!!!\   //!//\!!!\   ///!/         !!!!    !!!!    \!\!!!!", end="\n")
        print("                \!!!\!//!//  \!!!\!///!/          !!!!    !!!!     \!\!!!", end="\n")
        print("                 \!!!!!!!/    \!!!!!!!/           !!!!    !!!!      \!!!!", end="\n")
        print('                               YOU HAVE USE', self.moves, 'MOVES              ')

    def print_visual_tower(self):
        reversed_construction = [
            [0] * num_floors,
            [0] * num_floors,
            [0] * num_floors
        ]
        for j in range(3):
            for i in range(len(self.towers[j])):
                reversed_construction[j][i] = reversed_construction[j][i] + self.towers[j][i]

        mapping = {
            5: '  (====DISK==5====)  ',
            4: '   (===DISK==4===)   ',
            3: '    (==DISK==3==)    ',
            2: '     (=DISK==2=)     ',
            1: '      (DISK==1)      ',
            0: '         | |         ',
        }

        for sublist in reversed_construction:
            for i in range(len(sublist)):
                sublist[i] = mapping[sublist[i]]
        #Reshape  the reversed_construction
        construction = [[reversed_construction[j][i] for j in range(len(reversed_construction))] for i in
                        range(len(reversed_construction[0]))]
        #overwrite construction over visual_tower
        for i in range(num_floors):
            for j in range(3):
                visual_tower[6 - i][j] = construction[i][j]

        #print visual_tower
        for i in range(8):
            print(visual_tower[i][0], visual_tower[i][1], visual_tower[i][2])

    def get_user_input(self):
        print('Choose : 1, 2 or 3')
        user_input_source = int(input('From: '))
        user_input_target = int(input('To: '))
        return user_input_source - 1 , user_input_target - 1

    def move_floors(self):
        user_input = self.get_user_input()
        source = user_input[0]
        target = user_input[1]

        if len(self.towers[source]) == 0:
            print('Invalid move. Tower', source, 'is empty.')
        elif len(self.towers[target]) > 0 and self.towers[source][-1] > self.towers[target][-1]:
            print('Invalid move. Cannot place a larger floor on top of a smaller one.')
        else:
            floor_source = self.towers[source].pop()
            self.towers[target].append(floor_source)
            self.moves += 1
            self.print_game_state()

    def print_game_state(self):
        if len(self.towers[1]) == self.num_floors or len(self.towers[2]) == self.num_floors:
            self.print_visual_tower()
            self.you_win()
        else:
            print('You have moved', self.moves, 'times')
            self.print_visual_tower()
    def play(self):
        self.print_visual_tower()
        while len(self.towers[1]) != self.num_floors and len(self.towers[2]) != self.num_floors:
            self.move_floors()


if __name__ == '__main__':
    num_floors = int(input('Choose the number of floors (max number is 5): '))
    tower_of_hanoi = TowerOfHanoi(num_floors)
    tower_of_hanoi.play()