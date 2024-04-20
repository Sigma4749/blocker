"""
PROGRAM TO CALCULATE THE BLOCKER OF A CLUTTER USING BIT OPERATIONS TO DETERMINE THE
MINIMAL TRANSVERSALS

# Algorithm steps
# 1. Receive the base set and clutter as a text string and a list of text strings
# 2. Convert clutter sets to integers
# 3. The sequence of integers i is generated from 0 to 2**n, each one corresponds to a set of the power set
#   3.1 Compare with operation & if the generated set-number A is transversal of each set B of the clutter (i.e. A & B != 0)
#   3.2 To choose the minimal sets we have to: if A is a subset of B, then A | B = B

"""

def conjunto_a_entero(conjunto, conjunto_base):
    codificacion_entero = 0
    for dummy_index in range(len(conjunto_base)):
        if (conjunto_base[dummy_index] in conjunto):
            codificacion_entero += 2**(len(conjunto_base)-1-dummy_index)
    return codificacion_entero

def entero_a_conjunto(entero, conjunto_base):
    combo = ""
    for j in range(len(conjunto_base),-1,-1):
        if (entero >> j) % 2 == 1: 
            combo += conjunto_base[len(conjunto_base)-1-j]
    return(combo)


# Example: Hyperplanes of projective geometry PG(2,3)
conjunto_base = "123456789ABCD"
clutter = ["1238", "1459", "246A", "789A", "167B", "35AB", "257C", "369C", "48BC", "347D", "568D", "29BD", "1ACD"] 

print("Ground set: " + conjunto_base )
print("Given clutter: ", end=' ' )
for dummy_index in range(len(clutter)):
    print(clutter[dummy_index] , end=' ' )

print("\n\nBlocker clutter:", end='')
clutter_enteros = []

for conjunto in clutter:
    clutter_enteros.append(conjunto_a_entero(conjunto, conjunto_base))

formato = '{0:0' + str(len(conjunto_base)) + 'b}'

bloqueador = []
for i in range(2**len(conjunto_base)):
    flag = 1
    for h in clutter_enteros:
        if i & h == 0:  
            flag = 0
            break
    if flag == 1:
        # check if it is a minimal transversal
        flag = 1
        for conjunto in bloqueador:
            if conjunto | i == i:
                flag = 0
                break
        if flag == 1:
            bloqueador.append(i)

print("")

for entero in bloqueador:
    print(entero_a_conjunto(entero,conjunto_base), end= ' ')
print("\n")