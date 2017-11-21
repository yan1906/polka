from itertools import combinations

def check_palindrome(s):
    number = str(s)
    return number == number[::-1]

def is_prime(n):
  for x in range(2,int(n**0.5)+1):
    if not n%x:
      return False
  return True


prime_list = [x for x in xrange(99999,10000,-1) if is_prime(x)]
a = (max((p*q,p,q) for p,q in combinations(prime_list,2) if check_palindrome(p*q)))
print(a)