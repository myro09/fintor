#FinTor - The AI Financial Mentor
#A simple finance tracking and learning app (Streamlit demo version)

import streamlit as st
import pandas as pd
import datetime

# Page config
st.set_page_config(page_title="FinTor - Financial Mentor", layout="centered")
st.title("FinTor 💸 - Your AI Financial Mentor")

# Sidebar - User profile
with st.sidebar:
    st.header("User Profile")
    name = st.text_input("Name", "Miheer")
    age = st.slider("Age", 13, 40, 17)
    income = st.number_input("Monthly Income (₹)", 0, 100000, 10000)
    st.markdown("---")

# Section 1: Track Expenses
st.subheader("1. Track Your Expenses")
if "expense_data" not in st.session_state:
    st.session_state.expense_data = pd.DataFrame(columns=["Date", "Category", "Amount"])

with st.form("expense_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        exp_date = st.date_input("Date", datetime.date.today())
    with col2:
        exp_category = st.selectbox("Category", ["Food", "Travel", "Savings", "Shopping", "Other"])
    with col3:
        exp_amount = st.number_input("Amount (₹)", 0, 100000, step=100)
    submit_expense = st.form_submit_button("Add Expense")

if submit_expense:
    new_data = pd.DataFrame([[exp_date, exp_category, exp_amount]], columns=["Date", "Category", "Amount"])
    st.session_state.expense_data = pd.concat([st.session_state.expense_data, new_data], ignore_index=True)
    st.success("Expense added!")

if not st.session_state.expense_data.empty:
    st.dataframe(st.session_state.expense_data)
    st.subheader("📊 Expense Breakdown")
    st.bar_chart(st.session_state.expense_data.groupby("Category")["Amount"].sum())

# Section 2: Set Savings Goal
st.subheader("2. Savings Goal")
goal_name = st.text_input("Goal (e.g. New Phone)", "Buy a Phone")
goal_amount = st.number_input("Target Amount (₹)", 0, 100000, 10000)
target_date = st.date_input("Target Date", datetime.date(2025, 9, 30))

# Calculate months left and monthly saving needed
months_left = max((target_date - datetime.date.today()).days // 30, 1)
monthly_needed = goal_amount // months_left

st.info(f"To reach your goal '{goal_name}', you should save ₹{monthly_needed}/month for {months_left} months.")

# Section 3: Investment Tips
st.subheader("3. Investment Suggestion")
if age < 18:
    st.write("💡 Learn UPI, Digital Wallets, Piggy Banking")
elif age <= 22:
    st.write("💡 Start SIPs, PPF, Digital Gold, Learn Mutual Funds")
else:
    st.write("💡 Diversify in Index Funds, ELSS, NPS, Insurance")

# Section 4: Financial Quiz
st.subheader("4. Financial Literacy Quiz")
quiz_q = st.radio("If you invest ₹1,000 at 10% interest compounded annually, how much after 2 years?",
                 ["₹1,100", "₹1,200", "₹1,210", "₹1,150"])
if st.button("Check Answer"):
    if quiz_q == "₹1,210":
        st.success("✅ Correct! That's compound interest in action.")
    else:
        st.error("❌ Incorrect. Try again. Compound interest = ₹1,210")

# Section 5: Dashboard Summary
st.subheader("5. Dashboard Summary")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Expenses", f"₹{st.session_state.expense_data['Amount'].sum():,.0f}")
with col2:
    st.metric("Monthly Saving Target", f"₹{monthly_needed:,.0f}")

st.markdown("---")
st.caption("FinTor by Miheer - Made for Innovate to Solve Design Challenge")

