import streamlit as st
import yaml
from datetime import datetime

st.set_page_config(page_title='Query builder', page_icon='🔍')

st.title("Query Builder")

st.subheader("Time range:")
start_date = st.date_input("Start Date", value=datetime(2020, 1, 1), min_value=None)
end_date = st.date_input("End Date", value=datetime.now(), min_value=None)

topics = None
countries = None
keywords = None

with st.sidebar:
    st.subheader("Optional Variables:")
    st.write("These are optional; if you don't include them, your query will default to grabbing all the options.")
    topic_sel = st.checkbox('Topic')
    country_sel = st.checkbox('Country')
    keyword_sel = st.checkbox('Keywords')

if topic_sel:
    st.markdown("***")
    st.subheader("Topic Selection:")
    topics = st.multiselect(
        'Choose your topics:',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

if country_sel:
    st.markdown("***")
    st.subheader("Country Selection:")
    selmethod = st.radio(
        "How do you want to define your countryset?",
        ('Lookup Table', 'Individual Countries'))

    if selmethod=='Lookup Table':
        countries = st.multiselect(
            'Select your group',
            ['Group1', 'Group2', 'Group3', 'Group4'],
            ['Group1', 'Group2'])
    elif selmethod=='Individual Countries':
        countries = st.multiselect(
            'Choose your countries:',
            ['Country1', 'Country2', 'Country3'], ['Country1'])

if keyword_sel:
    st.markdown("***")
    st.subheader('Keyword Selection')
    keywords = st.text_area("Enter your keywords; if you have more than one put them on separate lines", value="").split("\n")
    # print(keywords)
    if keywords == ['']:
        keywords = None
query_dict = {'start-date': start_date,
            'end-date': end_date,
            'topics': topics,
            'countries': countries,
            'keywords':keywords}

st.markdown("***")
go_button = st.button("Save query")

if go_button:
    with open('query.yaml', 'w') as file:
        dump = yaml.dump(query_dict, file)
        print(f"\n{datetime.now()} \nJust wrote:")
        print(yaml.dump(query_dict))
    # st.write("Query saved - Go run the pipeline!")
    st.success('This is a success message!')
    # print(query_dict)