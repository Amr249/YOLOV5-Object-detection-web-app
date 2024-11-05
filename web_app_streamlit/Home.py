import streamlit as st 


st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')


st.title("YOLO V5 Object Detection App")
st.caption('This web application demostrate Object Detection')

st.image("https://cdn.prod.website-files.com/614c82ed388d53640613982e/65390c0119ee1e54a61cac91_evolution-yolo.webp", width=750)

# Content
st.markdown("""
### This App detects objects from Images
- Automatically detects 20 objects from image
 

### Below give are the object the our model will detect

           
            """)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button('People', icon="🧑‍🦲")
    st.button('Cars', icon="🚗")
    st.button('Chair', icon="💺")
    st.button('Bottle', icon="🍾")
    st.button('Sofa', icon="🛋️")

with col2:
    st.button('Bicyle', icon="🚲")
    st.button('Horse', icon="🐎")
    st.button('Motor Bike', icon="🏍️")
    st.button('Cat', icon="🐈")
    st.button('Tv Monitor', icon='📺')

with col3:
    st.button('Cow', icon='🐄')
    st.button('Sheep', icon='🐏')
    st.button('Aeroplane', icon='✈️')
    st.button('Train', icon='🚄')
    st.button('Dining Table', icon='🛷')

with col4:
    st.button('Bus', icon='🚐')
    st.button('Potted Plant', icon='🪴')
    st.button('Bird', icon='🦅')
    st.button('Dog', icon='🐶')
    st.button('Boat', icon='🛶')

# 
# 1. Person
# 2. Car
# 3. Chair
# 4. Bottle
# 5. Sofa
# 6. Bicyle
# 7. Horse
# 8. Boat
# 9. Motor Bike
# 10. Cat
# 11. Tv Monitor
# 12. Cow
# 13. Sheep
# 14. Aeroplane
# 15. Train
# 16. Dining Table
# 17. Bus
# 18. Potted Plant
# 19. Bird
# 20. Dog