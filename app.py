import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="John Joseph Laborada | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = current_dir / "assets"

PROFILE = {
    "name": "JOHN JOSEPH LABORADA",
    "role": "IT Student | Aspiring Web Developer | UI/UX",
    "location": "Carcar City, Cebu, Philippines",
    "about_short": (
        "I build practical systems that solve real problems—from online ticketing platforms to admin dashboards. "
        "I specialize in turning requirements into working applications using modern web technologies, "
        "and I'm actively seeking a remote IT internship where I can contribute, learn, and deliver results."
    ),
    "links": {
        "GitHub": "https://github.com/moshiverse",
        "LinkedIn": "https://linkedin.com/in/johnjoseph-laborada-8b341430a",
        "Email": "mailto:laboradajohnji@gmail.com",
    },
}

ABOUT_ME_TEXT = """
I am John Joseph Laborada, 24 years of age and currently pursuing a degree in Information Technology, where I developed a strong interest 
in software development and solving problems through technology. My journey in tech started with 
curiosity about how applications and systems work, and over time, that curiosity turned into a 
passion for building them myself. Through various school projects and activities, I gained 
experience in programming, web development, and working with classmates as a team to complete 
systems and meet deadlines.
<br><br>
I am always open to learning new tools and technologies that can improve my skills as a 
developer. I enjoy taking on challenges because they help me grow and think more critically. 
Outside of coding, I like playing chess, watching movies and anime, and working on small side 
projects that allow me to practice and explore new ideas in programming.
"""

SKILLS_DATA = {
    "Programming / Web": ["ReactJS", "Spring Boot", "Java", "C", "C++", "Python", "HTML/CSS"],
    "UI/UX / Design": ["Figma", "Canva", "UI/UX Optimization", "UI Wireframes", "Wordpress"],
    "Databases & Tools": ["MySQL", "PostgreSQL", "Git", "GitHub", "VS Code"],
    "Other Skills": ["Problem Solving", "Team Collaboration", "Communication", "Time management", "Adaptability"],
}

PROJECTS = [
    {
        "name": "BusMate",
        "type": "Bus Ticketing System",
        "desc": "A modern intercity bus ticketing system designed to make travel booking faster, safer, and more convenient.",
        "tags": ["JavaScript", "Java", "CSS", "Kotlin"],
        "img": "busmate.png",
        "links": {
            "GitHub": "https://github.com/moshiverse/BusMate-OnlineTicketingSystem-IT342-G01-Group6"
        },
    },
    {
        "name": "SPMP Evaluator",
        "type": "Academic Tool",
        "desc": "An automated evaluation platform that provides feedback, scoring, and task management capabilities for student projects.",
        "tags": ["JavaScript", "Java", "CSS"],
        "img": "spmp.png",
        "links": {
            "GitHub": "https://github.com/lawas-tess/SPMP-Evaluator"
        },
    },
    {
        "name": "CardWise",
        "type": "Study Aid",
        "desc": "Solves study issues by providing a digital platform where students can easily create, categorize, and review flashcards.",
        "tags": ["JavaScript", "Java", "CSS"],
        "img": "cardwise.png",
        "links": {
            "GitHub": "https://github.com/myNameIsJoshua1/CardWise"
        },
    },
]

EDUCATION = [
    {
        "degree": "BS Information Technology",
        "school": "Cebu Institute of Technology - University",
        "year": "2022 – Present",
        "sub": "Expected Graduation: May 2026",
        "desc": "Relevant Coursework: Web Development, Data Management, UI/UX Design",
    },
    {
        "degree": "AWS Academy Graduate",
        "school": "Cloud Foundations & Architecting",
        "year": "2025",
        "sub": "Amazon Web Services",
        "desc": "Comprehensive training in cloud security, architecture, and core AWS services.",
    },
]

