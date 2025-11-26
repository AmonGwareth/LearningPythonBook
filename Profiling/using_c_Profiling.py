
from profiling_utils import calc_triples, calc_hypotenuse, is_int, calc_triples_faster, calc_triples_generator

# my_triples = calc_triples_faster(1000)

my_triples = list(calc_triples_generator(1000))
