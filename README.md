# movie_recommendation_system
A content-based Movie Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit. The system recommends movies similar to a user's selected movie by analyzing movie genres and metadata using TF-IDF vectorization and cosine similarity.
🚀 Features
1.Recommend movies similar to a selected movie
2.Fast and efficient recommendation engine
3.User-friendly web interface using Streamlit
4.Uses Machine Learning techniques for movie similarity
5.Easy to deploy on Streamlit Cloud
🛠️ Technologies Used
1.Python
2.Pandas
3.NumPy
4.Scikit-Learn
5.TF-IDF Vectorization
6.Nearest Neighbors Algorithm
7.Streamlit
8.Pickle
📂 Project Structure
movie-recommendation-system/
│
├── app.py                 # Streamlit application
├── model.pkl              # Trained recommendation model
├── tfidf.pkl              # TF-IDF vectorizer
├── movies.pkl             # Movie dataset
├── movies_dict.pkl        # Movie dictionary
├── requirements.txt       # Project dependencies
├── setup.sh               # Deployment configuration
├── movieRS.ipynb          # Jupyter Notebook used for development
├── .gitignore
└── README.md
📊 How It Works
Movie data is preprocessed.
Genres and movie features are transformed using TF-IDF Vectorization.
A Nearest Neighbors model is trained using cosine similarity.
When a user selects a movie, the model finds the most similar movies.
Recommended movies are displayed through the Streamlit interface.
📈 Machine Learning Model

The recommendation engine uses:

TF-IDF Vectorizer
Cosine Similarity
Nearest Neighbors Algorithm

These techniques help identify movies with similar characteristics and genres.

🌐 Deployment

The application can be deployed on:

Streamlit Community Cloud
Render
Railway
🔮 Future Improvements
Movie posters using TMDB API
Search functionality
User ratings integration
Hybrid recommendation system
Personalized recommendations
Genre-based filtering
👨‍💻 Author

Sahil Sharma

Data Science & Machine Learning Enthusiast
