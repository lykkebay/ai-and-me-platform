import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime
import random

# Set page configuration
st.set_page_config(
    page_title="AI & Me | Gemeente Amsterdam",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS to match the design
st.markdown("""
<style>
    /* General styling */
    [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header styling */
    header {
        background-color: white;
        border-bottom: 1px solid #e5e7eb;
    }
    
    /* Hero section */
    .hero {
        background: linear-gradient(to bottom, #dc2626, #b91c1c);
        color: white;
        padding: 4rem 2rem;
        border-radius: 0;
        text-align: center;
        margin: -4rem -4rem 2rem -4rem;
    }
    
    .hero h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .hero p {
        font-size: 1.25rem;
        margin-bottom: 2rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Button styling */
    .primary-button {
        background-color: white;
        color: #b91c1c;
        padding: 0.75rem 1.5rem;
        border-radius: 0.375rem;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin-right: 0.5rem;
        border: none;
    }
    
    .primary-button:hover {
        background-color: #f3f4f6;
    }
    
    .outline-button {
        background-color: transparent;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 0.375rem;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        border: 1px solid white;
    }
    
    .outline-button:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }
    
    .pillar-card {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .pillar-card h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .pillar-card p {
        color: #6b7280;
        margin-bottom: 1rem;
        flex-grow: 1;
    }
    
    .pillar-card-button {
        background-color: transparent;
        color: #111827;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-weight: 500;
        text-decoration: none;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #e5e7eb;
        width: 100%;
        margin-top: auto;
    }
    
    .pillar-card-button:hover {
        background-color: #f9fafb;
    }
    
    /* Concern card */
    .concern-card h3 {
        font-size: 1.125rem;
        font-weight: 600;
        color: #dc2626;
        margin-bottom: 0.5rem;
    }
    
    .concern-card p {
        color: #6b7280;
    }
    
    /* Section styling */
    .section {
        padding: 4rem 0;
    }
    
    .section-title {
        font-size: 1.875rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .bg-muted {
        background-color: #f9fafb;
        margin: 2rem -4rem;
        padding: 4rem;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .badge-secondary {
        background-color: #e5e7eb;
        color: #1f2937;
    }
    
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fecaca;
    }
    
    .badge-yellow {
        background-color: #fef3c7;
        color: #92400e;
        border: 1px solid #fde68a;
    }
    
    .badge-green {
        background-color: #d1fae5;
        color: #047857;
        border: 1px solid #a7f3d0;
    }
    
    /* Algorithm card */
    .algorithm-card {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .algorithm-card-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.75rem;
    }
    
    .algorithm-card h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .algorithm-card p {
        color: #6b7280;
        margin-bottom: 1rem;
        flex-grow: 1;
    }
    
    .algorithm-card-button {
        background-color: transparent;
        color: #111827;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-weight: 500;
        text-decoration: none;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #e5e7eb;
        width: 100%;
        margin-top: auto;
    }
    
    /* Trust indicator */
    .trust-indicator {
        margin-bottom: 1rem;
    }
    
    .trust-indicator-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
    }
    
    .trust-indicator-bar {
        height: 0.5rem;
        background-color: #e5e7eb;
        border-radius: 9999px;
        margin-bottom: 0.5rem;
    }
    
    .trust-indicator-fill {
        height: 100%;
        border-radius: 9999px;
    }
    
    .trust-indicator-description {
        font-size: 0.875rem;
        color: #6b7280;
    }
    
    /* Feedback form */
    .form-group {
        margin-bottom: 1.5rem;
    }
    
    .form-label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    /* Footer */
    .footer {
        border-top: 1px solid #e5e7eb;
        padding: 1.5rem 0;
        margin-top: 2rem;
    }
    
    /* Icons */
    .icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 2.5rem;
        height: 2.5rem;
        border-radius: 0.375rem;
        margin-bottom: 0.5rem;
    }
    
    .icon-red {
        color: #dc2626;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 2.5rem;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 0.375rem;
        border: 1px solid #e5e7eb;
        margin-right: 0.5rem;
    }

    .stTabs [aria-selected="true"] {
        background-color: #f3f4f6;
    }
    
    /* Hide Streamlit branding */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .hero {
            padding: 3rem 1rem;
        }
        
        .hero h1 {
            font-size: 2.25rem;
        }
        
        .section {
            padding: 2rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigation
def create_header():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 0.5rem;">
            <div style="background-color: #dc2626; color: white; padding: 0.25rem 0.5rem; border-radius: 0.375rem; font-weight: 700;">A'dam</div>
            <span style="font-weight: 700; font-size: 1.125rem;">AI & Me</span>
        </div>
        """, unsafe_allow_html=True)

# Create pages
def home_page():
    # Hero Section
    st.markdown("""
    <style>
        .hero h1 {
            color: white;
        }
    </style>

    <div class="hero">
        <h1>AI & Me: Understand, Question, Influence</h1>
        <p>A civic platform empowering Amsterdam citizens to understand how AI is used in their city, question how it might affect them, and influence how it evolves.</p>
        <div>
            <button class="primary-button" onclick="window.location.href='#understand'">Explore AI Systems</button>
            <button class="outline-button" onclick="window.location.href='#about'">Learn More</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Three Pillars Section
    st.markdown('<h2 class="section-title">Your Rights in the AI City</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card pillar-card">
            <div class="icon icon-red">👁️</div>
            <h3>Understand</h3>
            <p>Discover how AI systems are used in Amsterdam with clear, jargon-free explanations.</p>
            <button class="pillar-card-button" onclick="window.location.href='#understand'">
                <span>Explore</span>
                <span>→</span>
            </button>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card pillar-card">
            <div class="icon icon-red">💬</div>
            <h3>Question</h3>
            <p>Ask questions, report concerns, and share your experiences with AI systems.</p>
            <button class="pillar-card-button" onclick="window.location.href='#question'">
                <span>Explore</span>
                <span>→</span>
            </button>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="card pillar-card">
            <div class="icon icon-red">🗳️</div>
            <h3>Influence</h3>
            <p>Provide feedback and participate in the co-design of future AI systems.</p>
            <button class="pillar-card-button" onclick="window.location.href='#influence'">
                <span>Explore</span>
                <span>→</span>
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Concerns Section
    st.markdown("""
    <div class="bg-muted">
        <h2 class="section-title">Addressing Your Concerns</h2>
        <div class="container">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card concern-card">
            <h3>I feel powerless to influence how AI is used.</h3>
            <p>Our feedback modules give you a direct voice in AI governance.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card concern-card">
            <h3>I worry AI reinforces social inequality.</h3>
            <p>View our trust indicators showing bias testing and human rights impact.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card concern-card">
            <h3>I am concerned AI is used without my knowledge.</h3>
            <p>Explore our transparent registry of all AI systems in Amsterdam.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card concern-card">
            <h3>I'm afraid of being watched or profiled.</h3>
            <p>Learn exactly what data is used and how your privacy is protected.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
    <div style="text-align: center; padding: 4rem 0;">
        <h2 style="font-size: 1.875rem; font-weight: 700; margin-bottom: 1.5rem;">Join the Conversation Today</h2>
        <p style="font-size: 1.125rem; margin-bottom: 2rem; max-width: 42rem; margin-left: auto; margin-right: auto;">
            Your voice matters in shaping how AI is used in Amsterdam. Start exploring, asking questions, and sharing your perspective.
        </p>
        <button class="primary-button" style="background-color: #dc2626; color: white;" onclick="window.location.href='#understand'">Get Started</button>
    </div>
    """, unsafe_allow_html=True)

def understand_page():
    st.markdown("""
    <h1 style="font-size: 1.875rem; font-weight: 700; margin-bottom: 0.5rem;">Understand AI in Amsterdam</h1>
    <p style="color: #6b7280; font-size: 1.125rem; margin-bottom: 1.5rem;">
        Explore AI systems used in the city with clear, human-centered explanations.
    </p>
    """, unsafe_allow_html=True)
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text_input("", placeholder="Search AI systems...", label_visibility="collapsed")
    with col2:
        st.button("🔍 Filter")
    
    # Tabs
    tabs = st.tabs(["All Systems", "Neighborhood", "City Services", "Mobility"])
    
    with tabs[0]:
        # All systems tab
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="card algorithm-card">
                <div class="algorithm-card-header">
                    <span class="badge badge-secondary">Public Safety</span>
                    <span class="badge badge-yellow">Medium Risk</span>
                </div>
                <h3>Crowd Monitoring System</h3>
                <p>AI that analyzes crowd density in public spaces to prevent overcrowding.</p>
                <button class="algorithm-card-button">
                    <span>Learn More</span>
                    <span>→</span>
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card algorithm-card">
                <div class="algorithm-card-header">
                    <span class="badge badge-secondary">Tourism</span>
                    <span class="badge badge-yellow">Medium Risk</span>
                </div>
                <h3>Tourist Flow Prediction</h3>
                <p>System that forecasts tourist movements to manage city resources.</p>
                <button class="algorithm-card-button">
                    <span>Learn More</span>
                    <span>→</span>
                </button>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="card algorithm-card">
                <div class="algorithm-card-header">
                    <span class="badge badge-secondary">Mobility</span>
                    <span class="badge badge-green">Low Risk</span>
                </div>
                <h3>Parking Enforcement AI</h3>
                <p>System that identifies parking violations using camera footage.</p>
                <button class="algorithm-card-button">
                    <span>Learn More</span>
                    <span>→</span>
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card algorithm-card">
                <div class="algorithm-card-header">
                    <span class="badge badge-secondary">Social Affairs</span>
                    <span class="badge badge-red">High Risk</span>
                </div>
                <h3>Benefit Fraud Detection</h3>
                <p>AI that identifies potential fraud in social benefit applications.</p>
                <button class="algorithm-card-button">
                    <span>Learn More</span>
                    <span>→</span>
                </button>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="card algorithm-card">
                <div class="algorithm-card-header">
                    <span class="badge badge-secondary">Housing</span>
                    <span class="badge badge-red">High Risk</span>
                </div>
                <h3>Social Housing Allocation</h3>
                <p>Algorithm that helps distribute social housing based on need and waiting time.</p>
                <button class="algorithm-card-button" onclick="window.location.href='#housing-allocation'">
                    <span>Learn More</span>
                    <span>→</span>
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card algorithm-card">
                <div class="algorithm-card-header">
                    <span class="badge badge-secondary">Waste Management</span>
                    <span class="badge badge-green">Low Risk</span>
                </div>
                <h3>Waste Collection Optimization</h3>
                <p>AI that plans efficient routes for waste collection vehicles.</p>
                <button class="algorithm-card-button">
                    <span>Learn More</span>
                    <span>→</span>
                </button>
            </div>
            """, unsafe_allow_html=True)

def housing_allocation_page():
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <span class="badge badge-secondary">Housing</span>
        <span class="badge badge-red">High Risk</span>
    </div>
    <h1 style="font-size: 1.875rem; font-weight: 700; margin-bottom: 0.5rem;">Social Housing Allocation System</h1>
    <p style="color: #6b7280; font-size: 1.125rem; margin-bottom: 1.5rem;">
        An algorithm that helps distribute social housing based on need and waiting time.
    </p>
    """, unsafe_allow_html=True)
    
    # Tabs
    tabs = st.tabs(["Explanation", "Trust Indicators", "Your Rights", "Give Feedback"])
    
    with tabs[0]:
        # Explanation tab
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="card">
                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">What is this system for?</h2>
                <p style="margin-bottom: 1rem;">
                    The Social Housing Allocation System helps the city distribute limited social housing units to
                    those who need them most. Amsterdam faces a housing shortage, and this system aims to make the
                    allocation process fair and transparent.
                </p>

                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem; margin-top: 2rem;">How does it affect me?</h2>
                <p style="margin-bottom: 1rem;">
                    If you apply for social housing in Amsterdam, this system will analyze your application to
                    determine your position on the waiting list. It considers factors like:
                </p>
                <ul style="list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem;">
                    <li>How long you've been waiting</li>
                    <li>Your current housing situation</li>
                    <li>Your household composition (family size, etc.)</li>
                    <li>Your income level</li>
                    <li>Special circumstances (medical needs, etc.)</li>
                </ul>
                <p>
                    The system then assigns a priority score that determines when you might receive a housing offer.
                    Higher scores mean higher priority.
                </p>

                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem; margin-top: 2rem;">What kind of data does it use?</h2>
                <p style="margin-bottom: 1rem;">The system uses data from your housing application, including:</p>
                <ul style="list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem;">
                    <li>Personal information (age, household composition)</li>
                    <li>Financial information (income, assets, debt situation)</li>
                    <li>Current housing details (address, type of housing, rental amount)</li>
                    <li>Special circumstances (health issues, social needs)</li>
                    <li>Registration date and history</li>
                </ul>
                <p style="color: #6b7280; font-size: 0.875rem;">
                    Note: All data is processed in accordance with GDPR and local privacy regulations.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Explainability Rating
            st.markdown("""
            <div class="card" style="margin-top: 1.5rem;">
                <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem;">Was this explanation helpful?</h3>
                <p style="color: #6b7280; font-size: 0.875rem; margin-bottom: 1.5rem;">
                    Your feedback helps us improve how we explain AI systems.
                </p>
                
                <div style="margin-bottom: 1.5rem;">
                    <label style="display: block; margin-bottom: 0.5rem;">Was the explanation clear and easy to understand?</label>
                    <div style="display: flex; gap: 1rem;">
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="clarity-yes" name="clarity">
                            <label for="clarity-yes">Yes</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="clarity-somewhat" name="clarity">
                            <label for="clarity-somewhat">Somewhat</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="clarity-no" name="clarity">
                            <label for="clarity-no">No</label>
                        </div>
                    </div>
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <label style="display: block; margin-bottom: 0.5rem;">Did the explanation feel human and considerate?</label>
                    <div style="display: flex; gap: 1rem;">
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="care-yes" name="care">
                            <label for="care-yes">Yes</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="care-somewhat" name="care">
                            <label for="care-somewhat">Somewhat</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="care-no" name="care">
                            <label for="care-no">No</label>
                        </div>
                    </div>
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <label style="display: block; margin-bottom: 0.5rem;">Did you learn about your rights related to this system?</label>
                    <div style="display: flex; gap: 1rem;">
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="usefulness-yes" name="usefulness">
                            <label for="usefulness-yes">Yes</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="usefulness-somewhat" name="usefulness">
                            <label for="usefulness-somewhat">Somewhat</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <input type="radio" id="usefulness-no" name="usefulness">
                            <label for="usefulness-no">No</label>
                        </div>
                    </div>
                </div>
                
                <button style="background-color: #dc2626; color: white; padding: 0.5rem 1rem; border-radius: 0.375rem; font-weight: 500; border: none; width: 100%;">
                    Submit Ratings
                </button>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="card">
                <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem;">Quick Summary</h3>
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                        <div style="color: #dc2626; margin-top: 0.125rem;">👥</div>
                        <div>
                            <p style="font-weight: 500;">Who uses it</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">Housing Department, Social Affairs</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                        <div style="color: #dc2626; margin-top: 0.125rem;">💾</div>
                        <div>
                            <p style="font-weight: 500;">Data retention</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">7 years after application</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 0.75rem;">
                        <div style="color: #dc2626; margin-top: 0.125rem;">🛡️</div>
                        <div>
                            <p style="font-weight: 500;">Human oversight</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">Final decisions reviewed by housing officers</p>
                        </div>
                    </div>
                </div>
                
                <div style="border-top: 1px solid #e5e7eb; margin: 1.5rem 0;"></div>
                
                <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem;">Related Systems</h3>
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin-bottom: 0.5rem;">
                        <a href="#" style="color: #dc2626; text-decoration: none; display: flex; align-items: center;">
                            Housing Fraud Detection
                        </a>
                    </li>
                    <li>
                        <a href="#" style="color: #dc2626; text-decoration: none; display: flex; align-items: center;">
                            Neighborhood Development Planning
                        </a>
                    </li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        # Trust Indicators tab
        st.markdown("""
        <div class="card">
            <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Trust Indicators</h2>
            <p style="margin-bottom: 1.5rem;">
                These indicators show how this AI system was developed, tested, and monitored to ensure it's
                trustworthy and fair.
            </p>

            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;">
                <div class="trust-indicator">
                    <div class="trust-indicator-header">
                        <span style="font-weight: 500;">Bias Testing</span>
                        <span style="font-size: 0.875rem; font-weight: 500;">3/5</span>
                    </div>
                    <div class="trust-indicator-bar">
                        <div class="trust-indicator-fill" style="width: 60%; background-color: #f59e0b;"></div>
                    </div>
                    <p class="trust-indicator-description">Regular testing for bias against protected groups</p>
                </div>
                
                <div class="trust-indicator">
                    <div class="trust-indicator-header">
                        <span style="font-weight: 500;">Citizen Consultation</span>
                        <span style="font-size: 0.875rem; font-weight: 500;">2/5</span>
                    </div>
                    <div class="trust-indicator-bar">
                        <div class="trust-indicator-fill" style="width: 40%; background-color: #f97316;"></div>
                    </div>
                    <p class="trust-indicator-description">Limited consultation with housing applicants</p>
                </div>
                
                <div class="trust-indicator">
                    <div class="trust-indicator-header">
                        <span style="font-weight: 500;">Human Oversight</span>
                        <span style="font-size: 0.875rem; font-weight: 500;">4/5</span>
                    </div>
                    <div class="trust-indicator-bar">
                        <div class="trust-indicator-fill" style="width: 80%; background-color: #22c55e;"></div>
                    </div>
                    <p class="trust-indicator-description">Housing officers review all decisions</p>
                </div>
                
                <div class="trust-indicator">
                    <div class="trust-indicator-header">
                        <span style="font-weight: 500;">Transparency</span>
                        <span style="font-size: 0.875rem; font-weight: 500;">3/5</span>
                    </div>
                    <div class="trust-indicator-bar">
                        <div class="trust-indicator-fill" style="width: 60%; background-color: #f59e0b;"></div>
                    </div>
                    <p class="trust-indicator-description">Algorithm details published but complex</p>
                </div>
                
                <div class="trust-indicator">
                    <div class="trust-indicator-header">
                        <span style="font-weight: 500;">Impact Assessment</span>
                        <span style="font-size: 0.875rem; font-weight: 500;">4/5</span>
                    </div>
                    <div class="trust-indicator-bar">
                        <div class="trust-indicator-fill" style="width: 80%; background-color: #22c55e;"></div>
                    </div>
                    <p class="trust-indicator-description">Regular assessment of social impact</p>
                </div>
                
                <div class="trust-indicator">
                    <div class="trust-indicator-header">
                        <span style="font-weight: 500;">Data Protection</span>
                        <span style="font-size: 0.875rem; font-weight: 500;">5/5</span>
                    </div>
                    <div class="trust-indicator-bar">
                        <div class="trust-indicator-fill" style="width: 100%; background-color: #22c55e;"></div>
                    </div>
                    <p class="trust-indicator-description">Strong data protection measures in place</p>
                </div>
            </div>

            <div style="margin-top: 2rem;">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Independent Audits</h3>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div>
                                <p style="font-weight: 500;">University of Amsterdam - AI Ethics Lab</p>
                                <p style="font-size: 0.875rem; color: #6b7280;">Last audit: March 2023</p>
                            </div>
                            <span class="badge badge-secondary">External</span>
                        </div>
                        <p style="margin-top: 0.5rem; font-size: 0.875rem;">
                            Found potential bias against single-parent households. Recommended adjustments were implemented
                            in May 2023.
                        </p>
                    </div>
                    
                    <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div>
                                <p style="font-weight: 500;">Amsterdam Digital Rights Coalition</p>
                                <p style="font-size: 0.875rem; color: #6b7280;">Last review: November 2022</p>
                            </div>
                            <span class="badge badge-secondary">Civil Society</span>
                        </div>
                        <p style="margin-top: 0.5rem; font-size: 0.875rem;">
                            Raised concerns about transparency and accessibility of the appeals process. Improvements in
                            progress.
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with tabs[2]:
        # Your Rights tab
        st.markdown("""
        <div class="card">
            <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Your Rights</h2>
            <p style="margin-bottom: 1.5rem;">
                As a citizen affected by this AI system, you have specific rights under GDPR and local regulations:
            </p>

            <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">Right to Explanation</h3>
                    <p>
                        You can request a specific explanation of how a decision about your housing application was made.
                        The Housing Department must provide this in clear, non-technical language.
                    </p>
                    <button style="margin-top: 1rem; background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem; font-weight: 500;">
                        Request an Explanation
                    </button>
                </div>

                <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">Right to Object</h3>
                    <p>
                        If you believe the system has made an unfair decision, you can object and request human review. A
                        housing officer will manually review your case.
                    </p>
                    <button style="margin-top: 1rem; background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem; font-weight: 500;">
                        File an Objection
                    </button>
                </div>

                <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">Right to Access Your Data</h3>
                    <p>
                        You can request all personal data used by the system in your case. This includes all factors
                        considered in your priority score calculation.
                    </p>
                    <button style="margin-top: 1rem; background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem; font-weight: 500;">
                        Request Your Data
                    </button>
                </div>

                <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">Right to Correction</h3>
                    <p>
                        If you find incorrect information in your data, you have the right to have it corrected. This may
                        affect your priority score.
                    </p>
                    <button style="margin-top: 1rem; background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem; font-weight: 500;">
                        Request a Correction
                    </button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with tabs[3]:
        # Give Feedback tab
        st.markdown("""
        <div class="card">
            <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Share Your Feedback</h2>
            <p style="color: #6b7280; margin-bottom: 1.5rem;">Tell us what you think about the Social Housing Allocation System</p>
            
            <div style="margin-bottom: 1.5rem;">
                <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.75rem;">Type of Feedback</h3>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <input type="radio" id="concern" name="feedback-type" checked>
                        <label for="concern" style="display: flex; align-items: center; cursor: pointer;">
                            <span style="color: #ef4444; margin-right: 0.5rem;">⚠️</span>
                            Report a concern
                        </label>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <input type="radio" id="question" name="feedback-type">
                        <label for="question" style="display: flex; align-items: center; cursor: pointer;">
                            <span style="color: #3b82f6; margin-right: 0.5rem;">💬</span>
                            Ask a question
                        </label>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <input type="radio" id="suggestion" name="feedback-type">
                        <label for="suggestion" style="display: flex; align-items: center; cursor: pointer;">
                            <span style="color: #22c55e; margin-right: 0.5rem;">👍</span>
                            Make a suggestion
                        </label>
                    </div>
                </div>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label for="concern-type" style="display: block; margin-bottom: 0.5rem;">What are you concerned about?</label>
                <select id="concern-type" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem; background-color: white;">
                    <option value="">Select a concern...</option>
                    <option value="fairness">Fairness or discrimination</option>
                    <option value="privacy">Privacy or data protection</option>
                    <option value="transparency">Lack of transparency or explanation</option>
                    <option value="accuracy">Accuracy of decisions</option>
                    <option value="other">Other concern</option>
                </select>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label for="feedback-details" style="display: block; margin-bottom: 0.5rem;">Describe your concern</label>
                <textarea id="feedback-details" placeholder="Please provide details..." style="width: 100%; min-height: 150px; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;"></textarea>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label for="impact" style="display: block; margin-bottom: 0.5rem;">How has this affected you personally? (optional)</label>
                <textarea id="impact" placeholder="Share your experience..." style="width: 100%; min-height: 100px; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;"></textarea>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 1rem;">Contact Information (optional)</h3>
                <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 1rem;">
                    If you'd like us to follow up with you about your feedback, please provide your contact information.
                </p>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                    <div>
                        <label for="name" style="display: block; margin-bottom: 0.5rem;">Name</label>
                        <input id="name" placeholder="Your name" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;">
                    </div>
                    <div>
                        <label for="email" style="display: block; margin-bottom: 0.5rem;">Email</label>
                        <input id="email" type="email" placeholder="Your email" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;">
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <input type="checkbox" id="public">
                    <label for="public" style="font-size: 0.875rem;">
                        I'm comfortable with my feedback (without personal details) being shared publicly
                    </label>
                </div>
            </div>
            
            <button style="width: 100%; background-color: #dc2626; color: white; padding: 0.75rem; border: none; border-radius: 0.375rem; font-weight: 500;">
                Submit Feedback
            </button>
        </div>
        """, unsafe_allow_html=True)

def question_page():
    st.markdown("""
    <h1 style="font-size: 1.875rem; font-weight: 700; margin-bottom: 0.5rem;">Question AI in Amsterdam</h1>
    <p style="color: #6b7280; font-size: 1.125rem; margin-bottom: 1.5rem;">
        Ask questions, report concerns, and share your experiences with AI systems in the city.
    </p>
    """, unsafe_allow_html=True)
    
    # Tabs
    tabs = st.tabs(["Public Feedback", "Submit Feedback", "FAQ"])
    
    with tabs[0]:
        # Public Feedback tab
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text_input("", placeholder="Search feedback...", label_visibility="collapsed")
        with col2:
            st.button("🔍 Filter")
            
        # Feedback cards
        st.markdown("""
        <div class="card">
            <div style="margin-bottom: 0.75rem;">
                <span class="badge badge-red">Concern</span>
                <span class="badge badge-secondary">Social Housing Allocation</span>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Housing allocation seems biased against single parents</h3>
            <p style="color: #6b7280; margin-bottom: 1rem;">
                I've been waiting for social housing for 3 years as a single parent, but I know couples who got housing faster. The algorithm seems to prioritize two-parent households.
            </p>
            <p style="font-size: 0.75rem; color: #6b7280; margin-bottom: 1.5rem;">Posted 2 days ago</p>
            
            <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid #e5e7eb;">
                <h4 style="font-weight: 500; margin-bottom: 1rem;">Responses</h4>
                <div style="padding-left: 1rem; border-left: 2px solid #e5e7eb;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.25rem;">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-weight: 500;">Housing Department</span>
                            <span class="badge" style="font-size: 0.75rem; padding: 0.125rem 0.375rem;">Official</span>
                        </div>
                        <span style="font-size: 0.75rem; color: #6b7280;">1 day ago</span>
                    </div>
                    <p style="font-size: 0.875rem;">
                        Thank you for your feedback. We're investigating this concern and will update our bias testing procedures. We've scheduled an audit specifically looking at outcomes for single-parent households.
                    </p>
                </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.5rem;">
                <button style="color: #6b7280; background: none; border: none; display: flex; align-items: center; gap: 0.25rem; font-size: 0.875rem;">
                    <span>❤️</span>
                    <span>Helpful</span>
                </button>
                <button style="background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem; display: flex; align-items: center; gap: 0.25rem;">
                    <span>💬</span>
                    <span>Respond</span>
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="margin-top: 1.5rem;">
            <div style="margin-bottom: 0.75rem;">
                <span class="badge badge-blue">Question</span>
                <span class="badge badge-secondary">Parking Enforcement AI</span>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">How does the parking enforcement system handle privacy?</h3>
            <p style="color: #6b7280; margin-bottom: 1rem;">
                I'm curious about how the parking enforcement cameras handle privacy. Do they record and store footage of people walking by? How long is data kept?
            </p>
            <p style="font-size: 0.75rem; color: #6b7280; margin-bottom: 1.5rem;">Posted 1 week ago</p>
            
            <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid #e5e7eb;">
                <h4 style="font-weight: 500; margin-bottom: 1rem;">Responses</h4>
                <div style="padding-left: 1rem; border-left: 2px solid #e5e7eb; margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.25rem;">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-weight: 500;">Mobility Department</span>
                            <span class="badge" style="font-size: 0.75rem; padding: 0.125rem 0.375rem;">Official</span>
                        </div>
                        <span style="font-size: 0.75rem; color: #6b7280;">6 days ago</span>
                    </div>
                    <p style="font-size: 0.875rem;">
                        The parking enforcement cameras only capture license plates, not pedestrians. Images are automatically processed to detect violations, and all data is deleted after 72 hours unless a violation is detected.
                    </p>
                </div>
                
                <div style="padding-left: 1rem; border-left: 2px solid #e5e7eb;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.25rem;">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-weight: 500;">Amsterdam Privacy Coalition</span>
                        </div>
                        <span style="font-size: 0.75rem; color: #6b7280;">5 days ago</span>
                    </div>
                    <p style="font-size: 0.875rem;">
                        We've reviewed this system and can confirm the data retention policies are being followed. However, we're advocating for clearer signage in areas where these cameras operate.
                    </p>
                </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.5rem;">
                <button style="color: #6b7280; background: none; border: none; display: flex; align-items: center; gap: 0.25rem; font-size: 0.875rem;">
                    <span>❤️</span>
                    <span>Helpful</span>
                </button>
                <button style="background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem; display: flex; align-items: center; gap: 0.25rem;">
                    <span>💬</span>
                    <span>Respond</span>
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        # Submit Feedback tab
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="card">
                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Share Your Feedback</h2>
                <p style="color: #6b7280; margin-bottom: 1.5rem;">Tell us what you think about any AI system in Amsterdam</p>
                
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.75rem;">Type of Feedback</h3>
                    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <input type="radio" id="concern" name="feedback-type" checked>
                            <label for="concern" style="display: flex; align-items: center; cursor: pointer;">
                                <span style="color: #ef4444; margin-right: 0.5rem;">⚠️</span>
                                Report a concern
                            </label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <input type="radio" id="question" name="feedback-type">
                            <label for="question" style="display: flex; align-items: center; cursor: pointer;">
                                <span style="color: #3b82f6; margin-right: 0.5rem;">💬</span>
                                Ask a question
                            </label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <input type="radio" id="suggestion" name="feedback-type">
                            <label for="suggestion" style="display: flex; align-items: center; cursor: pointer;">
                                <span style="color: #22c55e; margin-right: 0.5rem;">👍</span>
                                Make a suggestion
                            </label>
                        </div>
                    </div>
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <label for="system" style="display: block; margin-bottom: 0.5rem;">Which AI system?</label>
                    <select id="system" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem; background-color: white;">
                        <option value="">Select a system...</option>
                        <option value="housing">Social Housing Allocation</option>
                        <option value="parking">Parking Enforcement AI</option>
                        <option value="crowd">Crowd Monitoring System</option>
                        <option value="waste">Waste Collection Optimization</option>
                        <option value="other">Other system</option>
                    </select>
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <label for="feedback-title" style="display: block; margin-bottom: 0.5rem;">Title</label>
                    <input id="feedback-title" placeholder="Brief summary of your feedback" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;">
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <label for="feedback-details" style="display: block; margin-bottom: 0.5rem;">Details</label>
                    <textarea id="feedback-details" placeholder="Please provide details..." style="width: 100%; min-height: 150px; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;"></textarea>
                </div>
                
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 1rem;">Contact Information (optional)</h3>
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                        <div>
                            <label for="name" style="display: block; margin-bottom: 0.5rem;">Name</label>
                            <input id="name" placeholder="Your name" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;">
                        </div>
                        <div>
                            <label for="email" style="display: block; margin-bottom: 0.5rem;">Email</label>
                            <input id="email" type="email" placeholder="Your email" style="width: 100%; padding: 0.5rem; border: 1px solid #e5e7eb; border-radius: 0.375rem;">
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <input type="checkbox" id="public">
                        <label for="public" style="font-size: 0.875rem;">
                            I'm comfortable with my feedback (without personal details) being shared publicly
                        </label>
                    </div>
                </div>
                
                <button style="width: 100%; background-color: #dc2626; color: white; padding: 0.75rem; border: none; border-radius: 0.375rem; font-weight: 500;">
                    Submit Feedback
                </button>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="card">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">About Your Feedback</h3>
                <p style="margin-bottom: 1rem;">
                    Your feedback is valuable in making AI systems in Amsterdam more transparent, fair, and accountable.
                </p>
                <div style="margin-bottom: 0.5rem;">
                    <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <span style="color: #ef4444; margin-top: 0.125rem;">⚠️</span>
                        <div>
                            <p style="font-weight: 500;">Report concerns</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">
                                If you believe an AI system is causing harm or discrimination
                            </p>
                        </div>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <span style="color: #3b82f6; margin-top: 0.125rem;">💬</span>
                        <div>
                            <p style="font-weight: 500;">Ask questions</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">
                                If you want to understand how a system works or affects you
                            </p>
                        </div>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <span style="color: #22c55e; margin-top: 0.125rem;">👍</span>
                        <div>
                            <p style="font-weight: 500;">Make suggestions</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">
                                If you have ideas for improving AI systems in the city
                            </p>
                        </div>
                    </div>
                </div>
                <div style="padding-top: 1rem; border-top: 1px solid #e5e7eb;">
                    <p style="font-size: 0.875rem; font-weight: 500;">What happens next?</p>
                    <ul style="font-size: 0.875rem; color: #6b7280; list-style-type: disc; padding-left: 1.25rem; margin-top: 0.5rem;">
                        <li>Your feedback is reviewed by the responsible department</li>
                        <li>You'll receive a response within 10 working days</li>
                        <li>With your permission, feedback may be published anonymously</li>
                        <li>Feedback is used to improve AI systems and policies</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[2]:
        # FAQ tab
        st.markdown("""
        <div class="card">
            <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Frequently Asked Questions</h2>
            <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                <div>
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">How is my feedback used?</h3>
                    <p style="color: #6b7280;">
                        Your feedback is reviewed by the department responsible for the AI system. It helps identify
                        issues, improve explanations, and shape future development. Feedback may lead to system audits,
                        policy changes, or improvements to user interfaces.
                    </p>
                </div>
                <div>
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">Is my feedback anonymous?</h3>
                    <p style="color: #6b7280;">
                        By default, your personal information is kept private. Only if you explicitly consent will your
                        feedback (without personal details) be shared publicly. You can always submit feedback completely
                        anonymously.
                    </p>
                </div>
                <div>
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">How quickly will I get a response?</h3>
                    <p style="color: #6b7280;">
                        We aim to respond to all feedback within 10 working days. Complex issues may take longer to
                        investigate, but you'll receive regular updates on progress.
                    </p>
                </div>
                <div>
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">What if I'm not satisfied with the response?</h3>
                    <p style="color: #6b7280;">
                        If you're not satisfied with the response to your feedback, you can escalate your concern to the
                        Digital Rights Office. They provide independent oversight of AI systems in Amsterdam.
                    </p>
                </div>
                <div>
                    <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">Can I report technical issues with this platform?</h3>
                    <p style="color: #6b7280;">
                        Yes, if you encounter any technical issues with the AI & Me platform itself, please use the
                        "Report a Technical Issue" option in the feedback form or email support@aiandme.amsterdam.nl.
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def influence_page():
    st.markdown("""
    <h1 style="font-size: 1.875rem; font-weight: 700; margin-bottom: 0.5rem;">Influence AI in Amsterdam</h1>
    <p style="color: #6b7280; font-size: 1.125rem; margin-bottom: 1.5rem;">
        Participate in the co-design of AI systems and help shape the future of technology in your city.
    </p>
    """, unsafe_allow_html=True)
    
    # Tabs
    tabs = st.tabs(["Participate", "Your Impact", "Policy Input"])
    
    with tabs[0]:
        # Participate tab
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Upcoming Opportunities</h2>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card">
                <div style="margin-bottom: 0.75rem;">
                    <span class="badge badge-secondary">Co-Design Workshop</span>
                    <span class="badge badge-red">Only 12 spots left</span>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Traffic Management AI</h3>
                <p style="color: #6b7280; margin-bottom: 1rem;">
                    Help design a new AI system that will manage traffic flow in the city center. We want to hear from residents, commuters, and business owners.
                </p>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">📅</span>
                        <span style="font-size: 0.875rem;">June 15, 2023</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">🕔</span>
                        <span style="font-size: 0.875rem;">18:00 - 20:00</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">📍</span>
                        <span style="font-size: 0.875rem;">Public Library Amsterdam</span>
                    </div>
                </div>
                <button style="width: 100%; background-color: #dc2626; color: white; padding: 0.75rem; border: none; border-radius: 0.375rem; font-weight: 500;">
                    Register
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card" style="margin-top: 1.5rem;">
                <div style="margin-bottom: 0.75rem;">
                    <span class="badge badge-secondary">Citizen Panel</span>
                    <span class="badge badge-red">Only 8 spots left</span>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">AI Ethics Guidelines Review</h3>
                <p style="color: #6b7280; margin-bottom: 1rem;">
                    Join a diverse panel of citizens to review and provide feedback on Amsterdam's AI ethics guidelines. No technical knowledge required.
                </p>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">📅</span>
                        <span style="font-size: 0.875rem;">June 22, 2023</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">🕔</span>
                        <span style="font-size: 0.875rem;">13:00 - 16:00</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">📍</span>
                        <span style="font-size: 0.875rem;">Pakhuis de Zwijger</span>
                    </div>
                </div>
                <button style="width: 100%; background-color: #dc2626; color: white; padding: 0.75rem; border: none; border-radius: 0.375rem; font-weight: 500;">
                    Register
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card" style="margin-top: 1.5rem;">
                <div style="margin-bottom: 0.75rem;">
                    <span class="badge badge-secondary">Online Survey</span>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Neighborhood Safety Cameras</h3>
                <p style="color: #6b7280; margin-bottom: 1rem;">
                    Share your opinions on the proposed AI-powered safety camera system for residential neighborhoods. Survey takes approximately 15 minutes.
                </p>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">📅</span>
                        <span style="font-size: 0.875rem;">Open until July 5, 2023</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">🕔</span>
                        <span style="font-size: 0.875rem;">Complete anytime</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #6b7280;">📍</span>
                        <span style="font-size: 0.875rem;">Online</span>
                    </div>
                </div>
                <button style="width: 100%; background-color: #dc2626; color: white; padding: 0.75rem; border: none; border-radius: 0.375rem; font-weight: 500;">
                    Take Survey
                </button>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="card">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Why Participate?</h3>
                <p style="margin-bottom: 1rem;">
                    Your participation helps ensure AI systems in Amsterdam reflect the needs and values of all citizens.
                </p>
                <div style="margin-bottom: 0.75rem;">
                    <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.75rem;">
                        <span style="color: #dc2626; margin-top: 0.125rem;">👥</span>
                        <div>
                            <p style="font-weight: 500;">Diverse perspectives</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">
                                We need input from people of all backgrounds and experiences
                            </p>
                        </div>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.75rem;">
                        <span style="color: #dc2626; margin-top: 0.125rem;">🗳️</span>
                        <div>
                            <p style="font-weight: 500;">Real influence</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">
                                Your input directly shapes how systems are designed and implemented
                            </p>
                        </div>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                        <span style="color: #dc2626; margin-top: 0.125rem;">📅</span>
                        <div>
                            <p style="font-weight: 500;">Early involvement</p>
                            <p style="font-size: 0.875rem; color: #6b7280;">
                                Participate before systems are finalized, when changes are easier to make
                            </p>
                        </div>
                    </div>
                </div>
                <div style="padding-top: 1rem; border-top: 1px solid #e5e7eb;">
                    <p style="font-size: 0.875rem; font-weight: 500;">Compensation for your time</p>
                    <p style="font-size: 0.875rem; color: #6b7280; margin-top: 0.25rem;">
                        Participants in workshops, panels, and testing sessions receive a €50 voucher for local businesses or VVV bonnen.
                    </p>
                </div>
            </div>
            
            <div class="card" style="margin-top: 1.5rem;">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Stay Informed</h3>
                <p style="margin-bottom: 1rem;">
                    Sign up to receive notifications about new participation opportunities that match your interests.
                </p>
                <button style="width: 100%; background-color: #dc2626; color: white; padding: 0.75rem; border: none; border-radius: 0.375rem; font-weight: 500;">
                    Subscribe
                </button>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        # Your Impact tab
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Citizen Impact Stories</h2>
                <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                    <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                        <div style="display: flex; align-items: flex-start; gap: 1rem;">
                            <div style="width: 3rem; height: 3rem; border-radius: 9999px; background-color: #e5e7eb; flex-shrink: 0;"></div>
                            <div>
                                <h3 style="font-weight: 500;">Accessibility Improvements</h3>
                                <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Fatima K., De Pijp resident</p>
                                <p style="font-size: 0.875rem;">
                                    "I participated in testing the waste collection app and pointed out it wasn't accessible for
                                    screen readers. The team redesigned the interface, and now it works for everyone. It shows
                                    they really listened to feedback."
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                        <div style="display: flex; align-items: flex-start; gap: 1rem;">
                            <div style="width: 3rem; height: 3rem; border-radius: 9999px; background-color: #e5e7eb; flex-shrink: 0;"></div>
                            <div>
                                <h3 style="font-weight: 500;">Privacy Protections Added</h3>
                                <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Jan V., Oost resident</p>
                                <p style="font-size: 0.875rem;">
                                    "During a citizen panel on crowd monitoring, I raised concerns about facial recognition. The
                                    final system now uses anonymous counting instead, which still achieves the goal without
                                    compromising privacy."
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div style="padding: 1rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                        <div style="display: flex; align-items: flex-start; gap: 1rem;">
                            <div style="width: 3rem; height: 3rem; border-radius: 9999px; background-color: #e5e7eb; flex-shrink: 0;"></div>
                            <div>
                                <h3 style="font-weight: 500;">Multilingual Support Added</h3>
                                <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Sophia L., Nieuw-West resident</p>
                                <p style="font-size: 0.875rem;">
                                    "I suggested that the city services chatbot needed to support more languages. Now it works
                                    in Dutch, English, Arabic, and Turkish, making it accessible to more residents."
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="card">
                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Changes Made Based on Citizen Input</h2>
                <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                    <div>
                        <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">Parking Enforcement AI</h3>
                        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                                <span class="badge badge-secondary" style="margin-top: 0.125rem;">Before</span>
                                <p style="font-size: 0.875rem;">System stored all vehicle images for 30 days</p>
                            </div>
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                                <span class="badge badge-green" style="margin-top: 0.125rem;">After</span>
                                <p style="font-size: 0.875rem;">
                                    Images deleted immediately after processing unless violation detected
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div>
                        <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">Social Housing Allocation</h3>
                        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                                <span class="badge badge-secondary" style="margin-top: 0.125rem;">Before</span>
                                <p style="font-size: 0.875rem;">Complex algorithm with limited explanation</p>
                            </div>
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                                <span class="badge badge-green" style="margin-top: 0.125rem;">After</span>
                                <p style="font-size: 0.875rem;">Simplified scoring system with detailed personalized explanations</p>
                            </div>
                        </div>
                    </div>
                    
                    <div>
                        <h3 style="font-size: 1.125rem; font-weight: 500; margin-bottom: 0.5rem;">Crowd Monitoring</h3>
                        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                                <span class="badge badge-secondary" style="margin-top: 0.125rem;">Before</span>
                                <p style="font-size: 0.875rem;">No public information about system locations</p>
                            </div>
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
                                <span class="badge badge-green" style="margin-top: 0.125rem;">After</span>
                                <p style="font-size: 0.875rem;">
                                    Interactive map showing all monitoring locations and public dashboard
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div style="padding-top: 1rem; border-top: 1px solid #e5e7eb;">
                        <h3 style="font-weight: 500; margin-bottom: 0.5rem;">Impact by Numbers</h3>
                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
                            <div style="padding: 0.75rem; background-color: #f3f4f6; border-radius: 0.5rem; text-align: center;">
                                <p style="font-size: 1.5rem; font-weight: 700; color: #dc2626;">1,240</p>
                                <p style="font-size: 0.75rem; color: #6b7280;">Citizens participated in 2022</p>
                            </div>
                            <div style="padding: 0.75rem; background-color: #f3f4f6; border-radius: 0.5rem; text-align: center;">
                                <p style="font-size: 1.5rem; font-weight: 700; color: #dc2626;">76%</p>
                                <p style="font-size: 0.75rem; color: #6b7280;">Of feedback led to changes</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[2]:
        # Policy Input tab
        st.markdown("""
        <div class="card">
            <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;">Help Shape AI Policy in Amsterdam</h2>
            <p style="margin-bottom: 1.5rem;">
                Amsterdam is developing policies to govern the use of AI in the city. Your input helps ensure these
                policies reflect citizen values and concerns.
            </p>

            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; margin-bottom: 2rem;">
                <div style="padding: 1.5rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Current Consultations</h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.25rem;">
                                <h4 style="font-weight: 500;">Draft AI Ethics Framework</h4>
                                <span class="badge badge-secondary">Open</span>
                            </div>
                            <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Closes July 15, 2023</p>
                            <p style="font-size: 0.875rem; margin-bottom: 0.75rem;">
                                Review and comment on the proposed ethical guidelines for all AI systems used by the city.
                            </p>
                            <button style="background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem;">
                                Participate
                            </button>
                        </div>

                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.25rem;">
                                <h4 style="font-weight: 500;">AI Transparency Requirements</h4>
                                <span class="badge badge-secondary">Open</span>
                            </div>
                            <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Closes August 3, 2023</p>
                            <p style="font-size: 0.875rem; margin-bottom: 0.75rem;">
                                Help define what information about AI systems should be publicly available.
                            </p>
                            <button style="background-color: transparent; border: 1px solid #e5e7eb; color: #111827; padding: 0.375rem 0.75rem; border-radius: 0.375rem; font-size: 0.875rem;">
                                Participate
                            </button>
                        </div>
                    </div>
                </div>

                <div style="padding: 1.5rem; border: 1px solid #e5e7eb; border-radius: 0.5rem;">
                    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Policy Impact</h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <h4 style="font-weight: 500; margin-bottom: 0.25rem;">AI Procurement Guidelines</h4>
                            <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Consultation closed: March 2023</p>
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.25rem;">
                                <span class="badge badge-green" style="margin-top: 0.125rem;">Implemented</span>
                                <p style="font-size: 0.875rem;">
                                    Citizen input led to stronger requirements for explainability and bias testing.
                                </p>
                            </div>
                            <a href="#" style="font-size: 0.875rem; color: #dc2626; text-decoration: none;">View Results</a>
                        </div>

                        <div>
                            <h4 style="font-weight: 500; margin-bottom: 0.25rem;">Facial Recognition Limitations</h4>
                            <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem;">Consultation closed: November 2022</p>
                            <div style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.25rem;">
                                <span class="badge badge-yellow" style="margin-top: 0.125rem;">In Progress</span>
                                <p style="font-size: 0.875rem;">
                                    Policy being finalized based on strong citizen concerns about privacy.
                                </p>
                            </div>
                            <a href="#" style="font-size: 0.875rem; color: #dc2626; text-decoration: none;">View Results</a>
                        </div>
                    </div>
                </div>
            </div>

            <div style="background-color: #f3f4f6; padding: 1.5rem; border-radius: 0.5rem;">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Join the Citizen AI Advisory Board</h3>
                <p style="margin-bottom: 1rem;">
                    We're recruiting citizens to serve on Amsterdam's AI Advisory Board. Members meet quarterly to
                    review AI initiatives and provide ongoing input on policy and implementation.
                </p>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
                    <span style="color: #6b7280;">🕔</span>
                    <span style="font-size: 0.875rem; color: #6b7280;">Applications close June 30, 2023</span>
                </div>
                <button style="background-color: #dc2626; color: white; padding: 0.75rem 1rem; border: none; border-radius: 0.375rem; font-weight: 500; display: flex; align-items: center; gap: 0.25rem;">
                    <span>Learn More & Apply</span>
                    <span>→</span>
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
    <div class="footer">
        <div style="display: flex; flex-direction: column; gap: 1rem; justify-content: space-between; align-items: center; text-align: center;">
            <div>
                <div style="display: flex; align-items: center; gap: 0.5rem; justify-content: center; margin-bottom: 0.25rem;">
                    <div style="background-color: #dc2626; color: white; padding: 0.25rem 0.5rem; border-radius: 0.375rem; font-weight: 700; font-size: 0.75rem;">A'dam</div>
                    <span style="font-weight: 600; font-size: 0.875rem;">AI & Me</span>
                </div>
                <p style="font-size: 0.75rem; color: #6b7280;">A civic platform for AI transparency and citizen empowerment</p>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; font-size: 0.875rem;">
                <a href="#" style="color: inherit; text-decoration: none; hover: underline;">Privacy Policy</a>
                <a href="#" style="color: inherit; text-decoration: none; hover: underline;">Accessibility</a>
                <a href="#" style="color: inherit; text-decoration: none; hover: underline;">Contact</a>
                <a href="https://www.amsterdam.nl" target="_blank" style="color: inherit; text-decoration: none; hover: underline;">Gemeente Amsterdam</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main app
def main():
    # Create header
    create_header()
    
    # Navigation
    page = st.sidebar.selectbox("Navigation", ["Home", "Understand", "Housing Allocation", "Question", "Influence"])
    
    # Display selected page
    if page == "Home":
        home_page()
    elif page == "Understand":
        understand_page()
    elif page == "Housing Allocation":
        housing_allocation_page()
    elif page == "Question":
        question_page()
    elif page == "Influence":
        influence_page()
    
    # Create footer
    create_footer()

if __name__ == "__main__":
    main()
