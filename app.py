from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_content(prompt, custom_instructions=None):
    """
    Generates content based on the prompt and optional custom instructions.
    """
    response = f"Processed prompt: {prompt}"
    if custom_instructions:
        response += f" | Custom instructions: {custom_instructions}"
    return response

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    custom_instructions = data.get('custom_instructions')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    content = generate_content(prompt, custom_instructions)
    return jsonify({'generated_content': content})

if __name__ == "__main__":
    app.run(debug=True)
