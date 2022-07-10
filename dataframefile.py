# project
'''
Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5

Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10

Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)

Concatenate both 'bank_df_1' and 'bank_df_2' dataframes

Merge client names and their newly added salary information using the 'Bank Client ID'

Let's assume that you became a new client to the bank

Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.

Add this new dataframe to the original dataframe 'bank_df_all'.
'''
import pandas as pd
bank_df_1 = pd.DataFrame({'Bank_Client_ID': [1,2,3,4,5],
                         'first_name': ['chanel','joe','yelow','micheal','james'],
                        'last_name': ['jackie', 'york', 'doe', 'dalio', 'smith']})
print(bank_df_1)

bank_df_2 = pd.DataFrame({'Bank_Client_ID': [6,7,8,9,10],
                         'first_name': ['jared','holy','romano','masimo','kasuka'],
                        'last_name': ['minar', 'jackson', 'antali', 'milano', 'yashita']})
print(bank_df_2)

bank_df_all = pd.concat([bank_df_1, bank_df_2])  # concatenation done
print("df_3 = ", bank_df_all)
df_sal = {'Bank_Client_ID':[1,2,3,4,5,6,7,8,9,10],
            'Annual_salary[$]': [23000,34000,43000,20000,45000,25000,24000,45000,76000,48000]}
print("df_sal : ", df_sal)
bank_salary = pd.DataFrame(df_sal, columns=["Bank_Client_ID", "Annual_salary[$]"])
print("result  = ",bank_salary)

bank_df_all = pd.merge (bank_df_all, bank_salary, on="Bank_Client_ID" )
print(bank_df_all)

# new client
new_client = {
'Bank_Client_ID': [11],
    'first_name': ['ricky'],
    'last_name': ['mantori'],
    'Annual_salary[$]': [66000]
}
new_client_df = pd.DataFrame(new_client, columns=['Bank_Client_ID','first_name','last_name','Annual_salary[$]'])
print(new_client_df)

bank_df_all = pd.concat([bank_df_all,new_client_df], axis = 0) #to put it below
print("final = ", bank_df_all)

