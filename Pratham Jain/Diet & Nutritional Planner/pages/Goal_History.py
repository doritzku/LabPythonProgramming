import streamlit as st
from utils.db import create_connection
from datetime import datetime
from zoneinfo import ZoneInfo

st.subheader("View Past Goals")

user = st.session_state.get("user")
if not user:
    st.error("Please login to view this page!")
    st.stop()

conn = create_connection()
cursor = conn.cursor()

cursor.execute('''
        SELECT goal_type, target_weight, target_time_months, daily_calorie_change, target_calories, health_warning, timestamp
        FROM goals
        WHERE user_id = ?
        ORDER BY timestamp DESC
''', (user[0],))

rows = cursor.fetchall()
conn.close()

if not rows:
    st.info("No past goal records!")
else:
    count = 1
    for row in rows:
        goal_type, target_weight, months, change, target_calories, warning, timestamp = row

        utc = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        ist = utc.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Kolkata"))
        time = ist.strftime("%d %b %Y, %I:%M %p")

        with st.expander(f"{count}. [{time}] • {goal_type.capitalize()} Goal"):
            st.markdown(f"- Target Weight: {target_weight} kg")
            st.markdown(f"- Time Frame: {months} months")
            st.markdown(f"- Daily Calorie {'Deficit' if goal_type == 'loss' else 'Surplus'}: {int(change)} kcal")
            st.markdown(f"- Target Calories: {int(target_calories)} kcal/day")
            if warning:
                st.warning(warning)
        count += 1