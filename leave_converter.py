import streamlit as st

# App title
st.title("Annual Leave Converter")

# Inputs
total_hours = st.number_input("Enter total hours:", min_value = 0, value = 0)
total_minutes = st.number_input("Enter total minutes:", min_value = 0, max_value = 59, value = 0)
hours_per_day = st.number_input("Working hours per day:", min_value = 1.0, max_value = 24.0, value = 7.4, step = 0.25)

# Calculate total minutes
total_minutes_all = total_hours * 60 + total_minutes

# Convert to days, hours, and minutes
days = int(total_minutes_all // (hours_per_day * 60))
remaining_minutes = total_minutes_all % (hours_per_day * 60)
hours = int(remaining_minutes // 60)
minutes = int(remaining_minutes % 60)

# Output
st.markdown("### Result")
st.write(f"{days} days, {hours} hours, {minutes} minutes")


