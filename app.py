from LluitadorRandom import LluitadorRandom
from Ring import Ring

lluitador1 = LluitadorRandom("DestrossaCervells")
lluitador2 = LluitadorRandom("MatxacaPilotes")

ring = Ring()

ring.EntradaLluitadors(lluitador1, lluitador2)
resultat = ring.Lluiteu()

print(resultat[0], "vs", resultat[1])
