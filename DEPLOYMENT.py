import streamlit as st
import pandas as pd
import numpy as np




st.title('KKBOX Churn Prediction')

sentence = st.text_input('Input your mnso:')

members_data = pd.read_csv('members_v3.csv')
transactions_data = pd.read_csv('transactions_v2.csv')
user_logs_data = pd.read_csv('user_logs_v2.csv')

a = members_data[members_data.isin([sentence]).any(axis=1)]

b = transactions_data[transactions_data.isin([sentence]).any(axis=1)]

c = user_logs_data[user_logs_data.isin([sentence]).any(axis=1)]

result = pd.concat([a, b, c], ignore_index=True, sort=False)

def preprocessing(data):
    '''This preprocessing function is used to perform outliers removal, nan imputation '''
    
    # nan = 0  in city 
    data['city'] = data['city'].fillna(0)

    # removing outliers
    data['bd'] = data['bd'].apply(lambda x: x if (x < 60.0) and (x > 0.0) else np.nan)
    # nan = median age in bd
    data['bd'] = data['bd'].fillna(19.0)

    #  male = 1 in gender
    data['gender'] = data['gender'].replace(to_replace='male', value=1)
    #  male = 2 in gender
    data['gender'] = data['gender'].replace(to_replace='female', value=2)
    #  nan = 0 in gender
    data['gender'] = data['gender'].fillna(0)

    # nan = 0 in registered_via
    data['registered_via'] = data['registered_via'].fillna(0)

    # nan = median date in the registration_init_time
    data['registration_init_time'] = data['registration_init_time'].fillna(20131114.0)
    # converting float date to datetime
    #data['registration_init_time'] = pd.to_datetime(data['registration_init_time'], format='%Y%m%d')

    # nan = 0 in payment_method_id
    data['payment_method_id'] = data['payment_method_id'].fillna(0)
    
    # nan = 30 in payment_plan_days
    data['payment_plan_days'] = data['payment_plan_days'].fillna(30.0)

    # nan = 149 in  plan_list_price
    data['plan_list_price'] = data['plan_list_price'].fillna(149.0)

    # nan = 149 in actual_amount_paid
    data['actual_amount_paid'] = data['actual_amount_paid'].fillna(149.0)

    # nan =  2 in is_auto_renew (2 is not mentioned)
    data['is_auto_renew'] = data['is_auto_renew'].fillna(2)

    # nan = median date in transaction_date
    data['transaction_date'] = data['transaction_date'].fillna(20170315.0)
    # converting float date to datetime
    #data['transaction_date'] = pd.to_datetime(data['transaction_date'], format='%Y%m%d')

    # nan = median date in membership_expire_date
    data['membership_expire_date'] = data['membership_expire_date'].fillna(20170419.0)
    # converting float date to datetime
    #data['membership_expire_date'] = pd.to_datetime(data['membership_expire_date'], format='%Y%m%d')

    #  nan =  2 in is_cancel (2 is not mentioned)
    data['is_cancel'] = data['is_cancel'].fillna(2)

    # nan = median date in 'date'
    data['date'] = data['date'].fillna(20170316.0)
    # converting float date to datetime
    #data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')

    # removing outliers
    data['num_25'] = data['num_25'].apply(lambda x: x if (x <= 56.0) else np.nan)
    #  nan = 2 in num_25
    data['num_25'] = data['num_25'].fillna(2.0)

    # removing outliers
    data['num_50'] = data['num_50'].apply(lambda x: x if (x <= 21.0) else np.nan)
    # nan = 0 in num_50
    data['num_50'] = data['num_50'].fillna(0)

    # removing outliers
    data['num_75'] = data['num_75'].apply(lambda x: x if (x <= 10.0) else np.nan)
    # nan = 0 in num_75
    data['num_75'] = data['num_75'].fillna(0)

    # removing outliers
    data['num_985'] = data['num_985'].apply(lambda x: x if (x <= 11.0) else np.nan)
    # nan = 0 in num_985
    data['num_985'] = data['num_985'].fillna(0)

    # removing outliers
    data['num_100'] = data['num_100'].apply(lambda x: x if (x <= 75.0) else np.nan)
    # nan = 17 in num_100
    data['num_100'] = data['num_100'].fillna(14.0)

    # removing outliers
    data['num_unq'] = data['num_unq'].apply(lambda x: x if (x <= 69.0) else np.nan)
    #nan = 18 in num_unq
    data['num_unq'] = data['num_unq'].fillna(16.0)

    # removing outliers
    data['total_secs'] = data['total_secs'].apply(lambda x: x if (x <= 19476.59) else np.nan)
    # nan = 4548 in total_secs
    data['total_secs'] = data['total_secs'].fillna(4548.5495)
    
preprocessing(result)






