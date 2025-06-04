from clean import clean_text
from scraper import scrape
from model import load_model
from process import process_text, tokenizer
import sqlite3
import os
model = load_model("C:/model/my_model_v3.keras")

def analyze_news(url):

    conn = sqlite3.connect(r'C:\SQLiteStudio\news.db')
    cursor = conn.cursor()

    print ("Using Database at: ", os.path.abspath(r'C:\SQLiteStudio\news.db'))
    cursor.execute("SELECT Title, label FROM news_table WHERE URL = ?", (url,))
    existing = cursor.fetchone()

    if existing:
        title, label = existing
        print("Article already exists in the database.")
        conn.close()
        return label, title

    title, text = scrape(url)
    cleaned_text = clean_text(text)
    input_seq = process_text(cleaned_text, tokenizer)
    prediction = model.predict(input_seq)[0][0]
    #score = prediction.item()
    label = "Fake" if prediction < 0.5 else "Real"
    
    
    cursor.execute('INSERT INTO news_table (URL, Title, Text, label) VALUES (?, ?, ?, ?)', (url, title, cleaned_text, label))
    conn.commit()
    conn.close()
    return label, title

if __name__ == "__main__":
    url = input("Enter the news URL: ")
    analyze_news(url)