import json
import random
from os import path
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load frequency data
def load_frequency_data(freq_file="frequency_data.json"):
    if path.exists(freq_file):
        try:
            with open(freq_file, "r") as file:
                data = json.load(file)
                if not data:
                    return {
                        '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions': ['positive', 'unity', 'compassionate', 'peace', 'loving']},
                        '777 Hz': {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions': ['joy', 'celebration', 'abundance', 'luck']}
                    }
                return data
        except (json.JSONDecodeError, ValueError):
            return {
                '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions': ['positive', 'unity', 'compassionate', 'peace', 'loving']},
                '777 Hz': {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions': ['joy', 'celebration', 'abundance', 'luck']}
            }
    return {
        '432 Hz': {'link': 'https://www.youtube.com/watch?v=IU13sdrLQ-M', 'emotions': ['positive', 'unity', 'compassionate', 'peace', 'loving']},
        '777 Hz': {'link': 'https://www.youtube.com/watch?v=yD6dpHRvPXA', 'emotions': ['joy', 'celebration', 'abundance', 'luck']}
    }

# Save frequency data
def save_frequency_data(data, filename='frequency_data.json'):
    with open(filename, 'w') as save_to_freq_file:
        json.dump(data, save_to_freq_file, indent=4)

frequency_data = load_frequency_data()

@app.route('/')
def index():
    return render_template('index.html')

# Route for Feature 1: Feel the Frequency
@app.route('/feel_the_frequency', methods=['POST'])
def feel_the_frequency():
    global frequency_data
    pick_frequency = random.choice(list(frequency_data.keys()))
    user_emotions = request.json.get('emotions', '').lower().split(', ')
    known_emotions = frequency_data[pick_frequency]['emotions']
    overlapping_emotions = [feeling for feeling in user_emotions if feeling in known_emotions]
    new_emotions = [feeling for feeling in user_emotions if feeling not in known_emotions]
    for emotion in new_emotions:
        frequency_data[pick_frequency]['emotions'].append(emotion)
    save_frequency_data(frequency_data)
    return jsonify({
        'frequency': pick_frequency,
        'link': frequency_data[pick_frequency]['link'],
        'overlapping_emotions': overlapping_emotions if overlapping_emotions else 'None',
        'new_emotions': new_emotions if new_emotions else 'None'
    })

# Route for Feature 2: Generate Frequency
@app.route('/generate_frequency', methods=['POST'])
def generate_frequency():
    global frequency_data
    current_mood = request.json.get('mood', '').lower()
    for frequency, emotion_data in frequency_data.items():
        if current_mood in emotion_data['emotions']:
            return jsonify({
                'frequency': frequency,
                'link': emotion_data['link'],
                'message': f'We found this frequency to align with your current mood of {current_mood}: {frequency}'
            })
    return jsonify({'message': 'Sorry, we found no matching frequencies for that current mood'})

if __name__ == '__main__':
    app.run(debug=True)