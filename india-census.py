import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('final_df.csv')
df['Buddhists'] = df['Buddhists'].astype(int)
# df['District'] = pd.to_numeric(df['District'], errors='coerce')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')
x = df.groupby('State')[
    ['Population', 'Male', 'Female', 'Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains',
     'Male_Literate', 'Female_Literate']].sum().sort_values(by='Population', ascending=False).reset_index()
decimals = 2
x['Male Percentage'] = (x['Male'] * 100) / x['Population']

x['Male Percentage'] = x['Male Percentage'].apply(lambda x: round(x, decimals))

x['Female Percentage'] = (x['Female'] * 100) / x['Population']

x['Female Percentage'] = x['Female Percentage'].apply(lambda x: round(x, decimals))

x['Hindus Percentage'] = (x['Hindus'] * 100) / x['Population']

x['Hindus Percentage'] = x['Hindus Percentage'].apply(lambda x: round(x, decimals))

x['Muslims Percentage'] = (x['Muslims'] * 100) / x['Population']

x['Muslims Percentage'] = x['Muslims Percentage'].apply(lambda x: round(x, decimals))

x['Christians Percentage'] = (x['Christians'] * 100) / x['Population']

x['Christians Percentage'] = x['Christians Percentage'].apply(lambda x: round(x, decimals))

x['Jains Percentage'] = (x['Jains'] * 100) / x['Population']

x['Jains Percentage'] = x['Jains Percentage'].apply(lambda x: round(x, decimals))

x['Sikhs Percentage'] = (x['Sikhs'] * 100) / x['Population']
x['Sikhs Percentage'] = x['Sikhs Percentage'].apply(lambda x: round(x, decimals))

x['Buddhists Percentage'] = (x['Buddhists'] * 100) / x['Population']
x['Buddhists Percentage'] = x['Buddhists Percentage'].apply(lambda x: round(x, decimals))

x.drop(
    columns=['Hindus', 'Buddhists', 'Muslims', 'Christians', 'Male_Literate', 'Female_Literate', 'Male', 'Female',
             'Jains', 'Sikhs'],
    inplace=True)

st.sidebar.title('India Census')

selected_state = st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[:56]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[:56]))

plot = st.sidebar.button('Plot Graph')
if plot:

    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
st.sidebar.title("Summary of India")
overall_analysis = st.sidebar.button('Summary of India')
if overall_analysis:
    st.dataframe(x)

