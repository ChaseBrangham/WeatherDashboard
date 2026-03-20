import info
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤",
    layout="wide"
)

st.markdown("""
<style>

    .recent-box {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.92), rgba(17, 24, 39, 0.96));
        padding: 22px;
        border-radius: 22px;
        box-shadow: 0 18px 40px rgba(0, 0, 0, 0.28);
        border: 1px solid rgba(96, 165, 250, 0.18);
        margin-top: 20px;
    }

    div[data-testid="stTextInput"] input {
        text-align: center;
    }

    div[data-testid="stTextInput"] input::placeholder {
        text-align: center;
        color: white;
        opacity: 1;
    }
    
    div[data-testid="stTextInput"] input::placeholder {
        color: white;
        opacity: 1;
    }

    [data-testid="stDataFrame"] {
        background: rgba(15, 23, 42, 0.75) !important;
        border-radius: 16px;
        overflow: hidden;
    }

    iframe {
        border-radius: 16px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }

    h3 {
        color: #f8fafc !important;
    }
    
    section-header {
        color: #0f172a;
    }

    .stApp {
        background:
            radial-gradient(circle at top, rgba(124, 58, 237, 0.22), transparent 35%),
            radial-gradient(circle at right, rgba(37, 99, 235, 0.18), transparent 30%),
            linear-gradient(180deg, #081120 0%, #0b1220 45%, #0f172a 100%);
    }
    
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 8px;
    }
    
    .block-container {
    max-width: 1400px;
    padding-left: 3rem;
    padding-right: 3rem;
}
    
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    .weather-card {
        background: white;
        padding: 30px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
        margin-top: 25px;
    }

    .city-name {
        text-align: center;
        font-size: 34px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 25px;
    }

    .metric-card {
        background: #f8fafc;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: inset 0 0 0 1px #e2e8f0;
    }

    .metric-label {
        font-size: 15px;
        font-weight: 600;
        color: #64748b;
        margin-bottom: 10px;
    }

    .metric-value {
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
    }

    .weather-box {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.92), rgba(17, 24, 39, 0.96));
        padding: 28px;
        border-radius: 22px;
        box-shadow: 0 18px 40px rgba(0, 0, 0, 0.32);
        margin-top: 25px;
        border: 1px solid rgba(96, 165, 250, 0.18);
    }

    .desc-value {
        font-size: 22px;
        font-weight: 700;
        color: #0f172a;
        text-transform: capitalize;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 14px;
        border: 1px solid #334155;
        padding: 12px;
        font-size: 16px;
        background: rgba(15, 23, 42, 0.9);
        color: #f8fafc;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 16px;
        border: none;
        background: linear-gradient(90deg, #7c3aed, #2563eb);
        color: white;
        font-size: 17px;
        font-weight: 700;
        padding: 12px 0;
        box-shadow: 0 8px 18px rgba(99, 102, 241, 0.28);
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #6d28d9, #1d4ed8);
        color: white;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #1e40af);
        color: white;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #0369a1, #075985);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌤 Weather Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter a location to check the weather.</div>', unsafe_allow_html=True)

location = st.text_input("Location", placeholder="Type a city or location", label_visibility="collapsed")

if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

if "error_message" not in st.session_state:
    st.session_state.error_message = ""

def showWeather():
    latest = info.WeatherDataManager().getLatestWeather()

    if latest:
        city, temp, feels_like, description, humidity = latest

        temp = round(temp)
        feels_like = round(feels_like)
        description = str(description).title()
        col_left, col_center, col_right = st.columns([1, 3, 1])

        with col_center:
            with st.container(border=True):
                st.markdown(
                    f"""
                    <div style="
                        text-align: center;
                        font-size: 2.4rem;
                        font-weight: 700;
                        line-height: 1.2;
                        margin-bottom: 25px;
                        width: 100%;
                        color: #f8fafc;
                    ">
                        📍 {city}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                left1, col1, col2, right1 = st.columns([1, 2, 2, 1])
                with col1:
                    st.metric("🌡 Temperature", f"{temp}°F")
                with col2:
                    st.metric("🥵 Feels Like", f"{feels_like}°F")

                left2, col3, col4, right2 = st.columns([1, 2, 2, 1])
                with col3:
                    st.markdown('<p style="color:#94a3b8; font-weight:600; margin-bottom:6px;">☁ Description</p>',
                                unsafe_allow_html=True)
                    st.markdown(f'<p style="color:#f8fafc; font-size:1.1rem;">{description}</p>',
                                unsafe_allow_html=True)
                    st.write(description)
                with col4:
                    st.metric("💧 Humidity", f"{humidity}%")

    chart_data = pd.DataFrame({
        "Weather Stat": ["Temperature", "Feels Like", "Humidity"],
        "Value": [temp, feels_like, humidity]
    })
    st.bar_chart(chart_data.set_index("Weather Stat"))

    recent = info.WeatherDataManager().getRecentWeather()

    df = pd.DataFrame(
        recent,
        columns=["City", "Temp", "Feels Like", "Description", "Humidity"]
    )

    st.markdown('<div class="recent-box">', unsafe_allow_html=True)
    st.subheader("Recent Searches")
    st.dataframe(df, width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

    compare_data = pd.DataFrame({
        "Type": ["Temperature", "Feels Like"],
        "Degrees": [temp, feels_like]
    })

    st.subheader("Temperature Comparison")
    st.bar_chart(compare_data.set_index("Type"))

    st.subheader("Humidity Level")
    st.progress(int(humidity))



col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    clicked = st.button("Get Weather", use_container_width=True)

if clicked:
    saveit = info.WeatherDataManager().saveIntoDatabase(location)

    if saveit and saveit.lower() != "could not find any weather data there...":
        st.session_state.error_message = ""
        st.session_state.weather_data = True
    else:
        st.session_state.weather_data = None
        st.session_state.error_message = saveit

if st.session_state.error_message:
    st.error(st.session_state.error_message)

if st.session_state.weather_data:
    showWeather()

