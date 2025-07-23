import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grain Spoilage Prevention System", page_icon="🌾", layout="centered")

# Custom CSS for smaller fonts
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-size: 14px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌾 Grain Spoilage Prevention System")

# Section 1: Sensors Connected
st.subheader("✅ Connected Sensors")
sensors = [" Temperature Sensor", "Air Quality Sensor", " Moisture Sensor"]
for sensor in sensors:
    st.success(sensor)

# Section 2: AI Model
st.subheader("🤖 AI Model Status")
model_status = True  # Simulating that the model is loaded
if model_status:
    st.info("AI Model loaded successfully!")
else:
    st.warning("Loading AI Model...")

# Section 3: Current Condition
st.subheader("📊 Current Environment Status")
st.markdown("""
<div style="
    background-color: #e6ffe6;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    border: 2px solid #66bb6a;">
    <h2 style="color: #2e7d32;">ALERT CHECK YOUR CONDITIONS!!</h2>
</div>
""", unsafe_allow_html=True)

# Section 4: Live Sensor Charts from ThingSpeak
st.subheader("📈 Live Sensor Readings")

channel_id = "2960360"  # Replace with your ThingSpeak channel ID

# Temperature
st.markdown("🌡 Temperature**")
components.html(f"""
<iframe width="450" height="260" style="border: 1px solid #cccccc;" 
src="https://thingspeak.com/channels/{channel_id}/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&type=line&title=Temperature"></iframe>
""", height=270)

# Humidity
st.markdown("💧 Humidity**")
components.html(f"""
<iframe width="450" height="260" style="border: 1px solid #cccccc;" 
src="https://thingspeak.com/channels/{channel_id}/charts/2?bgcolor=%23ffffff&color=%2300aaff&dynamic=true&type=line&title=Humidity"></iframe>
""", height=270)

# Gas
st.markdown("🌬 Gas Level**")
components.html(f"""
<iframe width="450" height="260" style="border: 1px solid #cccccc;" 
src="https://thingspeak.com/channels/{channel_id}/charts/3?bgcolor=%23ffffff&color=%2333cc33&dynamic=true&type=line&title=Gas"></iframe>
""", height=270)

# Moisture
st.markdown("🌾 Moisture**")
components.html(f"""
<iframe width="450" height="260" style="border: 1px solid #cccccc;" 
src="https://thingspeak.com/channels/{channel_id}/charts/4?bgcolor=%23ffffff&color=%23ff9900&dynamic=true&type=line&title=Moisture"></iframe>
""", height=270)

# Footer
st.caption("Predicting LSTM + GA Model")