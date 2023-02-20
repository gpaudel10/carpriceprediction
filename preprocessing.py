import pandas as pd
import streamlit as st

@st.cache()
def load_data():
    df = pd.read_csv("data/car-prices.csv")
    #print(df)
    car_companies = pd.Series([car.split(" ")[0]for car in df['CarName']], index = df.index)
    df['car_company'] = car_companies

    df.loc[(df['car_company']=="vw") | (df['car_company'] == "vokswagen"),'car_company'] = 'volkswagen'
    df.loc[df['car_company']=="porcshce",'car_company'] = 'porsche'
    df.loc[df['car_company']=="toyouta",'car_company'] = 'toyota'
    df.loc[df['car_company']=="Nissan",'car_company'] = 'nissan'
    df.loc[df['car_company']=="maxda",'car_company'] = 'mazda'
    df.drop(columns = ['CarName'],axis = 1,inplace = True)
    cars_numeric_df = df.select_dtypes(include = ['int64','float64'])
    cars_numeric_df.drop(columns = ['car_ID'],axis = 1,inplace = True)
#axis.....column


    df[['cylindernumber','doornumber']] = df[['cylindernumber','doornumber']].apply(num_map,axis = 1)

    car_body_dummies = pd.get_dummies(df['carbody'], dtype =int)
    car_body_new_dummies = pd.get_dummies(df['carbody'],drop_first = True,dtype = int)

    car_categorical_df = df.select_dtypes(include = [object])

    car_dummy_df = pd.get_dummies(car_categorical_df,drop_first = True,dtype = int)

    df.drop(list(car_categorical_df.columns),axis =1,inplace = True)

    df = pd.concat([df,car_dummy_df],axis = 1)

    df.drop('car_ID',axis =1, inplace = True)

    final_col = ['carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick','price']
    return df[final_col]

def num_map(series):
        word_dict = {"two": 2,"three": 3, "four":4, "five": 5,"six": 6,"eight": 8,"twelve": 12}
        return series.map(word_dict)    