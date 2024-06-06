import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="AgroGuard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About AgroGuard", "Disease Information"])

# About AgroGuard page
if page == "About AgroGuard":
    st.title("About AgroGuard")
    st.write("""
    Welcome to the Plant Disease Information web application! This app is designed to provide valuable insights into various plant diseases, their causes, symptoms, and prevention methods. It also promotes our mobile application that helps you classify plant diseases by simply taking a photo.

    **Download the mobile app now!**
    Our mobile app leverages advanced machine learning techniques to accurately classify plant diseases from photos taken with your phone. It is an essential tool for farmers, gardeners, and agricultural professionals to ensure the health and productivity of their plants.

    **Why is this app useful?**
    - **Accurate Disease Classification:** Quickly identify diseases affecting your plants.
    - **Comprehensive Information:** Learn about common plant diseases, their symptoms, causes, and prevention methods.
    - **User-Friendly:** Easy to use interface with step-by-step instructions.
    - **Time-Saving:** Save time and resources by accurately diagnosing plant health issues.

    [Download the mobile app on the Play Store](https://play.google.com/store/apps/details?id=com.example.yourapp)
    """)

# Disease Information page
elif page == "Disease Information":
    st.title("Plant Disease Information")
    st.write("Select a plant from the dropdown list below to get detailed information about its common diseases, their causes, symptoms, and prevention methods.")

    # Sidebar for plant selection
    plant = st.selectbox(
        "Select a plant",
        ["Apple", "Bell Pepper", "Cherry", "Corn", "Grape", "Peach", "Potato", "Rice", "Tomato"]
    )

    # Function to display disease information
    def show_disease_info(disease_name, symptoms, causes, prevention, image_path):
        st.header(disease_name)
        image = Image.open(image_path)
        st.image(image, width=200)
        st.write(f"**Symptoms:** {symptoms}")
        st.write(f"**Causes:** {causes}")
        st.write(f"**Prevention:** {prevention}")

    # Information about diseases
    if plant == "Apple":
        show_disease_info(
            "Apple Scab",
            "Dark, velvety spots on leaves and fruit.",
            "Fungus Venturia inaequalis.",
            "Use resistant varieties, prune trees for better air circulation, and apply fungicides.",
            "images/apple_scab.jpg"
        )
        show_disease_info(
            "Fire Blight",
            "Brown, wilted leaves and branches that look scorched.",
            "Bacterium Erwinia amylovora.",
            "Remove and destroy infected branches, apply bactericides, and avoid overhead watering.",
            "images/fire_blight.jpg"
        )
    elif plant == "Bell Pepper":
        show_disease_info(
            "Bacterial Spot",
            "Water-soaked spots on leaves and fruit, turning brown and scabby.",
            "Bacterium Xanthomonas campestris.",
            "Use disease-free seeds, practice crop rotation, and apply copper-based fungicides.",
            "images/bacterial_spot.jpg"
        )
        show_disease_info(
            "Phytophthora Blight",
            "Dark, water-soaked lesions on stems, leaves, and fruit.",
            "Fungus Phytophthora capsici.",
            "Improve soil drainage, avoid overhead irrigation, and apply fungicides.",
            "images/phytophthora_blight.jpg"
        )
    elif plant == "Cherry":
        show_disease_info(
            "Brown Rot",
            "Brown, sunken lesions on fruit, withering of blossoms.",
            "Fungus Monilinia fructicola.",
            "Remove mummified fruit, apply fungicides, and prune trees to improve air circulation.",
            "images/brown_rot.jpg"
        )
        show_disease_info(
            "Cherry Leaf Spot",
            "Small, purple spots on leaves, leading to yellowing and premature leaf drop.",
            "Fungus Blumeriella jaapii.",
            "Apply fungicides, remove fallen leaves, and use resistant varieties.",
            "images/cherry_leaf_spot.jpg"
        )
    elif plant == "Corn":
        show_disease_info(
            "Northern Corn Leaf Blight",
            "Long, grayish-green lesions on leaves.",
            "Fungus Exserohilum turcicum.",
            "Plant resistant hybrids, rotate crops, and apply fungicides.",
            "images/northern_corn_leaf_blight.jpg"
        )
        show_disease_info(
            "Gray Leaf Spot",
            "Small, rectangular lesions on leaves.",
            "Fungus Cercospora zeae-maydis.",
            "Rotate crops, improve field drainage, and apply fungicides.",
            "images/gray_leaf_spot.jpeg"
        )
    elif plant == "Grape":
        show_disease_info(
            "Powdery Mildew",
            "White, powdery growth on leaves, stems, and fruit.",
            "Fungus Erysiphe necator.",
            "Use resistant varieties, apply sulfur-based fungicides, and prune for better air circulation.",
            "images/powdery_mildew.jpg"
        )
        show_disease_info(
            "Downy Mildew",
            "Yellow spots on leaves, white downy growth on the underside.",
            "Fungus Plasmopara viticola.",
            "Apply fungicides, remove infected leaves, and ensure good air circulation.",
            "images/downy_mildew.jpg"
        )
    elif plant == "Peach":
        show_disease_info(
            "Peach Leaf Curl",
            "Distorted, reddened leaves.",
            "Fungus Taphrina deformans.",
            "Apply fungicides in late winter, remove infected leaves, and use resistant varieties.",
            "images/peach_leaf_curl.jpg"
        )
        show_disease_info(
            "Brown Rot",
            "Brown, sunken lesions on fruit, withering of blossoms.",
            "Fungus Monilinia fructicola.",
            "Remove mummified fruit, apply fungicides, and prune trees to improve air circulation.",
            "images/brown_rot_peach.jpg"
        )
    elif plant == "Potato":
        show_disease_info(
            "Late Blight",
            "Dark, water-soaked spots on leaves and tubers.",
            "Fungus Phytophthora infestans.",
            "Use resistant varieties, apply fungicides, and practice crop rotation.",
            "images/late_blight.jpg"
        )
        show_disease_info(
            "Early Blight",
            "Small, dark spots on leaves with concentric rings.",
            "Fungus Alternaria solani.",
            "Rotate crops, apply fungicides, and ensure good field drainage.",
            "images/early_blight.jpg"
        )
    elif plant == "Rice":
        show_disease_info(
            "Rice Blast",
            "Diamond-shaped lesions on leaves.",
            "Fungus Magnaporthe oryzae.",
            "Use resistant varieties, apply fungicides, and avoid excessive nitrogen fertilizer.",
            "images/rice_blast.jpeg"
        )
        show_disease_info(
            "Bacterial Blight",
            "Water-soaked lesions on leaves, turning yellow.",
            "Bacterium Xanthomonas oryzae.",
            "Use resistant varieties, apply bactericides, and avoid overhead irrigation.",
            "images/bacterial_blight.jpeg"
        )
    elif plant == "Tomato":
        show_disease_info(
            "Late Blight",
            "Dark, water-soaked spots on leaves and fruit.",
            "Fungus Phytophthora infestans.",
            "Use resistant varieties, apply fungicides, and ensure good air circulation.",
            "images/late_blight_tomato.jpg"
        )
        show_disease_info(
            "Early Blight",
            "Small, dark spots on leaves with concentric rings.",
            "Fungus Alternaria solani.",
            "Rotate crops, apply fungicides, and ensure good field drainage.",
            "images/early_blight_tomato.jpg"
        )