st.markdown(
    """
    <style>
        .stApp { 
            background-color: #0A0A0F;
            color: #e0e0e0;
        }
        
        header[data-testid="stHeader"] {
            z-index: 1001 !important;
            background-color: #0b0c10; 
        }
        
        .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1002;
        padding: 26px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        pointer-events: none;
        background: transparent;
        }

        .navbar::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(11, 12, 16, 0.95);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(168, 85, 247, 0.2);
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        z-index: -1;
        pointer-events: none;
        }
        
        .brand-name,
        .navbar-links,
        .navbar a {
            pointer-events: auto;
        }

        .navbar-links { 
            display: flex; 
            gap: 30px; 
        }
        
        .navbar a {
            color: #b0b0b0; 
            text-decoration: none; 
            font-size: 0.9rem; 
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
        }
        
        .navbar a:hover { 
            color: #d8b4fe;
            text-shadow: 0 0 8px rgba(168, 85, 247, 0.6);
        }

        .brand-name {
            font-weight: 900; 
            font-size: 1.2rem;
            background: linear-gradient(90deg, #d8b4fe, #a855f7);
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            letter-spacing: 1px;
        }
        
        .anchor-offset { 
            position: relative;
            top: -200px;
            height: 0;
            pointer-events: none; 
        }
        
        div[data-testid="stVerticalBlockBorderWrapper"] {
            padding: 24px 28px !important;
        }
        
        .justified-text {
            text-align: justify;
            line-height: 1.7;
            font-size: 1rem;
            color: #d1d5db;
            padding: 6px 2px;
        }

        .skill-pill {
            display: inline-block;
            background: rgba(168, 85, 247, 0.15);
            border: 1px solid rgba(168, 85, 247, 0.3);
            color: #e9d5ff;
            padding: 6px 16px;
            border-radius: 99px;
            font-size: 0.85rem;
            margin: 5px;
            font-weight: 500;
            transition: all 0.2s;
        }
        
        .skill-pill:hover {
            background: rgba(168, 85, 247, 0.3);
            transform: translateY(-2px);
        }
        
        .skill-container {
            background-color: rgba(255,255,255,0.03);
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(255,255,255,0.08);
        }
        
        .section-header {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 15px;
            color: #f3f4f6;
            text-shadow: 0 0 20px rgba(168, 85, 247, 0.15);
        }

        .equal-height-container {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .info-box {
            background-color: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 30px;
            color: #e5e7eb;
            display: flex;
            flex-direction: column;
        }
        
        .box-wide { flex: 2; }
        .box-narrow { flex: 1; }
        
        @media (max-width: 768px) {
            .navbar-links { display: none; }
            .equal-height-container { flex-direction: column; }
        }
    </style>
    
    <div class="navbar">
        <div class="brand-name">PORTFOLIO</div>
        <div class="navbar-links">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#education">Education</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

def load_pdf_bytes(pdf_name: str) -> bytes | None:
    pdf_path = ASSETS_DIR / pdf_name
    if pdf_path.exists():
        return pdf_path.read_bytes()
    return None

def load_image(image_name):
    image_path = ASSETS_DIR / image_name
    if image_path.exists():
        return str(image_path)
    return None

st.markdown('<div id="home" class="anchor-offset"></div>', unsafe_allow_html=True)

c1, c2 = st.columns([2.5, 1], gap="medium")

with c1:
    st.markdown("<div style='font-size: 3.5rem; font-weight: 800; line-height: 1.1;'>Hello, I'm Joseph</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #a855f7; margin-bottom: 20px;'>{PROFILE['role']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='justified-text'>{PROFILE['about_short']}</div>", unsafe_allow_html=True)

    st.write("")
    cols = st.columns(4, gap="small")
    with cols[0]:
        st.link_button("GitHub", PROFILE["links"]["GitHub"], use_container_width=True)
    with cols[1]:
        st.link_button("LinkedIn", PROFILE["links"]["LinkedIn"], use_container_width=True)
    with cols[2]:
        st.link_button("Email", PROFILE["links"]["Email"], use_container_width=True)
    with cols[3]:
        cv_bytes = load_pdf_bytes("CV.pdf")
        if cv_bytes:
            st.download_button(
                "Download CV",
                data=cv_bytes,
                file_name="John_Joseph_Laborada_CV.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        else:
            st.button("CV (missing)", disabled=True, use_container_width=True)

    

with c2:
    avatar_path = load_image("avatar.jpg")
    if avatar_path:
        st.markdown(
            """
            <div style="display:flex; justify-content:flex-end; margin-top:40px;">
            """,
            unsafe_allow_html=True
        )
        st.image(avatar_path, width=250)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Place 'avatar.jpg' in assets folder")


st.markdown("---")

st.markdown('<div id="about" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>About Me</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="equal-height-container">
        <div class="info-box box-wide">
            <div class="justified-text">{ABOUT_ME_TEXT}</div>
        </div>
        <div class="info-box box-narrow">
            <h3 style="margin-top: 0; color: #a855f7;">Details</h3>
            <p><strong>Location:</strong><br>{PROFILE['location']}</p>
            <div style="flex-grow:1;"></div>
            <p><strong>Status:</strong><br>Intern at Knowles Training Institute</p>
            <div style="flex-grow:1;"></div>
            <p><strong>Interests:</strong><br>Chess, Anime, Coding</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.markdown("<div class='section-header'>My BSIT Journey</div>", unsafe_allow_html=True)

row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)
with row1_col1:
    with st.container(border=True):
        st.metric("Experience", "3 Years", "Coding")
with row1_col2:
    with st.container(border=True):
        st.metric("Education", "4th Year", "Cebu Institute of Technology - University")
with row1_col3:
    with st.container(border=True):
        st.metric("Status", "Intern", "Knowles Training Institute")
with row1_col4:
    with st.container(border=True):
        st.metric("Projects", "10+", "Completed/Ongoing")

st.write("")
grid_c1, grid_c2 = st.columns(2, gap="medium")

with grid_c1:
    with st.container(border=True):
        st.markdown("#### The Beginning")
        st.markdown(
            """
            <div class="justified-text">
            When I first entered Cebu Institute of Technology - University as a BSIT student, I was unsure 
            which area of technology I would eventually pursue. I only knew that I was curious about how 
            applications worked behind the scenes. During my first year, I found programming challenging, 
            especially when debugging errors that I did not fully understand. There were moments when projects 
            felt overwhelming, but instead of giving up, I treated every mistake as part of the learning process.
            <br><br>
            Over time, those struggles became stepping stones. Through lectures, projects, and hands-on activities, 
            I gradually improved my problem-solving skills and gained confidence in building applications. I began to 
            appreciate not just writing code, but understanding how software is designed, structured, and improved over time.
            </div>
            """,
            unsafe_allow_html=True
        )

with grid_c2:
    with st.container(border=True):
        st.markdown("#### Discovering My Strengths")
        st.markdown(
            """
            <div class="justified-text">
            As I progressed through my degree, I started exploring different areas of development and discovered a growing interest 
            in full-stack systems. I enjoyed seeing how the frontend and backend connect to create a complete and functional application. 
            Working with technologies such as Java, ReactJS, PostgreSQL, and Figma helped me understand how ideas are transformed into real 
            systems.
            <br><br>
            Each project taught me something new, whether it was designing user interfaces, structuring databases, or solving unexpected technical 
            issues. More than just learning tools, I learned how to think critically, adapt to challenges, and continuously improve my work.
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
with st.container(border=True):
    st.markdown("#### Looking Ahead")
    st.markdown(
        """
        As I approach graduation, I reflect on how much I have grown, not only as a student, but as a future professional in the technology field. 
        What started as curiosity has turned into a clear direction and purpose. I aim to continue developing my skills in software and full-stack 
        development while gaining real-world experience that will challenge me further.
        <br><br>
        My goal is not only to build systems, but to build solutions that are useful, reliable, and meaningful. I look forward to the next chapter of 
        my journey, where I can continue learning, contributing, and evolving as a developer.
        """,
        unsafe_allow_html=True
    )

st.markdown('<div id="skills" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Skills & Technologies</div>", unsafe_allow_html=True)

tabs = st.tabs(list(SKILLS_DATA.keys()))
for i, (category, skills) in enumerate(SKILLS_DATA.items()):
    with tabs[i]:
        pills_html = "".join([f"<span class='skill-pill'>{skill}</span>" for skill in skills])
        st.markdown(
            f"""
            <div class="skill-container">
                <h4 style="margin-bottom: 15px; color: #d8b4fe;">{category}</h4>
                <div>{pills_html}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown('<div id="projects" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Featured Projects</div>", unsafe_allow_html=True)

search = st.text_input("Search projects", "")
tag_options = sorted({t for p in PROJECTS for t in p["tags"]})
selected_tags = st.multiselect("Filter", tag_options)

filtered_projects = []
for p in PROJECTS:
    text = f"{p['name']} {p['type']} {p['desc']}".lower()
    matches_search = search.lower() in text if search else True
    matches_tags = any(t in selected_tags for t in p["tags"]) if selected_tags else True
    if matches_search and matches_tags:
        filtered_projects.append(p)

st.caption(f"Currently showing {len(filtered_projects)} project(s) for now")

p_cols = st.columns(3, gap="medium")
for i, project in enumerate(filtered_projects):
    with p_cols[i % 3]:
        with st.container(border=True):
            img_path = load_image(project["img"])
            if img_path:
                st.image(img_path, use_container_width=True)

            st.subheader(project["name"])
            st.caption(project["type"])
            st.write(project["desc"])
            st.markdown(" ".join([f"`{t}`" for t in project["tags"]]))

            st.write("")
            for label, url in project.get("links", {}).items():
                st.link_button(label, url, use_container_width=True)

st.markdown("---")
st.markdown('<div id="education" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Education & Certifications</div>", unsafe_allow_html=True)

for edu in EDUCATION:
    with st.container(border=True):
        c_edu1, c_edu2 = st.columns([3, 1])
        with c_edu1:
            st.markdown(f"### {edu['degree']}")
            st.markdown(f"**{edu['school']}**")
            st.caption(edu.get("sub", ""))
            st.write(edu["desc"])
        with c_edu2:
            st.markdown(f"<h4 style='text-align:right; color:#a855f7'>{edu['year']}</h4>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #333; color: #666;">
        <p>© 2026 John Joseph Laborada · Built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
