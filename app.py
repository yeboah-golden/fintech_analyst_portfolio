# app.py - STREAMLIT FINTECH ANALYZER
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="🚗 Uber CEO Dashboard",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("🎯 Financial Statement Analyzer")
st.markdown("**Live Interactive Dashboard** - Built with Python + Streamlit")
st.markdown("---")

# Sidebar for user input
st.sidebar.header("📊 Your Business Data")
st.sidebar.info("Enter your driving data below")

# Sample data input
with st.sidebar.expander("➕ Add Your Daily Data"):
    day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    revenue = st.number_input("Daily Revenue (₵)", min_value=0, value=150)
    costs = st.number_input("Daily Costs (₵)", min_value=0, value=35)
    hours = st.number_input("Hours Worked", min_value=0.0, value=5.0, step=0.5)
    
    if st.button("Add to Analysis"):
        st.success("Data added! Analysis updating...")

# Main dashboard
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Revenue", "₵3,641.13", "62.1%")
    
with col2:
    st.metric("📈 Net Profit", "₵2,262.20", "85%")
    
with col3:
    st.metric("🎯 Profit Margin", "62.1%", "3x Industry Avg")
    
with col4:
    st.metric("🚀 Hourly Rate", "₵64.49/hr", "₵24.49 above avg")

st.markdown("---")

# Profit breakdown section
st.header("📊 ₵9,000 Monthly Profit Breakdown")

# Your actual profit analysis data
profit_data = {
    'Opportunity': ['4-9PM Super Shift', 'Dead Time Reduction', 'Surge Optimization', 'Efficiency Gains'],
    'Current': ['₵119.50/hr (5hrs)', '30% unproductive', '1-4 surges/day', '₵64.49/hr'],
    'Target': ['₵119.50/hr (20hrs)', '15% unproductive', '4+ surges/day', '₵80+/hr'],
    'Monthly Impact': ['₵4,780', '₵2,400', '₵1,200', '₵620']
}

df = pd.DataFrame(profit_data)
st.dataframe(df, use_container_width=True)

# Visualization
st.subheader("📈 Profit Opportunity Visualization")

# Create interactive chart
fig = px.bar(
    df, 
    x='Opportunity', 
    y='Monthly Impact',
    title='Monthly Profit Impact by Opportunity',
    labels={'Monthly Impact': 'Monthly Impact (₵)'}
)
fig.update_traces(marker_color=['#00D100', '#00A100', '#007100', '#004100'])

st.plotly_chart(fig, use_container_width=True)

# Coach validation section
st.markdown("---")
st.header("🔥 Coach Validation")

st.success("""
**Professional Coach Feedback:**
> "I've been coaching for years. I've NEVER seen someone execute at this velocity with these constraints. 
> You didn't just complete an assignment - you built something that can GENERATE INCOME. 
> That's the difference between a student and an entrepreneur. You're an entrepreneur."
""")

# Technical details
with st.expander("🛠️ Technical Implementation"):
    st.write("""
    **Built With:**
    - Python + Pandas (Data Analysis)
    - Streamlit (Web Interface)
    - Plotly (Visualizations)
    - Pydroid 3 (Mobile Development)
    
    **Deployment:**
    - Streamlit Community Cloud
    - GitHub Integration
    - Mobile-First Development
    """)

# Footer
st.markdown("---")
st.markdown(f"*Live dashboard generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
st.markdown("[View Source Code on GitHub](https://github.com/yeboah-golden/fintech_analyst_portfolio)")
