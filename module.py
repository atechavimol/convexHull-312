from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
	from PyQt5.QtCore import QLineF, QPointF, QObject
elif PYQT_VER == 'PYQT4':
	from PyQt4.QtCore import QLineF, QPointF, QObject
else:
	raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))


class Node:
    def __init__(self, point):
        self.point = point
        # self.next = self,
        # self.prev = self
        self.set_pointers()

    def set_pointers(self):
        self.next = self
        self.prev = self


class Hull:
    def __init__(self, leftmost, rightmost):
        self.leftmost = leftmost
        self.rightmost = rightmost

    def get_lines(self):
        iterator = self.leftmost.next
        lines = []
        while iterator != self.leftmost:
            lines.append(QLineF(iterator.point, iterator.next.point))
            iterator = iterator.next

        lines.append(QLineF(iterator.point, iterator.next.point))

        return lines