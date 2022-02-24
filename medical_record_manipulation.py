names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add Priscilla and her insurance cost here
names.insert(10, "Priscilla")
insurance_costs.insert(10, 8320.0)

# Zip the two lists together to create pairs
medical_records = list(zip(insurance_costs, names))
print(medical_records)

# New list alphebtically
alpha_medical_records = list(zip(names, insurance_costs))
alpha_medical_records.sort()
print("This list is sorted alphabetically: " + str(alpha_medical_records))

# How many records are there
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

# First medical record (element)
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

# Sorting the records
medical_records.sort(reverse = True)
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

cheapest_three = medical_records[8:11]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

priciest_three = medical_records[0:3]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

middle_five_records = medical_records[3:8]
print("Here are the five records from the middle of the list: " + str(middle_five_records))

# How many Pauls?
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")