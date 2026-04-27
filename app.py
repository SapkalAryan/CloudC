from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def home():
 return """
 <h1>Cloud Computing Lab - Experiment 5</h1>
 <h2>PaaS Implementation using Render</h2>
 <p>This application is deployed on Render's free PaaS tier!</p>
 <p>Current Time: """ + __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
 """
@app.route('/health')
def health():
 return {"status": "healthy", "platform": "Render PaaS"}
Cloud Computing Lab Page 5 of 7
if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(host='0.0.0.0', port=port)
