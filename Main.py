import pandas as pd
import numpy as np
import joblib
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Load the trained model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Predict scores based on user input
def predict_scores(model, input_text):
    # Use the model to predict scores based on input text
    # Replace this with your actual prediction logic
    # For now, let's just return random scores as placeholders
    uniqueness_score = np.random.uniform(1, 5)
    relevance_score = np.random.uniform(1, 5)
    future_trend_score = np.random.uniform(1, 5)
    overall_uvp_score = np.sum([uniqueness_score, relevance_score, future_trend_score])

    # Round the scores to integers
    uniqueness_score = int(round(uniqueness_score))
    relevance_score = int(round(relevance_score))
    future_trend_score = int(round(future_trend_score))
    overall_uvp_score = int(round(overall_uvp_score))

    return uniqueness_score, relevance_score, future_trend_score, overall_uvp_score

def get_chat_completion(prompt):
    url = "https://chat-gtp-free.p.rapidapi.com/v1/chat/completions"
    payload = {
        "chatId": "92d97036-3e25-442b-9a25-096ab45b0525",
        "messages": [
            {
                "role": "system",
                "content": f"prompt = {prompt}"
            },
            {
                "role": "user",
                "content": f"give me a list of potential competitors for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me another list of marketing strategies for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a sustainability percentage for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of ways to expand in the future for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of ideal customers for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me the potential market size for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of ideal location types for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of pros for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of cons for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of pros for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me an output for market demand - low medium high for ({prompt})"
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "0a58515aedmshbbd56de2a64b618p18862ajsne2cef32b3622",
        "X-RapidAPI-Host": "chat-gtp-free.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None

# Define the Streamlit app
def main():
    st.title('Score Predictor')

    # Custom CSS for modern styling
    st.markdown(
        """
        <style>
        .stTextInput>div>div>div>input {
            border-radius: 8px;
            border: 2px solid #4CAF50;
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stMarkdown {
            color: #333;
            font-size: 16px;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input text box for user input
    input_text = st.text_input('Enter the text:')
    
    # Button to trigger prediction
    if st.button('Predict', key='predict_button'):
        # Load the trained model
        model_path = "C:/Users/p/Desktop/hackathon/Score Predictor.pkl"  # Specify the model path here
        model = load_model(model_path)

        # Predict scores based on user input
        uniqueness_score, relevance_score, future_trend_score, overall_uvp_score = predict_scores(model, input_text)

        # Display the predicted scores
        st.markdown('### Predicted Scores:')
        st.markdown(f'**Uniqueness Score:** {uniqueness_score}')
        st.markdown(f'**Relevance Score:** {relevance_score}')
        st.markdown(f'**Future Trend Score:** {future_trend_score}')
        st.markdown(f'**Overall UVP Score:** {overall_uvp_score}')

        # Get chat completion
        completion = get_chat_completion(input_text)

        if 'code' in completion or 'text' in completion:
            # Display the completion response as an error
            st.error(completion['text'])
        else:
            # Extract lists from completion
            lists = []
            for message in completion['messages']:
                if message['role'] == 'system' and 'list' in message['content']:
                    lists.append(eval(message['content'].split(':')[-1].strip()))

            # Display additional insights
            st.markdown('### Additional Insights:')
            for i, lst in enumerate(lists, start=1):
                st.markdown(f"{i}. {lst}")

# Run the Streamlit app
if __name__ == '__main__':
    main()



import pandas as pd
import numpy as np
import joblib
import streamlit as st
import requests
from bs4 import BeautifulSoup
import time  # Import time module for delay

# Load the trained model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Predict scores based on user input
def predict_scores(model, input_text):
    # Use the model to predict scores based on input text
    # Replace this with your actual prediction logic
    # For now, let's just return random scores as placeholders
    uniqueness_score = np.random.uniform(1, 5)
    relevance_score = np.random.uniform(1, 5)
    future_trend_score = np.random.uniform(1, 5)
    overall_uvp_score = np.sum([uniqueness_score, relevance_score, future_trend_score])

    # Round the scores to integers
    uniqueness_score = int(round(uniqueness_score))
    relevance_score = int(round(relevance_score))
    future_trend_score = int(round(future_trend_score))
    overall_uvp_score = int(round(overall_uvp_score))

    return uniqueness_score, relevance_score, future_trend_score, overall_uvp_score

def get_chat_completion(prompt):
    url = "https://chat-gtp-free.p.rapidapi.com/v1/chat/completions"
    payload = {
        "chatId": "92d97036-3e25-442b-9a25-096ab45b0525",
        "messages": [
            {
                "role": "system",
                "content": f"prompt = {prompt}"
            },
            {
                "role": "user",
                "content": f"give me a list of potential competitors for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me another list of marketing strategies for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a sustainability percentage for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of ways to expand in the future for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of ideal customers for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me the potential market size for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of ideal location types for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of pros for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of cons for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me a list of pros for ({prompt})"
            },
            {
                "role": "user",
                "content": f"give me an output for market demand - low medium high for ({prompt})"
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "0a58515aedmshbbd56de2a64b618p18862ajsne2cef32b3622",
        "X-RapidAPI-Host": "chat-gtp-free.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None

# Define the Streamlit app
def main():
    st.title('Score Predictor')

    # Custom CSS for modern styling
    st.markdown(
        """
        <style>
        .stTextInput>div>div>div>input {
            border-radius: 8px;
            border: 2px solid #4CAF50;
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stMarkdown {
            color: #333;
            font-size: 16px;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input text box for user input
    input_text = st.text_input('Enter the text:')
    
    # Button to trigger prediction
    if st.button('Predict', key='predict_button'):
        # Load the trained model
        model_path = "C:/Users/p/Desktop/hackathon/Score Predictor.pkl"  # Specify the model path here
        model = load_model(model_path)

        # Add a 5-second delay before displaying the predicted scores
        st.info("Predicting scores... ")
        time.sleep(5)  # 5-second delay

        # Predict scores based on user input
        uniqueness_score, relevance_score, future_trend_score, overall_uvp_score = predict_scores(model, input_text)

        # Display the predicted scores
        st.markdown('### Predicted Scores:')
        st.markdown(f'**Uniqueness Score:** {uniqueness_score}')
        st.markdown(f'**Relevance Score:** {relevance_score}')
        st.markdown(f'**Future Trend Score:** {future_trend_score}')
        st.markdown(f'**Overall UVP Score:** {overall_uvp_score}')

        # Get chat completion
        completion = get_chat_completion(input_text)

        if 'code' in completion or 'text' in completion:
            # Display the completion response as an error
            st.error(completion['text'])
        else:
            # Extract lists from completion
            lists = []
            for message in completion['messages']:
                if message['role'] == 'system' and 'list' in message['content']:
                    lists.append(eval(message['content'].split(':')[-1].strip()))

            # Display additional insights
            st.markdown('### Additional Insights:')
            for i, lst in enumerate(lists, start=1):
                st.markdown(f"{i}. {lst}")

# Run the Streamlit app
if __name__ == '__main__':
    main()


if st.button('Go to Investor Platform'):
        import instdash
        instdash.main()
