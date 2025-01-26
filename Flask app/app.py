import pickle
import flask
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the model
with open(r'C:\Users\madhu\DSML19\Projects\Machine Learning\MBTI Personality detection\Flask app\MBTI model 1', 'rb') as f:
    model = pickle.load(f)

# Define the routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    input_data = request.form['input_text']

    # Make the prediction
    prediction = model.predict([input_data])[0]

    # Define the personality type full forms
    personality_types = {
        'ISTJ': 'You are Inspector. ISTJs are responsible organizers, driven to create and enforce order within systems and institutions. They are neat and orderly, inside and out, and tend to have a procedure for everything they do.',
        'ISFJ': 'You are Protector. ISFJs are industrious caretakers, loyal to traditions and organizations. They are practical, compassionate, and caring, and are motivated to provide for others and protect them from the perils of life.',
        'INFJ': 'You are Counselor. INFJs are creative nurturers with a strong sense of personal integrity and a drive to help others realize their potential. Creative and dedicated, they have a talent for helping others with original solutions to their personal challenges.',
        'INTJ': 'You are Mastermind. INTJs are analytical problem-solvers, eager to improve systems and processes with their innovative ideas. They have a talent for seeing possibilities for improvement, whether at work, at home, or in themselves.',
        'ISTP': 'You are Craftsperson. ISTPs are observant artisans with an understanding of mechanics and an interest in troubleshooting. They approach their environments with a flexible logic, looking for practical solutions to the problems at hand.',
        'ISFP': 'You are Composer. ISFPs are gentle caretakers who live in the present moment and enjoy their surroundings with cheerful, low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy what life has to offer.',
        'INFP': 'You are Healer. INFPs are imaginative idealists, guided by their own core values and beliefs. To a Healer, possibilities are paramount; the reality of the moment is only of passing concern. They see potential for a better future, and pursue truth and meaning with their own flair.',
        'INTP': 'You are Architect INTPs are philosophical innovators, fascinated by logical analysis, systems, and design. They are preoccupied with theory, and search for the universal law behind everything they see. They want to understand the unifying themes of life, in all their complexity.',
        'ESTP': 'You are Dynamo. ESTPs are energetic thrillseekers who are at their best when putting out fires, whether literal or metaphorical. They bring a sense of dynamic energy to their interactions with others and the world around them',
        'ESFP': 'You are Performer. ESFPs are vivacious entertainers who charm and engage those around them. They are spontaneous, energetic, and fun-loving, and take pleasure in the things around them: food, clothes, nature, animals, and especially people.',
        'ENFP': 'You are Champion. ENFPs are people-centered creators with a focus on possibilities and a contagious enthusiasm for new ideas, people and activities. Energetic, warm, and passionate, ENFPs love to help other people explore their creative potential.',
        'ENTP': 'You are Visionary. ENTPs are inspired innovators, motivated to find new solutions to intellectually challenging problems. They are curious and clever, and seek to comprehend the people, systems, and principles that surround them',
        'ESTJ': 'You are Supervisor. ESTJs are hardworking traditionalists, eager to take charge in organizing projects and people. Orderly, rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about projects in a systematic, methodical way.',
        'ESFJ': 'You are Provider. ESFJs are conscientious helpers, sensitive to the needs of others and energetically dedicated to their responsibilities. They are highly attuned to their emotional environment and attentive to both the feelings of others and the perception others have of them.',
        'ENFJ': 'You are Teacher .ENFJs are idealist organizers, driven to implement their vision of what is best for humanity. They often act as catalysts for human growth because of their ability to see potential in other people and their charisma in persuading others to their ideas.',
        'ENTJ': 'You are Commander ENTJs are strategic leaders, motivated to organize change. They are quick to see inefficiency and conceptualize new solutions, and enjoy developing long-range plans to accomplish their vision. They excel at logical reasoning and are usually articulate and quick-witted.',
    }

    # Get the personality type full form
    personality_type_full = personality_types[prediction]

    # Render the prediction template with the result
    return render_template('predict.html', input_text=input_data, prediction=prediction, personality_type_full=personality_type_full)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
