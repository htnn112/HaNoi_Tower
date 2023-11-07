#Python 3.7.4

'''
Những vấn đề cần cải thiện:
- get_place_input:
        + xét điều kiện của biến nhập vào (từ 1 tới 3)
        + yêu cầu nhập lại nếu nhập sai: in message nhập sai
        + yêu cầu nhập lại nếu lặp lại vị trí đang đứng: in message nhập lại
        + không tăng biến "moves" nếu nhập lặp lại vị trí đang đứng

- clear console mỗi khi nhập get_place_input

- print_visual_tower cần được tối ưu hóa, các construction, reversed_construction, construction_upside_dower nên được
 lưu dưới dạng mảng số học, và chỉ in visual ở output cuối cùng.
'''

def get_first_input():
    while True:
        try:
            num_floors = int(input("Enter the number of floors (between 3 and 9): "))
            if num_floors <= 2 or num_floors >= 10:
                raise ValueError
            break
        except ValueError:
            print("              INVALID INPUT.\n"
                  "Please enter a number between 3 and 9.")
    return  num_floors

class TowerOfHanoi():
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.towers = [[], [], []]
        self.moves = 0

        for i in range(num_floors, 0, -1):
            self.towers[0].append(i)

    def initialization(self, num_floors):
        # Init visual_tower:
        visual_tower = []

        # Init tops of visual_tower

        top = (num_floors+6)* " " + "_" + (num_floors+6)* " "
        tower_top = [top] * 3
        visual_tower.append(tower_top)

        # Init axises of visual_tower
        # axis = " " * (self.num_floors + 5) + "| |" + " " * (self.num_floors + 5)
        tower_axis_row = [" " * (self.num_floors + 5) + "| |" + " " * (self.num_floors + 5)] * 3
        for i in range(num_floors + 1):
            visual_tower.append(tower_axis_row)

        # Init bases of visual_tower
        tower_base = []
        for i in range(3):
            tower_base.append("(" +
                              "=" * (num_floors + 2) +
                              "TOWER=" +
                              str(i + 1) +
                              "=" * (num_floors + 2) +
                              ")")
        visual_tower.append(tower_base)
        return visual_tower

    def disk_and_mapping(self, num_floors):
        '''
            Hàm tạo các cấu trúc các đĩa dựa thep số num_floors(lớn hơn hoặc bằng 3), trụ tháp và gán giá trị tương ứng vào
            dictionary. Ví dụ:
            Nếu : num_floors = 5
            disk = [
                    '      (=DISK==1=)      ',
                    '     (==DISK==2==)     ',
                    '    (===DISK==3===)    ',
                    '   (====DISK==4====)   ',
                    '  (=====DISK==5=====)  ',
                    '          | |          ',
                    ]
            Hàm xuất ra dict có dạng:
            mapping = {
                         0: '         | |         ',
                         1: '      (DISK==1)      ',
                         2: '     (=DISK==2=)     ',
                         3: '    (==DISK==3==)    ',
                         4: '   (===DISK==4===)   ',
                         5: '  (====DISK==5====)  '}

            '''
        axis = " " * (self.num_floors + 5) + "| |" + " " * (self.num_floors + 5)
        disk = []
        disk.append(axis)
        for i in range(self.num_floors):
            disk.append(
                " " * (self.num_floors + 1 - i) +
                "(" +
                "=" * (i + 1) +
                "DISK" +
                "==" +
                str(i + 1) +
                "=" * (i + 1) +
                ")" +
                " " * (self.num_floors + 1 - i)
            )
        mapping = {}
        for i in range(len(disk)):
            mapping[i] = disk[i]
        return mapping

    def output_you_win(self):
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
        '''
        num_floors = 5
        towers = [
                    [5], [4], [3], [2], [1]
                    [],
                    [],
                 ]
        reversed_construction = [
                                 [0], [0], [0], [0], [0]
                                 [0], [0], [0], [0], [0]
                                 [0], [0], [0], [0], [0]
                                ]
        construction = [
                        [1], [0], [0]
                        [2], [0], [0]
                        [3], [0], [0]
                        [4], [0], [0]
                        [5], [0], [0]
                        ]
        '''
        visual_tower = self.initialization(num_floors)
        reversed_construction = [
            [0] * num_floors,
            [0] * num_floors,
            [0] * num_floors
        ]
        for j in range(3):
            for i in range(len(self.towers[j])):
                reversed_construction[j][i] = reversed_construction[j][i] + self.towers[j][i]
        '''
        mapping = {
            5: '  (=====DISK==5=====)  ',
            4: '   (====DISK==4====)   ',
            3: '    (===DISK==3===)    ',
            2: '     (==DISK==2==)     ',
            1: '      (=DISK==1=)      ',
            0: '          | |          ',
        }
        '''
        mapping = self.disk_and_mapping(self.num_floors)

        for sublist in reversed_construction:
            for i in range(len(sublist)):
                sublist[i] = mapping[sublist[i]]
        #Reshape  the reversed_construction/ Thay đổi kích thước của construction theo kiểu chuyển vị ma trận
        construction_up_side_down = [[reversed_construction[j][i] for j in range(len(reversed_construction))] for i in
                                     range(num_floors)]
        construction = [construction_up_side_down[num_floors - 1 - i] for i in range(num_floors)]

        #overwrite construction over visual_tower/ Ghi đè các giá trị của construction lên visual_tower
        for i in range(num_floors):
                visual_tower[2:2+num_floors] = construction

        #print visual_tower/ Vẽ visual_tower
        '''
        Số 3 là gồm 2 hàng thuộc về chóp của tower, 1 hàng thuộc về nền của tower
        '''
        for i in range(num_floors + 3):
            print(visual_tower[i][0], visual_tower[i][1], visual_tower[i][2])

    def get_source_input(self):
        while True:
            try:
                user_input_source = int(input("Move disk from: "))
                if user_input_source <= 0 or user_input_source >= 4:
                    raise ValueError("              INVALID INPUT.\n"
                                     "Please enter a valid disk's place that you want to pick the disk (from tower 1, 2 or 3)")
                else:
                    return user_input_source
            except ValueError as e:
                print("INVALID INPUT.\n" + str(e))

    def get_target_input(self, user_input_source):
        while True:
            try:
                user_input_target = int(input("Move disk to: "))
                if user_input_target <= 0 or user_input_target >= 4:
                    raise ValueError("              INVALID INPUT.\n"
                                     "Please enter a valid disk's place that you want to pick the disk (from tower 1, 2 or 3)")
                elif user_input_target == user_input_source:
                    raise ValueError("              INVALID INPUT.\n"
                                     "Please enter a valid tower number that you want to place the disk you have been picked")
                else:
                    return user_input_target
            except ValueError as e:
                print("INVALID INPUT.\n" + str(e))

    def get_place_input(self):
        print('Choose : 1, 2 or 3')
        user_input_source = self.get_source_input()
        user_input_target = self.get_target_input(user_input_source)
        return user_input_source - 1 , user_input_target - 1

    def move_floors(self):
        user_input = self.get_place_input()
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
            self.output_you_win()
        else:
            print('You have moved', self.moves, 'times')
            self.print_visual_tower()

    def play(self):
        self.print_visual_tower()
        while len(self.towers[1]) != self.num_floors and len(self.towers[2]) != self.num_floors:
            self.move_floors()

if __name__ == '__main__':
    num_floors = get_first_input()
    tower_of_hanoi = TowerOfHanoi(num_floors)
    tower_of_hanoi.play()