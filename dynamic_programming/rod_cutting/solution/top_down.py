import unittest

INF = 100000
r = [0] + [-1*INF]* 10

def top_down_rod_cutting(c, n):
    global r
    if(r[n] >= 0):
        return r[n]

    maximum_revenue = -1*INF

    if n == 0:
        maximum_revenue = 0
    
    else:
        for i in range(1, n+1):
            maximum_revenue = max(maximum_revenue, c[i] + top_down_rod_cutting(c, n-i))

    r[n] = maximum_revenue

    return r[n]

class RodCuttingTestCase(unittest.TestCase):
    def test_max_revenue(self):
        c = [1, 5, 8, 9, 10, 17, 17, 20] 
        length = len(c) 
        self.assertEqual(top_down_rod_cutting(c, length), 22)



if __name__ == '__main__':
    unittest.main() 