#!/usr/bin/python

import os
import sys
from math import atan
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QTransform

width = 500
height = 653
above_head = 70
head_height = 473
below_head = height - above_head - head_height


class GraphicsView(QtWidgets.QGraphicsView):
	def __init__(self, file_in, parent=None):
		super().__init__(parent)
		self.scene = QtWidgets.QGraphicsScene(self)
		self.setScene(self.scene)
		self.pixmap_item = QtWidgets.QGraphicsPixmapItem()
		self.scene.addItem(self.pixmap_item)
		self.image = QtGui.QPixmap(file_in)
		self.pixmap_item.setPixmap(self.image)
		self.showMaximized()
		self.clicks = []
		print("Click your eye")

	def mousePressEvent(self, event):
		if self.itemAt(event.pos()) is not self.pixmap_item:
			return
		point = self.pixmap_item.mapFromScene(self.mapToScene(event.pos())).toPoint()
		self.clicks.append(point)

		if len(self.clicks) == 1:
			print("Click the other eye")

		if len(self.clicks) == 2:
			self.eye_left, self.eye_right = self.clicks
			eye_dx = self.eye_right.x() - self.eye_left.x()
			if eye_dx == 0:
				return
			eye_dy = self.eye_right.y() - self.eye_left.y()
			self.angle = -atan(eye_dy/eye_dx)
			transform = QTransform().rotateRadians(self.angle)
			transform = self.image.trueMatrix(transform, self.image.width(), self.image.height())
			self.image = self.image.transformed(transform)
			self.pixmap_item.setPixmap(self.image)
			self.eye_left = transform.map(self.eye_left)
			self.eye_right = transform.map(self.eye_right)
			print("Click the top of your head")

		if len(self.clicks) == 3:
			print("Click the bottom of your head")

		if len(self.clicks) == 4:
			top, bottom = self.clicks[-2:]
			factor = head_height / (bottom.y()-top.y())
			crop_y = round(factor*top.y() - above_head)
			center_x = factor * (self.eye_left.x()+self.eye_right.x()) / 2
			crop_x = round(center_x - width/2)
			self.image = self.image.transformed(QTransform().scale(factor, factor))
			self.pixmap_item.setPixmap(self.image)
			self.image = self.image.copy(crop_x, crop_y, width, height)
			self.image.save(file_out)
			print("Done")
			sys.exit()


if len(sys.argv) != 3:
	print(f"{os.path.basename(__file__)} <input> <output>")
	sys.exit()

file_in = sys.argv[1]
file_out = sys.argv[2]

app = QtWidgets.QApplication(sys.argv)
view = GraphicsView(file_in)
app.exec()
