# TikTok Likes Prediction Project

This project was developed as part of a coursework aimed at building a neural network model to predict the number of likes on TikTok videos.

## 📁 Project Structure

```
tiktok_likes/
│
├── parser_tiktok.py              # Web scraper for TikTok video data
├── tiktok_data.csv               # Dataset
├── tiktok_model_linearregression.ipynb    # Jupyter Notebook with Linear Regression model
├── tiktok_model_nn_bert.ipynb    # Jupyter Notebook with Neural Network model
└── README.md                     # Project documentation
```

## 🧠 Model Overview

The project includes two distinct machine learning approaches for predicting TikTok video likes:

### 1. Neural Network with BERT Embeddings (`tiktok_model_nn_bert`)
- **Architecture**: Deep neural network with BERT-based text embeddings
- **Features**:
  - Text embeddings from video descriptions using multilingual BERT
  - Hashtag embeddings using the same BERT model
  - Numerical features (duration, author stats, views, etc.)
  - Temporal features (hour, day, month encoded cyclically)
- **Preprocessing**: Text cleaning, outlier removal, feature scaling
- **Evaluation**: RMSE, MAE, R² scores on log-transformed likes

### 2. Linear Regression with Custom Embeddings (`tiktok_model_linearregression`)
- **Approach**: Linear regression with custom word embeddings
- **Features**:
  - SimpleWord2Vec embeddings for text and hashtags
  - Standard numerical and temporal features
  - Pipeline-based preprocessing
- **Advantage**: Faster training and interpretation

## 🛠️ Technical Implementation

### Data Collection
- **Web Scraper**: `parser_tiktok.py` extracts video metadata from TikTok pages
- **Data Points**: Duration, text description, hashtags, author statistics, view counts, timestamps

### Feature Engineering
- Text cleaning and normalization
- Cyclical encoding of temporal features
- Custom embedding generation
- Outlier detection and removal (99th percentile)

### Model Training
- Train/validation split (80/20)
- Early stopping to prevent overfitting
- Comprehensive evaluation metrics
- Visualization of training progress and predictions

## 📊 Model Performance

Both models are evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE) 
- R² Score (coefficient of determination)
- Median Absolute Error (MedAE) for linear regression

## 🚀 Usage

1. **Data Collection**: Run the parser to collect TikTok video data
2. **Preprocessing**: Clean and prepare the data using the provided functions
3. **Model Training**: Execute the notebook cells to train either model
4. **Evaluation**: Analyze performance metrics and visualization results

## 📋 Requirements

Key dependencies:
- TensorFlow/Keras
- PyTorch
- Transformers (BERT)
- Scikit-learn
- Pandas, NumPy
- BeautifulSoup (for parsing)

## 🎯 Coursework Context

This project demonstrates:
- Practical application of NLP techniques (BERT embeddings)
- Feature engineering for social media data
- Comparison of neural network vs traditional ML approaches
- End-to-end ML pipeline development

The models provide insights into factors influencing TikTok video engagement and can be extended for content recommendation or viral prediction systems.