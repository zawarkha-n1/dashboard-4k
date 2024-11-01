import streamlit as st
import streamlit.components.v1 as components
import time
from functions import odyssey_values_for_insights, all_data_for_stats

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

st.markdown(
    """
    <style>
   
   header {visibility: hidden;}       
   footer {visibility: hidden;}         
   .stApp > header {display: none;}   

    
    
    /* Ensure all content aligns properly in the dark background */
    .stApp {
        background-color: #191B21;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


data = all_data_for_stats()
odyssey_youtube, odyssey_tiktok, odyssey_instagram, odyssey_facebook = odyssey_values_for_insights(data)

odyssey_first_html_code = f"""
    <style>
  .header {{
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        margin-top:-8px;
        color: white;
    }}
    .main-container {{
        margin-top:-17px;
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 20px;

}}

.main-card {{
    background-color: #272B34;
    height: 145px;
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

.image-containerf {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containerf img {{
    width: 70px; /* Adjust as needed */
    height: 25px;
}}



.image-containerx {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containerx img {{
    width: 28px; /* Adjust as needed */
    height: 24px;
}}
    .card {{
        background-color: #343844;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        height: 170px;
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
    .card-text {{
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 26.172px;
        font-style: normal;
        font-weight: 600;
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
            margin-top: 40px;
        }}
        .metric-row {{
            display: flex;
            justify-content: space-between;

            padding: 3px 0;
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
            font-size: 14px;
            font-style: normal;
            font-weight: 300;
            line-height: normal;
            text-align: left;
        }}
        .metric-right {{
            color: white;
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
            font-style: normal;
            font-weight: 500;
            line-height: normal;
            text-align: right;
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

 .image-containery {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containery img {{
    width: 70px; /* Adjust as needed */
    height: 25px;
}}

 .image-containerl {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containerl img {{
    width: 70px; /* Adjust as needed */
    height: 25px;
}}


.image-containeri {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containeri img {{
    width: 85px; /* Adjust as needed */
    height: 30px;
}}

.image-containert {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containert img {{
    width: 85px; /* Adjust as needed */
    height: 30px;
}}
 
 
    </style>
 
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>
 
    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
           <img style="padding-left:100px;" src="https://i.ibb.co/0jT4xCS/Logo-2-1.png" alt="logo" style="width:100px;">
            <div>
                <a href="#overview" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Overview</a>
 
                <a href="#zeniva" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none; text-decoration-color: none;">Zeniva</a>
 
                <a href="#odyssey" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: underline;">Odyssey</a>
 
                <a href="#exarta" style="padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Exarta</a>
 
            </div>
        </div>
    </div>
     <div class="progress-container">
    <div class="progress-bar"></div>
</div>
    <h2 style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal;'>Social Media</h2>
    <div class="main-container">
    <div class="main-card">
        <div class="image-containery">
            <img src="https://i.postimg.cc/ydp0KFCM/youtube.png" alt="logo">
        </div>
       <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(odyssey_youtube['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(odyssey_youtube['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(odyssey_youtube['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>

     <div class="main-card">
        <div class="image-containert">
            <img src="https://i.ibb.co/S0fVvSL/fc9958aff216c7090428e6fa1fa03889.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(odyssey_tiktok['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(odyssey_tiktok['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(odyssey_tiktok['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containeri">
             <img src="https://i.ibb.co/XFh4Bvy/insta.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(odyssey_instagram['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(odyssey_instagram['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(odyssey_instagram['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containerf">
            <img src="https://i.postimg.cc/X79mjgsS/image-11-1.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(odyssey_facebook['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(odyssey_facebook['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>
 
    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(odyssey_facebook['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
   
   
</div>
"""
 
 
components.html(odyssey_first_html_code, height=1000)
time.sleep(60)
st.switch_page("pages/ody_second.py")