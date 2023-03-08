# Alejandra Erazo / Juliana Mendoza
# Proyecto 1

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
## Se estandarizan las variables para el diagnostico:
# 0 -- No presenta heart disease
# 1 -- mild heart disease
# 3 -- severe heart disease
for j in range(0, data.shape[0]):
    if data[j, 13] == 2:
        data[j, 13] = 1
    elif data[j, 13] == 4:
        data[j, 13] = 3

## Se separan los pacientes dependiendo del diagnóstico
Pacientes = [[], [], []]
ValoresNum = [0,1,3]
for i in range(0, len((Pacientes))):
    for j in range(0, data.shape[0]):
        if data[j, 13] == ValoresNum[i]:
            Pacientes[i].append(data[j,])
    Pacientes[i] = np.array(Pacientes[i])

## Se convierte en DataFrame para calcular estadisticas descriptivas
df_no = pd.DataFrame(Pacientes[0], columns = names)
df_mild= pd.DataFrame(Pacientes[1], columns = names)
df_severe = pd.DataFrame(Pacientes[2], columns = names)

## Estadisticas descriptivas para diagnostico negativo
estad_age_NoHD = df_no["age"].describe()
estad_sex_NoHD = df_no["sex"].describe()
estad_cp_NoHD = df_no["cp"].describe()
estad_trestbps_NoHD = df_no["trestbps"].describe()
estad_chol_NoHD = df_no["chol"].describe()
estad_fbs_NoHD = df_no["fbs"].describe()
estad_restecg_NoHD = df_no["restecg"].describe()
estad_thalach_NoHD = df_no["thalach"].describe()
estad_exang_NoHD = df_no["exang"].describe()
estad_oldpeak_NoHD = df_no["oldpeak"].describe()
estad_slope_NoHD = df_no["slope"].describe()
estad_ca_NoHD = df_no["ca"].describe()
estad_thal_NoHD = df_no["thal"].describe()
estad_num_NoHD = df_no["num"].describe()

## Estadisticas descriptivas para diagnostico mild
estad_age_mild = df_mild["age"].describe()
estad_sex_mild = df_mild["sex"].describe()
estad_cp_mild= df_mild["cp"].describe()
estad_trestbps_mild = df_mild["trestbps"].describe()
estad_chol_mild = df_mild["chol"].describe()
estad_fbs_mild = df_mild["fbs"].describe()
estad_restecg_mild = df_mild["restecg"].describe()
estad_thalach_mild = df_mild["thalach"].describe()
estad_exang_mild = df_mild["exang"].describe()
estad_oldpeak_mild = df_mild["oldpeak"].describe()
estad_slope_mild = df_mild["slope"].describe()
estad_ca_mild = df_mild["ca"].describe()
estad_thal_mild = df_mild["thal"].describe()
estad_num_mild = df_mild["num"].describe()

## Estadisticas descriptivas para diagnostico severe
estad_age_severe = df_severe ["age"].describe()
estad_sex_severe = df_severe ["sex"].describe()
estad_cp_severe= df_severe ["cp"].describe()
estad_trestbps_severe = df_severe ["trestbps"].describe()
estad_chol_severe = df_severe ["chol"].describe()
estad_fbs_severe = df_severe ["fbs"].describe()
estad_restecg_severe = df_severe ["restecg"].describe()
estad_thalach_severe = df_severe ["thalach"].describe()
estad_exang_severe = df_severe ["exang"].describe()
estad_oldpeak_severe = df_severe ["oldpeak"].describe()
estad_slope_severe = df_severe ["slope"].describe()
estad_ca_severe = df_severe ["ca"].describe()
estad_thal_severe = df_severe ["thal"].describe()
estad_num_severe = df_severe ["num"].describe()

## Media calculada para todos los parámetros por grupo de pacientes, según el diagnóstico
mean_pacientes_No = []
mean_pacientes_mild = []
mean_pacientes_severe = []
for i in range (Pacientes[0].shape[1]):
    mean_pacientes_No.append(Pacientes[0][:,i].mean())
    mean_pacientes_mild.append(Pacientes[1][:, i].mean())
    mean_pacientes_severe.append(Pacientes[2][:, i].mean())
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
        plt.subplot(1, 3, i+1)
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

## Histogramas

Names= ["Age","Sex", "Chest Pain Type", "Resting Blood Pressure", "Serum Cholestorol", "Fasting Blood Sugar",
        "Resting Electrocardiographic Results", "Maximum Heart Rate Achieved", "Exercise Induced Angina",
        "ST Depression Induced by Exercise Relative to Rest", "Slope of the Peak Exercise ST Segment",
        "Number of Major Vessels Colored by Flourosopy", "Thal = Reversable Defect",
        "Diagnosis of Heart Disease"]
nivel = ['No Heart Disease', 'Mild Heart Disease', 'Severe Heart Disease']
labels = ['years', ' 1 = Male \n 0 = Female', ' 1: typical angina \n 2: atypical angina \n 3: non-anginal pain \n 4: asymptomatic',
          r'mm Hg', r'mg/dl', ' 1 = > 120 $mg/dl$ \n 0 = < 120 $mg/dl$',
          ' 0: Normal \n 1:  ST-T W.Abnormality \n 2: Left Vent.Hypertrophy',
          'Max', ' 1 = Yes\n 0 = No', 'Depression', ' 1: Upsloping \n 2: Flat \n 3: Downsloping', 'Number of Vessels \n0- 3',
          ' 3 = Normal\n 6 = Fixed Defect\n 7 = Reversable Defect', ' 0: No H.Disease \n 1: Mild H.Disease \n 3: Severe H.Disease']
for i in range(0, len(Names)):
    plt.figure(figsize=(12, 4))
    plt.suptitle(Names[i])
    for j in range(0, len(Pacientes)):
        plt.subplot(1, 3, j + 1)
        plt.hist(Pacientes[j][:, i], label = [labels[i]])
        plt.ylim(0,159)
        plt.title(nivel[j])
        plt.legend(loc = 'upper right')
        if j == 0:
            plt.ylabel("Frecuencia (Pacientes)", fontsize=12)
    plt.tight_layout()