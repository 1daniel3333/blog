import streamlit as st
import pandas as pd

def weather_main():
    body = '''<iframe src="https://www.cwa.gov.tw/V8/C/W/OBS_Radar.html" width="800" height="600" frameborder="0" allowfullscreen></iframe>'''
    st.markdown(body, unsafe_allow_html=True)

column_config = {
    'Selected': st.column_config.CheckboxColumn(
        label="Select",
        help="Select your preferred rows",
        default=False
    )
}
        
def get_action_mountain_climb():
    #get file
    judgement_df = pd.read_excel('climbing_levels.xlsx', sheet_name='judgement')
    skill_df = pd.read_excel('climbing_levels.xlsx', sheet_name='skill')
    experience_df = pd.read_excel('climbing_levels.xlsx', sheet_name='experience')
    
    # add a column for checkbox
    skill_df['Selected'] = False
    
    # Apply text wrapping using Pandas Styler
    df_styled = experience_df.style.set_properties(**{'white-space': 'pre-wrap'})
    st.dataframe(df_styled, use_container_width=True)

    # Define the options
    options = list(judgement_df['體能狀況'].unique())

    # Create a selectbox for single selection
    selection = st.selectbox("選定不同體能狀況:", options)

    current_condition = judgement_df[judgement_df['體能狀況']==selection]
    st.dataframe(current_condition, use_container_width=True)

    level = current_condition['Level'].unique()[0]

    columns_to_show = ['Selected','項目','內容']

    st.write('應具備技能:')
    st.data_editor(skill_df[(skill_df['Required_level']<=level) & (skill_df['項目']=='技能')][columns_to_show], column_config=column_config, hide_index=True)

    st.write('視狀況攜帶物品:')
    st.data_editor(skill_df[(skill_df['Required_level']<=level) & (skill_df['項目']=='裝備')][columns_to_show], column_config=column_config, hide_index=True)
    
def get_list_to_check():
    list_sum = ['爬山','騎車','出遊物品','出國清單','天氣']

    # Create a selectbox for single selection
    selection = st.selectbox("情況:", list_sum)
    if selection=='爬山':
        get_action_mountain_climb()
    elif selection=='騎車':
        motor_check_list = {
            "Selected":False,
            "項目": ["胎壓", "油量", "煞車", "燈光", "鏈條", "鏡子", "儀表板", "車身"],
            "檢查內容": [
                "確保前後輪胎壓在建議範圍內，這有助於保持良好的操控性和減少磨損。",
                "檢查油箱中的油量是否足夠，避免在途中沒油。",
                "檢查前後煞車是否正常運作，煞車片是否磨損過度。",
                "檢查前後燈、方向燈和煞車燈是否正常工作，確保在夜間或低能見度條件下的安全。",
                "檢查鏈條的張力是否適中，並確保鏈條潤滑良好。",
                "確保後視鏡位置正確，並且沒有破損或鬆動。",
                "檢查儀表板上的指示燈是否正常，特別是油量、引擎和電池指示燈。",
                "檢查車身是否有明顯的損壞或鬆動的部件。"
            ]
        }

        # Create DataFrame
        df = pd.DataFrame(motor_check_list)
        df['Selected'] = False
        st.write('檢查清單:')
        st.data_editor(df, column_config=column_config, hide_index=True)
    elif selection=='出遊物品':
        outdoor_check_list = {
            "Selected":False,
            "項目": ["太陽眼鏡", "衛生紙", "防曬", "充電器", "牙刷", "水壺",],
        }

        # Create DataFrame
        df = pd.DataFrame(outdoor_check_list)
        st.write('檢查清單:')
        st.data_editor(df, column_config=column_config, hide_index=True)
    elif selection=='出國清單':
        travel_check_list = {
            "Selected": False,
            "項目": ["護照", "簽證", "機票", "住宿確認", "信用卡", "現金", "手機", "充電器", "衣物", "雨具", "藥品", "盥洗用品", "旅行保險", "轉接插頭", "行李鎖", "行程表", "景點門票",],
        }

        # Create DataFrame
        df = pd.DataFrame(travel_check_list)
        st.write('檢查清單:')
        st.data_editor(df, column_config=column_config, hide_index=True)
    elif selection=='天氣':
        weather_main()