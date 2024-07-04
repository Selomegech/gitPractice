t= int(input())
arr=[]
for i in range(t):
    arr.append(list(map(int, input().split())))

n = int(t-1/2)
elements= []
indexes=[]
indexess = []
for i in range(t):
    for j in range(t):
        if i == j or i+j == t-1:

            if [i,j] not in indexes:
                indexes.append([i,j])
                elements.append(arr[i][j])
        if  i == t//2 or j == t//2 :
             if [i,j] not in indexes:
                indexes.append([i,j])
                elements.append(arr[i][j])

print(sum(elements))





    