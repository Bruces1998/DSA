'''
Points to Remember for Project Report:

- [ ]  Related approaches and their pros and cons
- [ ]  Overview of the algo be shorter and the implementation should be longer
- [ ]  Explain the implementation in clear manner
- [ ]  Code should match the algo description

'''
from collections import defaultdict
from itertools import combinations
import pandas as pd
from tabulate import tabulate

def pretty_print(array):
  # array = pd.DataFrame(array)

  print(tabulate(array))


def convert_to_binary(min_terms):
  binary_min_terms = []
  for term in min_terms:
    term = bin(term, )[2:]
    binary_min_terms.append(str(term).zfill(n_terms))

  return binary_min_terms

def combine_minterms(m1, m2):

    """ Combine two minterms if they differ by only one bit and have not been marked as combined."""

    diff_count = 0
    position = -1
    for i, (x, y) in enumerate(zip(m1, m2)):
        if x != y:
            diff_count += 1
            position = i
        if diff_count > 1:
            return None
    if diff_count == 1:
        result = list(m1)
        result[position] = '-'
        return ''.join(result)
    return None


def generate_prime_implicants(terms):

    current_terms = set(terms)
    next_terms = set()
    used = set()
    prime = set()

    while current_terms:
        for t1, t2 in combinations(current_terms, 2):
            res = combine_minterms(t1, t2)
            if res:
                next_terms.add(res)
                used.update([t1, t2])
        prime.update(current_terms - used)
        current_terms = next_terms
        next_terms = set()
        used = set()

    return list(prime)


def term_matches(term, implicant):

  for i in range(len(term)):
    if implicant[i] == '-' or implicant[i] == term[i]:
      continue
    else:
      return False

  return True


def branch_bound(binary_min_terms, prime_implicants):
  
  """
  The function takes input the min_terms and prime 
  implicants and returns the essential prime 
  implicants. 

  Data Structures:

  1.) min_mapper -> Stores list of prime implicants associated with a min_term and if its covered or not

  How it looks like

  {
    min_term1: { 
      prime_imps = [prime_imp1, prime_imp2, ......],
      covered = 0 or 1 
    }

    min_term2: {

    }
    .......so on

  }

  2.) prime_min_mapper -> reverse of min_mapper, stores min_terms associated with a prime_implicant

  How it looks like

  {
    prime_implicant1: [min_term1, min_term2, ...so on],
    
    primt_implicant2: [....]
  }

  3.) remaining_minterms -> List of terms that are not covered by the essential prime implicants

  How it looks like

  [min_term1, min_term2, min_term3, .....]

  4.) cover_mapper -> Stores the sorted count of remaining min_terms covered by prime_implicants

  How it looks like

  {
    prime_imp1: 3, (Count of remaining_min_terms_it_covers)
    prime_imp2: 2,
    prime_imp3: 1,
    .....so on
  }

  5.) essential_prime_implicants -> Stores the list of essential prime implicants. In the end it has all the final essential terms

  How it looks like

  [ess_prime_imp1, ess_prime_imp2, ......]


  """

  min_mapper = {}
  prime_min_mapper = defaultdict(list) 
  remaining_minterms = set() 
  cover_mapper = {} 
  essential_prime_implicants = set()


  for term in binary_min_terms:
    min_mapper[term] = {'prime_imps':[], 'covered':0}
    remaining_minterms.add(term)

    for imp in prime_implicants: 
      if term_matches(term, imp): #if a prime implicant and min_term match
        min_mapper[term]['prime_imps'].append(imp)
        prime_min_mapper[imp].append(term)



  
  for term in min_mapper:
    if len(min_mapper[term]['prime_imps']) == 1:
      current_essential_prime = min_mapper[term]['prime_imps'][0]
      essential_prime_implicants.add(current_essential_prime)
      min_mapper[term]['covered'] = 1
      if term in remaining_minterms:
        remaining_minterms.remove(term)

      for min_term in prime_min_mapper[current_essential_prime]:
        if min_mapper[min_term]['covered'] == 0:
          min_mapper[min_term]['covered'] = 1
          if min_term in remaining_minterms:
            remaining_minterms.remove(min_term)


  

  # print('Remaining minterms', remaining_minterms)
  # print('Essential Prime Implicants Before: ', essential_prime_implicants)

  for min_term in remaining_minterms:
    for prime_implicant in min_mapper[min_term]['prime_imps']:
      if cover_mapper.get(prime_implicant) is None:
        count = 0
        for covered_terms in prime_min_mapper[prime_implicant]:
          if covered_terms in remaining_minterms:
            count += 1

        cover_mapper[prime_implicant] = count

  for prime_implicant in sorted(cover_mapper.items(), key = lambda x: x[1]):
    if len(remaining_minterms) != 0:
      essential_prime_implicants.add(prime_implicant[0])
      for ele in prime_min_mapper[prime_implicant[0]]:
        if ele in remaining_minterms:
          remaining_minterms.remove(ele)

  return essential_prime_implicants



if __name__ == "__main__":
  n_terms = 10
  min_terms = [0,1,2,3,6,7,8,9,14,15, 20,28,45, 52,60, 136, 230, 411, 1021] #1024 -> 2^10
  binary_min_terms = convert_to_binary(min_terms)
  prime_implicants = generate_prime_implicants(binary_min_terms)
  final_prime_implicants = branch_bound(binary_min_terms, prime_implicants)

  print("Given Min Terms:" )
  pretty_print(binary_min_terms)

  print("\n")

  print("Prime Implicants:")
  pretty_print(prime_implicants)

  print("\n")

  print("Final Essential Prime Implicants:")
  pretty_print(final_prime_implicants)





