"""
Author: Chih-Yu Lee
Date: 01/27/2020
"""
import unittest

def classify_triangle(a, b, c):
    """
    a = smallest
    c = largest
    """
    if (a+b<=c):
        return 'Not a triangle!'
    elif (a*a + b*b == c*c):
        return 'Right triangle!'
    elif (a== b == c):
        return 'Equilateral triangle!'
    elif a==b or a==c or b==c:
        return 'Isosceles triangle!'
    else:
        return 'Scalene triangle!'


class TestClassifyTriangle(unittest.TestCase):

    def test_classify_triangle(self):
        a,b,c = (1,2,10)
        self.assertEqual(classify_triangle(a,b,c),'Not a triangle!')
        a,b,c = (3,4,5)
        self.assertEqual(classify_triangle(a,b,c),'Right triangle!')
        a,b,c = (6,6,6)
        self.assertEqual(classify_triangle(a,b,c),'Equilateral triangle!')
        a,b,c = (6,6,1)
        self.assertEqual(classify_triangle(a,b,c),'Isosceles triangle!')
        a,b,c = (2,3,4)
        self.assertEqual(classify_triangle(a,b,c),'Scalene triangle!')
        a,b,c = (3,4,5)
        self.assertNotEqual(classify_triangle(a,b,c),'Not a triangle!')

if __name__ == "__main__":
    a = input('Enter First lengths of the sides of a triangle:')
    b = input('Enter Second lengths of the sides of a triangle:')
    c = input('Enter Third lengths of the sides of a triangle:')
    try:
        lengths = sorted([float(a),float(b),float(c)])
    except ValueError:
        print('PLEASE ENTER NUMBER!') 
    else:
        a,b,c = lengths
        result = classify_triangle(a, b, c)
        print(result)
        unittest.main()

