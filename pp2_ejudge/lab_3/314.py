import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    q_index = n + 1
    q = int(input_data[q_index])
    
    current_pos = q_index + 1
    for _ in range(q):
        op = input_data[current_pos]
        if op == "abs":
            a = list(map(lambda x: abs(x), a))
            current_pos += 1
        else:
            x = int(input_data[current_pos + 1])
            if op == "add":
                a = list(map(lambda val: val + x, a))
            elif op == "multiply":
                a = list(map(lambda val: val * x, a))
            elif op == "power":
                a = list(map(lambda val: val ** x, a))
            current_pos += 2
            
    print(*(a))

if __name__ == "__main__":
    solve()