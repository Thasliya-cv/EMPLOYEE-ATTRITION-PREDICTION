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
    if session['Education_Level'] == 'Associate Degree':
        session['Education Level_Associate Degree']=1
        session['Education Level_Bachelor’s Degree']=0
        session['Education Level_Master’s Degree']=0
        session['Education Level_PhD']=0
        session['Education Level_High School']=0
    elif session['Education_Level'] == 'Bachelor’s Degree':
        session['Education Level_Associate Degree']=0
        session['Education Level_Bachelor’s Degree']=1
        session['Education Level_Master’s Degree']=0
        session['Education Level_PhD']=0
        session['Education Level_High School']=0
    elif session['Education_Level'] == 'Master’s Degree':
        session['Education Level_Associate Degree']=0
        session['Education Level_Bachelor’s Degree']=0
        session['Education Level_Master’s Degree']=1
        session['Education Level_PhD']=0
        session['Education Level_High School']=0
    elif session['Education_Level'] == 'PhD':
        session['Education Level_Associate Degree']=0
        session['Education Level_Bachelor’s Degree']=0
        session['Education Level_Master’s Degree']=0
        session['Education Level_PhD']=1
        session['Education Level_High School']=0
    else:
        session['Education Level_Associate Degree']=0
        session['Education Level_Bachelor’s Degree']=0
        session['Education Level_Master’s Degree']=0
        session['Education Level_PhD']=0
        session['Education Level_High School']=1
    session['Marital_Status'] = request.form['Marital_Status']
    session['Number_of_Dependents'] = int(request.form['Number_of_Dependents'])
    session['Years_at_Company'] = float(request.form['Years_at_Company'])
    session['Monthly_Income'] = int(request.form['Monthly_Income'])
    session['Number_of_Promotions'] = int(request.form['Number_of_Promotions'])
    session['Job_Level'] = request.form['Job_Level']
    if session['Job_Level'] == 'Entry_Level':
        session['Job_Level_Entry'] = 1
        session['Job_Level_Mid'] = 0
        session['Job_Level_Senior'] = 0
    elif session['Job_Level'] == 'Mid_Level':
        session['Job_Level_Entry'] = 0
        session['Job_Level_Mid'] = 1
        session['Job_Level_Senior'] = 0
    else:
        session['Job_Level_Entry'] = 0
        session['Job_Level_Mid'] = 0
        session['Job_Level_Senior'] = 1
    session['Job_Satisfaction'] = request.form['Job_Satisfaction']
    session['Work_Life_Balance'] = request.form['Work_Life_Balance']
    session['Overtime'] = request.form['Overtime']
    session['Distance_from_Home'] = int(request.form['Distance_from_Home'])
    session['Remote_Work'] = request.form['Remote_Work']
    
    input_data = [[
        float(session['Age']),
        float(session['Years_at_Company']),
        float(session['Monthly_Income']),
        float(session['Work_Life_Balance']),
        float(session['Job_Satisfaction']),
        float(session['Number_of_Promotions']),
        float(session['Overtime']),
        float(session['Distance_from_Home']),
        float(session['Marital_Status']),
        float(session['Number_of_Dependents']),
        float(session['Job_Level']),
        float(session['Remote_Work']),
        float(session['Gender_Female']),
        float(session['Gender_Male']),
        float(session['Education Level_Associate Degree']),
        float(session['Education Level_Bachelor’s Degree']),
        float(session['Education Level_High School']),
        float(session['Education Level_Master’s Degree']),
        float(session['Education Level_PhD']),
    ]]

    prediction = model.predict(input_data)
    return render_template('result.html', prediction_result=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)