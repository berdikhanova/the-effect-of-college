import pandas

filename = r'C:\Users\User\Downloads\salaries-by-college-type.csv'
#reading the dataset and separating the variables by ","
assignment_data = pandas.read_csv(filename, delimiter=",")

assignment_data.head(10)
import numpy as np
#separating the dataset into Engineering Schools and Liberal Arts schools
data_engineering = assignment_data[assignment_data['School Type'] == 'Engineering']
data_liberal = assignment_data[assignment_data['School Type'] == 'Liberal Arts']


#defining the outcome variables
engineering_mid_salary_ = data_engineering['Mid-Career Median Salary']
liberal_mid_salary_ = data_liberal['Mid-Career Median Salary']

engineering_mid_salary = []
liberal_mid_salary = []

for x in engineering_mid_salary_:
    engineering_mid_salary.append(float(x.replace('$', '').replace(',', '')))

for x in liberal_mid_salary_:
    liberal_mid_salary.append(float(x.replace('$', '').replace(',', '')))
    
#calculating summary statistics for the graduates of the Engineering Schools
print('Mid-career Median Salary of Graduates of Engineering schools')

variable_count1 = len(engineering_mid_salary)
print ('Count', variable_count1)

variable_mean1 = np.mean(engineering_mid_salary)
print('The mean of the function is', variable_mean1)

variable_median1 = np.median(engineering_mid_salary)
print ('The median of the function is', variable_median1) 

variable_mode1 = max(set(engineering_mid_salary), key=engineering_mid_salary.count)
print('The mode of the function is', variable_mode1) 

variable_range1 = (max(engineering_mid_salary)-min(engineering_mid_salary))
print('The range of the function is', variable_range1) 

variable_stdev1 = np.std(engineering_mid_salary)
print('The standard deviation of the function is', variable_stdev1)

#calculating summary statistics for the graduates of the Liberal Arts schools
print('Mid-career Median Salary of Graduates of Liberal Arts schools')

variable_count2 = len(liberal_mid_salary)
print ('Count', variable_count2)

variable_mean2 = np.mean(liberal_mid_salary)
print('The mean of the function is', variable_mean2)

variable_median2 = np.median(liberal_mid_salary)
print ('The median of the function is', variable_median2) 

variable_mode2 = max(set(liberal_mid_salary), key=liberal_mid_salary.count)
print('The mode of the function is', variable_mode2)

variable_range2 = (max(liberal_mid_salary)-min(liberal_mid_salary))
print('The range of the function is', variable_range2)

variable_stdev2 = np.std(liberal_mid_salary)
print('The standard deviation of the function is', variable_stdev2) 
the_whole_list  = engineering_mid_salary + liberal_mid_salary

variable_count3 = len(the_whole_list)
print ('Count', variable_count3)

variable_mean3 = np.mean(the_whole_list)
print('The mean of the function is', variable_mean3)

variable_median3 = np.median(the_whole_list)
print ('The median of the function is', variable_median3) 

variable_mode3 = max(set(the_whole_list), key=the_whole_list.count)
print('The mode of the function is', variable_mode3) 

variable_range3 = (max(the_whole_list)-min(the_whole_list))
print('The range of the function is', variable_range3) 

variable_stdev3 = np.std(the_whole_list)
print('The standard deviation of the function is', variable_stdev3)


#creating data visualizations 
import matplotlib.pyplot as plt 

x = the_whole_list # Assign a variable to the data-set which we want to visualize 

#assigning values for xaxis and set the number of bins for the histogram, 
#choosing 5 bins instead of 11 in order to make the clear visualization and identify the pattern
plt.hist(x, bins = 8)

plt.xlabel('Mid-career Median Salary', ) #naming the xaxis 
plt.ylabel('Frequency', color = 'black') #naming the yaxis 

plt.title('The frequency of Mid-career Median Salary of Liberal Arts and Engineering Graduates') #naming the histogram 

plt.show() #showing the result 
import scipy.stats as stats
from scipy import mean
confidence = 0.95
data = the_whole_list

n = len(data)
m = mean(data)
std_err = sem(data)
h = std_err * stats.norm.ppf((1 + confidence) / 2)

start = m - h
print (start)
end = m + h
print (end)
x = engineering_mid_salary
#assigning a variable to the data-set which we want to visualize 

#assigning values for x-axis and setting the number of bins for the histogram, 
#choosing 5 bins instead of 11 in order to make the clear visualization and identify the pattern
plt.hist(x, bins = 6)

plt.xlabel('Mid-career Median Salary', ) #naming the x-axis 
plt.ylabel('Frequency', color = 'black') #naming the y-axis 

plt.title('The frequency of Mid-career Median Salary of Engineering Graduates') #naming the histogram 

plt.show() #showing the result 
x = liberal_mid_salary#assigning a variable to the data-set which we want to visualize 

#assigning values for x-axis and setting the number of bins for the histogram, 
#choosing 5 bins instead of 11 in order to make the clear visualization and identify the pattern
plt.hist(x, bins = 7)

plt.xlabel('Mid-career Median Salary', ) #naming the x-axis 
plt.ylabel('Frequency', color = 'black') #naming the y-axis 

plt.title('The frequency of Mid-career Median Salary of Liberal Arts Graduates') #naming the histogram 

plt.show() #showing the result 
point_estimate = variable_mean2 - variable_mean1
print (point_estimate)

standard_error = (variable_stdev2**2/variable_count2 + variable_stdev1**2/variable_count1)**(1/2)

print (standard_error)

t_score = (point_estimate - 0)/standard_error

print (t_score)
data1 = engineering_mid_salary
data2 = liberal_mid_salary
tails = 1

#conducting difference of means test
def difference_of_means_test(data1,data2,tails):
    n1 = len(data1)
    n2 = len(data2)

    x1 = np.mean(data1)
    x2 = np.mean(data2)

    s1 = np.std(data1,ddof=1) # Bessel's correction
    s2 = np.std(data2,ddof=1)

    SE = np.sqrt(s1**2/n1 + s2**2/n2)
    Tscore = np.abs((x2 - x1))/SE
    df = min(n1,n2) - 1 
    pvalue = tails*stats.t.cdf(-Tscore,df)

    SDpooled = np.sqrt((s1**2*(n1-1) + s2**2*(n2-1))/(n1+n2-2)) 
    Cohensd = (x2 - x1)/SDpooled

    print('p =',pvalue)
    print('d =',Cohensd)
difference_of_means_test(data1, data2, tails)
