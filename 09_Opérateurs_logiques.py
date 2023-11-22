# # Opérations *bit à bit* (*bitwise*)

# ## Compléments - niveau avancé

# Les compléments ci-dessous expliquent des fonctions évoluées sur les entiers. Les débutants en programmation peuvent sans souci sauter cette partie en cas de difficultés.

# ### Opérations logiques : *ET* `&`, *OU* `|` et *OU* exclusif `^`

# Il est possible aussi de faire des opérations *bit à bit* sur les nombres entiers. Le plus simple est de penser à l'écriture du nombre en base 2.
# 
# Considérons par exemple deux entiers constants dans cet exercice


x49 = 49
y81 = 81


# Ce qui nous donne comme décomposition binaire :
# 
# x49  =  32 + 16 + 1 ==> en binaire (0,1,1,0,0,0,1) 
# y81  =  64 + 16 + 1 ==> en binaire (1,0,1,0,0,0,1)

# Pour comprendre comment passer de 32 + 16 + 1$ à (0,1,1,0,0,0,1) il suffit d'observer que :
# 
# * 32 + 16 + 1 =
# * 2^6 +
# * 2^5 +
# * 2^4 +
# * 2^3 +
# * 2^2 +
# * 2^1 +
# * 2^0

# #### *ET* logique : opérateur `&`

# L'opération logique `&` va faire un *et* logique bit à bit entre les opérandes, ainsi

x49 & y81


# Et en effet :
# 
# x49        ==> en binaire (0,1,1,0,0,0,1) 
# y81        ==> en binaire (1,0,1,0,0,0,1) 
# x49 & y81  ==>     And    (0,0,1,0,0,0,1) 
# Donc       ==>                 16  +   1  = 17


# #### *OU* logique : opérateur `|`

# De même, l'opérateur logique `|` fait simplement un *ou* logique, comme ceci :

x49 | y81


# On s'y retrouve parce que :
# 
# x49        ==> en binaire (0,1,1,0,0,0,1) 
# y81        ==> en binaire (1,0,1,0,0,0,1)
# x49 | y81  == >     OR    (1,1,1,0,0,0,1) 
# Donc                      64 + 32 + 16 + 1 = 113


# #### *OU* exclusif : opérateur `^`

# Enfin, on peut également faire la même opération à base de *ou* exclusif avec l'opérateur `^` :

x49 ^ y81


# Je vous laisse le soin de décortiquer le calcul à titre d'exercice (le *ou* exclusif de deux bits est vrai si 
# et seulement si exactement une des deux entrées est vraie).

# ### Décalages
# Un décalage **à gauche** de, par exemple, 4 positions, revient à décaler tout le champ de bits de 4 cases à gauche 
#(les 4 nouveaux bits insérés sont toujours des 0). C'est donc équivalent à une **multiplication** par $2^4 = 16$ :

x49 << 4

# Et Donc :
# x49       ==> en binaire  (0,1,1,0,0,0,1) 
# x49 << 4  ==> ajout 4 bits à gauche (0,1,1,0,0,0,1,0,0,0,0) 
# Donc                                    512 + 256 + 16          = 784


# De la même manière, le décalage à **droite** de $n$ revient à une **division** par $2^n$ (plus précisément, le quotient de la division) :

x49 >> 4


# $\begin{array}{rcl}
# x49       ==> en binaire (0,1,1,0,0,0,1) 
# x49 >> 4  ==> décalage de 4 bits à droite (0,0,0,0,0,1,1) 
# Donc 												 2 + 1  = 3


# ### Une astuce
# On peut utiliser la fonction *built-in* `bin` pour calculer la représentation binaire d'un entier. 
# Attention, la valeur de retour est une chaîne de caractères de type `str` :

bin(x49)


# Dans l'autre sens, on peut aussi entrer un entier directement en base 2 comme ceci :

x49bis = 0b110001
x49bis == x49


# Ici, comme on le voit, `x49bis` est bien un entier.

# ### Pour en savoir plus

# [Section de la documentation Python](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types).
