# Required Libraries

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import *
from streamlit_extras.colored_header import colored_header
from streamlit_extras.keyboard_url import keyboard_to_url
import json as js
import numpy as np
from datetime import date
import pickle
import pymongo as pm
import time 
from textblob import TextBlob 

class App:

    def model(self):

        st.set_page_config(page_title='Retail Sales Forecast Project By Praveen', layout="wide")

        
        with st.sidebar:  # Navbar
            selected = option_menu(
                menu_title="Project Workflow",
                options=['Intro','Tableau dashboard',"Inferencing",'Deployment','Feedback'],
                icons=['mic-fill', 'pie-chart-fill', 'graph-up-arrow', 'app','chat-heart-fill'],
                menu_icon='alexa',
                default_index=0,
            )
        

        def lottie(filepath):
            with open(filepath, 'r') as file:
              return js.load(file)
        
        
        if selected == 'Intro':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)



            # Start Intro
            col1, col2 = st.columns([11, 7])
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 79px;'><span style='color:white;'>Howdy ,</span> <span style='color: white;'>I'm </span><span style='color: cyan;'> Praveen</span> </h1>",
                    unsafe_allow_html=True)


            with col2:
                file = lottie("intro1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=700,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")
            with col1:
                file = lottie("sound.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=240,
                    width=600,
                    key=None
                )

            col1,col2,col3 = st.columns([3.4,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>Data</span> <span style='color: cyan;'> Scientist </span> <span style='color:white;'></span> <span style='color: white ;'> From </span> <span style='color: cyan;'> India </span></h1>",
                    unsafe_allow_html=True)
                
            col1,col2,col3 = st.columns([8,10,2])
            col2.markdown(
                    "<h1 style='font-size: 27px;'>  <span style='color: cyan;'>To Know About Me  </span> <span style='color: cyan;'>Press 'P'  </span></h1>",
                    unsafe_allow_html=True)
            keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")


            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([10,5,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 80px;'><span style='color:cyan;'>About </span><span style='color:white   ;'>Retail Sales Forecast Project </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([2,10,2])
            with col2:
                file = lottie("cyan_boy_lap2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=1200,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([16,10,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'> </span><span style='color:Cyan;'>Problem </span><span style='color:white;'> Statement </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([1,10,1])
            
            with col2:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 60px;'><span style='color:white;'> Build </span><span style='color:cyan;'> Regression Model  </span><span style='color:white;'>to predict department-wise weekly sales for each store of given year</span> </h1>",
                    unsafe_allow_html=True)
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 60px;'><span style='color:white;'>Model the effects of  </span><span style='color:cyan;'> markdown  </span><span style='color:white;'> on holiday weeks </span> </h1>",
                    unsafe_allow_html=True)
            # Data collection and understanding
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
                
            col1,col2,col3 = st.columns([16,10,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>What has </span><span style='color:Cyan;'>Praveen </span><span style='color:white;'> Done ? </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("boydoubtface.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=800,
                    key=None
                )
            with col2:
                file = lottie("lets_start.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=900,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            
        

            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:cyan;'>Information Gathering</span><span style='color:white;'> and  </span><span style='color:cyan;'>  Understanding </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("database.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=900,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Data </span><span style='color:white;'> Preprocessing </span><span style='color:cyan;'>  </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("vacuum Cleaner.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Exploratory </span><span style='color:white;'> Data  </span><span style='color:cyan;'> Analysis </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("data_exploaration.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=1000,
                    key=None
                )



            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:cyan;'> Model </span><span style='color:white;'>  </span><span style='color:white;'> Process </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
           
            with col2:
                file = lottie("model_training.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=1000,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:cyan;'> Docker  </span><span style='color:white;'> Deployment  </span><span style='color:white;'> </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
           
            with col2:
                file = lottie("docker.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=1000,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:cyan;'> Azure  </span><span style='color:white;'> Deployment  </span><span style='color:white;'></span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
           
            with col2:
                file = lottie("azure.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=1000,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            
















            colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )

        elif selected == 'Tableau dashboard':
                st.markdown("<style>div.block-container{padding-top:0rem;}</style>", unsafe_allow_html=True)

                col1,col2,col3 = st.columns([5,10,5])
                col2.write("")
                col2.write("")
                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([1, 10, 1])
                with col2:
                    file = lottie("d1.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        height=900,
                        width=1700,
                        key=None
                    )
                col1,col2,col3 = st.columns([7,10,5])
                col2.markdown( "<h1 style='font-size: 40px;'><span style='color: white;'>Press </span> <span style='color: cyan;'>'P'</span> <span style='color: white;'>To See Tableau Dashboard</span></h1>",unsafe_allow_html=True)
                keyboard_to_url(key="P", url="https://public.tableau.com/app/profile/praveen.x.decode/viz/retail-sales-forecast/Dashboard1?publish=yes")
       
        elif selected == 'Inferencing':

            

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            col1,col2,col3 = st.columns([4,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color: cyan;'>Regression </span><span style='color: white;'> Model</span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([4,10,7])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
            col1,col2,col3 = st.columns([2,10,2])
            # Start from options
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")  

            with col2 :
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Store </span><span style='color: white;'>Number </span> </h1>",
                    unsafe_allow_html=True)
                store = st.selectbox('',[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
                                        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                                        35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45])
                #___________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Department  </span><span style='color: white;'> Number </span> </h1>",
                unsafe_allow_html=True)
                dept = st.selectbox('',[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18,
                                        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                        36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56,
                                        58, 59, 60, 67, 71, 72, 74, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92,
                                        93, 94, 95, 97, 98, 78, 96, 50, 99, 65, 43, 39, 77])
                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Is </span><span style='color: white;'> Holiday </span> </h1>",
                    unsafe_allow_html=True)
                holiday =  st.selectbox(' ',['False','True']) 
                holiday_v = 0 if holiday=='False' else 1
                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Temperature  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                temp = st.number_input('',min_value=1.00, max_value=101.95, value=1.0)

                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Fuel Price </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                fuel_price = st.number_input('       ',min_value=2.000, max_value=4.468, value=2.000)
                
                
               
                #________________________________________________________________________
                
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'> </span><span style='color: cyan;'>Date</span> </h1>",
                    unsafe_allow_html=True)
                
                Date =  st.date_input(label='    ', min_value=date(2010,2,5), 
                                            max_value=date(2010,2,5), value=date(2010,2,5))
                
                #________________________________________________________________________
                with col2:
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Size  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    size =  st.selectbox('',[151315, 202307,  37392, 205863,  34875, 202505,  70713, 155078,
                                                125833, 126512, 207499, 112238, 219622, 200898, 123737,  57197,
                                                    93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107,
                                                152513, 204184, 206302,  93638,  42988, 203750, 203007,  39690,
                                                158114, 103681,  39910, 184109, 155083, 196321,  41062, 118221])
                    #_____________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Type  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    Type =  st.selectbox("    ",['A','B','C'])  
                    Type_v =  1 if Type =='A' else(2 if Type == "B" else 3 )

                #________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown1  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    MarkDown1 =  st.number_input('',min_value=-2781.450000, max_value=103184000.980000, value=1.0)
                    
                #___________________________________________________________________________
             

                #________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown2  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    MarkDown2 =  st.number_input('',min_value=-265.760000, max_value=104519000.540000, value=1.0)

                #__________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown3  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    MarkDown3 =  st.number_input('',min_value=-179.260000, max_value=149483000.310000, value=1.0)
                #___________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown4  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    MarkDown4 =  st.number_input('  ',min_value=-179.260000, max_value=149483000.310000, value=1.0)
                #_____________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown5  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    MarkDown5 =  st.number_input('   ',min_value=-179.260000, max_value=149483000.310000, value=1.0)
                #_____________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>CPI  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    CPI =  st.number_input('      ',min_value=100.06, max_value=100000.06, value=100.06)

                #__________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Unemployment  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    Unemployment =  st.number_input('      ',min_value=1.00, max_value=14.313000, value=3.684000)

                #______________________________________________________________________________________________________________



                predict_data = [store,dept,holiday_v,temp,fuel_price,Date.day,Date.month,Date.year,Type_v,size,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment]
                st.write(predict_data)
                
 
                col1,col2,col3 = st.columns([10,1,10])
                 
               
                with col1 :
                    
                    st.write("")
                   
                    if st.button('Process'):
                        with open('regressor_model.pkl', 'rb') as f:
                               model = pickle.load(f)
                        x = model.predict([predict_data])
                        st.markdown(
                                f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Predicted Weekly Sales : </span><span style='color: white;'> {round(x[0],2)}</span> </h1>",
                                unsafe_allow_html=True)  
        
        elif selected == 'Deployment':

            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:cyan;'> Azure  </span><span style='color:white;'> Deployment  </span><span style='color:white;'></span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
           
            with col2:
                file = lottie("azure.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=1000,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([8,10,5])
            col2.markdown( "<h1 style='font-size: 50px;'><span style='color: white;'>Press </span> <span style='color: cyan;'>'P'</span> <span style='color: white;'>to use</span><span style='color: cyan;'> Azure Deployment</span></h1>",unsafe_allow_html=True)
            keyboard_to_url(key="P", url="https://colab.research.google.com/drive/1h70p6bJhWNBF4Iwd5zAWQ9dB7Dlzgh1d?usp=sharing")
            




        elif selected == 'Feedback':
            praveen_1 = pm.MongoClient(
                'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
            db = praveen_1['Feedback_icm']
            collection = db['comment']

            st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                selected_1 = option_menu(
                    menu_title="OPINION BOX",
                    options=['CHOOSE OPTION', 'Your Feedback', "Explore User Thoughts"],
                    icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                    default_index=0)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            if selected_1 == 'CHOOSE OPTION':
                # animation

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3, col4 = st.columns([15, 15, 15, 15])
                with col2:
                    file = lottie("angry_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col1:
                    file = lottie("smile_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col3:
                    file = lottie("calm_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col4:
                    file = lottie("love_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )


            elif selected_1 == 'Your Feedback':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])
                col2.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                # animation

                st.write("")

                st.write("")

                st.write("")
                col1, col2, col3 = st.columns([15, 30, 5])
                with col2:
                    file = lottie("star_before_fb.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=600,
                        key=None
                    )

                col1, col2, col3, = st.columns([3, 8, 3])

                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                        unsafe_allow_html=True)
                    Comment = st.text_input('   ')
                    st.write(Comment)
                    if st.button('Save Comment'):
                        collection.insert_one({'comment of user': Comment})
                        st.write("")
                        st.write("")
                        senti = TextBlob(Comment)
                        value = senti.polarity
                        if value>=0.5:
                            review = "Positive Review"
                        elif value <0.0:
                            review = 'Negative Review'
                        else:
                            review = 'Neutral Review'



                        col1, col2, col3, = st.columns([5, 8, 5])
                        col2.markdown(
                        f"<h1 style='font-size: 40px;'><span style='color:cyan;'>{review}</span>  </h1>",
                        unsafe_allow_html=True)
                        col1, col2, col3, = st.columns([5, 8, 5])
 
                        st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                        col1, col2, col3 = st.columns([10, 30, 10])
                        
                        with col2:
                            file = lottie("star.json")
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                # renderer='svg',
                                height=100,
                                width=500,
                                key=None
                            )
                        
                    

                col1, col2, col3, = st.columns([3, 8, 3])
                with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )


            elif selected_1 == 'Explore User Thoughts':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])

                with col2:

                    file = lottie("down_arrow.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=800,
                        key=None
                    )
                col2.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                col2.write("")
                col2.write("")

                with col2:

                    file = lottie("thoughts.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=800,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                col1, col2, col3, = st.columns([3.6, 10, 3])
                with col2:
                    res = [i['comment of user'] for i in collection.find()]
                    st.write("")
                    with st.spinner('Wait for it...'):
                        time.sleep(5)

                    colored_header(
                        label="Comments By Users ⬇",
                        description="",
                        color_name="blue-green-70", )
                    for i in res:
                        print(st.code(i))

                    col1, col2, col3 = st.columns([1, 10, 1])
                    col2.write("")
                    col2.write('')
                    col2.markdown(
                        "<h1 style='font-size: 35px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                        unsafe_allow_html=True)
                    with col2:
                        keyboard_to_url(key="G", url="https://github.com/praveendecode")

                    def lottie(filepath):
                        with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                            return js.load(file)

                    with col2:
                        file = lottie("click2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=100,
                            width=700,
                            key=None
                        )

                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )                      
                                


# Object Creation for CLass App

Object = App()
Object.model()

#___________________________________________________________________COMPLETED______________________________________________________#