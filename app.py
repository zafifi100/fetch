from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

k = 0
month_total = 0
prediction = 0
max_value = 0
min_value = 0

# Load the pre-trained Keras model
model = tf.keras.models.load_model('model.h5')

#cold start prev count val
df = pd.read_csv("data_daily.csv")
max_value = df['Receipt_Count'].max()
min_value = df['Receipt_Count'].min()

scaler = MinMaxScaler()
df['Receipt_Count'] = scaler.fit_transform(df['Receipt_Count'].values.reshape(-1,1))


# Function to preprocess user inputs and make predictions
def predict(month):

    global k
    if k == 0:
        for i in range(len(df)):
            k = 1
            date = pd.to_datetime(df.loc[i, '# Date']).month
            if month == date:
                prev_count = df.loc[i, 'Receipt_Count']
                print(prev_count)
                break
            else:
                continue



    month_sin = np.sin(2*np.pi*month/11.0)
    month_cos = np.cos(2*np.pi*month/11.0)


    for i in range(30):
        inputs = np.array([month_sin,month_cos, prev_count]).reshape(1,-1)
        global prediction
        prediction = model.predict(inputs)
        global month_total
        month_total += prediction[0][0]
        prev_count = prediction[0][0]
    
    global max_value
    global min_value
    unscaled_value = month_total * ( max_value - min_value ) + min_value

    return round(unscaled_value, 0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs from the form
        input1 = request.form['input1']

        #process input
        date_obj = datetime.strptime(input1, '%m/%d/%Y')
        month = date_obj.month
        print(month)
        prediction = predict(month)

        return render_template('index.html', prediction=prediction)
    else:
        return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
