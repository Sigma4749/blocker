# Blocker
## Some implementations to compute the blocker of a Sperner family.

A clutter or Sperner Family is a hypergraph $\displaystyle (V,E)$ with the added property that $\displaystyle A\not \subseteq B$ whenever $\displaystyle A,B\in E$ and $\displaystyle A\neq B$ (i.e. no edge properly contains another).

If $\displaystyle F=(V,E)$ is a clutter, then the blocker of $F$, denoted by $\displaystyle b(F)$, is the clutter with vertex set $V$ and edge set consisting of all minimal sets $\displaystyle B\subseteq V$ so that $B \cap A \neq \emptyset$ for every $\displaystyle A\in E$. It can be shown that $\displaystyle b(b(F))=F$ (Edmonds & Fulkerson 1970), so blockers give us a type of duality.

# How to use the code?
This code calculates the blocker of a given clutter.  You only need to write the ground set and the collection of sets in the lines 30 and 31.

'''python
conjunto_base = "123456789ABCD"
clutter = ["1238", "1459", "246A", "789A", "167B", "35AB", "257C", "369C", "48BC", "347D", "568D", "29BD", "1ACD"] 
'''
