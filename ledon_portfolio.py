import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

st.set_page_config(
    page_title="Ledon Portfolio",
    page_icon="📂",
)

st.markdown(
    """
    <style>
        /* Main content container */
        .block-container {
            max-width: 60%;
            margin: 0 auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)


options = option_menu(
    menu_title = None,
    options=['About Me', 'Hobbies & Interest', 'Projects'],
    icons=['person-vcard-fill', 'lightbulb-fill', 'palette-fill'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        "nav-link-selected": {"background-color" : "#ff3131"}
    }
)



if options == 'About Me':
    st.markdown('<h2 style="text-align:center;">About Me 💬</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2]) 
    img = Image.open("media/dummypfp.jpg")
    with col1:
        st.image(img, use_container_width=True, caption="CATNIP 2017, EP")

    with col2:
        st.markdown("""
        <div style="margin-left:20px; line-height:1.5; font-size:1.050rem;">
            <span style="font-size: 1.5rem;">Hi, I'm <strong>Jhon Ryan D. Ledon</strong>👋</span><br> I'm an accidental Computer Science student who is somehow still surviving the chaos of deadlines, debugging, and whatever “automata theory” is trying to do to my sanity.
            I’ve always wanted to become an architect. I grew up sketching buildings, structures, and portraits, and in fact, I took up Technical Drafting way back in high school. But life had other plans, and now I am typing Python instead of designing houses.
            Even with the shift, I am still drawn to creative work. I enjoy building things, whether it is applications, art, or routines that only make sense after midnight, which is my peak productivity time.
            Right now, I am balancing coding, fitness, drawing, and figuring out who I want to be at 25. It is a work in progress, but that is the fun part.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center;">Tech Stack 👾</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-bottom:10px">
        <img src="https://skillicons.dev/icons?i=c,cpp,cs,java,kotlin,python,js,html,css,react">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align:center;">
            <img src="https://skillicons.dev/icons?i=django,spring,net,tailwind,github,figma">
            <img src="https://skills.syvixor.com/api/icons?perline=15&i=streamlit,pytest,numpy">
        </div>
                
        """, unsafe_allow_html=True)
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center;">Connect with Me 🤝</h2>', unsafe_allow_html=True)

    st.markdown("""
    <ul style="list-style:none; text-align:center; padding:0;">
        <li style="display:inline-block; margin:0 2px;">
            <a href="https://mail.google.com/mail/?tf=cm&to=<jhonryan.ledon05@gmail.com>" target="_blank">
                <img src="https://skills.syvixor.com/api/icons?perline=15&i=gmail">
            </a>
        </li>
        <li style="display:inline-block; margin:0 2px;">
            <a href="https://github.com/Joryuoo" target="_blank">
                <img src="https://skills.syvixor.com/api/icons?perline=15&i=github">
            </a>
        </li>
        <li style="display:inline-block; margin:0 2px;">
            <a href="https://ph.linkedin.com/in/ledonjhonryan" target="_blank">
                <img src="https://skills.syvixor.com/api/icons?perline=15&i=linkedin">
            </a>
        </li>
        <li style="display:inline-block; margin:0 2px;">
            <a href="https://www.instagram.com/joryuoo/" target="_blank">
                <img src="https://skills.syvixor.com/api/icons?perline=15&i=instagram">
            </a>
        </li>
    </ul>
    """, unsafe_allow_html=True)




if options == 'Hobbies & Interest':
    st.markdown('<h2>Who I Am Beyond Coding 🌟</h2>', unsafe_allow_html=True)
    st.write('I can draw realistic portraits — like, actual pencil shading, not Canva edits.')
    st.video("media/art_vid.mp4")

    art_img1 = Image.open("media/seulgi1.jpg")
    art_img2 = Image.open("media/seulgi2.jpg")
    art_img3 = Image.open("media/hanni.jpg")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(art_img1, use_container_width=True, caption="Seulgi")

    with col2:
        st.image(art_img2, use_container_width=True, caption="Still Seulgi")

    with col3:
        st.image(art_img3, use_container_width=True, caption="Hanni")

    st.write('I can also do a little bit of digital art')

    art_img4 = Image.open("media/karina1.jpg")
    art_img5 = Image.open("media/karina2.jpg")
    art_img6 = Image.open("media/karina3.jpg")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(art_img4, use_container_width=True, caption="Karina 1")

    with col5:
        st.image(art_img5, use_container_width=True, caption="Karina 2")

    with col6:
        st.image(art_img6, use_container_width=True, caption="Karina 3")

    st.write('I’m a determined go-getter — the same drive that helped me drop 20 kg and got me deep into calisthenics and weightlifting.')

    self_img1 = Image.open("media/lol1.jpg")
    self_img2 = Image.open("media/lol2.jpg")

    col7, col8 = st.columns(2)
    with col7:
        st.image(self_img1, use_container_width=True, caption="lol")

    with col8: 
        st.image(self_img2, use_container_width=True, caption="lol")


    st.write('An academic achiever, and I’m friends with highly intelligent people who keep me motivated and pushing forward.')
    group_pic = Image.open('media/group_pic.jpg')
    st.image(group_pic, use_container_width=True)
    st.markdown('<h2>Some of my passions include:</h2>', unsafe_allow_html=True)
    st.write('🛠️ Building apps & experimenting with small projects',
             '\n\n💻 Exploring technology, UI/UX, and front-end design', 
             '\n\n📊 Learning data science and machine learning',
             '\n\n🎯 Learning random skills I didn’t plan on but end up enjoying',
             '\n\n🎨 Music, photography, and anything that sparks creativity'
             )

        
    

if options == 'Projects':
    st.markdown('<h2>Projects 🚀</h2>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:1.75rem; font-weight:600">Note It</span>', unsafe_allow_html=True)
    st.markdown(
        '<span style="font-size:1rem;"><strong>NoteIt</strong> is an Android application designed for users to capture, organize, and manage their thoughts, ideas, '
        'and tasks efficiently directly on their device. It provides integrated functionalities for note-taking and task management. ' \
        'The app supports multiple user accounts, with each user\'s data kept separate and stored locally. It offers a reliable, offline-first experience for users to keep track of important information and to-dos.'
        '</span>', unsafe_allow_html=True)
    
    
    img1 = Image.open('media/1.jpg')
    img2 = Image.open('media/2.jpg')
    img3 = Image.open('media/3.jpg')
    img4 = Image.open('media/4.jpg')
    img5 = Image.open('media/5.jpg')

    cl1, cl2, cl3, cl4, cl5 = st.columns(5)

    with cl1:
        st.image(img1, use_container_width=True) 
    with cl2:
        st.image(img2, use_container_width=True)    
    with cl3:
        st.image(img3, use_container_width=True)
    with cl4:
        st.image(img4, use_container_width=True)
    with cl5:
        st.image(img5, use_container_width=True)        

    st.write(
        """
        <div style="display:flex; align-items:center; gap:10px;">
            <p style="margin:0; font-size:1.2rem; font-weight:bold;">Built With:</p>
            <img src="https://skills.syvixor.com/api/icons?perline=15&i=kotlin,xml" style="height:40px;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:1.75rem; font-weight:600">What Remains</span>', unsafe_allow_html=True)
    st.markdown(
        '<span style="font-size:1rem;">'
        'This mystery visual novel follows a detective uncovering the truth behind his friend’s murder. ' \
        'The game blends emotional storytelling with detail-focused investigation, allowing players to explore themes of grief, memory, and loyalty. ' \
        'It features multiple save options, cloud syncing, dialogue history, fast-forward/skip functions, and an auto-play mode for a smooth and flexible narrative experience.'
        '</span>', unsafe_allow_html=True)

    img6 = Image.open('media/6.png')
    st.image(img6, use_container_width=True)

    st.write(
        """
        <div style="display:flex; align-items:center; gap:10px;">
            <p style="margin:0; font-size:1.2rem; font-weight:bold;">Built With:</p>
            <img src="https://skills.syvixor.com/api/icons?perline=15&i=java,mysql" style="height:40px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<h2>Under Development 🛠️</h2>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:1.75rem; font-weight:600">NavCIT: WildMaps</span>', unsafe_allow_html=True)
    st.markdown(
        '<span style="font-size:1rem;">'
        'The Interactive CIT-University Map is a web-based application designed to enhance campus navigation '
        'by providing detailed information on buildings and hotspots through map pins that, when clicked, display location details, '
        'user comment options, and the path leading to the destination. Integrated with a chatbot-like AI, '
        'the system can answer frequently asked questions, provide directions, and offer real-time guidance, ' 
        'ensuring that newcomers such as students, parents, and guests enjoy a smooth, stress-free campus experience.'
        '</span>', unsafe_allow_html=True)

    img7 = Image.open('media/7.png')
    img8 = Image.open('media/8.png')
    img9 = Image.open('media/9.png')

    cl7, cl8, cl9 = st.columns(3)

    with cl7:
        st.image(img7, use_container_width=True) 
    with cl8:
        st.image(img8, use_container_width=True)    
    with cl9:
        st.image(img9, use_container_width=True)

    st.write(
        """
        <div style="display:flex; align-items:center; gap:10px;">
            <p style="margin:0; font-size:1.2rem; font-weight:bold;">Built With:</p>
            <img src="https://skills.syvixor.com/api/icons?perline=15&i=javafx,java,spring,supabase,html,css,javascript,reactjs,postman" style="height:40px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:1.75rem; font-weight:600">Dunzo</span>', unsafe_allow_html=True)
    st.markdown(
        '<span style="font-size:1rem;">'
        '<strong>Dunzo</strong> is a web application designed for students to assign, track, and complete group project tasks efficiently. '
        'It provides integrated functionalities for task management, progress tracking, and team collaboration. ' 
        'The app supports clear task delegation with deadlines, real-time status updates for leader oversight, smart reminders to keep members on track, and built-in comments for transparent feedback.'
        ' It offers a centralized, reliable experience for student groups to manage accountability and streamline project completion all in one place.'
        '</span>', unsafe_allow_html=True)
    
    img10 = Image.open('media/10.png')
    img11 = Image.open('media/11.png')
    img12 = Image.open('media/12.png')

    cl10, cl11, cl12 = st.columns(3)

    with cl10:
        st.image(img10, use_container_width=True) 
    with cl11:
        st.image(img11, use_container_width=True)    
    with cl12:
        st.image(img12, use_container_width=True)


    st.write(
        """
        <div style="display:flex; align-items:center; gap:10px;">
            <p style="margin:0; font-size:1.2rem; font-weight:bold;">Built With:</p>
            <img src="https://skills.syvixor.com/api/icons?perline=15&i=python,django,html,css,javascript,reactjs" style="height:40px;">
        </div>
        """,
        unsafe_allow_html=True)
    
    
