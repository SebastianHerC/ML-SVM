import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
#_______________EJEMPLOS________________
# Datos de ejemplo
"""text = ["I love writing code in Python. I love Python code",
        "I hate writing code in Java. I hate Java code"]

# Crear un DataFrame con los datos
df = pd.DataFrame({'review': ['review1', 'review2'], 'text': text})

# Crear una instancia de CountVectorizer
cv = CountVectorizer(stop_words='english')

# Ajustar y transformar los datos utilizando CountVectorizer
cv_matrix = cv.fit_transform(df['text'])

# Crear un DataFrame a partir de la matriz de conteo de palabras
df_dtm = pd.DataFrame(cv_matrix.toarray(),
                      index=df['review'].values,
                      columns=cv.get_feature_names_out())

print(df_dtm)"""


#TFIDF permite eliminar palabras que no presentan mayor relevancia y darles a los que si l onecesitan
text = ["I love writing code in Python. I love Python code",
        "I hate writing code in Java. I hate Java code"]

df = pd.DataFrame({'review': ['review1', 'review2'], 'text': text})
tfidf = TfidfVectorizer(stop_words='english', norm=None)
tfidf_matrix = tfidf.fit_transform(df['text'])
df_dtm = pd.DataFrame(tfidf_matrix.toarray(),
                      index=df['review'].values,
                      columns=tfidf.get_feature_names_out())

print(df_dtm)


#_______________FIN EJEMPLOS_____________