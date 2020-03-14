def solution(brown, red):
    for height in range(1, int(red**(1/2))+1):
        if red % height == 0:
            width = red // height
            if 2*height + 2*width + 4 == brown:
                return [width + 2, height + 2]