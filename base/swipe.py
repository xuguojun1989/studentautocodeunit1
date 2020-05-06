#coding=utf-8
import sys
sys.path.append("..")


class Swipe:
    def __init__(self,driver):
        self.driver=driver

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_up(self):
        x1 = self.get_size()[0] / 10 * 5
        y1 = self.get_size()[1] / 10 * 7
        y2 = self.get_size()[1] / 10 * 1
        self.driver.swipe(x1, y1, x1, y2)
