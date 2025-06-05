def horse(start, end):
    if ((abs(ord(start[0]) - ord(end[0])) == 1 and abs(int(start[1]) - int(end[1])) == 2) 
            or (abs(ord(start[0]) - ord(end[0])) == 2 and abs(int(start[1]) - int(end[1])) == 1)):
        print("True")
    else:
        print("False")