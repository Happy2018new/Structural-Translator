import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    weirdo_direction = share.ans["weirdo_direction"]
    upside_down_bit = share.ans["upside_down_bit"]
    #
    if upside_down_bit == 1:
        weirdo_direction = weirdo_direction + 4
    #
    return weirdo_direction