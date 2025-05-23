import streamlit as st

# Questions and options
questions = [
    {
        "question": "What is your primary energy source?",
        "options": {
            "Renewable (solar, wind, hydro)": 3,
            "Mixed (some renewable, some fossil fuel)": 2,
            "Mostly fossil fuel": 1
        }
    },
    {
        "question": "Do you measure your greenhouse gas emissions?",
        "options": {
            "Yes, regularly and report them": 3,
            "Occasionally or partially": 2,
            "No, we don’t": 1
        }
    },
    {
        "question": "How do you handle waste?",
        "options": {
            "Recycling, composting, and reduction policies": 3,
            "Basic recycling only": 2,
            "No structured waste management": 1
        }
    },
    {
        "question": "What are your water usage practices?",
        "options": {
            "Efficient systems and reuse methods": 3,
            "Conscious but not optimized": 2,
            "No water-saving initiatives": 1
        }
    },
    {
        "question": "Do you have any green certifications (e.g., ISO 14001)?",
        "options": {
            "Yes": 3,
            "In process or planning to apply": 2,
            "No": 1
        }
    }
]

def calculate_score(responses):
    total_possible = len(responses) * 3
    total_score = sum(responses)
    green_score = (total_score / total_possible) * 100
    return round(green_score, 2)

# Streamlit app layout
st.set_page_config(page_title="Green Score Estimator", layout="centered")

st.title("🌱 Green Score Estimator for SMEs & Agri-Businesses")
st.markdown("Answer the questions below to get your **Green Score** — your readiness for green funding, carbon credits, or ESG programs.")

responses = []

# Display questions
for i, q in enumerate(questions):
    choice = st.radio(f"{i+1}. {q['question']}", list(q["options"].keys()), key=i)
    responses.append(q["options"][choice])

# Calculate and show results
if st.button("Calculate My Green Score"):
    score = calculate_score(responses)
    st.subheader(f"✅ Your Green Score: {score}%")
    if score >= 80:
        st.success("🌿 Excellent! You're ready for green funding.")
    elif score >= 60:
        st.warning("🟡 Fair. Some improvements needed.")
    else:
        st.error("🔴 Poor. Consider adopting greener practices.")
