# Exercício 2
i, j = map(int, input("Digite dois números inteiros (i, j): ").split(","))
array_2d = [[i * j for j in range(j)] for i in range(i)]
print("Array 2D:", array_2d)
