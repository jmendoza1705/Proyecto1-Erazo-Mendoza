# Alejandra Erazo / Juliana Mendoza
# Modelo

## Médicos que quieran incorporar un apoyo de analítica de datos en el proceso de evaluación de pacientes y
# la toma de decisiones asociada (solicitud de exámenes, chequeos y otros procedimientos).

# Se importan las librerias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.sampling import BayesianModelSampling
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.estimators import BayesianEstimator


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
# Se estandarizan las variables para el diagnostico:
# 0 -- No presenta heart disease
# 1 -- mild heart disease
# 3 -- severe heart disease
for j in range(0, data.shape[0]):
    if data[j, 13] == 2:
        data[j, 13] = 1
    elif data[j, 13] == 4:
        data[j, 13] = 3


# Discretizacion del colesterol
# menos de 200 -- Deseable
# de 200 a 239 -- En el limite superior
# mas de 240 -- alto
# https://www.mayoclinic.org/es-es/tests-procedures/cholesterol-test/about/pac-20384601

for j in range(0, data.shape[0]):
    if data[j, 4] < 200:
        data[j, 4] = 0
    elif (200 <= data[j, 4] < 240):
        data[j, 4] = 1
    elif data[j, 4] >= 240:
        data[j, 4] = 2

# Discretización de OldPeak
# Menos de 2 - 0
# Entre 2 y 4 - 1
# Mayor o igual a 4 - 2

for j in range(0, data.shape[0]):
    if data[j, 9] < 2:
        data[j, 9] = 0
    elif (2 <= data[j, 9] < 4):
        data[j, 9] = 1
    elif data[j, 9] >= 4:
        data[j, 9] = 2


# Discretización de la edad
# 29 a 39 -- 30
# 40 a 49 -- 40
# 50 a 59 -- 50
# 60 a 69 -- 60
# Mayor o igual a 70 -- 70

for j in range(0, data.shape[0]):
    if (29 <= data[j, 0] < 40):
        data[j, 0] = 30
    elif (40 <= data[j, 0] < 50):
        data[j, 0] = 40
    elif (50 <= data[j, 0] < 60):
        data[j, 0] = 50
    elif (60 <= data[j, 0] < 70):
        data[j, 0] = 60
    elif data[j, 0] >= 70 :
        data[j, 0] = 70

#Se define el modelo

# Se define la red bayesiana
modelo_HD = BayesianNetwork([("AGE", "CHOL"), ("FBS", "CHOL"), ("CHOL", "HD"), ("THAL", "HD"), ("HD", "EXANG"),
                         ("HD", "OLDPEAK")])

# Se definen las muestras
info = np.zeros((296,7))
columnas = [0, 4, 5, 8, 9, 12, 13]
nombres = ["AGE", "CHOL", "FBS", "EXANG", "OLDPEAK", "THAL", "HD"]
for i in range(len(columnas)):
    info[:,i] = data[:,columnas[i]]
muestras = pd.DataFrame(info, columns = nombres)

# Estimador de máxima verosimilitud
estimador_HD = MaximumLikelihoodEstimator(model=modelo_HD, data=muestras)

#Estimación de las CPDs
modelo_HD.fit(data = muestras, estimator = MaximumLikelihoodEstimator)

for i in modelo_HD.nodes():
    print("CPD ", i,"\n", modelo_HD.get_cpds(i))
##
#Se imprime completa la CDP HD
for i in range(len(modelo_HD.get_cpds("HD").values)):
    print(modelo_HD.get_cpds("HD").values[i])

####
#Predicción con evidencia

def EstimacionEvidencia(Edad, Glucosa, Colesterol, ST, Ex, Talasemia):
    infer = VariableElimination(modelo_HD)
    posterior_p = infer.query(["HD"], evidence={"AGE": Edad, "FBS": Glucosa, "CHOL": Colesterol,  "OLDPEAK": ST, "EXANG": Ex, "THAL": Talasemia})
    return posterior_p




