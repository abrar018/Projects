#Member names: Abrar Rehan UCID 30143339 , Abdullah Al Zabi UCID 30155240
#Group number: L04 - 5

import numpy as np                          # numpy imported for use in the code
import matplotlib.pyplot as plt             # matplotlib.pyplot imported for use in the code

class Country:                      # class coded by Abrar
    """
    A class used to create a class object.

    Attributes:
    name (str) : String that represents the countries name
    region (str) : String that represents the region where the country is located
    sub_region (str): String that represents the sub region where the country is located
    area (int) : Integer that represents the area of a country

    """

    def __init__(self, name, region, sub_region, area):
        self.name = name 
        self.region = region
        self.sub_region = sub_region
        self.area = area


    def print_all_stats(self):
        """
        A function that prints the details of the country instance.

        Parameters: None
        Return: None

        """
        print("Country Name: {0}, UN region: {1}, UN sub-region: {2}, Area: {3}".format(self.name, self.region, self.sub_region, self.area))

def countries(country_name,country_data,population_data,threatened_species):
    """
    A function that calls the class 'Country' and presents the following menu of options 
    for the user to choose information regarding a certain country to be output:

    1 - Displays a graph of the populataion of said country from the years 2000 to 2020
    2 - Displays a bar graph of the threatened species for said country 
    3 - Calculates and outputs the population density of said country for a year that is chosen by the user
    4 - allows the user to return to the main menu where this function was initially called

    Parameters: country_name (str) : String that represents the country name
                country_data (array) : Array that stores data imported from the text of the csv file 'Country_Data'
                population_data (array) : Array that stores the data imported from the text of the csv file 'Population_Data'
                threatened_species (array) : Array that stores the data imported from the text of the scv file 'Threatened_Species'
    
    Return: None

    """
    for i in country_data:
        if i[0].lower() == country_name:        # ensures any input of the country name with the correct spelling is accepted
            country_values = i             # creates a list that will be passed to the class
    print_data = Country(country_values[0],country_values[1],country_values[2],country_values[3]) # class is called
    print_data.print_all_stats()
    boolean = False
    while boolean == False:
        print('--------------COUNTRY----------------')    # menu is displayed for each input 
        print('1. Graph of population from 2000 to 2020')
        print('2. Graph of endangered species.')
        print('3. Population denisty in a year from 2000-2020.')
        print('4. Go back to the last menu.')
        print()
        choice = input('Enter your choice: ')
        if choice in ['1','2','3','4']:                # verifies that the choice is valid
            if choice == '1':                          # code for the population growth plot    # coded by Abdullah
                pop_data = np.genfromtxt('Population_Data.csv', delimiter = ',', dtype = None, encoding = None)
                first_line = pop_data[0]
                z=[]
                for i in first_line:
                    z.append(i)
                z.pop(0)
                years=[]
                for i in z:
                    x=i.replace(' Pop','')
                    years.append(x)
                xpoints = np.array(years)              # points to be plotted on the x-axis
                count = 1
                years = []
                for b in population_data:
                    if b[0].lower() == country_name.lower():
                        while count < 22:
                            years.append(b[count])
                            count += 1    
                ypoints = np.array([years[0],years[1],years[2],years[3],years[4],years[5],years[6],years[7],years[8],years[9],years[10],years[11],years[12],years[13],years[14],years[15],years[16],years[17],years[18],years[19],years[20]]) # points to be plotted on the y-axis
                plt.xlabel('Year')
                plt.ylabel('Population')
                plt.title(f'Population of {country_name} over the years')
                plt.plot(xpoints,ypoints, '-', marker = 'o', color = 'b', label = 'Population curve')
                plt.legend(loc = 'upper left')
                plt.show()

            elif choice == '2':     # code for the threatened species plot     # coded by Abrar
                for i in threatened_species:
                    if i[0].lower() == country_name:
                        pop_data = np.genfromtxt('Threatened_species.csv', delimiter = ',', dtype = None, encoding = None)
                        first_line = pop_data[0]
                        z = []
                        for j in first_line:
                            z.append(j)
                        z.pop(0)
                        species = []                                   # points to plotted on the x-axis  
                        for k in z:
                            species.append(k)
                        data=[i[1],i[2],i[3],i[4]]                     # points to be plotted on the y-axis
                        plt.bar(species,data)
                        for i in range(len(species)):
                            plt.text(i,data[i],data[i])
                        plt.title("Endangered species")
                        plt.xlabel("Species")                      
                        plt.ylabel("Number of endangered species")     
                        plt.legend(loc = 'upper right')
                        plt.show()
                        print()
            elif choice == '3':                     # coded by Abrar
                pop_data = np.genfromtxt('Population_Data.csv', delimiter = ',', dtype = None, encoding = None)
                first_line = pop_data[0]
                z=[]
                for i in first_line:
                    z.append(i)
                z.pop(0)
                years=[]
                for i in z:
                    x=i.replace(' Pop','')
                    years.append(x)
                boolean_1 = False
                while boolean_1 == False:
                    year = input(f'Enter a year from {years[0]} to {years[20]}: ')
                    z = []
                    for i in years:
                        z.append(str(i))
                    if year in z:
                        for i in population_data:
                            if i[0].lower() == country_name:
                                index=z.index(year) + 1
                                population = i[index]
                        for i in country_data:
                            if i[0].lower() == country_name:
                                area = i[3]
                        print(f'The population density of {country_name.title()} on the year {year} is {population / area:.2f} per Sq Km')
                        print()
                        boolean_1 = True
                    else:
                        print('Invalid input. Please try again.')
                        print()

            elif choice == '4':          # sends the user back to main menu
                boolean = True
        
        else:
            print('Invalid input. Please try again.')   # notifies user that the coice is invalid, the loop then prompts for input at the top
            print()
            

