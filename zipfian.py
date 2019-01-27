# The Zipf distribution (also known as the zeta distribution)
# is a continuous probability distribution that satisfies Zipf’s law
# the frequency of an item is inversely proportional to its rank in a frequency table.
# Reference link: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.zipf.html

# a is distribution parameter (a > 1)
# size is number of elements
import numpy as np
import sys

a = int(sys.argv[1])
size = int(sys.argv[2])
output_file = sys.argv[3];
s = np.random.zipf(a, size)
with open(output_file, 'w') as zipf_dist:
    for i in range(0, len(s)):
        zipf_dist.write(str(i) + " " + str(s[i]) + '\n')

