import pandas as pd
import os

def calculate_demographic_data(print_data=True):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "adult.data.csv")

    df = pd.read_csv(csv_path)

    #People of each race 
    race_count = df['race'].value_counts()

    #Average age of men
    men = df[df['sex'] == "Male"]
    average_age_men = round(men['age'].mean(), 1)  

    #Percentage of people who have a Bachelor's degree
    people_with_bachelors = df[df['education'] == 'Bachelors']
    percentaje_with_bachelors = round((people_with_bachelors.shape[0]/df.shape[0])*100,1)

    #Percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K
    people_with_high_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    people_without_high_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    percentaje_win_fifty =  round((people_with_high_education[people_with_high_education['salary'] == ">50K"].shape[0]/people_with_high_education.shape[0])*100,1)
    percentaje_win_fifty_no_education = round((people_without_high_education[people_without_high_education['salary'] == ">50K"].shape[0]/people_without_high_education.shape[0])*100,1)

    #Minimum number of hours a person works per week
    minimum_hours_work = df['hours-per-week'].min()

    #Percentage of the people who work the minimum number of hours per week have a salary of more than 50K
    num_min_hours = df[df['hours-per-week']== minimum_hours_work]
    percentaje_min_fifty = round((num_min_hours[num_min_hours['salary'] == ">50K"].shape[0]/num_min_hours.shape[0])*100,1)

    #Country has the highest percentage of people that earn >50K and what is that percentage
    total_people_country = df['native-country'].value_counts()
    highest_paid = df[df['salary'] == ">50K"]['native-country'].value_counts()
    percentaje_country_paid = (highest_paid/total_people_country)*100

    highest_earning_country = percentaje_country_paid.idxmax()
    highest_earning_country_percentage = round(percentaje_country_paid.max(), 1)

    #Most popular occupation for those who earn >50K in India
    most_popular = df[(df['native-country']=="India") & (df['salary'] == ">50K")]
    most_popular_ocupation = most_popular['occupation'].mode()


    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentaje of people with bachelors:", percentaje_with_bachelors,"%")
        print("Percentaje of people with high education win more 50K:", percentaje_win_fifty,"%")
        print("Percentaje of people without high education win more 50K:", percentaje_win_fifty_no_education,"%")
        print("Minimum number of hours a person works per week:",  minimum_hours_work, "hours")
        print("Percentage of the people who work the minimum number of hours per week have a salary of more than 50K:",  percentaje_min_fifty, "%")
        print("Country has the highest percentage of people that earn >50K and what is that percentage:",  highest_earning_country)
        print("Percentaje country has the highest percentage of people that earn >50K and what is that percentage:",  highest_earning_country_percentage, "%")
        print("Most popular occupation for those who earn >50K in India:",  most_popular_ocupation)
