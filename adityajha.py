import streamlit as st
st.title('Latentview  Analytics App')


st.subheader('Bootcamp - B3')

text_area = st.text_area('Enter some name here')


options = ['Data Quality Issues', 'Lack of Relevant Insights', 'Lack of Data', 'Lack of Data Science Skills', 'Lack of Data Engineering Skills', 'Lack of Data Visualization Skills', 'Lack of Data Governance', 'Lack of Data Security', 'Lack of Data Strategy', 'Lack of Data Literacy', 'Lack of Data Culture', 'Lack of Data Infrastructure', 'Lack of Data Tools', 'Lack of Data Science Tools', 'Lack of Data Engineering Tools', 'Lack of Data Visualization Tools', 'Lack of Data Governance Tools', 'Lack of Data Security Tools', 'Lack of Data Strategy Tools', 'Lack of Data Literacy Tools', 'Lack of Data Culture Tools', 'Lack of Data Infrastructure Tools', 'Lack of Data Science Skills', 'Lack of Data Engineering Skills', 'Lack of Data Visualization Skills', 'Lack of Data Governance Skills', 'Lack of Data Security Skills', 'Lack of Data Strategy Skills', 'Lack of Data Literacy Skills', 'Lack of Data Culture Skills', 'Lack of Data Infrastructure Skills']
dropdown = st.selectbox('Choose an option:', options)

options2 = ['APAC', 'Europe', 'TechCally', 'Tech-NorthWest', 'Consumer', 'Retail', 'Data Science','Data Services']
dropdown2 = st.selectbox('Choose an option:', options2)



if st.button('Submit'):
    st.write(f' {text_area} is placed in {dropdown2} and has {dropdown}')


if st.button('Clear'):
    st.experimental_rerun()

st.image("https://www.teleinfotoday.com/wp-content/uploads/Banking&Retail/lakeview-9996.jpeg",width = 200)
