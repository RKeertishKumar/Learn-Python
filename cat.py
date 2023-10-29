
def main():
    n =  get_num()
    meow(n)
    
def meow(n):
    print("meow\n" * n,end="")
    
def get_num():
    while True:
        num = int(input("What's n? "))
        if num>0:
            return num
        
main()