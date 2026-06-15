import streamlit as st
import pickle

with open("movie_model.pkl", "rb") as f:
    model = pickle.load(f)

    st.title("🎬 Movie Recommendation System")

    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    movie_id = st.number_input("Enter Movie ID", min_value=1, step=1)

    if st.button("Predict Rating"):
        prediction = model.predict(user_id, movie_id)
        st.success(
            f"Predicted Rating: {prediction.est:.2f}"
                        )