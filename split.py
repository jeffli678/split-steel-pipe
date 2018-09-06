#encoding: utf-8

L = 6
demand = {}

def solve_one_pipe():
    max_n = []
    all_len = demand.keys()
    for l in all_len:
        max_n.append(int(L / l))
    print(max_n)

def read_input(file_name = 'input.txt'):
    lines = open(file_name).read().splitlines()
    for line in lines:
        if line.startswith('#'): 
            continue
        try:
            l, n = line.split()
            demand[float(l)] = int(n)
        except:
            pass
        
def main():
    read_input()
    print(demand)
    solve_one_pipe()


if __name__ == '__main__':
    main()

