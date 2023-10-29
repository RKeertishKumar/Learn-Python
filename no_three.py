
# Accept the n value for t function
def main():
    n = int(input("What's n? "))
    print(three(n))
    
def three(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n>2:
        return three(n-1) + three(n-2) - three(n-3)
    
main()
    
        
    
    