# AI_and_Me_Platform.py
# Streamlit application for AI & Me: Citizen Empowerment Platform

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import json
import base64
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="AI & Me: Citizen Empowerment Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# 1. SAMPLE DATA INITIALIZATION
# ===============================

# Create sample AI systems data
def create_ai_systems_data():
    systems = [
        {
            "id": 1,
            "title": "Housing Allocation Assistant",
            "description": "AI system that helps prioritize social housing applications based on various factors including waiting time, household composition, and special circumstances.",
            "department": "Housing",
            "risk_level": "high",
            "last_updated": "2023-04-15",
            "data_used": [
                "Household composition",
                "Current housing situation",
                "Income level",
                "Time on waiting list",
                "Special circumstances (medical, social)",
                "Neighborhood preference"
            ],
            "rights": [
                "Request human review of decisions",
                "Appeal automated decisions",
                "Access your data used in the system",
                "Request explanation of specific decisions"
            ],
            "audit_info": {
                "last_audit": "February 2023",
                "audited_by": "Independent Housing Algorithm Review Board",
                "bias_tested": True,
                "citizen_consulted": True
            },
            "feedback_count": 87
        },
        {
            "id": 2,
            "title": "Traffic Flow Optimization",
            "description": "AI system that adjusts traffic lights to reduce congestion and improve traffic flow throughout the city.",
            "department": "Transportation",
            "risk_level": "low",
            "last_updated": "2023-03-10",
            "data_used": [
                "Real-time traffic camera data",
                "Historical traffic patterns",
                "Public transport schedules",
                "Special events information"
            ],
            "rights": [
                "Access to traffic optimization logic",
                "Submit feedback on traffic flow issues"
            ],
            "audit_info": {
                "last_audit": "January 2023",
                "audited_by": "City Transportation Department",
                "bias_tested": True,
                "citizen_consulted": False
            },
            "feedback_count": 24
        },
        {
            "id": 3,
            "title": "Fraud Detection System",
            "description": "Identifies potential fraud in benefit applications and flags cases for human review.",
            "department": "Social Services",
            "risk_level": "high",
            "last_updated": "2023-02-20",
            "data_used": [
                "Application information",
                "Historical case data",
                "Cross-referenced public records",
                "Previous applications"
            ],
            "rights": [
                "Right to human review",
                "Right to explanation",
                "Right to contest automated decisions",
                "Right to correct inaccurate data"
            ],
            "audit_info": {
                "last_audit": "December 2022",
                "audited_by": "Independent Ethics Committee",
                "bias_tested": True,
                "citizen_consulted": True
            },
            "feedback_count": 56
        },
        {
            "id": 4,
            "title": "Public Space Monitoring",
            "description": "Analyzes camera feeds to detect crowding and incidents in public spaces.",
            "department": "Public Safety",
            "risk_level": "medium",
            "last_updated": "2023-01-15",
            "data_used": [
                "Anonymized video feeds",
                "Crowd density patterns",
                "Weather data",
                "Event schedules"
            ],
            "rights": [
                "Right to privacy in public spaces",
                "Right to know about monitoring",
                "Right to access monitoring policies"
            ],
            "audit_info": {
                "last_audit": "November 2022",
                "audited_by": "Privacy Commission",
                "bias_tested": True,
                "citizen_consulted": False
            },
            "feedback_count": 43
        },
        {
            "id": 5,
            "title": "Waste Collection Routing",
            "description": "Optimizes garbage collection routes based on fill levels and historical patterns.",
            "department": "Sanitation",
            "risk_level": "low",
            "last_updated": "2023-05-05",
            "data_used": [
                "Bin fill level sensors",
                "Historical collection data",
                "Traffic conditions",
                "Weather forecasts"
            ],
            "rights": [
                "Access to collection schedules",
                "Request special collections"
            ],
            "audit_info": {
                "last_audit": "March 2023",
                "audited_by": "Sanitation Department",
                "bias_tested": False,
                "citizen_consulted": True
            },
            "feedback_count": 12
        },
        {
            "id": 6,
            "title": "Energy Usage Optimization",
            "description": "Manages energy usage in public buildings to reduce consumption and costs.",
            "department": "Sustainability",
            "risk_level": "low",
            "last_updated": "2023-04-20",
            "data_used": [
                "Real-time energy consumption",
                "Building occupancy data",
                "Weather conditions",
                "Historical usage patterns"
            ],
            "rights": [
                "Access to energy usage data",
                "Submit suggestions for improvement"
            ],
            "audit_info": {
                "last_audit": "January 2023",
                "audited_by": "Energy Efficiency Board",
                "bias_tested": False,
                "citizen_consulted": False
            },
            "feedback_count": 8
        }
    ]
    return pd.DataFrame(systems)

# Create sample citizen concerns data
def create_citizen_concerns():
    concerns = [
        {"id": 1, "category": "Powerlessness", "description": "I feel powerless to influence how AI is used in my city.", "count": 142},
        {"id": 2, "category": "Lack of Transparency", "description": "I am concerned AI is used without my knowledge.", "count": 98},
        {"id": 3, "category": "Social Inequality", "description": "I worry AI reinforces existing social inequality.", "count": 76},
        {"id": 4, "category": "Privacy", "description": "I'm afraid of being watched or profiled.", "count": 65},
        {"id": 5, "category": "Explainability", "description": "I want explanations I can understand.", "count": 54}
    ]
    return pd.DataFrame(concerns)

