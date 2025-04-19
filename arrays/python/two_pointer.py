class Solution:
    def reverseWords(self, s):
        res = ''
        # Dois ponteiros: l (left) marca o início da palavra, r (right) marca o fim
        l, r = 0, 0

        # Percorre a string até o final
        while r < len(s):
            # Se não encontrou um espaço, continua avançando o ponteiro direito
            if s[r] != ' ':
                r += 1

            else:
                # Quando encontra um espaço:
                # Pega a substring da palavra atual (s[l:r+1]) e inverte ela ([::-1])
                # O +1 no r+1 é para incluir o próprio espaço
                res += s[l:r+1][::-1]
                r += 1  # Avança o ponteiro direito
                l = r   # Move o ponteiro esquerdo para a próxima palavra

        # Tratamento da última palavra:
        res += ' '  # Adiciona um espaço
        # Inverte a última palavra (que não termina com espaço)
        res += s[l:r+2][::-1]

        # Remove o primeiro caractere da string (que é um espaço extra)
        # pois adicionamos espaços extras durante o processo
        return res[1:]
