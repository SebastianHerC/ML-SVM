import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import f1_score, classification_report, confusion_matrix



df = pd.read_csv('IMDB Dataset.csv')


df_positive = df[df['sentiment']=='positive'][:9000]
df_negative = df[df['sentiment']=='negative'][:10000]


df_unbalanced= pd.concat([df_positive,df_negative])
count_unbalanced = df_unbalanced.value_counts('sentiment')


rus =RandomUnderSampler()
df_balanced, df_balanced['sentiment']= rus.fit_resample(df_unbalanced[['review']], 
                                                     df_unbalanced['sentiment'])


df_balanced.value_counts(['sentiment'])


train, test = train_test_split(df_balanced, test_size=0.33, random_state=42)

train_x, train_y= train['review'], train['sentiment']
test_x, test_y= test['review'], test['sentiment']



tfidf = TfidfVectorizer(stop_words='english')


train_x_vec = tfidf.fit_transform(train_x)

test_x_vec = tfidf.transform(test_x)




svc = SVC()
svc.fit(train_x_vec, train_y)

#___Prueba__
print(svc.predict(tfidf.transform(['A good movie'])))
print(svc.predict(tfidf.transform(['An excellent movie'])))
print(svc.predict(tfidf.transform(['I did not like this movie at all gave this movie away'])))




#____________Evaluación del modelo_____________________


#Score
print("________________________________________________________")
print(f'El Score es de: {svc.score(test_x_vec, test_y)}')


# F1 score (F1 score= 2*(recall * presición)/(recall + presición))
print("________________________________________________________")
f1_scores= f1_score(test_y, svc.predict(test_x_vec),
         labels=['positive', 'negative'],
         average=None)
print(f'El F1 score es: {f1_scores}')


#______________Reporte de clasificación________________________
print("________________________________________________________")
cr=classification_report(test_y, svc.predict(test_x_vec),
                    labels=['positive', 'negative'])

print(cr)

#__________Confusion Matrix__________ (revela los veradeoros + y -, falsos + y falsos- )

print("________________________________________________________")
cm=confusion_matrix(test_y, svc.predict(test_x_vec),
                    labels=['positive', 'negative'])
#TP- FP
#FN - TN
print(cm)

#____________Optimización del modelo__________________________

"""param = { 'C': [1,4,8,16,32], 'kernel': ['linear', 'rbf']}

#C= parametro de penailización, indica cuanto error es soportable
# Kernel= parte del sistema que hace procesamientos y especificar que funcion queremos usar
#        - lineal
#        - polinomicas 
#        - rbf

svc=SVC()
svc_g =GridSearchCV(svc, param, cv=5)
svc_g.fit(train_x_vec,train_y)
#cv= validacion cruzada

print(svc_g.best_estimator_)
print(svc_g.best_params_)"""