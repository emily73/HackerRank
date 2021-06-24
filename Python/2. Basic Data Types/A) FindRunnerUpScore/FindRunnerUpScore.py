if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    max1=arr[-1]
    arr.sort(reverse=True)
    for i in arr:
        if i!=max1:
            result = i
            print(result)
            break
