# Blocker
## Some implementations to compute the blocker of a Sperner family.

A clutter or Sperner Family is a hypergraph $\displaystyle (V,E)$ with the added property that $\displaystyle A\not \subseteq B$ whenever $\displaystyle A,B\in E$ and $\displaystyle A\neq B$ (i.e. no edge properly contains another).


If $\displaystyle F=(V,E)$ is a clutter, then the blocker of $F$, denoted by $\displaystyle b(F)$, is the clutter with vertex set $V$ and edge set consisting of all minimal sets $\displaystyle B\subseteq V$ so that $ \displaystyle B \cap A \neq \emptyset $ for every $\displaystyle A\in E$. It can be shown that $\displaystyle b(b(F))=F$ (Edmonds & Fulkerson 1970), so blockers give us a type of duality.
