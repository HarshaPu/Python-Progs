def print_v_pattren(name):
    n=len(name)
    for i in range (n):
        for j in range(n*2):
            if j==i or j==n*2-1-i:
                print(name[i],end=' ')
            else:
                print(' ',end=' ')
        print()
                    
name="harsha"
print_v_pattren(name)