import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from streamlit_option_menu import option_menu

df = pd.read_csv("C:\\Users\\abc\\Desktop\\earthquakes11.csv")
df1=df.dropna()
staticdata=pd.read_csv("C:\\Users\\abc\\Desktop\\data earth q.csv")
Deaths=df1['Deaths']
Year=df1['Year']
Magnitude=df1['Magnitude']



with st.sidebar:
    selected=option_menu(
         menu_title="App content Guide",
         options=['About this app', 'Earthquakes', 'About me'])

if selected=='About this app':
    st.title(":blue[Hello!]")
    st.subheader(" this streamlit app will tell you about some :blue[stats] of :red[earthquakes] held in last decades.")
    st.markdown("the fatalities they caused and their magnitude is shown in the table.")
    st.markdown("along with the places in which earthquakes occurs, we have classified them and given them rank based on thier magnitude of scale and the date of their occurence is aslo mentioned int he table.")
    st.dataframe(staticdata)
    

if selected=='Earthquakes':

    st.title(":red[EARTHQUAKES]")
    image = Image.open("C:\\Users\\abc\\Downloads\\ecuador-gdfca57680_1920.jpg")
    st.image(image)
    st.header("Earthquakes in the world")
    st.markdown("**:red[Earthquake]** is the shaking of the earth. An earth quake can" )
    st.markdown("be defined as a sudden :red[violent shaking] of the ground as a result")
    st.markdown("of :red[movements] in the earth’s crust or volcanic action.")
    st.header("**:blue[The]** overview of data")
    st.write(df1)
    st.subheader(":blue[Some] stats about :red[data]")
    st.write(df1.describe())
    st.subheader("No. of :red[Deaths] in Earthquakes")
    st.markdown(':blue[Understanding] through Bar chart')
    
    st.bar_chart(df1['Deaths'].value_counts().sample(20),x=['Location Name'])
    st.markdown(':blue[Understanding] through line chart')
    st.line_chart(df1, y=['Deaths','Injuries','Damage Description'])
    st.subheader("No. of :red[Injuries] in Earthquakes")
    st.bar_chart(df1['Injuries'].value_counts().sample(20))

    st.subheader(':blue[Stats] of total :red[deaths] and :blue[Magnitude] of Earthquakes')
    col1, col2 = st.columns(2)
    fig_1 = px.histogram(df1[df1['Deaths'] == Deaths], x="Deaths")
    col1.plotly_chart(fig_1, use_container_width=True)
    
    fig_2 = px.histogram(df1[df1['Magnitude'] == Magnitude], x="Magnitude")
    col2.plotly_chart(fig_2, use_container_width=True)


    st.subheader("Location wise :red[Deaths] due to :red[Earthquakes]")
    n_estimator = st.selectbox("**select any location !**", df1['Location Name'].unique())
    #st.subheader("Location wise :red[Deaths] due to :red[Earthquakes]")
    st.bar_chart(df1['Deaths'].value_counts().sample(20))

    #location wise Injuries
    st.subheader("Location wise :red[Injuries] due to :red[Earthquakes]")
    n_estimator = st.selectbox("**Choose Location !**", df1['Location Name'].unique())
    st.bar_chart(df1['Injuries'].value_counts().sample(20))

    #Magnitude location wise
    st.subheader("Highest :blue[Magnitude] of :red[Earthquake]")
    n_estimator = st.selectbox("**Select any Location**", df1['Location Name'].unique())
    st.bar_chart(df1['Magnitude'].value_counts().sample(20))

    #Home destroyed location wise
    st.subheader("maximum :blue[Houses destroyed] due to :red[Earthquake]")
    n_estimator = st.selectbox("**Choose any Location**", df1['Location Name'].unique())
    st.bar_chart(df1['Houses Destroyed'].value_counts().sample(20))
    


    

if selected=='About me':
    st.markdown("I am :green[Himanshu vaish], pursuing my Master's degree in :blue[Data Science] stream from :orange[Indore] Madhya Pradesh ")
    