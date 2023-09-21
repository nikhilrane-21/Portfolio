import streamlit as st
import webbrowser

st.set_page_config(page_title="Sixthsens AI Portfolio", page_icon="🤖", layout="wide")
hide_streamlit_style = """
            <style>
            .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
            .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
            .viewerBadge_text__1JaDK {display: none;}
            MainMenu {visibility: hidden;}
            header { visibility: hidden; }
            footer {visibility: hidden;}
            #GithubIcon {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    st.title("SixthSens AI Video Analytics Solutions")
    st.write("---")
    projects = {
        "Safety Gears Detection": {
            "description": "This project involves the detection of safety gears such as helmets and hard hats. It's crucial in ensuring the safety of individuals in hazardous work environments.",
            "live_link": "https://sixthsens-safety-gears-detection.streamlit.app/",
            "video_demo_link": "https://drive.google.com/file/d/112aQVwXRAMlRpZOToMm0vBn0aVQGq1rp/view?usp=drive_link"
        },
        "People Monitoring": {
            "description": "This project counts and monitors the number of people entering and exiting a premises. It also alerts when a certain number of people exceeds in a certain area.",
            "live_link": "https://people-monitoring.streamlit.app/",
            "video_demo_link": "https://drive.google.com/file/d/1mltbxjUMPwK7_JXkxsI00Y65x0mBTYi2/view?usp=drive_link"
        },
        "Abandoned Object Detection": {
            "description": "This project detects objects that are left unattended or obstructing pathways. It also calculates and returns the area of that particular object with respect to the camera.",
            "live_link": "https://abandoned-object-detection.streamlit.app/",
            "video_demo_link": "https://drive.google.com/file/d/1bgUczvD8Oal4rStWhdF-bRiC9ee071sp/view?usp=sharing"
        },
        "Automatic Number Plate Detection": {
            "description": "This project automatically detects license plates and reads the text on them. It's useful in various applications like traffic monitoring and vehicle tracking.",
            "live_link": "https://autolpr.streamlit.app/",
            "video_demo_link": "https://drive.google.com/file/d/16X255GVrmTkN0mwuQvnPIlv3-o_xqRqF/view?usp=drive_link"
        },
        "Speed Monitoring of Vehicles": {
            "description": "This project monitors the number of cars, trucks, and bikes entering and exiting lanes, measures their speed, and throws an alarm when a vehicle exceeds a certain speed threshold.",
            "live_link": "https://traffic-monitoring.streamlit.app/",
            "video_demo_link": "https://drive.google.com/file/d/1EFe0pEUwGQloBTNTy6BFOIKZ2-EQ4MQg/view?usp=drive_link"
        },
        "Human Fall Detection": {
            "description": "This project detects human falls from the camera's point of view. It's particularly useful in healthcare settings for monitoring patients or elderly individuals.",
            "live_link": "https://example.com/this-site-is-currently-under-development",
            "video_demo_link": "https://drive.google.com/file/d/1pQFy8Hmsv_YNTJllgjhrjhXdRg1w7u5x/view?usp=drive_link"
        },
        # Add entries for other projects here
    }

    for idx, (title, data) in enumerate(projects.items()):
        col1, col2, col3 = st.columns([4, 1, 1])
        with col1:
            st.header(title)
            st.write(data["description"])
            if idx < len(projects) - 1:  # Add a line break after all but the last project
                st.write("---")
        with col2:
            if st.button('Go to Project', key=f'live_{title}'):
                webbrowser.open(data["live_link"])
        with col3:
            if st.button('Video Demo', key=f'video_{title}'):
                webbrowser.open(data["video_demo_link"])

if __name__ == "__main__":
    main()
st.write("---")
