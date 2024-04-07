import streamlit as st
import numpy as np
import pandas as pd

def generate_random_ideas():
    ideas = [
        "Hyper-personalized financial planning app for young adults",
        "AI-powered customer service chatbots for small businesses",
        "3D-printed prosthetics with custom designs and biocompatible materials",
        "Subscription box for self-care products for men",
        "Online platform for peer-to-peer learning and skill exchange",
        "VR museum tours with interactive exhibits",
        "Culturally-focused cooking classes with international chefs",
        "On-demand mobile car detailing service",
        "AI-powered content creation platform for social media",
        "Sustainable and ethical office supply subscription service",
        "Personalized sleep coaching app with biofeedback monitoring",
        "Online marketplace for buying and selling used textbooks",
        "Agri-tourism experiences on local farms and vineyards",
        "AI-powered legal research and case analysis platform",
        "Subscription box for organic and fair-trade beauty products",
        "VR fitness classes with live instructors and social interaction",
        "Online platform connecting tutors with students for after-school help",
        "Personalized meal planning service with grocery delivery integration",
        "AI-powered mental health chatbot for anxiety and stress management",
        "Interactive escape room experiences designed for corporate team building",
        "On-demand personal styling service with virtual consultations",
        "Subscription box for educational coding kits for kids",
        "Personalized language learning app with gamified challenges",
        "Professional cybersecurity consulting services for small businesses",
        "3D-printed architectural models for construction and design projects",
        "Online marketplace for vintage clothing and accessories",
        "AI-powered songwriting assistant with music theory integration",
        "Eco-friendly cleaning service using natural and non-toxic products",
        "Online platform connecting businesses with freelance content creators"
    ]
    uvp_scores = np.random.randint(1, 10, size=len(ideas))
    return list(zip(ideas, uvp_scores))

def main():
    st.title('Investor Dashboard')
    st.markdown('007 Userbase')

    ideas = generate_random_ideas()
    df = pd.DataFrame(ideas, columns=['Idea', 'UVP Score'])

    st.dataframe(df.style.set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#f8f9fa')]
    }]))

    st.button('Connect')

if __name__ == '__main__':
    main()
