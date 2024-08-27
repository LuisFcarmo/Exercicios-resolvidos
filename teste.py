from math import floor, pow, sqrt
from dataclasses import dataclass

@dataclass
class pair:
    numerador: int 
    denominador: int

def inteiro(num: int) -> bool:
    return isinstance(num, int)

def d_max(num: int) -> int:
    return floor(pow(num, 1.0/4.0)/3)

def calcular_convergente(convergentes, indices, iesimo):
    if iesimo == 0:
        convergentes[0] = pair(indices[0], 1)
        print(convergentes[0].numerador, convergentes[0].denominador)
    elif iesimo == 1:
        convergentes[1] = pair(indices[0] * indices[1] + 1, indices[1])
    else:
        convergentes.append(
            pair(
                indices[iesimo]*convergentes[iesimo-1].numerador + convergentes[iesimo-2].numerador,
                indices[iesimo]*convergentes[iesimo-1].denominador + convergentes[iesimo-2].denominador
            )
        )
        
def verificar(exp_pub, mod_N, dlinha, klinha):
    if klinha == 0: return False
    phi = (exp_pub*dlinha-1)/klinha
    x = (mod_N - phi + 1)/2
    y = sqrt(x*x - mod_N)

    if (inteiro(phi) and inteiro(x) and inteiro(y)):
        return True
    return False

def WienerAttack(p, q, convergentes, i):
    indices = []
    exp_pub = p
    mod_N = q
    dmax = (d_max(mod_N))

    while(q != 0):
        indices.append(int(p/q))
        calcular_convergente(convergentes, indices, i)
        
        if(verificar(exp_pub, mod_N, convergentes[i].denominador, convergentes[i].numerador)):
            print(convergentes[i].denominador, convergentes[i].numerador)
            return True
        if(convergentes[i].denominador > dmax):
            return False
        
        i += 1
        auxiliar = p % q
        p = q
        q = auxiliar

    return False

def chaveprivada(convergentes, iesimo, exp_pub, mod_n):
    phi = (exp_pub*convergentes[iesimo].denominador - 1)/convergentes[iesimo].numerador;
    x = (mod_n - phi + 1)/2 ;
    y = sqrt(x*x - mod_n);
    p = x - y;
    q = x + y;

    print(f"(p,q,d) p = {p} q = {q} d = {convergentes[iesimo].denominador}")

mod_N = 0
exp_pub = 0
iesimo = 0
convergentes = 2*[0]

mod_N = int(input("digite o valor n"))
exp_pub = int(input("digite o valor do expoente publico"))


if (WienerAttack(exp_pub, mod_N, convergentes, iesimo)):
    chaveprivada(convergentes, iesimo, exp_pub, mod_N)
else:
    print("Ataque de Wiener ineficiente\n");

