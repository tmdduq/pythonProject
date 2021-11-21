# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as nu

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

7
def squre(inte):
    return inte*inte


if __name__ == '__main__':
    print_hi('PyCharm')

    s = pd.Series([1, 3, 5, nu.nan, 6, 8])
    print(s)

    dates = pd.date_range(start='20210101', end='20211231', freq='MS')
    #freq = M(Month End), MS(Month Start), D(Day) // 3D(3Day)

    print(dates)
    df = pd.DataFrame(nu.random.randn(12, 4), index=dates, columns=list("ABCD"))
    #randn - 가우시안분포 난수 매트릭스 생성
    #rand - 0~1 난수 매트릭스 생성
    #randint - 지정범위 내 난수 생성
    print(df)