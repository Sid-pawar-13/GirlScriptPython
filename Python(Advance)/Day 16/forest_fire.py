import pandas as pd
import numpy as np
import warnings
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
warnings.filterwarnings("ignore")

data = pd.read_csv("Forest_fire.csv")
data = np.array(data)

X = data[1:, 1:-1]
Y = data[1:, -1]
Y = Y.astype('int')
X = X.astype('int')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)
log_reg = LogisticRegression()

log_reg.fit(X_train, Y_train)

inputt = [int(x) for x in "45 32 60".split(" ")]
final = [np.array(inputt)]

b = log_reg.predict_proba(final)

pickle.dump(log_reg,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