def continents(continent_name,country_data,population_data):
    """
    A function that presents the following menu of options for the user to choose 
    information regarding a certain country to be output:

    1 - Calculates and dispays the largest and smallest countries for the chosen continent
    2 - calculates and displays the total area of the chosen continent
    3 - Calculates and displays the countries with the highest and lowest populations
    4 - allows the user to return to the main menu were this function was initially called

    Parameters: continent_name (str) : String that represents the continent name
                country_data (array) : Array that stores data imported from the text of the csv file 'Country_Data'
                population_data (array) : Array that stores the data imported from the text of the csv file 'Population_Data'
    
    Return: None

    """
    count = []
    for i in country_data:
        if i[1].lower() == continent_name:
            count.append(i[0])
    print(f'Continent name: {continent_name.title()}, Number of countries: {len(count)}')  # coded by Abrar

    boolean = False
    while boolean == False:
        print('--------------CONTINENTS----------------')          # menu is displayed for each input 
        print('1. Country with the largest and smallest land mass in the continent')
        print('2. Total area of continent.')
        print('3. Country with the largest and smallest population in the continent.')
        print('4. Go back to the last menu.')
        print()
        choice=input('Enter your choice: ')

        if choice in ['1','2','3','4']:                # choice is validated
            if choice == '1':                      # coded by Abrar
                min = []
                for i in country_data:
                    if i[1].lower() == continent_name:
                        min.append(i[3])
                minimum_area = np.amin(np.array(min))       # using numpy method 'min'
                for e in country_data:
                    if e[1].lower() == continent_name:
                        if e[3] == minimum_area:
                            print(f'The smallest country in {e[1]} is {e[0]} with an area of {e[3]} Sq Km.')
                max = []
                for q in country_data:
                    if q[1].lower() == continent_name:
                        max.append(q[3])
                maximum_area = np.amax(np.array(max))       # using numpy method 'max'
                for p in country_data:
                    if p[1].lower() == continent_name:
                        if p[3] == maximum_area:
                            print(f'The largest country in {p[1]} is {p[0]} with an area of {p[3]} Sq Km.')
                            print()

            elif choice == '2':                 # coded by Abdullah
                area = 0
                for u in country_data :
                    if u[1].lower() == continent_name:
                        area += u[3]           # total area is calculated by adding all the areas of countries in the continents 
                print(f'The total area of {continent_name.title()} is {area} Sq Km.')
                print()

            elif choice == '3':                # coded by Abrar
                pop_data = np.genfromtxt('Population_Data.csv', delimiter = ',', dtype = None, encoding = None)
                first_line = pop_data[0]
                z=[]
                for i in first_line:
                    z.append(i)
                z.pop(0)
                years=[]
                for i in z:
                    x=i.replace(' Pop','')
                    years.append(x)
                year = input(f'Enter a year from {years[0]} to {years[20]}: ')  # prompts user to choose a year to display data specific to it
                boolean_1 = False
                while boolean_1 == False:
                    if year in years:
                        boolean_1 = True
                    else:
                        print('Invalid input. Please try again.')
                        print()
                        year = input(f'Enter a year from {years[0]} to {years[19]}: ')
                dict = {}
                country = []
                for i in country_data:
                    if i[1].lower() == continent_name:
                        country.append(i[0])
                for i in population_data:
                    for j in country:
                        if i[0] == j:
                            index=z.index(year+' Pop') + 1
                            population = i[index]
                            dict[j] = population
                max = 0
                for i in dict:                              # finds the country with the highest population using for loop
                    if dict[i] > max :
                            max = dict[i]
                            country_name = i
                print(f'The country with the highest population in {continent_name.title()} is {country_name.title()} with a population of {max} during the year {year}.')
                min = 999999999999999999   
                for i in dict:                               # finds the country with the lowest population using for loop
                    if dict[i] < min :
                            min = dict[i]
                            country_name = i
                print(f'The country with the lowest population in {continent_name.title()} is {country_name.title()} with a population of {min} during the year {year}.')
                print()

            elif choice == '4':                 # sends the user back to the main menu
                boolean = True

        else:
            print('Invalid input. Please try again.') # notifies user that the coice is invalid, the loop then prompts for input at the top
            print()

