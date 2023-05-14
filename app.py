import streamlit as st
import openai
import base64


# Function to add a background image from a local file
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


# Set the Streamlit page title and icon
st.set_page_config(page_title="Baby Shark Tank", page_icon=":shark:")

# Add the background image
add_bg_from_local('shark3d.png')   

# Create a sidebar for user inputs
st.sidebar.title('Settings')

# User input for OpenAI API Key with option to view entered key
openai_api_key = st.sidebar.text_input('Enter OpenAI API Key:', type='password', help='Please enter your OpenAI API Key here')

# Verify the key before using it
if openai_api_key:
    openai.api_key = openai_api_key
else:
    st.error("Please enter your OpenAI API Key in the sidebar to proceed.")

# User selection between GPT-3 and GPT-4
model = st.sidebar.radio('Select Model:', options=['gpt-3.5-turbo', 'gpt-4'], help='Please select the model you want to use')

# User input for number of ideas
num_ideas = st.sidebar.slider("Number of ideas:", min_value=3, max_value=5)

st.write("Toss your ideas into the :blue[Baby Shark Tank] for a quick swim with destiny.")

ideas = []
for i in range(num_ideas):
    idea = st.text_input(f"Idea {i + 1}:")
    ideas.append(idea)

response = None

# When the user clicks the "Cannonball!" button, generate and display the idea analysis
if st.button("Go Swimming!", help = "When the user clicks this button, Baby Shark Tank will generate and display the idea analysis."):
    
        # Show a spinner while the app is working in the background
    with st.spinner('Generating idea analysis...'):

        if all(ideas):
            # Combine ideas into a single string
            combined_ideas = " ".join(ideas)

            # Create a GPT prompt
            # prompt = f"Analyze and combine the following ideas: {combined_ideas}. Generate 3 unique brand name alternatives, a experimental but pertinent innovative business idea driving the unique brand item in question, a 3-step startup plan, and 2 reasons for its potential success in its target market, formulate a convincing business proposal to raise capital for initial start-up investment funding, and a prompt engineered to instruct a web developer what support application to build for the brand item."
            prompt = f"Analyze and combine the following ideas: {combined_ideas}. Generate 3 unique brand name alternatives. Generate an experimental but pertinent innovative business idea driving the unique brand item in question. Provide a design plan in which you explain how the service or product will be engineered technically, what it would physically look like if tangible, or what does the non-tangible aspects look like including software, explain in as much detail as possible to help describe the actual item. Generate a 3-step startup plan. Generate 2 main reasons for its potential success in its target market. Formulate a convincing business proposal to raise capital for initial start-up investment funding. Create the prompt engineered proposal in order to instruct a web developer what support application to build for the brand item."
            response = openai.ChatCompletion.create(
            model=model,
            max_tokens=3500,
            temperature=0.5,
            messages=[
                {"role": "system", "content": "You are a helpful assistant who uses beautiful markdown to help organize the responses to the user's prompt."},
                {"role": "user", "content": prompt},
                ]
            )

            st.write(response.choices[0].message['content'])
        else:
            st.write("Please fill in all the ideas.")
