"""
--- Day 7: The Treachery of Whales ---
A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14
This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

Your puzzle answer was 342641.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?
"""

input_real = [1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,775,180,473,1346,1189,1553,196,427,788,25,159,204,851,24,1404,91,308,1096,747,278,1185,36,752,57,54,583,570,260,735,1192,72,552,103,693,383,202,78,1050,453,116,333,182,765,60,372,201,291,1642,49,80,918,98,1443,36,577,696,1289,56,220,56,51,550,1666,651,652,1508,70,40,1473,57,1065,32,6,537,1053,315,711,163,476,1006,3,1092,18,1304,237,358,457,888,36,639,39,1051,723,590,1242,210,1217,473,488,1554,729,776,307,375,243,186,436,94,451,1230,495,861,480,28,323,529,92,65,43,564,143,183,81,965,82,168,303,331,99,921,583,1349,182,353,626,150,475,1388,381,539,1190,664,923,1579,564,31,186,171,415,69,82,621,579,636,787,154,384,463,124,213,270,318,16,21,429,1285,1052,755,248,67,1021,20,165,789,7,456,18,1432,1379,3,108,96,40,42,1148,665,526,392,616,405,633,399,152,388,9,1078,159,454,945,330,2,455,288,288,72,313,827,521,939,186,680,253,386,917,317,346,1897,520,662,558,919,31,1141,1025,29,80,601,1001,199,128,1721,1221,367,29,722,186,344,136,415,718,122,7,879,195,1430,250,65,391,1296,154,39,647,861,175,18,448,131,568,322,20,290,828,844,135,622,409,236,40,341,767,31,917,5,335,27,205,63,18,1262,615,1819,291,1263,179,206,686,102,18,483,525,331,303,932,664,337,774,1080,22,177,891,780,523,362,38,219,281,72,861,48,1382,1497,249,343,404,292,1252,1,532,370,421,155,1728,110,1778,804,944,142,1508,155,967,1201,1066,706,613,1222,40,1000,558,616,693,378,124,35,91,514,1445,7,280,775,744,421,236,597,143,380,91,1564,111,1359,711,453,73,247,427,119,182,508,598,514,543,297,182,397,24,1317,107,766,428,877,580,1135,13,266,568,369,570,5,214,1222,150,225,93,1168,7,793,346,17,70,127,734,1428,1513,274,409,1291,498,958,535,37,268,994,165,662,59,125,267,557,28,259,77,1226,588,499,105,15,238,272,272,100,329,642,68,356,782,90,674,608,431,1,442,835,3,780,51,394,146,71,231,582,81,595,921,913,398,831,1107,491,801,371,407,746,1337,196,7,86,427,72,217,3,98,717,1268,991,187,103,256,616,172,125,831,1380,935,281,1534,435,868,1291,51,894,91,527,443,868,1300,72,1108,259,641,381,1103,580,422,310,953,97,8,198,1249,1069,342,953,464,66,648,683,184,702,1488,440,389,408,0,47,1023,45,63,999,131,73,135,256,1586,798,61,43,708,138,500,952,10,170,1287,956,1454,886,1117,405,1064,252,1218,334,316,1116,485,63,336,1218,528,309,86,833,168,955,45,993,841,480,336,512,835,296,285,340,81,1291,61,51,5,284,1114,120,794,1444,889,28,0,327,134,71,1040,230,48,49,837,1191,558,3,26,760,1038,104,320,87,464,270,115,357,277,285,488,1649,477,972,423,524,657,20,395,958,528,13,125,391,90,334,314,1022,1147,200,1357,1092,559,610,193,296,60,188,0,2,277,540,365,79,278,199,1327,573,615,95,677,285,143,182,226,12,661,492,189,526,75,1358,923,228,59,417,535,544,270,1040,197,2,216,1217,372,1034,84,16,725,1798,352,147,290,528,1091,105,476,725,137,474,75,1313,644,92,43,286,47,118,11,865,1316,1464,1189,673,67,612,183,379,309,464,207,31,64,1375,34,413,618,131,1459,178,179,81,245,316,223,230,697,337,977,188,1335,811,163,592,181,93,108,865,112,20,497,986,1124,73,128,96,107,1288,179,229,145,1293,1224,1308,748,768,143,38,33,1842,64,45,1209,984,269,371,1451,876,1372,65,275,173,1569,298,187,91,522,133,39,709,878,2,123,195,1435,1569,482,1047,322,382,796,38,903,24,950,387,510,460,570,499,545,561,158,383,213,978,1329,380,938,280,267,762,841,713,111,357,71,19,121,581,91,177,869,1138,173,14,145,155,21,353,340,1145,113,594,685,91,781,558,500,10,33,300,270,457,675,850,64,49,81,311,906,404,207,176,309,45,855,16,9,881,428,194,300,329,715,985,559,656,66,184,1529,8,1131,610,78,522,338,492,1378,47,163,448,111,700,3,19,796,876,224,212,51,524,273,597,980,0,10,205,8,985,38,876,6,91,435,1273,38,147,214,362,1,95,87,724,1126,807,378,105,89,276,1076,107,552,1082,32,896,202,177,946,753,1106,464,72,61,225,55]
input_example = [16,1,2,0,4,2,7,1,2,14]

def get_mode(input_list):
    res_dict = {}
    for pos in input_list:
        if pos in res_dict.keys():
            res_dict[pos] = res_dict[pos] + 1
        else:
            res_dict[pos] = 1
    max = 0
    res = 0
    for key in res_dict.keys():
        if res_dict[key] > max:
            max = res_dict[key]
            res = key
    return res 

def get_median(input_list):
    sorted_lst = sorted(input_list)
    n = len(sorted_lst)
    if n % 2 == 0:
        median1 = sorted_lst[n//2]
        median2 = sorted_lst[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = sorted_lst[n//2]
    return median

def get_mean(input_list):
    return sum(input_list)/len(input_list)

def get_fuel_solution_1(input_list):
    final_pos = get_median(input_list)
    total_fuel = 0
    for crab in input_list:
        total_fuel += abs(crab - final_pos)
    return total_fuel

def get_fuel_part_2(input_list, position):
    total_fuel = 0
    for crab in input_list:
        dist = abs(crab-position)
        total_fuel += (dist*(dist+1)/2)
    return total_fuel

def get_min_fuel_part_2(input_list):
    fuels = []
    for i in range(max(input_list)):
        fuels.append(get_fuel_part_2(input_list, i))
    return min(fuels)


# print(get_median(input_example))
# print(get_median(input_real))
# print(get_mode(input_real))
# print(get_fuel_solution_1(input_real))
print(get_min_fuel_part_2(input_real))

