import os
csvpath = os.path.join('Resources', 'employee_data1.csv')
output_path = os.path.join('Resources', 'clean_emp_data1.csv')

import csv

def date_conv(d): 
    d = d.split('-')
    year = d[0]
    month = d[1]
    day =d[2]
    return month + "/" + day + "/" + year
    


def soc_conv(s):
    s =s.split('-')
    soc_a = s[0]
    soc_b = s[1]
    soc_c = s[2]
    return "***-**-" + soc_c

def state_conv(s): 
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    return us_state_abbrev[s]
    





with open(csvpath, newline='') as csvfile:
    csvfile.readline()
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    #Then convert and export the data back into a csv
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        
        #  Each row is read as a row
        for row in csvreader:
            #Add employee Id
            emp_id = row[0]
            # Add name
            name = row[1]
            
            #The Name column should be split into separate First Name and Last Name columns.
            name = name.split(' ')
            first_name = name[0]
            last_name = name[1]
            
            # Add birth date
            birth_date = date_conv(row[2])
          

           

            # add social security number
            soc_sec_num = soc_conv(row[3])

            # add state 
            state = state_conv(row[4])
            
            # write the arrays to a csv 
            csvwriter.writerow([emp_id,first_name,last_name,birth_date,soc_sec_num,state])

