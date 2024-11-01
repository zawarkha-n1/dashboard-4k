import streamlit as st
import streamlit.components.v1 as components
import time
from functions import plot_histograms
 

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

odyssey_youtube_plot = plot_histograms("Odyssey", "youtube")
odyssey_meta_plot = plot_histograms("Odyssey", "meta")
odyssey_shopify_plot = plot_histograms("Odyssey", "shopify")
odyssey_ppc_plot = plot_histograms("Odyssey", "ppc")
 
 
ody_second_html_code = f"""
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
    height: 137px;
    width: 502px;
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

.image-containers {{
    position: absolute;
    top: 3px; /* Adjust as needed */
    left: 14px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containers img {{
    width: 70px; /* Adjust as needed */
    height: 40px;
}}

.image-containerp {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containerp img {{
    width: 80px; /* Adjust as needed */
    height: 25px;
}}

 .image-containerm {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 12px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containerm img {{
    width: 70px; /* Adjust as needed */
    height: 25px;
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
        padding-top:26px;
     
        width: 100%;
        height: 90%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

     .graph-containery {{
        padding-top:20px;
     
        width: 100%;
        height: 90%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
 
    .container {{
            display: flex;
            align-items: center; /* Align items vertically in the center */
            justify-content: space-between; /* Evenly space the heading and buttons */
            margin-top:15px;
            margin-bottom: 15px;
        }}
        .container h2 {{
            color: white;
            margin: 0;
            font-size: 24px;
        }}
        .buttons {{
            display: flex;
            gap: 20px; /* Gap between buttons */
        }}
        .buttons button {{
            padding: 10px 20px;
            font-size: 16px;
            background-color: #20232A;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
           
            text-align: center;
            font-family: Inter;
            font-size: 18px;
            font-style: normal;
            font-weight: 500;
            line-height: normal;
        }}
        .buttons button:hover {{
            background-color: #181A1F;
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
     <div class="container">
        <h2 style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal;' >Paid Campaigns</h2>
        <div class="buttons">
            <button>Today</button>
            <button>Week</button>
            <button>Month</button>
        </div>
    </div>
    <div class="main-container">
    <div class="main-card">
        <div class="image-containery">
            <img src="https://i.postimg.cc/ydp0KFCM/youtube.png" alt="logo">
        </div>
       <div class="graph-containery">
            {odyssey_youtube_plot}
        </div>
    </div>
    <div class="main-card">
        <div class="image-containerm">
            <img src="https://i.ibb.co/DwsPvBp/5b3aabc35e871898875a6b1ffb78876b.png" alt="logo">
        </div>
        <div class="graph-containery">
            {odyssey_meta_plot}
        </div>
    </div>
     <div class="main-card">
        <div class="image-containers">
            <img src="https://i.ibb.co/fdRd84G/e9e44a17e0bf09233723ecd1e89cd914.png" alt="logo">
        </div>
        <div class="graph-containery">
            {odyssey_shopify_plot}
        </div>
    </div>
    <div class="main-card">
        <div class="image-containerp">
            <img src="https://i.ibb.co/hL354d1/949af83cd742b7811af1bcdbd4733987.png" alt="logo">
        </div>
        <div class="graph-containery">
            {odyssey_ppc_plot}
        </div>
    </div>
   
   
</div>
"""
components.html(ody_second_html_code, height=1000)
time.sleep(60)
st.switch_page("pages/exarta_first.py")