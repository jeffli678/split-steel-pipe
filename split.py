#encoding: utf-8
from collections import defaultdict
import math
import logging
import sys
import json

L = 6
demand = defaultdict(int)
output_name = 'output.txt'

def parse_config():
    config = open('config.txt').read()
    config = json.loads(config)
    L = 6
    log_level = logging.INFO

    log_level_map = {'info' : logging.INFO, 'debug' : logging.DEBUG}
    try:
        L = config['length']
        log_level_str = config['log_level']
        log_level = log_level_map[log_level_str]
    except:
        pass

    return L, log_level
    

def clear_output(outptu_name):
    with open(outptu_name, 'w'):
        pass

def print_demand():
    logging.info('You input is: ')
    lengths = sorted(demand, reverse = True)
    nums = [demand[l] for l in lengths]
    for i in range(len(lengths)):
        logging.info('%-10s' % lengths[i] + '\t' + str(nums[i]))

def count_pipe():
    sum = 0
    for _, v in demand.items():
        sum += v

    return sum

def total_len():
    sum = 0
    for k, v in demand.items():
        sum += k * v
    
    return sum

def read_input(file_name = 'input.txt'):
    global demand
    try:
        lines = open(file_name).read().splitlines()
    except:
        print('fail to read input from %s, please check. ' % file_name)
        print('exiting...')
        sys.exit(0)
        
    for line in lines:
        if line.startswith('#'): 
            continue
        try:
            l, n = line.split()
            demand[float(l)] += int(n)
        except:
            pass
        
    demand = {k:v for k,v in demand.items() if v != 0}

def find_next_feasible(lengths, len_remaining):

    for i, l in enumerate(lengths):
        if l < len_remaining:
            return (i, l)
    
    return (-1, 0)

def greedy():
    # pick longer ones first, and then shorters ones
    # if the shortest one does not fit into the current pipe
    # proceed to the next one

    lengths = sorted(demand, reverse = True)
    nums = [demand[l] for l in lengths]

    logging.debug(lengths)
    logging.debug(nums)

    cnt = sum(nums)
    N = 0
    result = []

    while cnt > 0:

        current_len = 0
        picked = []

        # emulate a do-while
        while True:

            idx, length = find_next_feasible(lengths, L - current_len)

            if idx == -1:
                # even the shortest one does not fit
                # start a new one
                N += 1
                break

            else:

                current_len += length
                picked.append(length)
                cnt -= 1
                nums[idx] -= 1
                if nums[idx] == 0:
                    del lengths[idx]
                    del nums[idx]

        result.append(picked)

    return N, result

def print_result(N, result):

    logging.info('')
    logging.info('You need %d steel pipes.' % N)
    logging.info('Steel pipe length: %dm.' % L)

    for i, picked in enumerate(result):
        output = '%d:\t' %  (i + 1)
        output += ', '.join([str(elem) for elem in picked])
        logging.info(output)

        used_len = sum(picked)
        wasted_len = L - used_len
        logging.debug('used: %.3f\t wasted: %.3f' % (used_len, wasted_len))

def main():

    # global L
    # L, log_level = parse_config()
    log_level = logging.INFO

    clear_output(output_name)
    logging.basicConfig(format = '%(message)s',\
                    filename = output_name, level = log_level)
    logging.info('=' * 50)

    read_input()
    print_demand()
    
    l = total_len()
    logging.debug('# of different lengths: %d' % len(demand))
    logging.debug('# of sections of steel pipes: %d' % count_pipe())
    logging.info('total length: %.3f' % l)
    min_n = int(math.ceil(l / L))
    logging.info('lower bound for N (may be unreachable): %d' % min_n)

    N, result = greedy()
    print_result(N, result)
    logging.info('=' * 50)
    print('Done! Please check "output.txt"')


if __name__ == '__main__':
    main()

