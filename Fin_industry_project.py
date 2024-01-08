#  import modules
import os
import json
import csv

# store the file path to a variable
card_event_folder = r"C:\Users\user\Documents\AltSchool_Assessments\events\cards"
user_event_folder = r"C:\Users\user\Documents\AltSchool_Assessments\events\users"



#                        For Card Events

# create a list variable for card events that will be used to store the combined data
card_data = []
for card_events in os.listdir(card_event_folder):
    if card_events.endswith('.json'):
        with open(os.path.join(card_event_folder, card_events), 'r') as card_file:
            cards = json.load(card_file)
            card_data.append(cards)
            
"""
This part of the code extracts 'payload' and 'metadata' dictionaries from each entry in the 'card_data' list. 
It then merges these dictionaries into a single 'cards' dictionary and appends it to the 'card_event' list.
The final 'card_event' list contains the merged dictionaries from the 'payload' and 'metadata' of each entry.
"""
            
# Initialize an empty list to store  card events
card_event = []

# Iterate over each entry in the card list
for i in card_data:
    # Extract 'payload' and 'metadata' dictionaries from the current entry
    payload = i['payload']
    metadata = i['metadata']

    # Merge 'metadata' and 'payload' dictionaries into a single 'cards' dictionary
    merged_cards = {**metadata, **payload}

    # Append the 'cards' to the 'card_event' list
    card_event.append(merged_cards)
            
# Save the contents of the card_event object to a JSON file named 'card_event.json'
with open('card_event.json', 'w') as file:
    # Serialize user_data and write it to the file with an indentation of 4 spaces
    json.dump(card_event, file, indent=4)
    
# Open the 'card_event.json' file for reading
with open('card_event.json', 'r') as file:
    # Load the JSON data from the file into the 'card' variable
    card = json.load(file)
    

    


#                         For User Events


# create a list variable for user events that will be used to store the combined data
user_data = []
for user_events in os.listdir(user_event_folder):
    if user_events.endswith('.json'):
        with open(os.path.join(user_event_folder, user_events), 'r') as user_file:
            users = json.load(user_file)
            user_data.append(users)
            
"""
This part of the code extracts 'payload' and 'metadata' dictionaries from each entry in the 'user_data' list. 
It then merges these dictionaries into a single 'users' dictionary and appends it to the 'user_event' list.
The final 'card_event' list contains the merged dictionaries from the 'payload' and 'metadata' of each entry.
"""
            
# Initialize an empty list to store user events
user_event = []

# Iterate over each entry in the user list
for i in user_data:
    # Extract 'payload' and 'metadata' dictionaries from the current entry
    payload = i['payload']
    metadata = i['metadata']
    
# Replace newline characters with spaces in the address
    payload['address'] = payload['address'].replace('\n', ' ')

    # Merge 'metadata' and 'payload' dictionaries into a single 'merged_users' dictionary
    merged_users = {**metadata, **payload}

    # Append the 'merged_users' to the 'user_event' list
    user_event.append(merged_users)
            
# Save the contents of the user_event object to a JSON file named 'user_event.json'
with open('user_event.json', 'w') as file:
    # Serialize user_data and write it to the file with an indentation of 4 spaces
    json.dump(user_event, file, indent=4)
    
# Open the 'user_event.json' file for reading
with open('user_event.json', 'r') as file:
    # Load the JSON data from the file into the 'user' variable
    user = json.load(file)
    



"""
convert the card_event data to cards.csv file

"""

# Specify the CSV file name

cards_csv_file_name = 'cards.csv'

# define the column names

column_names = ["type",
                "event_at",
                "event_id",
                "id",
                "user_id",
                "created_by_name",
                "updated_at",
                "created_at",
                "active"]

# Open the CSV file in write mode
with open(cards_csv_file_name, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)

    # Write the header row
    csv_writer.writeheader()

    # Write the data rows to the CSV file
    csv_writer.writerows(card_event)



"""
convert the user_event data to users.csv file

"""

# Specify the CSV file name

users_csv_file_name = 'users.csv'
# define the column names

column_names = ["type",
                "event_at",
                "event_id",
                "id",
                "name",
                "address",
                "job",
                "score"]

# Open the CSV file in write mode
with open(users_csv_file_name, 'w', newline='') as u_csv_file:
    # Create a CSV writer object
    csv_writer = csv.DictWriter(u_csv_file, fieldnames=column_names)

    # Write the header row
    csv_writer.writeheader()

    # Write the data rows to the CSV file
    csv_writer.writerows(user_event)

    






