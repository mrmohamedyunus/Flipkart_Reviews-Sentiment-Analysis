import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# ----------------- Load Data -----------------
df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\Desktop\Flipkart_scapping\Flipkart_mobile_recommendation.csv")

# Ensure uniqueness and drop missing critical values
df = df.drop_duplicates(subset=["Product_Name"])
df = df.dropna(subset=["Reviews", "Product_Name"])

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="🌟 Smart Product Recommendation Engine", layout="wide")
st.title("📱 Smart Product Recommendation Engine")
st.markdown("""
Discover the most loved smartphones based on **real user sentiments** and your preferences.  
Simply describe what you're looking for below — e.g., *best camera*, *fast charging*, *good battery life*.
""")

# ----------------- User Input -----------------
query = st.text_input("🔍 What are you looking for?", placeholder="Type features like best camera, fast charging, gaming performance...")
top_n = st.slider("Select number of recommendations", min_value=3, max_value=10, value=5)

# ----------------- TF-IDF Recommendation Logic -----------------
def get_recommendations(query, data, top_n=5):
    data["combined_text"] = data["Product_Name"].astype(str) + " " + data["Reviews"].astype(str)
    
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(data["combined_text"])
    
    query_vec = vectorizer.transform([query])
    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    recommendations = data.iloc[top_indices]
    recommendations = recommendations.drop_duplicates(subset="Product_Name").head(top_n)
    return recommendations

# ----------------- Display Product Cards -----------------
def display_product_card(row):
    sentiment = str(row['Sentiment']).lower()
    if sentiment == 'positive':
        emoji = '🟢'
    elif sentiment == 'negative':
        emoji = '🔴'
    else:
        emoji = '🟡'

    review_text = str(row['Reviews']) if pd.notnull(row['Reviews']) else "No review available"

    with st.container():
        st.markdown(f"### 📦 {row['Product_Name']}")
        st.markdown(f"🧠 Sentiment: {emoji} **{row['Sentiment']}** | 💬 Score: `{row['Sentiment_Score']:.2f}`")
        st.markdown(f"🗣️ *{review_text[:250]}...*")
        st.markdown("---")

# ----------------- Run Search -----------------
if st.button("🔎 Search"):
    if query.strip():
        results = get_recommendations(query, df, top_n)
        
        if results.empty:
            st.warning("⚠️ No matching results found. Try a different keyword like 'battery', 'camera', or 'gaming'.")
        else:
            st.success(f"✅ Found {len(results)} relevant products for: *{query}*")
            
            for idx, row in results.iterrows():
                display_product_card(row)
    else:
        st.info("Please enter a query to start searching.")

# ----------------- Sentiment Visualization -----------------
st.markdown("## 📊 Sentiment Overview Across All Products")
sent_counts = df["Sentiment"].value_counts()
colors = ['#2ecc71', '#e74c3c', '#f1c40f']  # green, red, yellow

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(sent_counts, labels=sent_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontsize':13})
ax.set_title("Sentiment Distribution", fontsize=16, weight='bold')
st.pyplot(fig)

# ----------------- Footer -----------------
st.markdown("---")
st.markdown("🌟 *Built with Streamlit, TF-IDF NLP, and 💖 for smart recommendations.*")
