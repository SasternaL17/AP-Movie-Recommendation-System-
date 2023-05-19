import pandas as pd
import streamlit as st

def fetch_movie_data(pickle_file):
    try:
        data = pd.read_pickle(pickle_file)
        return data
    except FileNotFoundError:
        st.error("Pickle file not found.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

pickle_file_path = 'recommended_movies.pkl'  
recommended_movies = fetch_movie_data(pickle_file_path)

if recommended_movies is not None:
    
    recommended_movies['Movie 1'] = recommended_movies['Movie 1'].astype(str)
    recommended_movies['Movie 2'] = recommended_movies['Movie 2'].astype(str)

  
    unique_movies = recommended_movies["Movie 1"].unique()

    st.title("Amazon Prime Movie Recommendation")

   
    selected_movie = st.selectbox("Select a movie", unique_movies)

    submit_button = st.button("Suggest")

    if submit_button:
        filtered_movies = recommended_movies[recommended_movies["Movie 1"] == selected_movie]

      
        if not filtered_movies.empty:
            st.subheader("Recommended movies:")
            recommended_movie_names = filtered_movies["Movie 2"].tolist()
            st.write(", ".join(recommended_movie_names))
        else:
            st.error("No recommendation found for the selected movie.")
