# 🎬 Netflix Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on your preferences, built with Python and Streamlit.

![Netflix Movie Recommender](https://img.shields.io/badge/Netflix-Movie%20Recommender-red)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-blue)
![Machine Learning](https://img.shields.io/badge/ML-Content--based%20Filtering-green)

## 📝 Description

This project is a movie recommendation system that uses natural language processing and machine learning techniques to suggest similar movies based on content features. The system analyzes movie attributes like genres, cast, crew, keywords, and overview to find patterns and similarities between films.

## ✨ Features

- 🎯 Content-based movie recommendations
- 🔍 Search for any movie from a dataset of 5000 movies
- 🖼️ Visual display of movie recommendations with colorful posters
- 🌈 Modern, Netflix-inspired UI design
- 🚀 Fast recommendations using pre-computed similarity metrics

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms (CountVectorizer, Cosine Similarity)
- **NLTK**: Natural language processing for text preprocessing
- **Streamlit**: Web application framework
- **Pickle**: Model serialization

## 📊 How It Works

1. **Data Preprocessing**:
   - Extract relevant features (genres, cast, keywords, etc.)
   - Text preprocessing (stemming, tokenization, etc.)
   - Convert text data to vector representations using Bag of Words model

2. **Similarity Calculation**:
   - Calculate cosine similarity between movie vectors
   - Create a similarity matrix for quick lookups

3. **Recommendation Engine**:
   - When a user selects a movie, find the most similar movies based on the pre-computed similarity scores
   - Display the top 5 recommendations

## 🚀 Installation & Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DigarSingh/netflix-movie-recommendation-system.git
   cd netflix-movie-recommendation-system
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:

   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and go to `https://netflix-movie-recommendation-systemm.streamlit.app/`

## 📁 Project Structure

- `Netflix Recommendation model system.ipynb`: Jupyter notebook with data exploration, preprocessing and model building
- `app.py`: Streamlit web application
- `movies_dict.pkl`: Pickled dictionary containing movie data
- `similarity.pkl`: Pickled similarity matrix for recommendations
- `tmdb_5000_movies.csv`: TMDB movies dataset (source data)
- `tmdb_5000_credits.csv`: Movie credits dataset (source data)


## 🔮 Future Improvements

- Add user-based collaborative filtering for more personalized recommendations
- Integrate real-time movie poster fetching from TMDB API
- Implement user authentication and favorite movie tracking
- Add movie details and trailer links
- Deploy the application to the cloud

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- TMDb for providing the movies dataset
- Streamlit for the amazing web app framework
- All open-source contributors whose libraries made this project possible

---

### Made with ❤️ by Digar
