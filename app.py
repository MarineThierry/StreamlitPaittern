import streamlit as st
import streamlit.components.v1 as components
import cloudinary
import cloudinary.uploader
import os
from os.path import join,dirname
from dotenv import load_dotenv, find_dotenv
import streamlit as st
import requests
import pandas as pd
from PIL import Image

#welcome phrase
st.markdown('Hello and welcome in pAIttern ')
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Upload Your Video", type=["mp4", "MOV"])

# load the video input into cloudinary



# point to .env file
env_path = join(dirname(dirname('__file__')),'.env') # ../.env
env_path = find_dotenv() # automatic find

# load your api key as environment variables
load_dotenv(env_path)

#config cloudinary authentification
cloudinary.config(
  cloud_name = "paittern",
  api_key = os.getenv('CLOUDINARY_API_KEY'),
  api_secret = os.getenv('CLOUDINARY_API_SECRET'),
  secure = True
)

#upload on cloud
if  uploaded_file :
    response_cloud = cloudinary.uploader.unsigned_upload(uploaded_file.read(),
                                                         resource_type='video',
                                                         upload_preset='paittern',
                                                         public_id = "test")

    url_video_path = response_cloud['url']
    st.markdown(url_video_path)


#asking user for his or her height in meter 
height_cm = st.number_input('Enter your size (Height) in centimeter :')

st.write('You measure : ', height_cm / 100, ' m')

clothes_list= ["Sleeveless t-shirt", "Apron", "Dress", "Bow tie", "Boxer", "Coat",
                 "Coat", "Underbust corset", "Pants", "cycling breeches", "top with a draped neckline", "face mask", "Flat cap", "Hat", "Handbag",
                 "Zip-up hoodie", "Hooded jumper", "Sport coat style jacket", "Pants", "Pencil skirt ", "Circle skirt ", "Swim trunks", "Highly adaptable men shirt", "highly adaptable women shirt",
                 "straightforward sweater", "Zero-waste top", "Fitted T-shirt", "Classic trouser", "Tie", "Basic highly-customizable underwear",
                 "Classic fitted waistcoat", "Wrap pants", "Fancy zipless cardigan"]

department_list= ["Tops", "Accessories", "Tops", "Accessories", "Underwear", "Coats & jackets",
                 "Coats & jackets", "Underwear", "Bottoms", "Bottoms", "Tops", "Accessories", "Accessories", "Accessories", "Accessories",
                 "Tops", "Tops", "Coats & jackets", "Bottoms", "Bottoms", "Bottoms", "Swimwear", "Tops", "Tops",
                 "Tops", "Tops", "Tops", "Bottoms", "Accessories", "Underwear",
                 "Tops", "Bottoms", "Tops"]


pattern_list = ["Aaron", "Albert", "Bella", "Benjamin", "Bruce", "Carlita",
                 "Carlton", "Cathrin", "Charlie", "Cornelius", "Diana", "Florence", "Florent", "Holmes", "Hortensia",
                 "Huey", "Hugo", "Jaeger", "Paco", "Penelope", "Sandy", "Shin", "Simon", "Simone",
                 "Sven", "Tamiko", "Teagan", "Theo", "Trayvon", "Ursula",
                 "Wahid", "Waralee", "Yuri"]


family_pattern_list = [department_list,clothes_list,pattern_list]



@st.cache

def get_select_box_data():
    df = pd.DataFrame (family_pattern_list).transpose()
    df.columns = ['Clothes type','Clothes','Pattern']
    return df

df = get_select_box_data()


option1 = st.selectbox('Select a Clothes type', df['Clothes type'].unique())


filtered_df = df[df['Clothes type'] == option1]
st.write(filtered_df)

option = st.selectbox(
     'Choose your pAIttern !',
    filtered_df['Pattern'])
st.write('You selected:', option)

