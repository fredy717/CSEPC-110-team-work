print("Please enter the following information:\n")
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")
print('''
    The ID Card is:
    ----------------------------------------
    %s, %s
    %s
    D: %s
    
    %s
    %s
    
    Hair: %s\tEyes: %s
    Month: %s\tTraining: %s
    ----------------------------------------''' \
      % (last_name.upper(), first_name.capitalize(),
         job_title.title(), id_number,  email, phone,
         hair_color, eye_color, month, training))
