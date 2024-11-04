#O número de pessoas que clicaram no terceiro link é representado por 't'.

#O número de pessoas que clicaram no segundo link é o dobro do número de pessoas que clicaram no terceiro link, 
# ou seja, '2×𝑡'.

#O número de pessoas que clicaram no primeiro link é o dobro do número de pessoas que clicaram no segundo link, 
# então: 2×(2×𝑡)=4×𝑡.


#Função para calcular a qtde de click no primeiro link
def nClick_link1 (t):
    return 4*t

#Informar o número de pessoas que clicaram no 3° link
t = int(input("Insira o número de pessoas que clicaram no terceiro link: "))

#imprimindo a qtde de clicks no link 1
print ("O link 1 foi clicado: ", nClick_link1(t))