# FakeNews Detection Project

A machine learning project that detects whether a news headline or article is fake or real, using natural language processing (NLP). Built as a personal project to explore text classification, model deployment, and data preprocessing with Python.

## Why Streamlit?

Streamlit was chosen as the web interface framework to facilitate rapid prototyping and deployment of the application. This decision allowed the primary focus to remain on the core aspects of the project: scraping, processing, and tokenizing the data, as well as developing and refining the machine learning model. Streamlit’s simplicity and ease of use made it possible to quickly build an interactive interface without diverting significant resources from the main data and modeling tasks.

## Project Structure

```
FakeNews/
├── clean.py           # Text cleaning utilities
├── main.py            # Backend logic and analysis
├── model.py           # Model loading utilities
├── process.py         # Text preprocessing
├── scraper.py         # Article scraping
├── streamlit_app.py   # Streamlit web interface
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
└── my_model_v3.keras  # pre-trained model
└── tokenizer.pickel_v3   #saved tokenizer object
```

## Features

- Fake news detection using a trained machine learning model
- Web interface for article submission and analysis (Streamlit)
- Real-time classification results
- Confidence scores and explanations (planned)
- Historical analysis of submitted articles (via SQLite database)

## Setup Instructions

### Prerequisites

- Python 3.8 to 3.12
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone [repository-url]
    cd FakeNews
    ```

2. Create and activate a virtual environment:
    ```bash
    # Windows
    python -m venv env
    .\env\Scripts\activate

    # Linux/MacOS
    python -m venv env
    source env/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Streamlit web app:
    ```bash
    streamlit run streamlit_app.py
    ```

2. Access the web interface at `http://localhost:8501`

## Model Notes

**Current model shows signs of overfitting, likely due to:**
- Limited dataset size
- High expressiveness of dense layers
- High embedding dimension
- poor quality data

**Planned improvements:**
- Implement EarlyStopping during training (done)
- Add L2 regularization to dense layers (done)
- Reduce embedding size to 64 (done)

**Results after improvements**
- Model stopped overfitting. Acc is a bit lower than the Human Expected Standard (around 70% ACC).
- After analysing the training data manually, I concluded that the quality can be questioned. The next step is to look for better training data.

## Development Status

✅ The application is functional, although it is still being improved. 
Next Step: search for better data to train.

!More information about the model to be added.



## License

[License information to be added]

## Contact

[Contact information to be added]
