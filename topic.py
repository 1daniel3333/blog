import streamlit as st
import pandas as pd

def weather_main():
    body = '''<iframe src="https://www.cwa.gov.tw/V8/C/W/OBS_Radar.html" width="800" height="600" frameborder="0" allowfullscreen></iframe>'''
    st.markdown(body, unsafe_allow_html=True)
    
def get_action_mountain_climb():
    #get file
    judgement_df = pd.read_excel('climbing_levels.xlsx', sheet_name='judgement')
    skill_df = pd.read_excel('climbing_levels.xlsx', sheet_name='skill')
    experience_df = pd.read_excel('climbing_levels.xlsx', sheet_name='experience')
    
    st.dataframe(experience_df, use_container_width=True)

    # Define the options
    options = list(judgement_df['體能狀況'].unique())

    # Create a selectbox for single selection
    selection = st.selectbox("選定不同體能狀況:", options)

    current_condition = judgement_df[judgement_df['體能狀況']==selection]
    st.dataframe(current_condition, use_container_width=True)

    level = current_condition['Level'].unique()[0]

    st.write('應具備技能:')
    st.dataframe(skill_df[(skill_df['Required_level']<=level) & (skill_df['項目']=='技能')], use_container_width=True)

    st.write('視狀況攜帶物品:')
    st.dataframe(skill_df[(skill_df['Required_level']<=level) & (skill_df['項目']=='裝備')], use_container_width=True)