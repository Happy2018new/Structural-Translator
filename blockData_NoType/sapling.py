import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.ans["sapling_type"]
    #
    if type == 'oak':
        return 0
    if type == 'spruce':
        return 1
    if type == 'birch':
        return 2
    if type == 'jungle':
        return 3
    if type == 'acacia':
        return 4
    if type == 'dark_oak':
        return 5
    #