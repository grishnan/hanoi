#!/usr/bin/env python

class Tower:
    ''' класс для башен '''
    def __init__(self, volume = 0):
        ''' инициализатор '''
        self.volume    = volume # текущий объём башни
        self.tower = [disk for disk in range(self.volume, 0, -1)]

    def pushDisk(self, disk):
        ''' положить диск на башню '''
        self.tower.append(disk)
        self.__updateVolume__()

    def popDisk(self):
        ''' снять диск с башни '''
        disk = self.tower.pop()
        self.__updateVolume__()
        return disk

    def __updateVolume__(self):
        ''' внутренний метод для обновления текущего объема башни '''
        self.volume = len(self.tower)
