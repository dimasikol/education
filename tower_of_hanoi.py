import random
import sys
from operator import concat

TOTAL_DISK = 6
TOWERS = {'A':list(reversed(range(1,TOTAL_DISK+1))), 'B':[], 'C':[] }


def print_disk(disk_num):
    empty_space = ' ' * (TOTAL_DISK-disk_num)
    if disk_num == 0:
        sys.stdout.write(empty_space + '||'+empty_space)
    else:
        diskSpace = '@' * disk_num
        diskNumLabel = str(disk_num).rjust(2,'_')
        sys.stdout.write(empty_space+diskSpace+diskNumLabel+diskSpace+empty_space)

def print_towers():
    for level in range(TOTAL_DISK,-1,-1):
        for tower in (TOWERS["A"],TOWERS["B"],TOWERS["C"]):
            if level >= len(tower):
                print_disk(0)
            else:
                print_disk(tower[level])
        sys.stdout.write('\n')
    empty_space = ' ' * (TOTAL_DISK)
    print(f"{empty_space} A{empty_space}{empty_space} B{empty_space}{empty_space} ")

def moveOneDisk(start_tower,end_tower):
    disk = TOWERS[start_tower].pop()
    TOWERS[end_tower].append(disk)

def solve(num_of_disks, start_tower,end_tower,temp_tower):
        if num_of_disks == 1:
            moveOneDisk(start_tower, end_tower)
            print_towers()
        else:
            solve(num_of_disks-1, start_tower, temp_tower, end_tower)
            moveOneDisk(start_tower, end_tower)
            solve(num_of_disks-1, temp_tower, end_tower, start_tower)
            return
print_towers()
solve(TOTAL_DISK, 'A', 'B', 'C')


