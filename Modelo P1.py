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
## Se estandarizan las variables para el diagnostico:
# 0 -- No presenta heart disease
# 1 -- mild heart disease
# 3 -- severe heart disease
for j in range(0, data.shape[0]):
    if data[j, 13] == 2:
        data[j, 13] = 1
    elif data[j, 13] == 4:
        data[j, 13] = 3

## Se define el modelo

# Se define la red bayesiana
modelo_HD = BayesianNetwork([("AGE", "CHOL"), ("FBS", "CHOL"), ("CHOL", "HD"), ("CP", "HD"), ("HD", "THAL"), ("HD", "EXANG"),
                         ("HD", "OLDPEAK")])

## Discretizacion del colesterol
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

# Se definen las muestras
info = np.zeros((296,8))
columnas = [0, 2, 4, 5, 8, 9, 12, 13]
nombres = ["AGE", "CP", "CHOL", "FBS", "EXANG", "OLDPEAK", "THAL", "HD"]
for i in range(len(columnas)):
    info[:,i] = data[:,columnas[i]]
muestras = pd.DataFrame(info, columns = nombres)

# Estimador de máxima verosimilitud
estimador_HD = MaximumLikelihoodEstimator(model=modelo_HD, data=muestras)

#Estimación de las CPDs
modelo_HD.fit(data=muestras, estimator = MaximumLikelihoodEstimator)
for i in modelo_HD.nodes():
    print("CPD ", i,"\n", modelo_HD.get_cpds(i))

#Se imprime completa la CDP HD
for i in range(len(modelo_HD.get_cpds("HD").values)):
    print(modelo_HD.get_cpds("HD").values[i])

## FALTA PONER PSEUDOCOUNTS
estimador = BayesianEstimator(model=modelo_HD, data=muestras)

# Se estima la CPD de robo utilizando un prior.
cpd_HD_prior = estimador.estimate_cpd(node="HD", prior_type="dirichlet", pseudo_counts=[[200000, 200000],[200, 200]])
print("CPD HD con prior: \n", cpd_HD_prior)



