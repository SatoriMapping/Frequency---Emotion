import json
import random
from os import path

#frequency database: dict Hz key with nested dict youtube link and list of emotions
#version 1.0 
#frequency_data = {
#    '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions':['positive', 'unity', 'compassionate', 'peace','loving']},
#    '777 Hz' : {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions':['joy', 'celebration', 'abundance', 'luck']}
#}
#version 2.0
# Function to load data from file
def load_frequency_data(freq_file="frequency_data.json"):
   if path.exists(freq_file):
        try:
            with open(freq_file, "r") as file:
                data = json.load(file)
                # Check if data is empty or invalid
                if not data:  # If file is empty but valid JSON (e.g., {})
                    return {
                        '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions': ['positive', 'unity', 'compassionate', 'peace', 'loving']},
                        '777 Hz': {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions': ['joy', 'celebration', 'abundance', 'luck']}
                    }
                return data
        except (json.JSONDecodeError, ValueError):
            # If JSON is invalid or file is corrupted, use default data
            return {
                '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions': ['positive', 'unity', 'compassionate', 'peace', 'loving']},
                '777 Hz': {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions': ['joy', 'celebration', 'abundance', 'luck']}
            }
        else:
        # If file doesn’t exist, use default data
            return {
                '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions': ['positive', 'unity', 'compassionate', 'peace', 'loving']},
                '777 Hz': {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions': ['joy', 'celebration', 'abundance', 'luck']}
            }

# Load the data at startup
frequency_data = load_frequency_data()

#save data to file
def save_frequency_data(data, filename='frequency_data.json'):
    with open('frequency_data.json', 'w') as save_to_freq_file:
        json.dump(data, save_to_freq_file, indent=4)

#feature 1: feel the frequency
def feel_the_frequency():
    #pick frequency
    global frequency_data
    pick_frequency = random.choice(list(frequency_data.keys()))
    print(f'Play frequency: {pick_frequency} via {frequency_data[pick_frequency]['link']}')
    
    #get user emotions
    user_emotions = input("What emotions do you feel when tuning in on this frequency? Separate your emotions with commas").lower().split(', ')

    #compare user emotions with database stored emotions
    known_emotions = frequency_data[pick_frequency]['emotions']
    overlapping_emotions = [feeling for feeling in user_emotions if feeling in known_emotions]
    new_emotions = [feeling for feeling in user_emotions if feeling not in known_emotions]
    print(f'Others also felt: {overlapping_emotions if overlapping_emotions else 'None'}.')
    print(f'You were the first to add: {new_emotions if new_emotions else 'None'}.')

    #add new_emotions to database
    for emotion in new_emotions:
        frequency_data[pick_frequency]['emotions'].append(emotion)
    save_frequency_data(frequency_data)

#feature 2: generate frequency for current mood 
def generate_frequency():
    global frequency_data
    current_mood = input(f'In one word, how do you feel right now?').lower()
    found = False
    for frequency, emotion_data in frequency_data.items():
        if current_mood in emotion_data['emotions']:
            print(f'We found this frequency to align with your current mood of {current_mood}: {frequency}')
            print(f'Play it via {emotion_data['link']}')
            found = True
            break
    if not found:
        print('Sorry, we found no matching frequencies for that current mood')    

#feature 3: generate frequency for desired mood
def generate_emotion():
    global frequency_data    
    desired_mood = input(f'In one word, what feeling would you like to transition to?').lower()
    found = False
    for frequency, emotion_data in frequency_data.items():
        if desired_mood in emotion_data['emotions']:
            print(f'We found this frequency for you to tune into a mood of {desired_mood}: {frequency}')
            print(f'Play it via {emotion_data['link']}')
            found = True
            break
    if not found:
            print('Sorry, we found no matching frequencies for that desired mood')    

#feature 4: frequency/emotion graphing
def frequency_emotion_graph():
    global frequency_data
    user_freq = input('What frequency would you like to portray (e.g. 432)?') + ' Hz'
    if user_freq in frequency_data:
        user_freq_emotions = frequency_data[user_freq]['emotions']
        print(f'This {user_freq} frequency is associated with {', '.join(user_freq_emotions)}')
    else:
        print('Sorry, we found no emotions for that frequency')    

#focus interface on simple search bar 'search for frequency' (feature 3), alternative below plain text play random frequency (feature 1)
def main():
    while True:
        print('\nChoose feature')
        print('1. Feel The Frequency')
        print('2. Generate Frequency')
        print('3. Generate Emotion')
        print('4. Frequency/emotion graphing')
        print('5. Exit')
        user_selection = input('Choose your feature (1-5):')
        if user_selection == '1':
            feel_the_frequency()
        elif user_selection == '2':
            generate_frequency()
        elif user_selection == '3':
            generate_emotion()
        elif user_selection == '4':
            frequency_emotion_graph()
        else:
            break
    

#test database
#print(frequency_data)
#print(len(frequency_data))

#test feel_the_frequency()
#feel_the_frequency()

#test impact on database after feel_the_frequency()
#print(frequency_data)

#test generate_frequency()
#generate_frequency()

#test generate_emotion()
#generate_emotion()

#test frequency_emotion_graph()
#frequency_emotion_graph()

#test menu
main()