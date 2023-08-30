from PIL import Image
import requests
import streamlit as st 


#page config ( Title )
st.set_page_config(page_title="d3vsxnpai", page_icon=":star_struck:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#---------- LOAD ASSETS ---------
img_contact_form = Image.open("jjk.jpg")
img_yoimiya_sticker = Image.open("yoimiya.png")


#------- Header Section -------
with st.container():
    st.subheader("Senpai UwU! ")
    st.title("D3vsxnpai" " XD")
    st.write("Hello nerds, it's your senpai Dev. I'm a casual student who does stuff for fun. Dm me on instagram for commisions. YO!")
    st.write("[My Youtube Channel](https://www.youtube.com/@devsenpaiAMV)")

#------ What this Nigg does ------

st.write("---")
left_coloumn, right_coloumn = st.columns(2)
with left_coloumn:
    st.header("What I do")
    st.write("##")
    st.write(
        """I do anime edits for fun
        I also do stuff for commissions
        You can contact me on my instagram
        @d3vsxnpai"""
    )
    st.write("[My instagram](https://www.instagram.com/d3vsxnpai/)")
        
    


#-------------- Animation ------------
with right_coloumn:
    st.image(img_yoimiya_sticker, width=550)
    


#---------------------------------------------------------------------------------

st.write("---")
st.header("My content")
st.write("##")
image_coloumn, text_coloumn = st.columns((1,2))
with image_coloumn:
    st.image(img_contact_form)
with text_coloumn:
    st.subheader("2 Dangerous I Jujutsu Kaisen Trailer 'Shibuya Incident Arc' [AMV/Edit]")
    st.write("[Watch video >](https://www.youtube.com/watch?v=oMw2xqFE4Z8)")


#----------- CONTACT ----------#
st.write("---")
st.header("Get in touch with me !")
st.write("##")
contact_form = """
     <input type="hidden" name="_captcha" vlue="false">
     <form action="https://formsubmit.co/jmaillapalli1@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name"required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" requited></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()