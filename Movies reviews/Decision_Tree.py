import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, classification_report


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



dec_t = DecisionTreeClassifier()
dec_t.fit(train_x_vec, train_y)

print(dec_t.predict(tfidf.transform(['A good movie'])))
print(dec_t.predict(tfidf.transform(['An excellent movie'])))
print(dec_t.predict(tfidf.transform(['I did not like this movie at all gave this movie away'])))



#____________Evaluación del modelo_____________________


#Score
print("__________________________________________")
print(f'El Score es de: {dec_t.score(test_x_vec, test_y)}')

print("______________________________________")

f1_scores= f1_score(test_y, dec_t.predict(test_x_vec),
         labels=['positive', 'negative'],
         average=None)
print(f'El F1 score es: {f1_scores}')