dictionary_of_pattern = {'Aaron': 'https://res.cloudinary.com/paittern/image/upload/v1646751836/streamlit_images/Aaron_hjqvjy.png',
                        'Albert': 'https://res.cloudinary.com/paittern/image/upload/v1646752080/streamlit_images/Albert_rvgqaf.png',
                           'Bee': 'https://res.cloudinary.com/paittern/image/upload/v1646752080/streamlit_images/Bee_kz7wge.png' ,
                         'Bella': 'https://res.cloudinary.com/paittern/image/upload/v1646752080/streamlit_images/Bella_rn7vgs.png',
                      'Benjamin': 'https://res.cloudinary.com/paittern/image/upload/v1646752080/streamlit_images/Benjamin_g9ck5p.png',
                          'Bent': 'https://res.cloudinary.com/paittern/image/upload/v1646752080/streamlit_images/Bent_mmbaph.png',
                       'Breanna': 'https://res.cloudinary.com/paittern/image/upload/v1646752080/streamlit_images/Breanna_obbmzr.png',
                         'Brian': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Brian_ia0g95.png',
                         'Bruce': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Bruce_pozkpl.png',
                       'Carlita': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Carlita_n5ifjw.png',
                       'Carlton': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Carlton_trni4n.png',
                       'Cathrin': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Cathrin_vhwfbp.png',
                       'Charlie': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Charlie_igqbam.png',
                     'Cornelius': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Cornelius_zfcsyp.png',
                         'Diana': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Diana_atcoew.png',
                      'Florence': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Florence_wclq67.png',
                       'Florent': 'https://res.cloudinary.com/paittern/image/upload/v1646752081/streamlit_images/Florent_gw3ie3.png',
                        'Holmes': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Holmes_ibiaum.png',
                     'Hortensia': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Hortensia_aze9dz.png',
                          'Huey': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Huey_hwyzln.png',
                          'Hugo': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Hugo_wmtqak.png',
                        'Jaeger': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Jaeger_ywx0ns.png',
                          'Paco': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Paco_xucv6u.png',
                      'Penelope': 'https://res.cloudinary.com/paittern/image/upload/v1646752082/streamlit_images/Penelope_py7j7j.png',
                         'Sandy': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Sandy_xvobax.png',
                          'Shin': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Shin_oojbvt.png',
                         'Simon': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Simon_xvp8r6.png',
                        'Simone': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Simone_hemvgq.png',
                          'Sven': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Sven_usspff.png',
                        'Tamiko': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Tamiko_hg5ja0.png',
                        'Teagan': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Teagan_on3rs2.png',
                          'Theo': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Theo_qvqkcz.png',
                      'Tiberius': 'https://res.cloudinary.com/paittern/image/upload/v1646752083/streamlit_images/Tiberius_yezk4a.png',
                         'Titan': 'https://res.cloudinary.com/paittern/image/upload/v1646752084/streamlit_images/Titan_qfopdp.png',
                       'Trayvon': 'https://res.cloudinary.com/paittern/image/upload/v1646752084/streamlit_images/Trayvon_nsimdd.png',
                        'Ursula': 'https://res.cloudinary.com/paittern/image/upload/v1646752084/streamlit_images/Ursula_onbxaa.png',
                         'Wahid': 'https://res.cloudinary.com/paittern/image/upload/v1646752084/streamlit_images/Wahid_f8u0pt.png',
                      'Walburga': 'https://res.cloudinary.com/paittern/image/upload/v1646752085/streamlit_images/Walburga_pavgnn.png',
                       'Waralee': 'https://res.cloudinary.com/paittern/image/upload/v1646752084/streamlit_images/Waralee_rarfuh.png',
                          'Yuri': 'https://res.cloudinary.com/paittern/image/upload/v1646752084/streamlit_images/Yuri_dujtzk.png'}
                         
                         
                         
                        

# image = Image.open('https://res.cloudinary.com/paittern/image/upload/v1646751836/streamlit_images/Aaron_hjqvjy.png')

st.image(dictionary_of_pattern[option], caption=f'{option}')

if st.checkbox('Show progress bar'):
    import time

    'Starting a long computation process...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'


components.html("""
    hello world
    <div id="container" style="width: 450px; height: 600px">
      coco
    </div>

    <script type="module">
    import Aaron from 'https://cdn.skypack.dev/@freesewing/aaron';
    import theme from 'https://cdn.skypack.dev/@freesewing/plugin-theme';
    import svgAttr from 'https://cdn.skypack.dev/@freesewing/plugin-svgattr';

    const svg = new Aaron({
        sa: 10, // Seam allowance
        paperless: true, // Enable paperless mode
        // More settings, see: https://FreeSewing.dev/reference/api/settings
        measurements: { // Pass in measurements
        biceps: 387,
        chest: 1105,
        hips: 928,
        hpsToWaistBack: 502,
        neck: 420,
        shoulderSlope: 13,
        shoulderToShoulder: 481,
        waistToHips: 139,
        }
    })
    .use(theme)
    .use(svgAttr, {width: "100%", height: "100%"})
    .draft() // Draft the pattern
    .render()

    document.getElementById('container').innerHTML = svg
  </script>""", height=600)


## requests the predictions on measurements
url = 'to complete'


params = {
  'url_video_path': url_video_path,
  'height': height_cm,
  'pattern' : pattern

}

response_api = requests.get(url,params=params)
prediction = response_api.json()
measures = prediction["working"]



st.markdown('Am I working? ',str(measures))



"""
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)"""
