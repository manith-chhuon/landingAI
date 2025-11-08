from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # In a real app you'd store or forward this somewhere. For demo, we log.
    app.logger.info(f"Contact form received: %s <%s>: %s", name, email, message)
    return jsonify({'status': 'success', 'message': 'Thanks! Your message was received.'})

if __name__ == '__main__':
    # Local dev server
    app.run(debug=True, host='0.0.0.0', port=8000)
