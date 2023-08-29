import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report

#Input => reviews
#Output => Sentiment

#over_sampling para aumentar la data
#under_sampling para disminuir la data

df = pd.read_csv('IMDB Dataset.csv')

#Seleccionar cantidad de elementos a tomar
df_positive = df[df['sentiment']=='positive'][:9000]
df_negative = df[df['sentiment']=='negative'][:10000]

#concatenar listas
df_unbalanced= pd.concat([df_positive,df_negative])
count_unbalanced = df_unbalanced.value_counts('sentiment')

#Balancear Data utilizando imblearn
#RUS= Random- Under-Sampler
rus =RandomUnderSampler()            #aquí abajo esta el input e output
                                     # El imput siempre requiere una data 2D, agregar 2 []

df_balanced, df_balanced['sentiment']= rus.fit_resample(df_unbalanced[['review']], 
                                                     df_unbalanced['sentiment'])   #<=balancea la data

#contar la cantidad de elementos 
df_balanced.value_counts(['sentiment'])

#Separar Data para TRAIN y para TEST

#elegir la data y determinar los tamaños a dividir, elegir la varialbe de aleatoriedad
#Random_state "similar a seed". test_size idealmente entre 0.1 y 0.3
train, test = train_test_split(df_balanced, test_size=0.33, random_state=42)


    #Elegir las variables "x" e "y" de Teain y test

train_x, train_y= train['review'], train['sentiment']
test_x, test_y= test['review'], test['sentiment']

#previo a entrenar, transfomar la data de texto a 
#data numnerica. transformar a vectores
#Bag of words(representation of text)
#Existen 2 técnicas, 
# CountVectorizer=frecuencia con la cual aparece una palabra en una oracion
#Tfdf= la relevancia que tiene una palabra dentro de una oración, que no este tan repetida en otro "reviws"
#Quitar palabras con sto_words (en ingles solamente)

tfidf = TfidfVectorizer(stop_words='english')



#ajustar y transformar, fit_transform (fit: busca los paramentros ideales para la data
# y una vez seleciconados los mejores, los aplica con transform)
train_x_vec = tfidf.fit_transform(train_x)

test_x_vec = tfidf.transform(test_x) #solo transform ya que ya fueron optimizados en la linea anterior


#SELECCION DEL MODELO(EN ESTE CASO ES UN MODELO SUPERVISADO)
#ML Algoritmos
#   1. supervised learning: Regresion (output nunérico), clasificacion (output discreto). Siempre se define input para obtener output.
#       input: review
#       output: Sentiment(discrete)
#   2. Aprendizaje no supervisado: se intenta identificar patrones en el iunput para obtener el output.


#_______________________MODELOS DE CLASIFICACIÓN_____________________________

# 1.- Support Vector Machines (SVM)
svc = SVC()
svc.fit(train_x_vec, train_y)


print(svc.predict(tfidf.transform(['A good movie'])))
print(svc.predict(tfidf.transform(['An excellent movie'])))
print(svc.predict(tfidf.transform(['I did not like this movie at all gave this movie away'])))

# 2.- Decision Tree

dec_t = DecisionTreeClassifier()
dec_t.fit(train_x_vec, train_y)

print(dec_t.predict(tfidf.transform(['A good movie'])))
print(dec_t.predict(tfidf.transform(['An excellent movie'])))
print(dec_t.predict(tfidf.transform(['I did not like this movie at all gave this movie away'])))

# 3.- Naive Bayes

gnb = GaussianNB()
gnb.fit(train_x_vec.toarray(), train_y)

print(gnb.predict(tfidf.transform(['A good movie']).toarray()))
print(gnb.predict(tfidf.transform(['An excellent movie']).toarray()))
print(gnb.predict(tfidf.transform(['I did not like this movie at all gave this movie away']).toarray()))

# 4.- Logistic regression

lr = LogisticRegression()
lr.fit(train_x_vec, train_y)

print(lr.predict(tfidf.transform(['A good movie'])))
print(lr.predict(tfidf.transform(['An excellent movie'])))
print(lr.predict(tfidf.transform(['I did not like this movie at all gave this movie away'])))


#____________Evaluación del modelo_____________________
# Presicion del modelo:

#Score
print("__________________________________________")
print(f'El Score es de: {svc.score(test_x_vec, test_y)}')

# F1 score (F1 score= 2*(recall * presición)/(recall + presición))
f1_score(test_y, svc.predict(test_x_vec),
         labels=['positive', 'negative'],
         average=None)


#_________Reporte de clasificación
print("___________________")
classification_report(test_y, svc.predict(test_x_vec),
                    labels=['positive', 'negative'])