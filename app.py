from flask import Flask, render_template, request, session
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
app.secret_key = 'my_secret_key'  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    session['Age'] = int(request.form['Age'])

    session['Gender'] = request.form['Gender']
    if session['Gender'] =='Female':
        session['Gender_Female'] = 1
        session['Gender_Male'] = 0
    else:
        session['Gender_Female'] = 0
        session['Gender_Male'] = 1

    session['Education_Level'] = request.form['Education_Level']
        
    session['Marital_Status'] = request.form['Marital_Status']

    session['Number_of_Dependents'] = int(request.form['Number_of_Dependents'])

    session['Years_at_Company'] = float(request.form['Years_at_Company'])

    session['Job_Role'] = request.form['Job_Role']

    session['Number_of_Promotions'] = int(request.form['Number_of_Promotions'])

    session['Job_Level'] = request.form['Job_Level']

    session['Job_Satisfaction'] = request.form['Job_Satisfaction']

    session['Work_Life_Balance'] = request.form['Work_Life_Balance']

    session['Overtime'] = request.form['Overtime']
    if session['Overtime'] == 'Yes':
        session['Overtime_Yes'] = 1
        session['Overtime_No'] = 0
    else:
        session['Overtime_Yes'] = 0
        session['Overtime_No'] = 1

    session['Distance_from_Home'] = int(request.form['Distance_from_Home'])

    session['Remote_Work'] = request.form['Remote_Work']
    if session['Remote_Work'] == 'Yes':
        session['Remote_Work_Yes'] = 1
        session['Remote_Work_No'] = 0
    else:
        session['Remote_Work_Yes'] = 0
        session['Remote_Work_No'] = 1

    session['Monthly_Income'] = request.form['Monthly_Income']
    if session['Monthly_Income'] == '1k-4k':
        session['Monthly_Income_1k_4k'] = 1
        session['Monthly_Income_4k_7k'] = 0
        session['Monthly_Income_7k-10k'] = 0
        session['Monthly_Income_10k-13k'] = 0
        session['Monthly_Income_13k-17k'] = 0
    elif session['Monthly_Income'] == '4k-7k':
        session['Monthly_Income_1k_4k'] = 0
        session['Monthly_Income_4k_7k'] = 1
        session['Monthly_Income_7k-10k'] = 0
        session['Monthly_Income_10k-13k'] = 0
        session['Monthly_Income_13k-17k'] = 0
    elif session['Monthly_Income'] == '7k-10k':
        session['Monthly_Income_1k_4k'] = 0
        session['Monthly_Income_4k_7k'] = 0
        session['Monthly_Income_7k-10k'] = 1
        session['Monthly_Income_10k-13k'] = 0
        session['Monthly_Income_13k-17k'] = 0
    elif session['Monthly_Income'] == '10k-13k':
        session['Monthly_Income_1k_4k'] = 0
        session['Monthly_Income_4k_7k'] = 0
        session['Monthly_Income_7k-10k'] = 0
        session['Monthly_Income_10k-13k'] = 1
        session['Monthly_Income_13k-17k'] = 0
    else:
        session['Monthly_Income_1k_4k'] = 0
        session['Monthly_Income_4k_7k'] = 0
        session['Monthly_Income_7k-10k'] = 0
        session['Monthly_Income_10k-13k'] = 0
        session['Monthly_Income_13k-17k'] = 1


    input_data = [[
        float(session['Age']),
        float(session['Years_at_Company']),
        float(session['Job_Role']),
        float(session['Work_Life_Balance']),
        float(session['Job_Satisfaction']),
        float(session['Number_of_Promotions']),
        float(session['Distance_from_Home']),
        float(session['Education_Level']),
        float(session['Marital_Status']),
        float(session['Number_of_Dependents']),
        float(session['Job_Level']),
        float(session['Gender_Female']),
        float(session['Gender_Male']),
        float(session['Remote_Work_No']),
        float(session['Remote_Work_Yes']),
        float(session['Overtime_No']),
        float(session['Overtime_Yes']),
        float(session['Monthly_Income_1k_4k']),
        float(session['Monthly_Income_4k_7k']),
        float(session['Monthly_Income_7k-10k']),
        float(session['Monthly_Income_10k-13k']),
        float(session['Monthly_Income_13k-17k'])
        
    ]]

    prediction = model.predict(input_data)
    return render_template('result.html', prediction_result=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)