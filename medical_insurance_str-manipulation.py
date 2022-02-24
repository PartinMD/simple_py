medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#print(medical_data)
# Replace all instances of # with $
updated_medical_data = medical_data.replace('#', '$')
#print(updated_medical_data)

# How many total records are there in the data set.
num_records = 0

for character in updated_medical_data:
  if character == '$':
    num_records += 1

#print(num_records) #prints 10
print("There are {} medical records in the data.".format(num_records))

# Split the data into record form that is easier to analyze.
medical_data_split = updated_medical_data.split(';')
#print(medical_data_split)

medical_records = []
for data in medical_data_split:
  medical_records.append(data.split(','))
#print(medical_records)

# Clean the data
medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
print(medical_records_clean)

# Analyze the data
# Print the names of each record
for records in medical_records_clean:
  records[0] = records[0].upper()
  print(records[0])
# Sort data into new lists
names = []
ages = []
bmis = []
insurance_costs = []

for records in medical_records_clean:
  names.append(records[0])
  ages.append(records[1])
  bmis.append(records[2])
  insurance_costs.append(records[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)
# Detailed analyses BMIs and Costs
total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
print("Average BMI: " + str(average_bmi))

insurance_costs_clean = []
total_costs = 0

for costs in insurance_costs:
  insurance_costs_clean.append(costs.replace('$', ''))
#print(insurance_costs_clean)

for cost in insurance_costs_clean:
  total_costs += float(cost)

average_cost = total_costs / len(insurance_costs_clean)
print("Average Cost: " + str(average_cost))

# Print messages outlining each record.
for records in medical_records_clean:
  name = records[0]
  age = records[1]
  bmi = records[2]
  insurance_cost = records[3]
  print("{} is {} years old with a BMI of {} and an insurance cost of {}.".format(name, age, bmi, insurance_cost))

























