def colorHouse(N, red, green, blue, latest_color=None, count=0):
    if count == N:
        return 0

    if latest_color==None:
        return min(
            red[count] + colorHouse(N, red, green, blue, 'r', count+1 ), 
            green[count] + colorHouse(N, red, green, blue, 'g', count+1), 
            blue[count] + colorHouse(N, red, green, blue, 'b', count+1) 
        )
    elif latest_color=='r':
        return min(
            green[count] + colorHouse(N, red, green, blue, 'g', count+1), 
            blue[count] + colorHouse(N, red, green, blue, 'b', count+1) 
        )
    elif latest_color=='g':
        return min(
            red[count] + colorHouse(N, red, green, blue, 'r', count+1 ), 
            blue[count] + colorHouse(N, red, green, blue, 'b', count+1) 
        )
    else:
        return min(
            red[count] + colorHouse(N, red, green, blue, 'r', count+1 ), 
            green[count] + colorHouse(N, red, green, blue, 'g', count+1) 
        )


N = 3
Red = [6, 5, 3]
Green = [3, 1, 6]
Blue =  [9, 4, 2]
out = colorHouse(N, Red, Green, Blue)
print("Minimum cost to paint houses: ", out)
