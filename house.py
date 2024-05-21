from streamlit.components.v1 import html
import streamlit as st
import pandas as pd
    
def show_tableau():
    body = """
            <div class='tableauPlaceholder' id='viz1691080442321' style='width: 800px; height: 1000px;'> 
                <noscript>
                    <a href='#'>
                    <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ho&#47;house_trend&#47;overall_trend&#47;1_rss.png' style='border: none' />
                    </a>
                </noscript>
                <object class='tableauViz'  width='800' height='1000' style='display:none;'>
                    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                    <param name='embed_code_version' value='3' /> 
                    <param name='site_root' value='' />
                    <param name='name' value='house_trend&#47;overall_trend' />
                    <param name='tabs' value='no' />
                    <param name='toolbar' value='yes' />
                    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ho&#47;house_trend&#47;overall_trend&#47;1.png' /> 
                    <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
                    <param name='display_spinner' value='yes' />
                    <param name='display_overlay' value='yes' />
                    <param name='display_count' value='yes' />
                    <param name='language' value='zh-TW' />
                </object>
            </div>                
            <script type='text/javascript'>                    
                var divElement = document.getElementById('viz1691080442321');                    
                var vizElement = divElement.getElementsByTagName('object')[0];                    
                vizElement.style.width='100%';
                vizElement.style.height='100%';                   
                var scriptElement = document.createElement('script');                    
                scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                   
                vizElement.parentNode.insertBefore(scriptElement, vizElement);                
            </script>"""
    html(body)
    st.markdown('''<p><a href="https://public.tableau.com/views/house_trend/overall_trend?:language=zh-TW&:display_count=n&:origin=viz_share_link">
                House Trending Tableau form</a></p>''', unsafe_allow_html=True)

def get_2023_raw_data()->pd.DataFrame:
    house_data = pd.read_csv('house.csv')
    house_data_2023 = house_data[house_data['trade_date']>='2023']
    return house_data_2023

def get_linear_regression_result():
    house_data_2023 = get_2023_raw_data()
    x_column = [ '廳數', '房', '衛','建物面積']
    X = house_data_2023[x_column]
    from sklearn.linear_model import LinearRegression
    y = house_data_2023['總價元']/1000000
    
    from sklearn.model_selection import train_test_split

    # Assuming X and Y are your features and target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    #normalize data
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Assuming you have test data X_test and y_test
    y_pred = model.predict(X_test)
    eval = get_evaluation_data(y_test, y_pred)
    st.write('Linear Regression on 2023 House data evaluation:')
    for key, value in eval.items():
        st.write(f"{key}: {value:.2f}")
    
    get_predict_plot(y_test, y_pred)

def get_predict_plot(test, pred):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.scatter(test, pred, color='red')
    plt.plot(range(int(max(test))), range(int(max(test))), 'o')
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('True vs. Predicted Values')
    plt.show()
    st.pyplot(fig)

def get_evaluation_data(test, pred)->dict:
    from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    import numpy as np
    mse = mean_squared_error(test, pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(test, pred)
    mae = mean_absolute_error(test, pred)
    return {'MSE':mse, 'RMSE':rmse, 'R²':r2, 'MAE':mae}
    
    
def house_main():
    show_tableau()
    get_linear_regression_result()