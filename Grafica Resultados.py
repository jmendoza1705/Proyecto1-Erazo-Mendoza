
import matplotlib.pyplot as plt

colesterol = [0,1,2]
talasemia = [3,6,7]
heart = [' No Heart \nDisease', '  Mild Heart \nDisease', '  Severe Heart \nDisease']
col = 1
tal = 7

for i in range(0, len(colesterol)):
    if col == colesterol[i]:
        for j in range(0, len(talasemia)):
            if tal == talasemia[j]:
                valores = [round(modelo_HD.get_cpds('HD').values[0][i][j],2),
                           round(modelo_HD.get_cpds('HD').values[1][i][j],2),
                           round(modelo_HD.get_cpds('HD').values[2][i][j],2)]

plt.figure()
plt.bar(heart, valores, width = 0.3, color = 'thistle')
plt.ylim([0, max(valores) + 0.05])
plt.text(x = -0.16, y = valores[0] + 0.01, s = 'p = ' + f'{valores[0]}', fontstyle = 'italic', fontfamily = 'monospace', color = 'dimgrey')
plt.text(x = 0.83, y = valores[1] + 0.01, s = 'p = ' + f'{valores[1]}', fontstyle = 'italic', fontfamily = 'monospace', color = 'dimgrey')
plt.text(x = 1.83, y = valores[2] + 0.01, s = 'p = ' + f'{valores[2]}', fontstyle = 'italic', fontfamily = 'monospace', color = 'dimgrey')
