def check(grid):
    if grid[0][0] == "." and grid[1][1] == "." or grid[0][1] == "." and grid[1][0] == ".":
        return False
    return True

a = input().strip()
b = input().strip()

grid = [list(a) ,list(b)]

if check(grid):
    print("Yes")
else:
    print("No")