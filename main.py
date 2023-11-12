
import http.server
import socketserver
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import webbrowser
import json
import openai

# Your OpenAI API key (replace wit your actual key)
openai.api_key = "your-api-key"

# port to serve on
PORT = 8000

# handler for the HTTP server
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #  single HTML file when the root is accesed
        if self.path == '/':
            self.path = 'report.html' 
            # any html file name
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        #  AJAX POST request here
        if self.path == '/process-budget':
            # Parse the file from the POST request
            length = int(self.headers['content-length'])
            field_data = self.rfile.read(length)
            # The field data includes the file content, we need to extract it

            # Mock processing - in practice, you'd parse the file content and perform operations with pandas as needed
            budget_summary = process_budget_data(field_data)

            # Generate HTML output6
            generate_html(budget_summary)

            # Prepare and send the response
            response = {
                'status': 'success',
                'message': 'Budget processed and HTML generated successfully.'
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        elif self.path == '/chat-with-gpt':
            # Get the length of the data and read it
            length = int(self.headers['content-length'])
            field_data = self.rfile.read(length)
            data = json.loads(field_data)

            # Get the prompt from the data
            prompt = data.get('prompt')

            # Call the function to get the response 
            response = chat_with_gpt(prompt)

            # Prepare the response
            response_data = {'response': response}

            # Send the response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())

# Function to chat with GPT
def chat_with_gpt(prompt):
    # Call the OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            #whichever model
            messages=[{"role": "user", "content": prompt}]
        )
        # Return the chatbot's response
        return response.choices[0].message.content.strip()

    # Catching any OpenAI API errors
    except openai.error.OpenAIError as e:
        print(f"API call failed: {e}")
        if hasattr(e, 'headers'):
            rate_limit_remaining = e.headers.get('x-rate-limit-remaining')
            print(f"Rate limit remaining: {rate_limit_remaining}")
        return None

# Function to process the budget data (as provided earlier)
def process_budget_data(file_content):
    # Simulate reading file content
    # In practice, you would use pandas to read the file content and process it
    # eexample:
    # df = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
    # budget_summary = df.groupby('Category')['Full amount'].sum().reset_index()
    # This is a placeholder, so let's just return an empty DataFrame
    return pd.DataFrame()

# Generate HTML file from the budget data
def generate_html(budget_data):
    # Load the Jinja2 template environment
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    # Select the template file
    template = env.get_template('budget_template.html')

    # Render the template with the budget data
    output = template.render(budget_data=budget_data.to_dict(orient='records'))

    # Write the rendered HTML to a file
    with open('budget_output.html', 'w') as f:
        f.write(output)

# If the script is run directly, start the server
if __name__ == "__main__":
    # Set the current directory as the server's root

    # Start the HTTP server
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print("serving at port", PORT)
        webbrowser.open(f'http://localhost:{PORT}/report.html')
        httpd.serve_forever()
