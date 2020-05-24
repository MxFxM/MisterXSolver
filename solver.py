# location, taxi-targets, bus-targets, subway-targets, boat-target
london = [[0,   [], [], [], []],
          [1,   [8, 9], [58, 46], [46], []],
          [2,   [10, 20], [], [], []],
          [3,   [4, 11, 12], [22, 23], [], []],
          [4,   [3, 13], [], [], []],
          [5,   [15, 16], [], [], []],
          [6,   [7, 29], [], [], []],
          [7,   [6, 17], [42], [], []],
          [8,   [1, 18, 19], [], [], []],
          [9,   [1, 19, 20], [], [], []],
          [10,  [2, 11, 21, 34], [], [], []],
          [11,  [3, 10, 22], [], [], []],
          [12,  [3, 23], [], [], []],
          [13,  [4, 23, 24], [14, 23, 52], [46, 67, 89], []],
          [14,  [15, 25], [13, 15], [], []],
          [15,  [5, 14, 16, 26, 28], [14, 29], [], []],
          [16,  [5, 15, 28, 29], [], [], []],
          [17,  [7, 29, 30, 42], [], [], []],
          [18,  [8, 31, 42], [], [], []],
          [19,  [8, 9, 32], [], [], []],
          [20,  [2, 9, 33], [], [], []],
          [21,  [10, 33], [], [], []],
          [22,  [11, 23, 34, 35], [3, 23, 34, 65], [], []],
          [23,  [12, 13, 22, 37], [3, 13, 22, 67], [], []],
          [24,  [13, 37, 38], [], [], []],
          [25,  [14, 38, 39], [], [], []],
          [26,  [15, 27, 39], [], [], []],
          [27,  [26, 28, 40], [], [], []],
          [28,  [15, 16, 27, 41], [], [], []],
          [29,  [6, 16, 17, 41, 42], [15, 41, 42, 55], [], []],
          [30,  [17, 42], [], [], []],
          [31,  [18, 43, 44], [], [], []],
          [32,  [19, 33, 44, 45], [], [], []],
          [33,  [20, 21, 32, 46], [], [], []],
          [34,  [10, 22, 47, 48], [22, 46, 63], [], []],
          [35,  [22, 36, 48, 65], [], [], []],
          [36,  [35, 37, 49], [], [], []],
          [37,  [23, 24, 36, 50], [], [], []],
          [38,  [24, 25, 50, 51], [], [], []],
          [39,  [25, 26, 51, 52], [], [], []],
          [40,  [27, 41, 52, 53], [], [], []],
          [41,  [28, 29, 40, 54], [15, 29, 52, 87], [], []],
          [42,  [29, 30, 56, 72], [7, 29, 72], [], []],
          [43,  [18, 31, 57], [], [], []],
          [44,  [31, 32, 58], [], [], []],
          [45,  [32, 46, 58, 59, 60], [], [], []],
          [46,  [33, 45, 47, 61], [1, 34, 58, 78], [1, 13, 74, 79], []],
          [47,  [34, 46, 62], [], [], []],
          [48,  [34, 35, 62, 63], [], [], []],
          [49,  [36, 50, 66], [], [], []],
          [50,  [37, 38, 49], [], [], []],
          [51,  [38, 39, 52, 67, 68], [], [], []],
          [52,  [39, 40, 51, 69], [13, 41, 67, 86], [], []],
          [53,  [40, 54, 69], [], [], []],
          [54,  [41, 53, 55, 70], [], [], []],
          [55,  [54, 71], [29, 89], [], []],
          [56,  [42, 91], [], [], []],
          [57,  [43, 58, 73], [], [], []],
          [58,  [44, 45, 57, 59, 74], [1, 46, 74, 77], [], []],
          [59,  [45, 58, 75, 76], [], [], []],
          [60,  [45, 61, 76], [], [], []],
          [61,  [46, 60, 62, 76, 78], [], [], []],
          [62,  [47, 48, 61, 79], [], [], []],
          [63,  [48, 64, 79, 80], [34, 65, 79, 100], [], []],
          [64,  [63, 65, 80], [], [], []],
          [65,  [35, 64, 66, 82], [22, 63, 67, 82], [], []],
          [66,  [49, 65, 67, 82], [], [], []],
          [67,  [51, 66, 68, 84], [23, 52, 65, 82, 102], [13, 79, 89, 111], []],
          [68,  [51, 67, 69, 85], [], [], []],
          [69,  [52, 53, 68, 86], [], [], []],
          [70,  [54, 71, 87], [], [], []],
          [71,  [55, 70, 72, 89], [], [], []],
          [72,  [42, 71, 90, 91], [42, 105, 107], [], []],
          [73,  [57, 74, 92], [], [], []],
          [74,  [58, 73, 92], [58, 94], [46], []],
          [75,  [58, 59, 74, 94], [], [], []],
          [76,  [59, 60, 61, 77], [], [], []],
          [77,  [76, 78, 95, 96], [58, 78, 94, 124], [], []],
          [78,  [61, 77, 79, 97], [46, 77, 79], [], []],
          [79,  [62, 63, 78, 98], [63, 78], [46, 67, 93, 111], []],
          [80,  [63, 99, 100], [], [], []],
          [81,  [64, 82, 100], [], [], []],
          [82,  [65, 66, 81, 101], [65, 67, 100, 140], [], []],
          [83,  [101, 102], [], [], []],
          [84,  [67, 85], [], [], []],
          [85,  [68, 84, 103], [], [], []],
          [86,  [69, 103, 104], [52, 87, 102, 116], [], []],
          [87,  [70, 88], [41, 86, 105], [], []],
          [88,  [87, 89, 117], [], [], []],
          [89,  [71, 88, 105], [55, 105], [13, 67, 128, 140], []],
          [90,  [72, 91, 105], [], [], []],
          [91,  [56, 72, 90, 105, 107], [], [], []],
          [92,  [73, 74, 93], [], [], []],
          [93,  [92, 94], [94], [79], []],
          [94,  [75, 93, 95], [74, 93, 77], [], []],
          [95,  [77, 94, 122], [], [], []],
          [96,  [77, 97, 109], [], [], []],
          [97,  [78, 96, 98, 109], [], [], []],
          [98,  [79, 97, 99, 110], [], [], []],
          [99,  [80, 98, 110, 112], [], [], []],
          [100, [80, 81, 101, 112, 113], [63, 82, 111], [], []],
          [101, [82, 83, 100, 114], [], [], []],
          [102, [83, 103, 115], [67, 86, 127], [], []],
          [103, [85, 86, 102], [], [], []],
          [104, [86, 116], [], [], []],
          [105, [89, 90, 91, 106, 108], [72, 87, 89, 107, 108], [], []],
          [106, [105, 107], [], [], []],
          [107, [91, 106, 119], [72, 105, 161], [], []],
          [108, [105, 117, 119], [105, 116, 135], [], [115]],
          [109, [96, 97, 110, 124], [], [], []],
          [110, [98, 99, 109, 111], [], [], []],
          [111, [110, 112, 124], [100, 124], [67, 79, 153, 163], []],
          [112, [99, 100, 111, 125], [], [], []],
          [113, [100, 114, 125], [], [], []],
          [114, [101, 113, 115, 126, 131, 132], [], [], []],
          [115, [102, 114, 126, 127], [], [], [108, 157]],
          [116, [104, 117, 118, 127], [86, 108, 127, 142], [], []],
          [117, [88, 108, 116, 129], [], [], []],
          [118, [116, 129, 134, 142], [], [], []],
          [119, [107, 108, 136], [], [], []],
          [120, [121, 144], [], [], []],
          [121, [120, 122, 145], [], [], []],
          [122, [95, 121, 123, 146], [123, 144], [], []],
          [123, [124, 122, 137, 148, 149], [122, 124, 144, 165], [], []],
          [124, [109, 111, 123, 138], [77, 111, 123, 153], [], []],
          [125, [112, 113, 131], [], [], []],
          [126, [114, 115, 140], [], [], []],
          [127, [115, 116, 126, 133, 134], [102, 116, 133], [], []],
          [128, [142, 143, 160, 168, 172], [135, 142, 161, 187, 199], [89, 140, 185], []],
          [129, [117, 118, 135, 142, 143], [], [], []],
          [130, [124, 131, 139], [], [], []],
          [131, [114, 125, 130], [], [], []],
          [132, [114, 140], [], [], []],
          [133, [127, 140, 141], [127, 140, 157], [], []],
          [134, [118, 127, 141, 142], [], [], []],
          [135, [129, 136, 143, 161], [108, 142, 161], [], []],
          [136, [119, 135, 162], [], [], []],
          [137, [123, 147], [], [], []],
          [138, [124, 150, 152], [], [], []],
          [139, [130, 140, 153, 154], [], [], []],
          [140, [126, 132, 133, 139, 154, 156], [82, 133, 154, 156], [89, 128, 153], []],
          [141, [133, 134, 142, 158], [], [], []],
          [142, [118, 128, 129, 134, 141, 143, 158], [116, 128, 157], [], []],
          [143, [128, 129, 135, 142, 160], [], [], []],
          [144, [120, 145, 177], [122, 123, 163], [], []],
          [145, [121, 144, 146], [], [], []],
          [146, [122, 145, 147, 163], [], [], []],
          [147, [137, 146, 164], [], [], []],
          [148, [123, 149, 164], [], [], []],
          [149, [123, 148, 150, 165], [], [], []],
          [150, [138, 149, 151], [], [], []],
          [151, [150, 152, 165, 166], [], [], []],
          [152, [138, 151, 153], [], [], []],
          [153, [139, 152, 154, 166, 167], [124, 154, 180, 184], [111, 140, 163, 185], []],
          [154, [139, 140, 153, 155], [140, 153, 156], [], []],
          [155, [154, 156, 167, 168], [], [], []],
          [156, [140, 155, 157, 169], [140, 154, 157, 184], [], []],
          [157, [156, 158, 170], [133, 142, 156, 185], [], [115, 194]],
          [158, [141, 142, 157, 159], [], [], []],
          [159, [158, 170, 172, 186, 198], [], [], []],
          [160, [128, 143, 161, 173], [], [], []],
          [161, [135, 160, 174], [107, 128, 199], [], []],
          [162, [136, 175], [], [], []],
          [163, [146, 177], [144, 176, 191], [111, 153], []],
          [164, [147, 148, 178, 179], [], [], []],
          [165, [149, 151, 179, 180], [123, 180, 191], [], []],
          [166, [151, 152, 181, 183], [], [], []],
          [167, [153, 155, 168, 183], [], [], []],
          [168, [155, 167, 184], [], [], []],
          [169, [156, 184], [], [], []],
          [170, [157, 159, 185], [], [], []],
          [171, [173, 175, 199], [], [], []],
          [172, [128, 159, 187], [], [], []],
          [173, [160, 171, 174, 188], [], [], []],
          [174, [161, 173, 175], [], [], []],
          [175, [162, 171, 174], [], [], []],
          [176, [177, 189], [163, 190], [], []],
          [177, [144, 163, 176], [], [], []],
          [178, [164, 189, 191], [], [], []],
          [179, [164, 165, 191], [], [], []],
          [180, [165, 181, 193], [153, 165, 184, 190], [], []],
          [181, [166, 180, 182, 193], [], [], []],
          [182, [181, 183, 195], [], [], []],
          [183, [166, 167, 182, 196], [], [], []],
          [184, [168, 169, 185, 196, 197], [153, 156, 180, 185], [], []],
          [185, [170, 184, 186], [157, 184, 187], [128, 153], []],
          [186, [159, 185, 198], [], [], []],
          [187, [172, 188, 198], [128, 185], [], []],
          [188, [128, 173, 187, 199], [], [], []],
          [189, [176, 178, 190], [], [], []],
          [190, [189, 191, 192], [176, 180, 191], [], []],
          [191, [178, 179, 190, 192], [163, 165, 190], [], []],
          [192, [190, 191, 194], [], [], []],
          [193, [180, 181, 194], [], [], []],
          [194, [192, 193, 195], [], [], [157]],
          [195, [182, 194, 197], [], [], []],
          [196, [183, 184, 197], [], [], []],
          [197, [184, 195, 196], [], [], []],
          [198, [159, 186, 187, 199], [], [], []],
          [199, [171, 188, 198], [128, 161], [], []]]

def get_possible_stations(city, station, ticket):
    # this collects all possible stations
    possible_stations = []

    # if not black ticket
    if ticket != 4:
        # every possible next station
        for possible_station in city[station][ticket]:
            # gets appended to the result
            possible_stations.append(possible_station)
    
    # black ticket
    else:
        # every possible ticket, including black
        for ticket in [1, 2, 3, 4]:
            # every possible next station
            for possible_station in city[station][ticket]:
                # if it is not already in the list
                if not possible_station in possible_stations:
                    # gets appended to the result
                    possible_stations.append(possible_station)
    
    # clean the result
    possible_stations.sort()

    # return all possible stations
    return possible_stations

# zero for unknown start station
start_station = 4

# possible moves:
# 1 = taxi
# 2 = bus
# 3 = subway
# 4 = black-ticket (any)
tickets = [1, 3, 4]

result = [start_station]

for ticket in tickets:
    last_result = result.copy()
    result = []
    for station in last_result:
        next_result = get_possible_stations(london, station, ticket)
        for next_station in next_result:
            if not next_station in result:
                result.append(next_station)

print(result)