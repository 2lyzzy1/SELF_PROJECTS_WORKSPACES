

def divisor(real: int) -> list:
    """ Find all divisor of all N integer """
    diviseurs=[]
    for i in range(1, real+1):
        if (real%i)==0: diviseurs.append(i)
    return diviseurs

def isPrime(reals: list[int]=[2]) -> list:
    """ Say (Check) if any N integer(s) are prime(s) or not """
    primaR=[]
    for real in reals:
        diviseurs=divisor(real)
        primaR.append( (real,True) if len(diviseurs)==2 else (real,False) )
    return primaR


# print ( isPrime(reals=[i for i in range(22)]) )
# print( isPrime([57, 77]) )
# - -----------------------------------------------------------------------------

def ppcm(a:int, b:int):
    """ Find the 'smallest common multiple' of a & b """
    SCM: int = None; aZ, bZ, aZ_bZ = None, None, None
    for x,y in zip(list([a]),list([b])):
        for z_ in range(10):
            aZ, bZ = set([x*z for z in range(z_)]), set([y*z for z in range(z_)])
            aZ_bZ = aZ & bZ
            print (aZ, bZ)
    return SCM
print (ppcm(5, 10))
def pgcd(a:int, b:int):
    """ Find the 'greatest common divisor' of a & b """
    GCD: int = None
    return GCD

