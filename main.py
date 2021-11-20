import sys
from PySide2.QtWidgets import QApplication, QLabel

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    ap = QApplication(sys.argv)
    la = QLabel("abcdef")
    la.resize(400,400)
    la.show()
    sys.exit(ap.exec_())