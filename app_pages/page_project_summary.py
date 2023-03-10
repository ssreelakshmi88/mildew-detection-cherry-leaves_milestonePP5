import streamlit as st


def page_project_summary_body():
    """ Function to display project summary page """

    st.title("A Brief Summary of Project")

    st.header("General Information")

    st.info(
        f"Powdery mildew is a parasitic fungal disease caused by Podosphaera clandestina"
        f" in cherry trees."
        f" Infected plants display white powdery spots on the leaves and stems."
        f" The lower leaves are the most affected.\n\n"
        f" Powdery mildew is one of the plant diseases that can be "
        f" identified easily. "
        f" As the infection progresses, the spots get larger and "
        f" denser and it may spread to other parts of plant. \n\n"
        f" The disease occurs mostly in high humid and "
        f" moderate temperatures showing devastating "
        f" effects on the life of the host plant reducing plant harvest."
    )

    st.warning(
        f"**Project Dataset**\n\n"
        f"\n The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).\n"
        f"The available dataset contains 2104 healthy leaves and 2104 affected leaves. "
        f"The images dataset has been split evenly with "
        f" healthy cherry leaves and leaves with powdery Mildew."
    )

    st.success(
        f"The project has two business requirements:\n\n"
        f"1 - The client is interested in having a study to visually differentiate "
        f" a healthy from an infected leaf.\n\n"
        f"2 - The client is interested in telling whether a given leaf "
        f" is infected by powdery mildew or not ."
    )

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/ssreelakshmi88/mildew-detection-cherry-leaves_milestonePP5.git).")
