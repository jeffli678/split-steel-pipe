#encoding: utf-8

def read_input(file_name = 'input.txt'):
    lines = open(file_name).read().splitlines()
    demand = {}
    for line in lines:
        if line.startswith('#'): 
            continue
        try:
            l, n = line.split()
            demand[float(l)] = int(n)
        except:
            pass
        
    return demand

def main():
    demand = read_input()
    print(demand)


if __name__ == '__main__':
    main()