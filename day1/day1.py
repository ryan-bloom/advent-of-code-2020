"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

test_arr = [1721, 979, 366, 299, 675, 1456]

input_arr = [
    1664,
    1939,
    1658,
    1791,
    1011,
    1600,
    1587,
    1930,
    1846,
    1955,
    1885,
    1793,
    1876,
    1905,
    1997,
    1900,
    1956,
    1981,
    1890,
    1612,
    638,
    1897,
    1888,
    1742,
    1613,
    1982,
    1932,
    1923,
    1065,
    1827,
    1919,
    1236,
    1195,
    1917,
    1990,
    1764,
    1902,
    1911,
    1999,
    1906,
    1817,
    1841,
    368,
    747,
    1881,
    1941,
    1894,
    1898,
    1887,
    1958,
    1862,
    1940,
    1819,
    1873,
    1959,
    1977,
    1301,
    1945,
    1961,
    1673,
    1879,
    1889,
    1872,
    155,
    1718,
    1637,
    1899,
    1988,
    1720,
    1856,
    1816,
    1866,
    1963,
    1880,
    1884,
    1970,
    1985,
    1869,
    1686,
    1832,
    1697,
    1381,
    1585,
    1993,
    2000,
    587,
    1891,
    1928,
    1721,
    1904,
    1708,
    1934,
    1912,
    1927,
    1575,
    1802,
    2009,
    1871,
    1867,
    1882,
    1974,
    1994,
    784,
    1868,
    1967,
    1842,
    1771,
    2001,
    1843,
    1621,
    1926,
    1978,
    2003,
    1921,
    1815,
    1757,
    2005,
    1699,
    1960,
    2007,
    1626,
    1944,
    2008,
    1611,
    2004,
    1991,
    1924,
    1875,
    1915,
    1920,
    1810,
    1805,
    1936,
    1968,
    882,
    1976,
    1874,
    1987,
    1826,
    1910,
    1483,
    1964,
    1855,
    1979,
    1996,
    438,
    1863,
    1952,
    1929,
    1986,
    1937,
    1773,
    1861,
    1909,
    1870,
    1922,
    1623,
    1948,
    1984,
    1957,
    1755,
    1655,
    1950,
    1635,
    2006,
    1618,
    1966,
    1735,
    1935,
    1908,
    1589,
    1886,
    1971,
    1949,
    1707,
    1995,
    1992,
    1953,
    1925,
    1783,
    1954,
    1998,
    1980,
    1644,
    1916,
    1883,
    1913,
    1962,
    1972,
    1602,
    1896,
    1969,
    1596,
    1680,
    1907,
    1983,
    1784,
    1671,
    1807,
    1943,
]


def find_two(total, input_arr):
    for number in input_arr:
        looking_for = total - number
        if looking_for in input_arr:
            return number * looking_for
    return False


assert find_two(2020, test_arr) == 514579

print("solution 1:", find_two(2020, input_arr))


def find_three(total, input_arr):
    for number in input_arr:
        new_total = total - number
        if found := find_two(new_total, input_arr):
            return number * found


assert find_three(2020, test_arr) == 241861950

print("solution 2:", find_three(2020, input_arr))
