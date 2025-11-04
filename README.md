📦 AI-Driven Flipkart Product Review Analysis & Recommendation System

In today’s competitive e-commerce landscape, understanding customer sentiment in real-time is essential for delivering better product insights, improving customer experience, and optimizing business decisions.

This repository presents a complete AI-powered sentiment analysis and product recommendation system built using live Flipkart customer reviews. The project automates data extraction, processes user sentiments, and recommends products based on authentic customer opinions. The end solution simulates a real-world e-commerce intelligence pipeline and is deployed for interactive use.

🎯 Project Objective

To develop a scalable pipeline that:

Scrapes live reviews from Flipkart

Performs sentiment analysis to classify customer feedback

Generates data-driven product recommendations

Provides visual insights and dashboards

Integrates LLM-based logic (LangChain) for intelligent ranking

Prepares the system for AWS deployment

📁 Project Structure
🧠 Jupyter Notebooks
File: reviews_scrapping.ipynb

Description:
Implements the web scraping workflow using Selenium & BeautifulSoup to extract real-time product reviews, ratings, and metadata from Flipkart pages. Includes:

Dynamic page navigation

Review extraction

Cleaning & formatting raw HTML text

CSV export of structured dataset

File: sentiment-analysis.ipynb

Description:
Performs text preprocessing and sentiment analysis using NLP techniques and TextBlob. Covers:

Text normalization

Sentiment scoring

Polarity classification (Positive/Neutral/Negative)

Dataset labeling

File: visualization.ipynb

Description:
Generates visual insights for customer sentiment distribution, product comparison, and trend analysis using Python visualization libraries.

💻 Application
File: newapp.py

Description:
Application script integrating scraping output and sentiment results, allowing users to interact with the model and view processed insights. Designed to be cloud-deployable (AWS support).

📊 Capabilities & Output

✅ Real-time scraping from Flipkart

✅ Sentiment classification using NLP

✅ Insight dashboards & charts

✅ AI-based ranking using LangChain

✅ Cloud-ready application script

🛠️ Tech Stack
Category	Tools
Programming	Python
Scraping	Selenium, BeautifulSoup, Requests
Data Processing	Pandas
NLP & Sentiment	TextBlob
LLM Framework	LangChain
Visualization	Matplotlib / Seaborn
Deployment	AWS
🚀 Key Features

Live data ingestion pipeline

Automatic sentiment tagging

Product recommendation engine

Real-time result visualization

Modular code for scalability

Cloud deployment readiness

📈 Evaluation Metrics

Sentiment classification accuracy

Review extraction completeness

Recommendation relevance

Code modularity & documentation quality

📂 Repository Contents
File / Folder	Description
reviews_scrapping.ipynb	Live scraping & data extraction
sentiment-analysis.ipynb	Sentiment computation pipeline
visualization.ipynb	Graphs & insights visualization
newapp.py	Application & deployment script
data/ (if added)	Processed datasets & exports
🙌 Acknowledgements

This project uses public Flipkart web data, open-source Python libraries, and LangChain for AI workflow integration.

📬 Contact

For queries, suggestions, or collaboration opportunities:

📧 Email: mryunus.in@gmail.com

🔗 GitHub: github.com/mrmohamedyunus
