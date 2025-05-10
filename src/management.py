#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from user import User
import numpy as np
import matplotlib.pyplot as plt

# This type of user is only able to access statistics about visits across different demographics
class Management(User):

    # Creates line plots of visits vs year and saves them to the current directory
    def create_plots(self):

        # Overall plot of visits vs year
        # For each line in the records, extracts the year of the visit, and saves the years as a numpy array
        years = self.records.df['Visit_time'].str.extract('^(\\d{4})', expand = False).to_numpy(dtype = int)

        # Gets the total number of occurrences of each year in the array
        unique_years, counts = np.unique(years, return_counts = True)

        # Creates and saves the line plot
        plt.plot(unique_years, counts)
        plt.title('Overall visits per year')
        plt.xlabel('Year')
        plt.ylabel('Number of visits')
        plt.savefig('./overall_plot.png')
        plt.clf()

        # Gets the unique values of Gender that exist in the records
        genders = self.records.df['Gender'].unique()
        # Creates plots like above, but stratified by gender value
        for gender in genders:
            years = self.records.df.loc[self.records.df['Gender'] == gender]['Visit_time'].str.extract('^(\\d{4})', expand = False).to_numpy(dtype = int)
            unique_years, counts = np.unique(years, return_counts = True)
            plt.plot(unique_years, counts)
            plt.title('Visits by ' + gender + ' patients per year')
            plt.xlabel('Year')
            plt.ylabel('Number of visits')
            plt.savefig('./gender_' + gender + '_plot.png')
        plt.clf()

        # Creates plots like above, but stratified by race value
        races = self.records.df['Race'].unique()
        for race in races:
            years = self.records.df.loc[self.records.df['Race'] == race]['Visit_time'].str.extract('^(\\d{4})', expand = False).to_numpy(dtype = int)
            unique_years, counts = np.unique(years, return_counts = True)
            plt.plot(unique_years, counts)
            plt.title('Visits by ' + race + ' race patients per year')
            plt.xlabel('Year')
            plt.ylabel('Number of visits')
            plt.savefig('./race_' + race + '_plot.png')
            plt.clf()

        # Creates plots like above, but stratified by ethnicity value
        ethnicities = self.records.df['Ethnicity'].unique()
        for ethnicity in ethnicities:
            years = self.records.df.loc[self.records.df['Ethnicity'] == ethnicity]['Visit_time'].str.extract('^(\\d{4})', expand = False).to_numpy(dtype = int)
            unique_years, counts = np.unique(years, return_counts = True)
            plt.plot(unique_years, counts)
            plt.title('Visits by ' + ethnicity + ' ethnicity patients per year')
            plt.xlabel('Year')
            plt.ylabel('Number of visits')
            plt.savefig('./ethn_' + ethnicity + '_plot.png')
            plt.clf()

