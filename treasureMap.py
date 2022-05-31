row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Vertical and horizontal (1,3) ")
separatePosition = position.split(",")
verticalPosition = int(separatePosition[0])
horizontalPosition = int(separatePosition[1])


map[verticalPosition-1][horizontalPosition-1]="X"

print(f"{row1}\n{row2}\n{row3}")