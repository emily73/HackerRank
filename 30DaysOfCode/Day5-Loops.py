#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        r = n*i
        print("%i x %i = %i" % (n, i, r))
