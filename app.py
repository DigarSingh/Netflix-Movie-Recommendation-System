import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
)

# Custom CSS for theme
def local_css():
    st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stApp {
        background-image: linear-gradient(to bottom right, #0e1117, #2e3c55);
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF2B2B;
        color: white;
    }
    h1, h2, h3 {
        color: #FF4B4B;
    }
    .recommendation-card {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_resource
def load_data():
    movies = pickle.load(open('movies_dict.pkl', mode='rb'))
    data = pd.DataFrame(movies)
    similarity = pickle.load(open('similarity.pkl', mode='rb'))
    return data, similarity

data, similarity = load_data()

def fetch_movie_poster(movie_title):
    placeholder_url = f"https://ui-avatars.com/api/?name={movie_title.replace(' ', '+')}&background=random&color=fff&size=200"
    return placeholder_url

def recommend(movie):
    recommended_movies = []
    recommended_posters = []
    
    try:
        movie_index = data[data['title'] == movie].index[0]
        similar = similarity[movie_index]
        movies_list = sorted(list(enumerate(similar)), reverse=True, key=lambda x: x[1])[1:6]

        for i in movies_list:
            movie_title = data.iloc[i[0]].title
            recommended_movies.append(movie_title)
            
            # Get poster URL for this movie
            poster_url = fetch_movie_poster(movie_title)
            recommended_posters.append(poster_url)
            
        return recommended_movies, recommended_posters
    except IndexError:
        return [], []
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []

local_css()

st.markdown("<h1 style='text-align: center;'>🎬 Netflix Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Find your next favorite movie!</h3>", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("<h3 style='text-align: center;'>Select a Movie</h3>", unsafe_allow_html=True)
    # Movie selection dropdown
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        data['title'].values
    )
    # Recommend button
    if st.button('Show Recommendations'):
        with st.spinner('Finding movies you might like...'):
            names, posters = recommend(selected_movie)
            
            if names:
                with col2:
                    st.markdown(f"### Top 5 Recommendations for '{selected_movie}'")
                    
                    # Create 5 columns for movie recommendations
                    rec_cols = st.columns(5)
                    
                    for i in range(len(names)):
                        with rec_cols[i]:
                            # Display movie poster
                            try:
                                if posters[i].startswith('http'):
                                    # If it's a URL, fetch the image
                                    response = requests.get(posters[i])
                                    img = Image.open(BytesIO(response.content))
                                    st.image(img, caption=names[i], use_container_width=True)
                                else:
                                    # If it's a local path
                                    st.image(posters[i], caption=names[i], use_container_width=True)
                                    
                                # Add movie title in a nice card below the poster
                                st.markdown(f"<div class='recommendation-card'><h4>{names[i]}</h4></div>", 
                                            unsafe_allow_html=True)
                            except Exception as e:
                                st.error(f"Could not display image for {names[i]}: {e}")
            else:
                with col2:
                    st.error("No recommendations found for this movie. Please try another one.")
    else:
        # Empty space or simple display when no recommendations are shown
        with col2:
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 400px;">
                <div style="text-align: center; padding: 30px; background-color: rgba(255,255,255,0.1); 
                border-radius: 10px;">
                    <h2>Ready for movie recommendations?</h2>
                    <p>Select a movie and click the button to get started!</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 20px; background-color: rgba(0,0,0,0.2);">
    <p>Made by Digar with ❤️ | Movie Recommender System</p>
</div>
""", unsafe_allow_html=True)