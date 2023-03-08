## Médicos que quieran incorporar un apoyo de analítica de datos en el proceso de evaluación de pacientes y
# la toma de decisiones asociada (solicitud de exámenes, chequeos y otros procedimientos).

# Se importan las librerias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

##
# Se leen los datos


data =  pd.read_csv("Proyecto 1/processed.cleveland.data", sep=",")
data_names = open("Proyecto 1/heart-disease.names").read()
names= ["age","sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope","ca", "thal", "num"]
data.columns = names
data['ca'] = pd.to_numeric(data['ca'], errors='coerce')
data['thal'] = pd.to_numeric(data['thal'], errors='coerce')
data = data.astype(float)

data = data.dropna()
data = data.to_numpy()
##
for j in range(0, data.shape[0]):
    if data[j, 13] == 2:
        data[j, 13] = 1
    elif data[j, 13] == 4:
        data[j, 13] = 3
##
for j in range(0, data.shape[0]):
    if data[j, 13] == 3:
        data[j, 13] = 2


####
Pacientes = [[], [], []]
ValoresNum = [0,1,2]
for i in range(0, len((Pacientes))):
    for j in range(0, data.shape[0]):
        if data[j, 13] == ValoresNum[i]:
            Pacientes[i].append(data[j,])
    Pacientes[i] = np.array(Pacientes[i])
## Se convierten todos los valores a float

## Estadisticas descriptivas

estad_age = data["age"].describe()
estad_sex = data["sex"].describe()
estad_cp = data["cp"].describe()
estad_trestbps = data["trestbps"].describe()
estad_chol = data["chol"].describe()
estad_fbs = data["fbs"].describe()
estad_restecg = data["restecg"].describe()
estad_thalach = data["thalach"].describe()
estad_exang = data["exang"].describe()
estad_oldpeak = data["oldpeak"].describe()
estad_slope = data["slope"].describe()
estad_ca = data["ca"].describe()
estad_thal = data["thal"].describe()
estad_num = data["num"].describe()
##
plt.style.use('seaborn-muted')
plt.figure(figsize=(14,5))
plt.suptitle('Diagramas de Cajas')
for i in range(0, len(names)):
    plt.subplot(2, 7, i+1)
    plt.boxplot(data[names[i]])
    plt.title(names[i])
    plt.xticks([ ])
plt.tight_layout()

##
plt.style.use('seaborn-pastel')
plt.figure(figsize=(14,5))
plt.suptitle('Histogramas')
for i in range(0, len(names)):
    plt.subplot(2, 7, i+1)
    plt.hist(data[names[i]], bins = 15)
    plt.title(names[i])
plt.tight_layout()

##
plt.style.use('seaborn-pastel')
plt.figure(figsize=(14,5))
plt.suptitle('Diagramas de Violin')
for i in range(0, len(names)):
    plt.subplot(2, 7, i+1)
    plt.violinplot(data[names[i]])
    plt.title(names[i])
plt.tight_layout()

##
plt.style.use('seaborn-pastel')
for j in range(0, len(Pacientes)):
    plt.figure(figsize=(12, 4))
    plt.suptitle('Histogramas Pacientes Diagnosticados ' + f'{j}')
    for i in range(0, len(Pacientes[0][1])):
        plt.subplot(2, 7, i+1)
        plt.hist(Pacientes[j][:,i], bins = 15)
        plt.title(names[i])
    plt.tight_layout()

##
plt.style.use('seaborn-pastel')
for j in range(0, len(Pacientes)):
    plt.figure(figsize=(12, 4))
    plt.suptitle('Diagramas de Cajas Pacientes Diagnosticados ' + f'{j}')
    for i in range(0, len(Pacientes[0][1])):
        plt.subplot(2, 7, i+1)
        plt.boxplot(Pacientes[j][:,i])
        plt.title(names[i])
    plt.tight_layout()


##
plt.style.use('seaborn-pastel')
for j in range(0, len(Pacientes)):
    plt.figure(figsize=(12, 4))
    plt.suptitle('Diagramas de Violin Pacientes Diagnosticados ' + f'{j}')
    for i in range(0, len(Pacientes[0][1])):
        plt.subplot(2, 7, i+1)
        plt.violinplot(Pacientes[j][:,i])
        plt.title(names[i])
    plt.tight_layout()