def main():      # defines the main function             # coded by Abrar
    """
    A function that imports data from csv files using numpy
    The function then presents the user with the following choices:
    1 - Allows the user to learn about a certain country by calling the function 'countries'
    2 - Allows the user to learn about a certain continent by calling the function 'continents'
    3 - Allows the user to exit the program

    Parameters: None
    Return: None

    """

    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', skip_header = True, dtype = None, encoding = None)
    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True, dtype = None, encoding = None)
    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter = ',', skip_header = True, dtype = None, encoding = None)
 
    country = []                                   # A list of all the countries is initiated 
    continent = []                                  # A list of all the continents is initiated 

    for i in country_data:     
        country.append(i[0].lower())             # the list of counties is filled using the for loop
        if i[1] not in continent:
            continent.append(i[1].lower())           # the list of continents is filled using the for loop

    print('WELCOME TO THE PROGRAM!')       # first piece of output displayed to the user
    print()
    boolean = False
    while boolean == False:
        print('-------------MENU------------')     # menu is displayed for each input
        print('Choose the option about which you would like to learn about')
        print('1. Countries')
        print('2. Continents')
        print('3. Exit the program')
        print()
        choice = input('Enter the option you would like to choose: ')

        if choice in ['1','2','3']:          # ensures choice is valid
            if choice == '1':
                boolean_1 = False
                while boolean_1 == False:
                    country_name = input('Enter the name of the country you would like to learn about: ').lower()
                    if country_name in country:
                        countries(country_name,country_data,population_data,threatened_species)  # calls the function 'countries' and passes the parameters required
                        boolean_1 = True
                    else:
                        print('Input is invalid. Please try again.')
                        print()

            elif choice == '2':
                boolean_1 = False
                while boolean_1 == False:
                    continent_name = input('Enter the name of the continent you would like to know about: ').lower()
                    if continent_name in continent:
                        continents(continent_name,country_data,population_data)  # calls the function 'continents' and passes the parameters required
                        boolean_1 = True
                    else:
                        print('Input is invalid. Please try again.')
                        print()

            elif choice == '3':     # Allows the user to exit the program
                print()
                print('Thank you for using the program.')
                boolean = True

        else:
            print('Invalid input. Please try again.') # notifies user that the coice is invalid, the loop then prompts for input at the top 
            print()

if __name__ == '__main__':
    main()                     # calls the main function

#Coding of the major outlines by Abrar 
#Docstrings and comments written by Abdullah