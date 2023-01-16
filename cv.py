from pathlib import Path

import streamlit as st
from PIL import Image


# Path settings

directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = directory / 'styles' / 'main.css'
pdf_file = directory / 'assets' / 'VerttiLeppikangas_cv.pdf'
profile_pic = directory / 'assets' / 'cv_profile_pic.png'




# CV settings

cv_title = 'Digital CV - Vertti Leppikangas'
cv_icon = 'wave'
name = 'Vertti Leppikangas'
descript = 'Young student from Finland, currently serving in the finnish navy as a military police.'
email = 'verttileppikangas@gmail.com'
phone_number = '+358 0404692678'
adress = 'Tähkäpää 7, 04500 Kellokoski'
github_link = {'Github': 'https://github.com/VerttiMikael'}



st.set_page_config(page_title=cv_title, page_icon=cv_icon)



# loading css, pdf & pfp


with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(pdf_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# Intro section and contact information

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=260)

with col2:
    st.title(name)
    st.write(descript)
    st.write('📧', email)
    st.write('📞', phone_number)
    st.write('📫', adress)
    st.download_button(
        label = " 📄 Download finnish pdf-version",
        data = PDFbyte,
        file_name = 'VerttiLeppikangas_cv.pdf',
        mime = "application/octet-stream",
    )
      


# Experience 

st.write('---')
st.write('#')
st.subheader('Coding Experience')
st.write(
    '''
- Started 6 months ago studying python independently using few courses that are:
    - >Basics of programming 2022 by University of Helsinki (MOOC)
    - >Python crash course  by Eric Matthes

- Before that participated in a videogame programming course in high school (C#)

- Continuously growing in knowledge of programming and having a burning passion about learning more '''
)


# Education & work history 

# job 1
st.write('#')
st.subheader('Education & Work History')
st.write(
    '''
2019-2022
- Graduated from Tuusula High School in 2022
    - >Tutored during my 2nd year
    - >Student council secretary
'''
)

# job 2
st.write('\n')
st.write(
    '''
3/2022 - 6/2022
- Substitute teacher in the School Of Kellokoski  
    - >Taught in primary school, middle school and high school
 '''
)

# job 3
st.write('\n')
st.write(
    '''
4/2022 - 5/2022
- Security guard 
    - >Patrolled various structures and important warehouses
    - >Ended early because of entrance exams for the uni'''
)

# About me and skills

st.write('#')
st.write('---')
st.subheader('About Me & Skills')
st.write(
    '''
- 19-year-old boy from Kellokoski, Finland. I'm a social person and I bring a good atmosphere with me, thanks to which I also get along with everyone. In addition, I can interpret things seriously and take responsibility. As an employee, my strengths are sheer determination about getting to my goal and the desire to build my skills.

- I have a vast experience working with groups. That experience comes from high school and now the military where I just got promoted to corporal
    - >In both of these I've been part of responsible positions whether it was a tutor or a squad leader 
    '''
)


# My Future and skills


st.write('#')

col3, col4 = st.columns(2, gap='small')
with col3:
    st.subheader('Future Plans')
    st.write(
        '''
    - At the moment I'm still serving in the navy, but my service ends in March so I can start focusing on my career.
    - My plan is to build a future in the programming world. I have a spot in Tampere University for information technology, but before going there, I might collect some real world experience from the industry.
      '''
    )

with col4:
    st.subheader('Other IT-Skills')
    st.write(
        ''' 
    - ▪ Adobe Photoshop
    - ▪ Adobe After Effects
    - ▪ Office 365-apps'''
    )

st.write('---')

# Info about the cv

st.write('*')
st.write('> This CV was made entirely in python. For full sourcecode, click on the github button below')
cols = st.columns(len(github_link))
for index, (platform, link) in enumerate(github_link.items()):
    cols[index].write(f'>[{platform}]({link})')