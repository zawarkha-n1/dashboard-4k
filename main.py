import streamlit as st
import streamlit.components.v1 as components
import time
from functions import zeniva_overview, odyssey_overview, df_for_comp
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

hideTopBar = True

# Inject custom CSS to target the entire page background dddddd
st.markdown(
    """
    <style>
   
   header {visibility: hidden;}       
   footer {visibility: hidden;}         
   .stApp > header {display: none;}
   .st-emotion-cache-19u4bdk.eczjsme5 > {visibility: hidden;}      
   
    /* Ensure all content aligns properly in the dark background */
    .stApp {
        background-color: #191B21;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

df_for_comparisons = df_for_comp()
 
today_paid_installs_for_zin, todays_free_installs_zin, lifetime_installs_zin, today_paid_uninstalls_zin, today_free_uninstalls_zin, lifetime_uninstalls_zin= zeniva_overview(df_for_comparisons)

todays_forge_installs_for_odyssey, todays_free_installs_for_odyssey, lifetime_installs_for_odyssey, todays_forge_uninstalls_for_odyssey, today_free_uninstalls_for_odyssey, lifetime_uninstalls_for_odyssey = odyssey_overview(df_for_comparisons) 



html_code = f"""
    <style>
     .header {{
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        margin-top:-8px;
        color: white;
    }}
    .main-container {{
    display: grid;
    grid-template-columns: repeat(2,1fr);
     gap: 20px;
 
}}
 
.main-card {{
     background-color: #272B34;
    height: 280px;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    position: relative;
}}
 
.image-container {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-container img {{
    width: 100px; /* Adjust as needed */
    height: auto;
}}
 
 
.image-containerx {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containerx img {{
    width: 100px; /* Adjust as needed */
    height: 29px;
}}
   
    .paid-installs {{
        background-color: #A6B174;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .today-installs {{
        background-color: #F68C5B;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .today-paid-users {{
        background-color: #BC679C;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .row {{
        display: flex;
        justify-content: space-between;
    }}
    .column {{
        flex: 1;
        margin: 0 10px;
    }}
    .number-text {{
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 48px;
        font-style: normal;
        font-weight: 800;
        line-height: normal;
    }}
   
   
     .graph-container {{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
 
    .metric-container {{
            margin-top: 100px;
        }}
        .metric-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
        }}
        .metric-row p {{
            margin: 0;
        }}
        .metric-line {{
            border-bottom: 1px solid rgba(209, 209, 209, 0.1); /* Correct property for creating a line */
            margin: 10px 0;
        }}
        .metric-left {{
            color: #F0F0F0;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-style: normal;
            font-weight: 300;
            line-height: normal;
            text-align: left;
        }}
        .metric-right {{
             color: white;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-style: normal;
            font-weight: 500;
            line-height: normal;
            text-align: right;
        }}
 
 
.main-card {{
    background-color: #272B34;
    height: 400px;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
 
.firstrowcards {{
    display: flex;
    margin-top: 60px; /* Decrease this value to reduce space from the top */
    gap: 10px;
    margin-bottom: 0px; /* Reduce or remove space between rows */
}}
 
.secondrowcards {{
    display: flex;
    gap:10px;
    margin-top: 5px; /* Optional: add a small margin between the rows */
    margin-bottom: 10px;
}}
 
.card {{
    background-color: #444B57;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
.card1 {{
    background-color:#A6B174  ;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
.card2 {{
    background-color:#F68C5B  ;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
.card3 {{
    background-color:#BC679C  ;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
 
 
.card-number {{
    font-size: 3em; /* Adjust this for a larger number */
    font-weight: 800;
    color: white; /* Adjust the color to your preference */
    margin-bottom: 5px; /* Add spacing between number and text */
}}
 
.card-text {{
 
font-family: Roboto;
font-size: 15px;
font-style: normal;
font-weight: 600;
line-height: normal;
margin-bottom: 22px;
}}
 
.progress-container {{
    width: 100%; /* Full width relative to the parent container */
    max-width: 1800px; /* Maximum width to ensure it doesn't exceed 1800px */
    height: 10px;
    background-color: #323743; /* Background color of the entire container */
    border-radius: 0px; /* No rounding for the container edges */
    overflow: hidden; /* Ensures that the progress bar stays within the container */
    margin: 0 auto; /* Center the progress container */
}}
 
.progress-bar {{
    width: 0; /* Initial width of the progress bar */
    height: 100%; /* Full height of the container */
    background: #495161; /* Progress bar color */
    border-radius: 5px;
    animation: grow 60s linear forwards; /* Animation: grow over 10 seconds */
}}
 
@keyframes grow {{
    from {{
        width: 0;
    }}
    to {{
        width: 100%; /* Grow to full width */
    }}
}}

  @media (min-width: 2560px) {{
        .main-container {{
            grid-template-columns: repeat(3, 1fr); /* More columns for large screens */
            gap: 30px;
        }}
        .main-card {{
            padding: 30px;
        }}
        .card-number {{
            font-size: 4em; /* Increase font size for large screens */
        }}
        .card-text {{
            font-size: 18px;
        }}
    }}

    .h2{{
        margin-top:15px;
        margin-bottom:15px;
    }}
    </style>
 
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>
 
    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
                       <img style="padding-left:100px;" src="https://i.ibb.co/0jT4xCS/Logo-2-1.png" alt="logo" style="width:100px;">
            <div>
                <a href="#overview" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: underline;">Overview</a>
 
                <a href="#zeniva" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none; text-decoration-color: none;">Zeniva</a>
 
                <a href="#odyssey" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Odyssey</a>
 
                <a href="#exarta" style="padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Exarta</a>
 
            </div>
        </div>
    </div>
      <div class="progress-container">
    <div class="progress-bar"></div>
</div>
    <h2 class="h2" style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal; margin-top:15px; margin-bottom:15px;'>Social Media</h2>
    <div class="main-container">
   
   
    <div class="main-card">
        <div class="image-container">
            <img src="https://i.ibb.co/3WLkjzJ/7bdf715624ed952d97ee1983147bfc6e.png" alt="logo">
        </div>
 
         <div class="firstrowcards">
         <div class="card1">
        <p class="card-number">{int(today_paid_installs_for_zin)}</p>
        <p class="card-text">Today's Paid Installs</p>
    </div>
    <div class="card2">
        <p class="card-number">{int(todays_free_installs_zin)}</p>
        <p class="card-text">Today's Free Installs</p>
    </div>
    <div class="card3">
        <p class="card-number">{int(lifetime_installs_zin)}</p>
        <p class="card-text">Total Installs</p>
    </div>
    </div>
  <div class="secondrowcards">
    <div class="card">
        <p class="card-number">{int(today_paid_uninstalls_zin)}</p>
        <p class="card-text">Today's Paid Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(today_free_uninstalls_zin)}</p>
        <p class="card-text">Today's Free Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(lifetime_uninstalls_zin)}</p>
        <p class="card-text">Total Uninstalls</p>
    </div>
</div>
   
    </div>
    <div class="main-card">
        <div class="image-containerx">
            <img src="https://i.ibb.co/sqWcC9d/becbd639884fea2ce7449a6c2aabe320.png" alt="logo">
        </div>
 
 <div class="firstrowcards">
        <div class="card1">
        <p class="card-number">{int(todays_forge_installs_for_odyssey)}</p>
        <p class="card-text">Today's Forge installs</p>
    </div>
    <div class="card2">
        <p class="card-number">{int(todays_free_installs_for_odyssey)}</p>
        <p class="card-text">Today's Free installs</p>
    </div>
    <div class="card3">
        <p class="card-number">{int(lifetime_installs_for_odyssey)}</p>
        <p class="card-text">Total installs</p>
    </div>
    </div>
     <div class="secondrowcards">
    <div class="card">
        <p class="card-number">{int(todays_forge_uninstalls_for_odyssey)}</p>
        <p class="card-text">Today's Forge Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(today_free_uninstalls_for_odyssey)}</p>
        <p class="card-text">Today's Free Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{int(lifetime_uninstalls_for_odyssey)}</p>
        <p class="card-text">Total Uninstalls</p>
    </div>
</div>
</div>
   
   
   
</div>
"""
 
 

components.html(html_code, height=1000)
time.sleep(60)
st.switch_page("pages/zeniva_first.py")