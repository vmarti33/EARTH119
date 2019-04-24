#!pyhton2.7
'''
Write a script that computes the annual rate of return and the absolute 
return on an investment of $1,000 at 10% over 30 years-  lessons in compounding interest
'''
# Params 
f_iniInvest= float(input('what are initial savings?'))
f_interest= float(input('specify Interest Rtaae:'))
f_income= float(input('what is your desired monthly income?'))
i_Years= 30.
#Calculations bellow
def retirement(f_money0, f_int, f_income, verbose= False):
    '''
    -  compute annual return on toal savings - f_money0
        :input
        f_money0  - total savings in year 0
        f_int     - interest rate
        f_income  - desired retirement earnings (monthly) 
        :return float() - savings in year N
    '''
    N        = 1000
    currSave = f_money0
    for i in range( N):
        growth = currSave*.1
        currSave += growth 
        if growth>= (f_income*12):
            retire_year= i
            break
        return retire_year 
totSav1=  retirement( f_iniInvest, f_interest, i_Years, verbose = True)
#here is the easier formula to get total savings in year n 

