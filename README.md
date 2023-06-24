# Baby Shark Tank

Baby Shark Tank is an innovative application powered by OpenAI's GPT-3.5-turbo model. It uses Streamlit to create an interactive web application that generates creative ideas.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.6 or higher
* An OpenAI API key
* Streamlit

## Setup

Follow these steps to get your development environment set up:

1. Clone this repository to your local machine.
2. Install the required Python packages:

```bash
pip install streamlit openai

Create a .env file in the root directory of the project and add your OpenAI API key:

OPENAI_API_KEY=your-openai-api-key

Run the Streamlit app:  bash streamlit run app.py

The app will start a web server that listens on http://localhost:8501.

Code Explanation
The app.py file contains the main logic for the application. It uses Streamlit to create an interactive web application. The application generates creative ideas using OpenAI's GPT-3.5-turbo model.

The add_bg_from_local function is used to add a background image to the application. The image is encoded in base64 and added to the application using Streamlit's unsafe_allow_html function.

The application uses the openai package to interact with the OpenAI API. The dotenv package is used to load the OpenAI API key from the .env file.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


Copyright (c) [2023] [peterholt@peterholt.io] 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