# Create sample citizen feedback data
def create_feedback_data():
    # Generate random dates within the last 3 months
    today = datetime.now()
    dates = [(today - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d") for _ in range(200)]
    
    # Generate random feedback for different systems
    systems = [1, 2, 3, 4, 5, 6]
    system_ids = [random.choice(systems) for _ in range(200)]
    
    # Generate sentiment
    sentiments = ["positive", "negative", "neutral", "confused", "concerned"]
    sentiment_weights = [0.2, 0.4, 0.15, 0.15, 0.1]  # More negative feedback than positive
    feedback_sentiments = [np.random.choice(sentiments, p=sentiment_weights) for _ in range(200)]
    
    # Generate feedback text
    feedback_texts = [
        "The system works well for my needs.",
        "I don't understand how decisions are made.",
        "This seems biased against certain groups.",
        "The explanation was clear and helpful.",
        "I'm concerned about my privacy with this system.",
        "The system is too slow to respond.",
        "I appreciate the transparency in how this works.",
        "This system seems to favor certain neighborhoods.",
        "I couldn't find information about how my data is used.",
        "The decision made in my case seemed unfair."
    ]
    
    # Create DataFrame
    feedback_df = pd.DataFrame({
        "id": range(1, 201),
        "system_id": system_ids,
        "date": dates,
        "sentiment": feedback_sentiments,
        "feedback_text": [random.choice(feedback_texts) for _ in range(200)],
        "resolved": [random.choice([True, False]) for _ in range(200)]
    })
    
    return feedback_df

# Create sample co-design sessions
def create_codesign_sessions():
    sessions = [
        {
            "id": 1,
            "title": "Housing Allocation Algorithm Redesign",
            "date": "2023-06-15",
            "time": "18:00-20:00",
            "location": "Public Library Amsterdam, Main Branch",
            "spots_left": 10,
            "system_id": 1,
            "description": "Help us redesign aspects of the Housing Allocation Algorithm to better serve all citizens."
        },
        {
            "id": 2,
            "title": "Public Space Monitoring Ethics Workshop",
            "date": "2023-06-22",
            "time": "13:00-16:00",
            "location": "De Balie, Kleine-Gartmanplantsoen",
            "spots_left": 0,
            "system_id": 4,
            "description": "Discuss ethical considerations in public space monitoring and help establish guidelines."
        },
        {
            "id": 3,
            "title": "Traffic Management AI Feedback Session",
            "date": "2023-07-05",
            "time": "17:00-19:00",
            "location": "Online (Zoom)",
            "spots_left": 25,
            "system_id": 2,
            "description": "Provide feedback on the traffic management system and suggest improvements."
        },
        {
            "id": 4,
            "title": "Fraud Detection Fairness Workshop",
            "date": "2023-07-12",
            "time": "14:00-17:00",
            "location": "Amsterdam City Hall",
            "spots_left": 15,
            "system_id": 3,
            "description": "Help ensure the fraud detection system is fair and unbiased for all citizens."
        }
    ]
    return pd.DataFrame(sessions)

# Create sample questions
def create_questions():
    questions = [
        {
            "id": 1,
            "system_id": 1,
            "question": "How does the housing allocation system decide who gets priority?",
            "answer": "The system assigns different weights to factors based on the city's housing policy. Currently, time on the waiting list accounts for 40% of the priority score, household needs for 30%, special circumstances for 20%, and neighborhood preference for 10%.",
            "date": "2023-05-01",
            "is_public": True
        },
        {
            "id": 2,
            "system_id": 1,
            "question": "Can I see my priority score?",
            "answer": "Yes, you can request your priority score and the factors that contributed to it by contacting the Housing Department or through your online housing account.",
            "date": "2023-05-05",
            "is_public": True
        },
        {
            "id": 3,
            "system_id": 3,
            "question": "How is my data protected in the fraud detection system?",
            "answer": "Your data is encrypted and access is restricted to authorized personnel only. The system uses anonymized data for pattern recognition, and personal identifiers are only used when a case requires human review.",
            "date": "2023-05-10",
            "is_public": True
        },
        {
            "id": 4,
            "system_id": 4,
            "question": "Can I opt out of the public space monitoring?",
            "answer": "The public space monitoring system uses anonymized data and does not track individuals. Clear signage is posted in areas where monitoring occurs. While you cannot opt out entirely, no personally identifiable information is stored unless there is a safety incident.",
            "date": "2023-05-07",
            "is_public": True
        },
        {
            "id": 5,
            "system_id": 1,
            "question": "How often is the housing algorithm audited for bias?",
            "answer": "The housing allocation algorithm undergoes a comprehensive bias audit every six months, with the most recent audit completed in February 2023. Additionally, ongoing monitoring occurs monthly to detect any potential issues.",
            "date": "2023-05-15",
            "is_public": True
        }
    ]
    return pd.DataFrame(questions)

# Initialize session state for data persistence
if 'ai_systems' not in st.session_state:
    st.session_state.ai_systems = create_ai_systems_data()

if 'citizen_concerns' not in st.session_state:
    st.session_state.citizen_concerns = create_citizen_concerns()

if 'feedback_data' not in st.session_state:
    st.session_state.feedback_data = create_feedback_data()

if 'codesign_sessions' not in st.session_state:
    st.session_state.codesign_sessions = create_codesign_sessions()

if 'questions' not in st.session_state:
    st.session_state.questions = create_questions()

# ===============================
# 2. STYLING AND HELPER FUNCTIONS
# ===============================

# Custom CSS
def load_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: white;
            background-color: #1e293b;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .sub-header {
            font-size: 1.8rem;
            margin-top: 2rem;
        }
        .card {
            border: 1px solid #e2e8f0;
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            background-color: white;
        }
        .risk-high {
            color: white;
            background-color: #ef4444;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .risk-medium {
            color: white;
            background-color: #f59e0b;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .risk-low {
            color: white;
            background-color: #10b981;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .department-badge {
            background-color: #e2e8f0;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.8rem;
        }
        .feedback-count {
            display: flex;
            align-items: center;
            font-size: 0.9rem;
            color: #6b7280;
        }
        .trust-indicator {
            margin-bottom: 1rem;
        }
        .trust-label {
            font-weight: bold;
            margin-bottom: 0.25rem;
        }
        .trust-bar-bg {
            background-color: #e2e8f0;
            height: 0.5rem;
            border-radius: 0.25rem;
            margin-top: 0.25rem;
        }
        .trust-bar {
            height: 0.5rem;
            border-radius: 0.25rem;
        }
        .trust-bar-yes {
            background-color: #10b981;
        }
        .trust-bar-no {
            background-color: #ef4444;
        }
        .footer {
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #e2e8f0;
            text-align: center;
            color: #6b7280;
        }
        .tab-content {
            padding: 1rem 0;
        }
        .explainer-box {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .data-list {
            list-style-type: none;
            padding-left: 0;
        }
        .data-list li {
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        .data-list li:before {
            content: "✓";
            color: #10b981;
            margin-right: 0.5rem;
        }
        .rights-list {
            list-style-type: none;
            padding-left: 0;
        }
        .rights-list li {
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        .rights-list li:before {
            content: "🛡️";
            margin-right: 0.5rem;
        }
        .concern-card {
            border-left: 4px solid;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
            border-radius: 0.25rem;
        }
        .concern-purple {
            border-left-color: #8b5cf6;
        }
        .concern-blue {
            border-left-color: #3b82f6;
        }
        .concern-amber {
            border-left-color: #f59e0b;
        }
        .concern-count {
            font-size: 0.9rem;
            color: #6b7280;
        }
        .session-card {
            border: 1px solid #e2e8f0;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
        }
        .session-date {
            font-size: 0.9rem;
            color: #6b7280;
        }
        .spots-available {
            color: #10b981;
            font-weight: bold;
        }
        .spots-full {
            color: #ef4444;
            font-weight: bold;
        }
        .question-card {
            border: 1px solid #e2e8f0;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
        }
        .question-date {
            font-size: 0.8rem;
            color: #6b7280;
        }
        .question-text {
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .answer-text {
            color: #1f2937;
        }
        .impact-card {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1.5rem;
        }
        .impact-icon {
            background-color: #ecfdf5;
            color: #10b981;
            padding: 0.75rem;
            border-radius: 9999px;
            margin-right: 1rem;
        }
        .impact-content h4 {
            margin: 0 0 0.5rem 0;
            font-weight: bold;
        }
        .impact-date {
            font-size: 0.8rem;
            color: #6b7280;
            margin-top: 0.25rem;
        }
    </style>
    """, unsafe_allow_html=True)

# Risk level badge
def risk_badge(risk_level):
    if risk_level == "high":
        return '<span class="risk-high">HIGH RISK</span>'
    elif risk_level == "medium":
        return '<span class="risk-medium">MEDIUM RISK</span>'
    else:
        return '<span class="risk-low">LOW RISK</span>'

# Department badge
def department_badge(department):
    return f'<span class="department-badge">{department}</span>'

# Format date
def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%B %d, %Y")

# ===============================
# 3. PAGE COMPONENTS
# ===============================

# Home page
def home_page():
    st.markdown('<h1 class="main-header">AI & Me: Understand, Question, Influence</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1.2rem;">
        A civic platform empowering Amsterdam citizens to understand how AI is used in their city, 
        question how it affects them, and influence how it evolves.
    </p>
    """, unsafe_allow_html=True)
    
    # Language selector in sidebar
    st.sidebar.title("Language")
    language = st.sidebar.selectbox(
        "Select your language",
        ["English", "Nederlands", "العربية", "Türkçe", "Polski"]
    )
    
    # Top citizen concerns
    st.markdown('<h2 class="sub-header">Top Citizen Concerns</h2>', unsafe_allow_html=True)
    
    concerns = st.session_state.citizen_concerns.sort_values('count', ascending=False)
    
    # Display concerns as cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="concern-card concern-purple">
            <h3>{concerns.iloc[0]['category']}</h3>
            <p>{concerns.iloc[0]['description']}</p>
            <p class="concern-count">Mentioned by {concerns.iloc[0]['count']} citizens</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="concern-card concern-blue">
            <h3>{concerns.iloc[1]['category']}</h3>
            <p>{concerns.iloc[1]['description']}</p>
            <p class="concern-count">Mentioned by {concerns.iloc[1]['count']} citizens</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="concern-card concern-amber">
            <h3>{concerns.iloc[2]['category']}</h3>
            <p>{concerns.iloc[2]['description']}</p>
            <p class="concern-count">Mentioned by {concerns.iloc[2]['count']} citizens</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualize concerns
    fig = px.bar(
        concerns, 
        x='category', 
        y='count',
        title='Citizen Concerns About AI Systems',
        labels={'category': 'Concern Category', 'count': 'Number of Citizens'},
        color='count',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["Understand", "Question", "Influence"])
    
    # Understand tab
    with tab1:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h3>What is AI in Amsterdam?</h3>
                <p>The City of Amsterdam uses various AI systems to improve services, manage resources, and make decisions. These range from traffic management to social service allocation.</p>
                <p>All systems are registered and explained here to ensure transparency and accountability.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
                <h3>Your Rights</h3>
                <p>As a citizen of Amsterdam, you have the right to:</p>
                <ul class="rights-list">
                    <li>Know when AI is being used to make decisions affecting you</li>
                    <li>Understand how these systems work in plain language</li>
                    <li>Challenge automated decisions</li>
                    <li>Provide feedback on AI systems</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<h3>AI Systems in Amsterdam</h3>', unsafe_allow_html=True)
        
        # Display AI systems as cards
        systems = st.session_state.ai_systems
        
        # Create three columns
        cols = st.columns(3)
        
        # Display each system in a card
        for i, (_, system) in enumerate(systems.iterrows()):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="card">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <h4>{system['title']}</h4>
                        {risk_badge(system['risk_level'])}
                    </div>
                    <p>{system['description']}</p>
                    <div style="margin: 0.5rem 0;">
                        {department_badge(system['department'])}
                    </div>
                    <p class="feedback-count">
                        <span style="margin-right: 0.25rem;">💬</span> {system['feedback_count']} citizen feedback
                    </p>
                    <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                        <a href="/?page=system_details&id={system['id']}">Understand</a>
                        <a href="/?page=system_feedback&id={system['id']}">Give Feedback</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Question tab
    with tab2:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="card">
                <h3>Ask About AI in Amsterdam</h3>
                <p>Submit your questions about how AI is used in the city</p>
            </div>
            """, unsafe_allow_html=True)
            
            question = st.text_area("Your Question", placeholder="e.g., How does the housing allocation system decide who gets priority?", height=120)
            
            system_options = ["Select a system"] + list(systems['title'])
            selected_system = st.selectbox("Related AI System (optional)", system_options)
            
            make_public = st.checkbox("Make my question public (anonymous)")
            
            if st.button("Submit Question"):
                if question:
                    st.success("Your question has been submitted. A representative will respond within 5 business days.")
                else:
                    st.error("Please enter a question before submitting.")
        
        with col2:
            st.markdown("""
            <div class="card">
                <h3>Recent Public Questions</h3>
                <p>Questions from other citizens</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display recent questions
            questions = st.session_state.questions
            for _, question in questions.iterrows():
                system_name = systems[systems['id'] == question['system_id']].iloc[0]['title']
                
                st.markdown(f"""
                <div class="question-card">
                    <p class="question-text">{question['question']}</p>
                    <div style="margin-bottom: 0.5rem;">
                        <span class="department-badge">{system_name}</span>
                        <span class="question-date">{format_date(question['date'])}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('<a href="/?page=all_questions">View All Questions</a>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Influence tab
    with tab3:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="card">
                <h3>Share Your Experience</h3>
                <p>Tell us how AI systems have affected you or your community</p>
            </div>
            """, unsafe_allow_html=True)
            
            system_options = ["Select a system"] + list(systems['title'])
            selected_system = st.selectbox("Which AI System?", system_options, key="feedback_system")
            
            experience = st.text_area("Your Experience", placeholder="Describe how this AI system affected you or your community...", height=120)
            
            impact_type = st.radio(
                "Impact Type",
                ["Positive", "Negative", "Neutral", "Confusing", "Concerning"]
            )
            
            anonymous = st.checkbox("Submit anonymously")
            
            if st.button("Submit Feedback"):
                if experience and selected_system != "Select a system":
                    st.success("Thank you for your feedback! It will help us improve AI systems in Amsterdam.")
                else:
                    st.error("Please select a system and describe your experience before submitting.")
        
        with col2:
            st.markdown("""
            <div class="card">
                <h3>Upcoming Co-Design Sessions</h3>
                <p>Help shape the future of AI in Amsterdam</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display upcoming sessions
            sessions = st.session_state.codesign_sessions
            for _, session in sessions.iterrows():
                system_name = systems[systems['id'] == session['system_id']].iloc[0]['title']
                spots_class = "spots-available" if session['spots_left'] > 0 else "spots-full"
                spots_text = f"{session['spots_left']} spots left" if session['spots_left'] > 0 else "Fully booked"
                
                st.markdown(f"""
                <div class="session-card">
                    <h4>{session['title']}</h4>
                    <p class="session-date">{session['date']} • {session['time']}</p>
                    <p>{session['location']}</p>
                    <p class="{spots_class}">{spots_text}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('<a href="/?page=all_sessions">View All Sessions</a>', unsafe_allow_html=True)
        
        st.markdown('<h3>Impact of Your Feedback</h3>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <div class="impact-card">
                <div class="impact-icon">👍</div>
                <div class="impact-content">
                    <h4>Housing Allocation Algorithm Updated</h4>
                    <p>After 87 citizen feedback reports highlighting bias against single-parent households, the algorithm was audited and updated in March 2023.</p>
                    <p class="impact-date">Implemented: March 2023</p>
                </div>
            </div>
            
            <div class="impact-card">
                <div class="impact-icon">🛡️</div>
                <div class="impact-content">
                    <h4>Public Space Monitoring Privacy Enhancements</h4>
                    <p>Citizen concerns led to improved anonymization techniques and clearer signage about camera monitoring in public spaces.</p>
                    <p class="impact-date">Implemented: January 2023</p>
                </div>
            </div>
            
            <div class="impact-card">
                <div class="impact-icon">💬</div>
                <div class="impact-content">
                    <h4>Fraud Detection Explanation Improvements</h4>
                    <p>Based on feedback about confusing notifications, the system now provides clearer explanations when flagging potential issues.</p>
                    <p class="impact-date">Implemented: December 2022</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# System details page
def system_details_page(system_id):
    system = st.session_state.ai_systems[st.session_state.ai_systems['id'] == system_id].iloc[0]
    
    # Back button
    st.markdown('<a href="/" style="display: inline-flex; align-items: center; margin-bottom: 1rem;"><span style="margin-right: 0.25rem;">←</span> Back to Overview</a>', unsafe_allow_html=True)
    
    # Header
    st.markdown(f"""
    <div style="background-color: #1e293b; color: white; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1>{system['title']}</h1>
                <p>Department of {system['department']}</p>
            </div>
            <div>
                {risk_badge(system['risk_level'])}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        tab1, tab2, tab3 = st.tabs(["Understand", "Question", "Influence"])
        
        # Understand tab
        with tab1:
            st.markdown("""
            <div class="card">
                <h3>What is this system for?</h3>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<p>{system['description']}</p>", unsafe_allow_html=True)
            
            st.markdown("""
                <h3 style="margin-top: 1.5rem;">How does it affect me?</h3>
            """, unsafe_allow_html=True)
            
            if system['id'] == 1:  # Housing Allocation
                st.markdown("""
                <p>If you've applied for social housing in Amsterdam, this system may influence your position on the waiting list and the housing options presented to you. The system considers factors like your household composition, current housing situation, time on the waiting list, and special circumstances.</p>
                <p><strong>Important:</strong> This system does not make final decisions. Housing officers review the system's recommendations before making allocation decisions.</p>
                """, unsafe_allow_html=True)
            elif system['id'] == 2:  # Traffic Flow
                st.markdown("""
                <p>This system affects your daily commute by optimizing traffic light timings to reduce congestion. It may adjust signal patterns based on real-time traffic conditions, potentially changing your wait times at intersections throughout the city.</p>
                <p><strong>Important:</strong> The system prioritizes overall traffic flow efficiency while maintaining safety standards.</p>
                """, unsafe_allow_html=True)
            elif system['id'] == 3:  # Fraud Detection
                st.markdown("""
                <p>If you apply for benefits or services from the city, this system may analyze your application to identify potential inconsistencies. It does not make final decisions about fraud, but flags cases for human review.</p>
                <p><strong>Important:</strong> Being flagged by the system does not mean you've done anything wrong. Human reviewers carefully evaluate all flagged cases.</p>
                """, unsafe_allow_html=True)
            elif system['id'] == 4:  # Public Space Monitoring
                st.markdown("""
                <p>This system monitors public spaces to detect unusual crowding or incidents that may require attention. It does not track or identify individuals but analyzes patterns in anonymized video feeds.</p>
                <p><strong>Important:</strong> The system is designed with privacy protections and does not use facial recognition technology.</p>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <p>This system may affect various aspects of city services you use. The specific impacts depend on how you interact with the relevant department.</p>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                <h3 style="margin-top: 1.5rem;">What data does it use?</h3>
                <div class="explainer-box">
                    <ul class="data-list">
            """, unsafe_allow_html=True)
            
            for data_item in system['data_used']:
                st.markdown(f"<li>{data_item}</li>", unsafe_allow_html=True)
            
            st.markdown("""
                    </ul>
                </div>
                
                <h3 style="margin-top: 1.5rem;">What rights do I have?</h3>
                <div class="explainer-box">
                    <ul class="rights-list">
            """, unsafe_allow_html=True)
            
            for right in system['rights']:
                st.markdown(f"<li>{right}</li>", unsafe_allow_html=True)
            
            st.markdown("""
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Explainability feedback
            st.markdown("""
            <div style="margin-top: 2rem; border-top: 1px solid #e2e8f0; padding-top: 1rem;">
                <h3>Was this explanation helpful?</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👍 Yes, it was clear"):
                    st.success("Thank you for your feedback!")
            with col2:
                if st.button("👎 No, I'm still confused"):
                    st.text_area("Please tell us what was confusing or what questions you still have...", key="confusion_feedback")
                    if st.button("Submit Feedback", key="submit_confusion"):
                        st.success("Thank you for your feedback! We'll use it to improve our explanations.")
        
        # Question tab
        with tab2:
            st.markdown("""
            <div class="card">
                <h3>Ask a Question</h3>
                <p>Have questions about how this system works or how it might affect you? Submit your question below and a department representative will respond within 5 business days.</p>
            </div>
            """, unsafe_allow_html=True)
            
            question = st.text_area("Your Question", placeholder=f"e.g., How does the {system['title']} consider my specific situation?", height=120)
            
            make_public = st.checkbox("Make my question public (anonymous)")
            
            if st.button("Submit Question", key="submit_system_question"):
                if question:
                    st.success("Your question has been submitted. A representative will respond within 5 business days.")
                else:
                    st.error("Please enter a question before submitting.")
            
            st.markdown("""
            <h3 style="margin-top: 2rem;">Frequently Asked Questions</h3>
            """, unsafe_allow_html=True)
            
            # Filter questions for this system
            system_questions = st.session_state.questions[st.session_state.questions['system_id'] == system_id]
            
            for _, question in system_questions.iterrows():
                st.markdown(f"""
                <div class="question-card">
                    <p class="question-text">{question['question']}</p>
                    <p class="answer-text">{question['answer']}</p>
                    <p class="question-date">{format_date(question['date'])}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Influence tab
        with tab3:
            st.markdown("""
            <div class="card">
                <h3>Share Your Experience</h3>
                <p>Your feedback helps us improve this system. Share how it has affected you or your community.</p>
            </div>
            """, unsafe_allow_html=True)
            
            experience = st.text_area("Your Experience", placeholder=f"Describe your experience with the {system['title']}...", height=120)
            
            impact = st.radio("How did this system affect you?", ["Positively", "Negatively", "Neutral"])
            
            contact_me = st.checkbox("I'm willing to be contacted for follow-up (optional)")
            
            if contact_me:
                email = st.text_input("Email (optional)")
            
            if st.button("Submit Feedback", key="submit_system_feedback"):
                if experience:
                    st.success("Thank you for your feedback! It will help us improve this system.")
                else:
                    st.error("Please describe your experience before submitting.")
            
            st.markdown("""
            <h3 style="margin-top: 2rem;">Recent System Changes</h3>
            """, unsafe_allow_html=True)
            
            if system['id'] == 1:  # Housing Allocation
                st.markdown("""
                <div class="impact-card">
                    <div class="impact-icon">👨‍👩‍👧‍👦</div>
                    <div class="impact-content">
                        <h4>Improved consideration for single-parent households</h4>
                        <p>Based on citizen feedback, the system was updated to better account for the unique challenges faced by single-parent households.</p>
                        <p class="impact-date">Implemented: March 2023</p>
                    </div>
                </div>
                
                <div class="impact-card">
                    <div class="impact-icon">📄</div>
                    <div class="impact-content">
                        <h4>Clearer explanation of decisions</h4>
                        <p>The system now provides more detailed explanations when housing offers are made, helping applicants understand why they were matched with specific properties.</p>
                        <p class="impact-date">Implemented: January 2023</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif system['id'] == 2:  # Traffic Flow
                st.markdown("""
                <div class="impact-card">
                    <div class="impact-icon">🚌</div>
                    <div class="impact-content">
                        <h4>Public transport prioritization</h4>
                        <p>Based on citizen feedback, the system now gives higher priority to public transport vehicles at intersections.</p>
                        <p class="impact-date">Implemented: February 2023</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif system['id'] == 3:  # Fraud Detection
                st.markdown("""
                <div class="impact-card">
                    <div class="impact-icon">📝</div>
                    <div class="impact-content">
                        <h4>Improved notification clarity</h4>
                        <p>Based on citizen feedback about confusing notifications, the system now provides clearer explanations when flagging potential issues.</p>
                        <p class="impact-date">Implemented: December 2022</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif system['id'] == 4:  # Public Space Monitoring
                st.markdown("""
                <div class="impact-card">
                    <div class="impact-icon">🔒</div>
                    <div class="impact-content">
                        <h4>Enhanced privacy protections</h4>
                        <p>Based on citizen concerns, we've implemented improved anonymization techniques and added clearer signage in monitored areas.</p>
                        <p class="impact-date">Implemented: January 2023</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Co-design session for this system
            system_sessions = st.session_state.codesign_sessions[st.session_state.codesign_sessions['system_id'] == system_id]
            
            if not system_sessions.empty:
                session = system_sessions.iloc[0]
                spots_class = "spots-available" if session['spots_left'] > 0 else "spots-full"
                spots_text = f"{session['spots_left']} spots left" if session['spots_left'] > 0 else "Fully booked"
                
                st.markdown(f"""
                <div style="margin-top: 2rem; background-color: #eff6ff; padding: 1rem; border-radius: 0.5rem;">
                    <h3 style="color: #1e40af; display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">ℹ️</span> Upcoming Co-Design Session
                    </h3>
                    <p style="color: #1e3a8a; margin-top: 0.5rem;">
                        Join us on {session['date']} ({session['time']}) at {session['location']} to help redesign aspects of this system.
                    </p>
                    <p class="{spots_class}" style="margin-top: 0.5rem;">{spots_text}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if session['spots_left'] > 0:
                    if st.button("Register to Participate"):
                        st.success("Thank you for registering! You will receive a confirmation email with details.")
    
    with col2:
        # Trust Indicators
        st.markdown("""
        <div class="card">
            <h3>Trust Indicators</h3>
        """, unsafe_allow_html=True)
        
        # Independent Audit
        audit_value = "Independent" in system['audit_info']['audited_by']
        st.markdown(f"""
        <div class="trust-indicator">
            <div class="trust-label">Independent Audit</div>
            <div class="trust-details">Last audited: {system['audit_info']['last_audit']} by {system['audit_info']['audited_by']}</div>
            <div class="trust-bar-bg">
                <div class="trust-bar {'trust-bar-yes' if audit_value else 'trust-bar-no'}" style="width: {'100%' if audit_value else '0%'};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bias Testing
        bias_value = system['audit_info']['bias_tested']
        st.markdown(f"""
        <div class="trust-indicator">
            <div class="trust-label">Bias Testing</div>
            <div class="trust-details">{'Tested for bias against protected groups' if bias_value else 'Not tested for bias'}</div>
            <div class="trust-bar-bg">
                <div class="trust-bar {'trust-bar-yes' if bias_value else 'trust-bar-no'}" style="width: {'100%' if bias_value else '0%'};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Citizen Consultation
        citizen_value = system['audit_info']['citizen_consulted']
        st.markdown(f"""
        <div class="trust-indicator">
            <div class="trust-label">Citizen Consultation</div>
            <div class="trust-details">{'Citizens were consulted during development' if citizen_value else 'No citizen consultation'}</div>
            <div class="trust-bar-bg">
                <div class="trust-bar {'trust-bar-yes' if citizen_value else 'trust-bar-no'}" style="width: {'100%' if citizen_value else '0%'};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Human Oversight (assumed for all systems)
        st.markdown(f"""
        <div class="trust-indicator">
            <div class="trust-label">Human Oversight</div>
            <div class="trust-details">All decisions are reviewed by department staff</div>
            <div class="trust-bar-bg">
                <div class="trust-bar trust-bar-yes" style="width: 100%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Transparency
        transparency_value = len(system['data_used']) >= 4 and len(system['rights']) >= 3
        st.markdown(f"""
        <div class="trust-indicator">
            <div class="trust-label">Transparency</div>
            <div class="trust-details">{'Full algorithm documentation is publicly available' if transparency_value else 'Limited documentation available'}</div>
            <div class="trust-bar-bg">
                <div class="trust-bar {'trust-bar-yes' if transparency_value else 'trust-bar-no'}" style="width: {'100%' if transparency_value else '0%'};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        </div>
        """, unsafe_allow_html=True)
        
        # System Details
        st.markdown("""
        <div class="card">
            <h3>System Details</h3>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="margin-bottom: 0.75rem;">
            <p style="color: #6b7280; font-size: 0.875rem;">Department</p>
            <p style="font-weight: 500;">{system['department']}</p>
        </div>
        
        <div style="margin-bottom: 0.75rem;">
            <p style="color: #6b7280; font-size: 0.875rem;">Last Updated</p>
            <p style="font-weight: 500;">{format_date(system['last_updated'])}</p>
        </div>
        
        <div style="margin-bottom: 0.75rem;">
            <p style="color: #6b7280; font-size: 0.875rem;">Citizen Feedback</p>
            <p style="font-weight: 500;">{system['feedback_count']} reports</p>
        </div>
        
        <div style="margin-bottom: 0.75rem;">
            <p style="color: #6b7280; font-size: 0.875rem;">Technical Documentation</p>
            <a href="#" style="color: #2563eb;">View Technical Details</a>
        </div>
        
        <div>
            <p style="color: #6b7280; font-size: 0.875rem;">Data Protection Impact Assessment</p>
            <a href="#" style="color: #2563eb;">View Assessment</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

# Housing allocation simulator
def housing_simulator_page():
    st.markdown('<a href="/" style="display: inline-flex; align-items: center; margin-bottom: 1rem;"><span style="margin-right: 0.25rem;">←</span> Back to Overview</a>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #1e293b; color: white; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.5rem;">
        <h1>Civic AI Simulator</h1>
        <p>Explore how AI systems make decisions in Amsterdam</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h2>Housing Allocation Simulator</h2>
        <p>See how the Housing Allocation Assistant might evaluate your application</p>
        
        <div style="background-color: #fff7ed; border: 1px solid #fdba74; border-radius: 0.375rem; padding: 1rem; margin: 1rem 0; display: flex; align-items: flex-start;">
            <span style="color: #c2410c; margin-right: 0.75rem; font-size: 1.25rem;">⚠️</span>
            <div>
                <p style="font-weight: 500; color: #9a3412; margin-bottom: 0.25rem;">This is a simplified simulation</p>
                <p style="color: #9a3412; font-size: 0.875rem;">This simulator provides a general idea of how the system works, but the actual algorithm is more complex and considers additional factors. Results are for educational purposes only.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3>Your Situation</h3>", unsafe_allow_html=True)
        
        waiting_time = st.slider("Years on waiting list", 0, 10, 5)
        household_size = st.slider("Household size", 1, 6, 2)
        income = st.slider("Annual household income (€)", 10000, 60000, 30000, step=1000)
        
        current_housing = st.selectbox(
            "Current housing situation",
            ["Renting privately", "Temporary accommodation", "Sharing with family/friends", "Homeless/emergency housing"],
            index=0
        )
        
        neighborhood_preference = st.selectbox(
            "Neighborhood preference",
            ["Any neighborhood", "Centrum", "West", "Oost", "Zuid", "Noord"],
            index=0
        )
        
        medical_need = st.checkbox("Medical or accessibility needs")
    
    with col2:
        if 'simulation_run' not in st.session_state:
            st.session_state.simulation_run = False
        
        if not st.session_state.simulation_run:
            st.markdown("""
            <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem;">
                <div style="background-color: #f1f5f9; border-radius: 9999px; padding: 1.5rem; margin-bottom: 1rem;">
                    <span style="font-size: 2rem;">ℹ️</span>
                </div>
                <h3>See how the system evaluates your case</h3>
                <p style="color: #6b7280; margin-bottom: 1.5rem;">
                    Adjust the sliders and options on the left to represent your situation, then run the simulation to see how the system might prioritize your application.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Run Simulation"):
                st.session_state.simulation_run = True
                st.experimental_rerun()
        else:
            # Calculate priority score (simplified version of the algorithm)
            score = 0
            
            # Waiting time (40% weight)
            score += (waiting_time / 10) * 40
            
            # Household needs (30% weight)
            household_score = 30 if household_size > 3 else household_size * 10
            score += household_score
            
            # Special circumstances (20% weight)
            if medical_need:
                score += 20
            
            if current_housing == "Homeless/emergency housing":
                score += 20
            elif current_housing == "Temporary accommodation":
                score += 15
            else:
                score += 5
            
            # Neighborhood preference (10% weight)
            if neighborhood_preference != "Any neighborhood":
                score -= 5  # Slight penalty for being selective
            
            # Ensure score is between 0 and 100
            score = max(0, min(100, round(score)))
            
            # Determine priority level
            if score >= 80:
                priority = "High"
                priority_color = "emerald"
                wait_time = "6-12 months"
            elif score >= 50:
                priority = "Medium"
                priority_color = "amber"
                wait_time = "1-2 years"
            else:
                priority = "Low"
                priority_color = "red"
                wait_time = "2+ years"
            
            # Display results
            st.markdown("<h3>Simulation Results</h3>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background-color: white; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1.5rem;">
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <div style="font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem;">{score}</div>
                    <div style="color: #6b7280;">Priority Score (out of 100)</div>
                </div>
                
                <div style="width: 100%; background-color: #f1f5f9; height: 0.75rem; border-radius: 9999px; margin-bottom: 1.5rem;">
                    <div style="height: 0.75rem; border-radius: 9999px; background-color: {'#10b981' if priority_color == 'emerald' else '#f59e0b' if priority_color == 'amber' else '#ef4444'}; width: {score}%;"></div>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
                    <div style="background-color: #f8fafc; padding: 1rem; border-radius: 0.375rem;">
                        <div style="color: #6b7280; font-size: 0.875rem; margin-bottom: 0.25rem;">Priority Level</div>
                        <div style="font-weight: 700; color: {'#10b981' if priority_color == 'emerald' else '#f59e0b' if priority_color == 'amber' else '#ef4444'}; display: flex; align-items: center;">
                            <span style="margin-right: 0.25rem;">{'✓' if priority == 'High' else 'ℹ️' if priority == 'Medium' else '⚠️'}</span>
                            {priority}
                        </div>
                    </div>
                    <div style="background-color: #f8fafc; padding: 1rem; border-radius: 0.375rem;">
                        <div style="color: #6b7280; font-size: 0.875rem; margin-bottom: 0.25rem;">Est. Wait Time</div>
                        <div style="font-weight: 700;">{wait_time}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h4>Key Factors in Your Score</h4>", unsafe_allow_html=True)
            
            waiting_points = round((waiting_time / 10) * 40)
            household_points = household_size > 3 and 30 or household_size * 10
            
            special_points = 0
            if medical_need:
                special_points += 20
            
            if current_housing == "Homeless/emergency housing":
                special_points += 20
            elif current_housing == "Temporary accommodation":
                special_points += 15
            else:
                special_points += 5
            
            neighborhood_points = 5 if neighborhood_preference != "Any neighborhood" else 10
            
            st.markdown(f"""
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Waiting time (40%)</span>
                    <span style="font-weight: 500;">{waiting_points} points</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Household needs (30%)</span>
                    <span style="font-weight: 500;">{household_points} points</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Special circumstances (20%)</span>
                    <span style="font-weight: 500;">{special_points} points</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Neighborhood preference (10%)</span>
                    <span style="font-weight: 500;">{neighborhood_points} points</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Adjust Parameters"):
                    st.session_state.simulation_run = False
                    st.experimental_rerun()
            with col2:
                if st.button("Save Results"):
                    st.success("Results saved to your profile.")
    
    st.markdown("<h3 style='text-align: center; margin-top: 2rem;'>Try Other AI Simulators</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card" style="cursor: pointer;">
            <h4>Traffic Flow Simulator</h4>
            <p>See how the traffic management AI optimizes signal timing</p>
            <div style="text-align: center; margin: 1rem 0;">
                <div style="background-color: #f1f5f9; border-radius: 9999px; padding: 1rem; display: inline-block; margin-bottom: 0.5rem;">
                    <div style="background-color: #ef4444; height: 1rem; width: 1rem; border-radius: 9999px;"></div>
                </div>
                <p style="font-size: 0.875rem; color: #6b7280;">Explore traffic patterns and signal optimization</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="cursor: pointer;">
            <h4>Fraud Detection Simulator</h4>
            <p>Understand how the fraud detection system works</p>
            <div style="text-align: center; margin: 1rem 0;">
                <div style="background-color: #f1f5f9; border-radius: 9999px; padding: 1rem; display: inline-block; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.5rem;">⚠️</span>
                </div>
                <p style="font-size: 0.875rem; color: #6b7280;">Learn about risk factors and detection methods</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card" style="cursor: pointer;">
            <h4>Energy Usage Simulator</h4>
            <p>See how the energy optimization system works</p>
            <div style="text-align: center; margin: 1rem 0;">
                <div style="background-color: #f1f5f9; border-radius: 9999px; padding: 1rem; display: inline-block; margin-bottom: 0.5rem;">
                    <div style="height: 1.5rem; width: 1.5rem; display: flex; align-items: center; justify-content: center;">
                        <div style="background-color: #10b981; height: 0.75rem; width: 0.25rem; margin: 0 0.125rem; border-radius: 0.125rem;"></div>
                        <div style="background-color: #10b981; height: 1rem; width: 0.25rem; margin: 0 0.125rem; border-radius: 0.125rem;"></div>
                        <div style="background-color: #10b981; height: 1.25rem; width: 0.25rem; margin: 0 0.125rem; border-radius: 0.125rem;"></div>
                        <div style="background-color: #10b981; height: 0.5rem; width: 0.25rem; margin: 0 0.125rem; border-radius: 0.125rem;"></div>
                    </div>
                </div>
                <p style="font-size: 0.875rem; color: #6b7280;">Explore energy usage optimization in public buildings</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# All questions page
def all_questions_page():
    st.markdown('<a href="/" style="display: inline-flex; align-items: center; margin-bottom: 1rem;"><span style="margin-right: 0.25rem;">←</span> Back to Overview</a>', unsafe_allow_html=True)
    
    st.markdown("""
    <h1>Public Questions & Answers</h1>
    <p>Questions from citizens about AI systems in Amsterdam</p>
    """, unsafe_allow_html=True)
    
    # Filter options
    systems = st.session_state.ai_systems
    system_options = ["All Systems"] + list(systems['title'])
    selected_system = st.selectbox("Filter by System", system_options)
    
    # Get questions
    questions = st.session_state.questions
    
    if selected_system != "All Systems":
        system_id = systems[systems['title'] == selected_system].iloc[0]['id']
        questions = questions[questions['system_id'] == system_id]
    
    # Display questions
    for _, question in questions.iterrows():
        system_name = systems[systems['id'] == question['system_id']].iloc[0]['title']
        
        st.markdown(f"""
        <div class="question-card">
            <p class="question-text">{question['question']}</p>
            <p class="answer-text">{question['answer']}</p>
            <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                <span class="department-badge">{system_name}</span>
                <span class="question-date">{format_date(question['date'])}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# All co-design sessions page
def all_sessions_page():
    st.markdown('<a href="/" style="display: inline-flex; align-items: center; margin-bottom: 1rem;"><span style="margin-right: 0.25rem;">←</span> Back to Overview</a>', unsafe_allow_html=True)
    
    st.markdown("""
    <h1>Co-Design Sessions</h1>
    <p>Help shape the future of AI in Amsterdam by participating in these sessions</p>
    """, unsafe_allow_html=True)
    
    # Filter options
    systems = st.session_state.ai_systems
    system_options = ["All Systems"] + list(systems['title'])
    selected_system = st.selectbox("Filter by System", system_options)
    
    # Get sessions
    sessions = st.session_state.codesign_sessions
    
    if selected_system != "All Systems":
        system_id = systems[systems['title'] == selected_system].iloc[0]['id']
        sessions = sessions[sessions['system_id'] == system_id]
    
    # Display sessions
    for _, session in sessions.iterrows():
        system_name = systems[systems['id'] == session['system_id']].iloc[0]['title']
        spots_class = "spots-available" if session['spots_left'] > 0 else "spots-full"
        spots_text = f"{session['spots_left']} spots left" if session['spots_left'] > 0 else "Fully booked"
        
        st.markdown(f"""
        <div class="session-card">
            <h3>{session['title']}</h3>
            <p>{session['description']}</p>
            <p class="session-date">{session['date']} • {session['time']}</p>
            <p>{session['location']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                <span class="department-badge">{system_name}</span>
                <span class="{spots_class}">{spots_text}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if session['spots_left'] > 0:
            if st.button(f"Register for {session['title']}", key=f"register_{session['id']}"):
                st.success("Thank you for registering! You will receive a confirmation email with details.")

# System feedback page
def system_feedback_page(system_id):
    system = st.session_state.ai_systems[st.session_state.ai_systems['id'] == system_id].iloc[0]
    
    st.markdown('<a href="/" style="display: inline-flex; align-items: center; margin-bottom: 1rem;"><span style="margin-right: 0.25rem;">←</span> Back to Overview</a>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <h1>Submit Feedback for {system['title']}</h1>
    <p>Your feedback helps us improve this system and ensure it serves all citizens fairly.</p>
    """, unsafe_allow_html=True)
    
    # Feedback form
    st.markdown("""
    <div class="card">
        <h3>Share Your Experience</h3>
        <p>Tell us how this AI system has affected you or your community</p>
    </div>
    """, unsafe_allow_html=True)
    
    experience = st.text_area("Your Experience", placeholder="Describe how this AI system affected you or your community...", height=150)
    
    impact_type = st.radio(
        "Impact Type",
        ["Positive", "Negative", "Neutral", "Confusing", "Concerning"]
    )
    
    st.markdown("<h3>What aspects of the system are you providing feedback on?</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        transparency = st.checkbox("Transparency")
        fairness = st.checkbox("Fairness")
        accuracy = st.checkbox("Accuracy")
    
    with col2:
        privacy = st.checkbox("Privacy")
        usability = st.checkbox("Usability")
        other = st.checkbox("Other")
    
    if other:
        other_aspect = st.text_input("Please specify:")
    
    anonymous = st.checkbox("Submit anonymously")
    
    if not anonymous:
        st.markdown("<p>Contact Information (optional)</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
        with col2:
            email = st.text_input("Email")
    
    if st.button("Submit Feedback"):
        if experience:
            # In a real implementation, this would save to a database
            new_id = len(st.session_state.feedback_data) + 1
            new_feedback = {
                "id": new_id,
                "system_id": system_id,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "sentiment": impact_type.lower(),
                "feedback_text": experience,
                "resolved": False
            }
            
            # Add to DataFrame (in a real implementation, this would be saved to a database)
            st.session_state.feedback_data = pd.concat([st.session_state.feedback_data, pd.DataFrame([new_feedback])], ignore_index=True)
            
            # Update feedback count for the system
            system_idx = st.session_state.ai_systems[st.session_state.ai_systems['id'] == system_id].index[0]
            st.session_state.ai_systems.at[system_idx, 'feedback_count'] += 1
            
            st.success("Thank you for your feedback! It will help us improve AI systems in Amsterdam.")
        else:
            st.error("Please describe your experience before submitting.")
    
    # Display feedback statistics
    st.markdown("<h2>Feedback Statistics</h2>", unsafe_allow_html=True)
    
    system_feedback = st.session_state.feedback_data[st.session_state.feedback_data['system_id'] == system_id]
    
    if len(system_feedback) == 0:
        st.info("No feedback data available for this system yet.")
    else:
        # Sentiment breakdown
        sentiment_counts = system_feedback['sentiment'].value_counts()
        
        fig = px.pie(
            names=sentiment_counts.index,
            values=sentiment_counts.values,
            title=f"Feedback Sentiment Distribution ({len(system_feedback)} reports)",
            color=sentiment_counts.index,
            color_discrete_map={
                'positive': '#10b981',
                'negative': '#ef4444',
                'neutral': '#9ca3af',
                'confused': '#f59e0b',
                'concerned': '#3b82f6'
            }
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        
        # Resolution rate
        resolved_count = system_feedback['resolved'].sum()
        resolution_rate = resolved_count / len(system_feedback) * 100
        
        st.markdown(f"""
        <p>Resolution Rate: <strong>{resolution_rate:.1f}%</strong> ({resolved_count} out of {len(system_feedback)} reports)</p>
        """, unsafe_allow_html=True)
        
        # Feedback over time
        system_feedback['date'] = pd.to_datetime(system_feedback['date'])
        feedback_by_date = system_feedback.groupby([pd.Grouper(key='date', freq='W')])['id'].count().reset_index()
        feedback_by_date.columns = ['date', 'count']
        
        fig = px.line(
            feedback_by_date,
            x='date',
            y='count',
            title='Feedback Submissions Over Time',
            labels={'date': 'Date', 'count': 'Number of Submissions'},
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)

# About page
def about_page():
    st.markdown('<a href="/" style="display: inline-flex; align-items: center; margin-bottom: 1rem;"><span style="margin-right: 0.25rem;">←</span> Back to Overview</a>', unsafe_allow_html=True)
    
    st.markdown("""
    <h1>About AI & Me</h1>
    <p>A civic platform empowering Amsterdam citizens to understand, question, and influence AI systems in their city.</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Our Mission</h3>
        <p>AI & Me is a public-facing platform that empowers citizens to:</p>
        <ul>
            <li>Understand how AI is used in their city</li>
            <li>Question how it might affect them</li>
            <li>Influence how it evolves through feedback and co-design</li>
        </ul>
        <p>We believe that AI systems should be transparent, accountable, and designed with input from the citizens they affect.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Key Features</h3>
        
        <h4>🔍 Human-Centered Explanation Pages</h4>
        <p>Every algorithm in use is paired with a plain-language, illustrated explanation:</p>
        <ul>
            <li>What is it for?</li>
            <li>How does it affect me?</li>
            <li>What kind of data does it use?</li>
            <li>What rights do I have?</li>
        </ul>
        <p>Available in multiple languages and accessible formats</p>
        
        <h4>🧠 Emotion-Aware Trust Indicators</h4>
        <p>Visual indicators that show:</p>
        <ul>
            <li>Who audits the system</li>
            <li>Whether bias testing was done</li>
            <li>Whether citizens were consulted</li>
            <li>Level of risk to human rights</li>
        </ul>
        <p>Similar to a "nutrition label" for AI</p>
        
        <h4>🗣️ "Tell Us What You Think" Feedback Module</h4>
        <p>Citizens can anonymously:</p>
        <ul>
            <li>Report concerns</li>
            <li>Ask questions</li>
            <li>Share stories of how an algorithm affected them</li>
        </ul>
        <p>Feedback is publicly visible, and responses from the municipality are tracked and transparent</p>
        
        <h4>🧭 "Was This Clear?" Explainability Feedback</h4>
        <p>After reading any explanation, users can rate:</p>
        <ul>
            <li>Clarity (Did it make sense?)</li>
            <li>Care (Did it feel human or robotic?)</li>
            <li>Usefulness (Did it help me understand my rights?)</li>
        </ul>
        <p>This builds a live metric of how explainability is perceived, not just delivered.</p>
        
        <h4>🧩 Civic AI Simulator</h4>
        <p>Users can "test" a sample algorithm by inputting mock data to see:</p>
        <ul>
            <li>How decisions might change based on different inputs</li>
            <li>What the system "considers" in its logic</li>
        </ul>
        <p>Designed to de-mystify black boxes without oversimplifying</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Contact Us</h3>
        <p>If you have questions, suggestions, or would like to get involved, please contact us at:</p>
        <p><strong>Email:</strong> info@aiandme.amsterdam</p>
        <p><strong>Address:</strong> Amsterdam City Hall, Amstel 1, 1011 PN Amsterdam</p>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# 4. MAIN APP
# ===============================

def main():
    # Load CSS
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    
    if st.sidebar.button("Home"):
        st.experimental_set_query_params(page="home")
    
    if st.sidebar.button("AI Systems"):
        st.experimental_set_query_params(page="home")
    
    if st.sidebar.button("Housing Simulator"):
        st.experimental_set_query_params(page="simulator")
    
    if st.sidebar.button("Co-Design Sessions"):
        st.experimental_set_query_params(page="all_sessions")
    
    if st.sidebar.button("Public Questions"):
        st.experimental_set_query_params(page="all_questions")
    
    if st.sidebar.button("About"):
        st.experimental_set_query_params(page="about")
    
    # Get query parameters
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["home"])[0]
    system_id = query_params.get("id", [None])[0]
    
    # Render the appropriate page
    if page == "home":
        home_page()
    elif page == "system_details" and system_id:
        system_details_page(int(system_id))
    elif page == "system_feedback" and system_id:
        system_feedback_page(int(system_id))
    elif page == "simulator":
        housing_simulator_page()
    elif page == "all_questions":
        all_questions_page()
    elif page == "all_sessions":
        all_sessions_page()
    elif page == "about":
        about_page()
    else:
        home_page()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>AI & Me: Citizen Empowerment Platform for AI Governance</p>
        <p>© 2023 Gemeente Amsterdam | <a href="/?page=about">About</a> | <a href="#">Privacy Policy</a> | <a href="#">Accessibility</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
