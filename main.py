#úkol 1
isWorking = True
index_to_pos = {0: [0, 0],
                        1: [0, 2],
                        2: [1, 1],
                        3: [1, -1],
                        4: [0, -2],
                        5: [-1, -1],
                        6: [-1, 1],
                        7: [0, 4],
                        8: [1, 3],
                        9: [2, 2],
                        10: [2, 0],
                        11: [2, -2],
                        12: [1, -3],
                        13: [0, -4],
                        14: [-1, -3],
                        15: [-2, -2],
                        16: [-2, 0],
                        17: [-2, 2],
                        18: [-1, 3],
                        19: [0, 6],
                        20: [1, 5],
                        21: [2, 4],
                        22: [3, 3],
                        23: [3, 1],
                        24: [3, -1],
                        25: [3, -3],
                        26: [2, -4],
                        27: [1, -5],
                        28: [0, -6],
                        29: [-1, -5],
                        30: [-2, -4],
                        31: [-3, -3],
                        32: [-3, -1],
                        33: [-3, 1],
                        34: [-3, 3],
                        35: [-2, 4],
                        36: [-1, 5],
                        37: [0, 8],
                        38: [1, 7],
                        39: [2, 6],
                        40: [3, 5],
                        41: [4, 4],
                        42: [4, 2],
                        43: [4, 0],
                        44: [4, -2],
                        45: [4, -4],
                        46: [3, -5],
                        47: [2, -6],
                        48: [1, -7],
                        49: [0, -8],
                        50: [-1, -7],
                        51: [-2, -6],
                        52: [-3, -5],
                        53: [-4, -4],
                        54: [-4, -2],
                        55: [-4, 0],
                        56: [-4, 2],
                        57: [-4, 4],
                        58: [-3, 5],
                        59: [-2, 6],
                        60: [-1, 7]}
while isWorking:
    cmd = input()
    if cmd == "exit":
        isWorking = False
    elif cmd == "get_name":
        print("Ivan_Zakablukov")
#úkol 2
    elif cmd.startswith("index_to_position"):
        #dict pro index:pozice
            parts = cmd.split()
            index = int(parts[1])
            print(index_to_pos[index])
    
    elif cmd.startswith("distance_between"):
         def hex_distance(index1, index2):
            q1, r1 = index_to_pos[index1]
            q2, r2 = index_to_pos[index2]
            dq = abs(q2 - q1)
            dr = abs(r2 - r1)
            return (dq + dr + 1) // 2

         parts = cmd.split()
         ind1 = int(parts[1])
         ind2 = int(parts[2])
         print(hex_distance(ind1, ind2))
