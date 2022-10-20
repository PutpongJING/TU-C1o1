"""
print(f'{"Number":6}{"Square":^10}')
print('-'*16)
for num in range(1,11):
    square = num ** 2
    print(f"{num:^6d}{square:^10d}")
print("-" * 16) 
"""
start = int(input("Enter the starting number :"))
end = int(input("How high shoud I go?"))
if start < end:
    print("=" * 16) 
    print(f'{"Number":6}{"Square":^10}')
    print('-'*16)
    for num in range(start, end):
        square = num ** 2
        print(f"{num:^6d}{square:^10d}")
    print("-" * 16) 
print("error")