#loading the necessary libraries
import numpy as np
import pickle
import streamlit as st

#now loading the model
loaded_model = pickle.load(open('C:/Users/swapn/OneDrive/Desktop/Jignesh/HealthInsurance_Cost Prediction/SAV files/trained_model1.sav','rb'))

#now creating a function for making the predictions
def HealthInsurance_Cost(input_data):
    input_data_as_numpy_array = np.asarray(input_data) #changing the input data into a numpy array
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    #in the above loc we have reshaped the array because our training data predicted the prices on the basis of all the tuples
    #i.e 1070
    
    prediction = loaded_model.predict(input_data_reshaped)

    pred = "{:.0f}".format(prediction[0]*78.95) #here we have done the formatting of the predicted value and multiplied it by the value of 1 dollar
    #because the prices are predicted on the basis of dollar because of the dataset
    
    return'The insurance cost will be \u20B9'+pred+'/-'
    
def main():
    st.title('Health Insurance Cost Prediction') #Giving a title for our web page
    
    #Getting the inputs from the user
    Age=st.text_input('Enter Your Age')
    Sex=st.selectbox("Gender",("Male","Female"))
    BMI=st.text_input("Enter your Body Mass Index(BMI)")
    Children=st.text_input("Number of children")
    Smoker=st.selectbox("Do You Smoke",("Yes","No"))
    Region=st.selectbox("In which region do you stay",("Southeast","Southwest","Northeast","Northwest"))
    Insurance_Cost=""
    
    if(Sex=="Male"):
        Sex=1;
    else:
        Sex=0
        
        
    if(Region=="Southeast"):
        Region=0;
    elif(Region=="Southwest"):
        Region=1;
    elif(Region=="Northeast"):
        Region=2;
    else:
        Region=3
    
    if(Smoker=="Yes"):
        Smoker=0;
    else:
        Smoker=1;
     
        
    if st.button("Calculate Cost"):
        Insurance_Cost=HealthInsurance_Cost([Age,Sex,BMI,Children,Smoker,Region])
        
    st.success(Insurance_Cost)
    
    
    
if __name__=='__main__':
    main()
    