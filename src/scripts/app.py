from flask import Flask, request, jsonify, render_template
from src.scripts.chat_with_openai import chat_with_openai, load_memory

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.form.get('user_input')
        if not user_input:
            return jsonify({'error': 'No user input provided'}), 400
            
        memory = load_memory()
        response = chat_with_openai(user_input, memory)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
