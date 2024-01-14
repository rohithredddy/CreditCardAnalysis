import pandas as pd
import time
import sqlalchemy
import matplotlib.pyplot as plt

df = pd.DataFrame()
csv_file = "/content/BankChurners.csv"


def introduction():
    msg = '''
          A manager at the bank is disturbed with more and more customers leaving their credit card services.
          They would really appreciate if one could predict for them who is gonna get churned so they can 
          proactively go to the customer to provide them better services and turn customers' decisions in 
          the opposite direction.
           
          I got this dataset from a website with the URL as https://leaps.analyttica.com/home. I have been 
          using this for a while to get datasets and accordingly work on them to produce fruitful results.
          The site explains how to solve a particular business problem.
          
          Now, this dataset consists of 10,000 customers mentioning their age, salary, marital_status, 
          credit card limit, credit card category, etc. There are nearly 18 features.
          
          We have only 16.07 % of customers who have churned. Thus, it's a bit difficult to train our model
          to predict churning customers.

          In this project we are going to analyse the same dataset using Python Pandas on windows machine but
          the project can be run on any machine support Python and Pandas. Besides pandas we also used 
          matplotlib python module for visualization of this dataset. 

          The whole project is divided into four major parts ie reading, analysis, visualization and export. all these
          part are further divided into menus for easy navigation

          NOTE: Python is case-SENSITIVE so type exact Column Name wherever required.

          If you have any query or suggestions please contact me at rakesh@binarynote.com \n\n\n\n'''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')


def made_by():
    msg = ''' 
            Credit Card Analysis made by    : xyx
            Roll No                         : 1234
            School Name                     : Your school name
            session                         : 2020-21
            
            Thanks for evaluating my Project.
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')


def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen


def clear():
    for x in range(65):
               print()


def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nD A T A   A N A L Y S I S   M E N U  ')
            print('_'*100,'\n')
            print('1.   Show Whole DataFrame')
            print('2.   Show Columns')
            print('3.   how Top Rows')
            print('4.   Row Bottom Rows')
            print('5.   Show Specific Column')
            print('6.   Add a New Record')
            print('7.   Add a New Column')
            print('8.   Delete a Column')
            print('9.   Delete a Record')
            print('10.  Card Type User')
            print('11.  Gender wise User')
            print('12.  Data Summery')
            print('13.  Exit (Move to main menu)')
            ch = int(input('\n\nEnter your choice:'))
            if ch == 1:
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 2:
                print(df.columns)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 6:
                a = input('Enter Customer ID :')
                b = input('Enter Customer Type :')
                c = input(' Enter Customer Age:')
                d = input('Enter Customer Gender :')
                e = input('Enter Customer Dependent Count :')
                f = input('Enter Education Level :')
                g = input('Enter Marital Status :')
                h = input('Enter Income Category :')
                i = input('Enter Card Category :')
                j = input('Enter Month on Book')
                k = input('Enter Total Relationship count :')
                l = input('Enter Total Month Inactive in last 12 month  :')
                m = input('Enter Total Contacted in last 12 months :')
                n = input('Enter Credit Limit :')
                o = input('Enter Revolving Balance :')
                p = input('Enter Average Open to Buy Card :')
                q = input('Enter Total amount change Q4 to Q1 :')
                r = input('Enter Total Transaction amount :')
                s = input('Enter Total Transaction Credit:')
                t = input('Enter Total Credit Change Q4 Q1 :')
                u = input('Enter Average Utilization Ratio  :')
               
                data = {'clientID': a, 'Type': b, 'age': c,
                        'gender': d, 'Dependent_count': e, 'Educational_Level': f, 'Marital_Status': g,
                        'Income_Category':h,'Card_Category':i,'Months_on_book':j,'Total_Relationship_count':k,
                        'Month_Inactive_12_month':l,'Contacts_count_12_mon':m,'Credit_Limit':n,
                        'Total_Revolving_Bal':o,'Avg_Open_To_Buy':p,'Total_Amt_chng_Q4_Q1':q,'Total_Trans_Amt':r,
                        'Total_Trans_Ct':s,'Total_Ct_Chng_Q4_Q1':t,'Average_Utilization_Ration':u
                        }
                df = df.append(data, ignore_index=True)
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name] = col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 8:
                col_name = input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 9:
                index_no = int(
                    input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                print(df.columns)
                print(df['Type'].unique())
                tipe = input('Enter Card Type ')
                g = df.groupby('Type')
                print('Card Type : ', tipe)
                print(g['Type'].count())
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 11:
                df1 = df.Gender.unique()
                print('Available Gender :', df1)
                print('\n\n')
                schName = input('Enter Gender Type :')
                df1 = df[df.Gender == schName]
                print(df1)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 12:
                print(df.describe())
                print("\n\n\nPress any key to continue....")
                wait = input()
            if ch == 13:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1.  Whole Data LINE Graph\n')
        print('2.  Whole Data Bar Graph\n')
        print('3.  Whole Data Scatter Graph\n')
        print('4.  Whole Data Pie Chart\n')
        print('5.  Bar Graph By Education Level\n')
        print('6.  Bar Graph By Income Level\n')
        print('7.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        if ch == 2:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.bar(x, y)  #bar graph
            plt.grid(True)
            plt.show()
            wait = input()

        if ch == 3:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.grid(True)
            plt.scatter(x, y)
            plt.show()
            wait = input()

        if ch == 4:
            g = df.groupby("Card_Category")
            x = df['Card_Category'].unique()
            y = g['Card_Category'].count()
            plt.pie(y, labels=x, autopct='% .2f', startangle=90)  #pie graph
            plt.xticks(rotation='vertical')
            plt.show()

        if ch == 5:
            g = df.groupby("Education_Level")
            x = df['Education_Level'].unique()
            y = g['Education_Level'].count()
            plt.bar(x, y)
            #plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title('Education Level wise Card User')
            plt.xlabel('Education Level')
            plt.show()
            wait = input()

        if ch == 6:
            g = df.groupby("Income_Category")
            x = df['Income_Category'].unique()
            y = g['Income_Category'].count()
            plt.grid(True)
            plt.title('Credit Card User- Income Group')
            plt.xlabel('Income Group')
            plt.ylabel('Card Users')
            plt.bar(x,y)
            plt.show()

        if ch == 7:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  Excel File\n')
        print('3.  MySQL Table\n')
        print('4.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch == 1:
            df.to_csv('/content/BankChurners.csv')
            print('\n\nCheck your new file "bankchurner_backup.csv"  on C: Drive.....')
            wait = input('\n\n\n Press any key to continuee.....')

        if ch == 2:
            df.to_excel('c:/backup/bankchurner_backup.xlsx')
            print('\n\nCheck your new file "bankchurner_backup.xlsx"  on C: Drive.....')
            wait = input('\n\n\n Press any key to continuee.....')

        if ch == 3:
            engine = sqlalchemy.create_engine(
                'mysql+pymysql://root:@localhost:3306/davschool')
            df.to_sql(name='bankchurner_backup', con=engine,
                      index=False, if_exists='replace')
            print('\n\nPlease check DAVSCHOOL database for bankchurner_backup table.....')
            wait = input('\n\n\n Press any key to continuee.....')

        if ch == 4:
            break


def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))

                      if choice == 1:
                                read_csv_file()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 2:
                                data_analysis_menu()
                                wait = input('\n\n Press any key to continue....')

                      if choice == 3:
                                graph()
                                wait = input('\n\n Press any key to continue....')
                      if choice == 4:
                                export_menu()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 5:
                                 break
           clear()
           made_by()


# call your main menu
main_menu()