import turtle

# t = turtle.Turtle()
# t.circle(20)
# t1 = turtle.Turtle()
# t1.circle(25)
#
# t3 = turtle.Turtle()
# t3.circle(50)


def solution(n:int = 600851475143) -> int:
    """Returns the largest prime factor of a given number n.
       >>> solution(13195)
       29
       >>> solution(10)
       5
       >>> solution(17)
       17
       >>> solution(3.4)
       3
       >>> solution(0)
       Traceback (most recent call last):
           ...
       ValueError: Parameter n must be greater or equal to one.
       >>> solution(-17)
       Traceback (most recent call last):
           ...
       ValueError: Parameter n must be greater or equal to one.
       >>> solution([])
       Traceback (most recent call last):
           ...
       TypeError: Parameter n must be int or passive of cast to int.
       >>> solution("asd")
       Traceback (most recent call last):
           ...
       TypeError: Parameter n must be int or passive of cast to int.
       """
    try:
        n = int(n);
    except (TypeError,ValueError):
        raise TypeError("Parameter n must be int or passive of cast to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater or equal to one.")

    i = 2;
    ans = 0;

    if n == 2:
        return 2
    while n > 2:
        while n % i != 0:
            i+=1
        ans = i;

        while n % i == 0:
            n = n/i
        i += 1
    return int(ans);

def area_of_triangle(a:int,b:int,c:int) -> int:
    '''
    :param a:
    :param b:
    :param c:
    :return:  calculates area of traingle in efficient way
    '''
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def base_structure():
    fruits = ['apple', 'kiwi', 'mango']
    fruits.append("kiwi")

    print(fruits)

if __name__ == '__main__':
    base_structure()
    # print(area_of_triangle(5, 6, 7))
    # import doctest
    # doctest.testmod()
    # print(solution(int(input().strip())))