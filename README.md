# Amharic E-commerce Data Extractor for FinTech Analysis

This project, part of the 10Academy B5W4 challenge, focuses on building an end-to-end data pipeline to extract structured information from unstructured Amharic e-commerce posts on Telegram. The ultimate goal is to create a FinTech engine that can assess vendor activity to identify suitable candidates for micro-lending, based on a project for a hypothetical company, **EthioMart**.

## 🚀 Key Objectives

-   **Data Ingestion:** Programmatically scrape and collect posts from multiple Ethiopian e-commerce Telegram channels.
-   **Data Annotation:** Create a high-quality, manually labeled dataset for Named Entity Recognition (NER) using the CoNLL format.
-   **Model Fine-Tuning:** Fine-tune a pre-trained transformer model (e.g., XLM-Roberta) to accurately identify `PRODUCT`, `PRICE`, and `LOCATION` entities in Amharic text.
-   **Model Evaluation & Selection:** Compare the performance of different models to choose the most suitable one for the task.
-   **FinTech Analytics:** Develop a "Vendor Scorecard" by combining NER-extracted entities with post metadata (like views and post frequency) to create a "Lending Score".

## 🛠️ Tech Stack

-   **Programming Language:** Python 3.10+
-   **Data Ingestion:** Telethon
-   **Data Manipulation:** Pandas
-   **NLP/ML Framework:** Hugging Face (Transformers, Datasets, Evaluate)
-   **Interpretability:** SHAP
-   **Environment Management:** venv
-   **Development Environment:** JupyterLab

## 📂 Project Structure

```
week4-amharic-ecommerce-extractor/
├── data/
│   └── labeled_data.conll          # Manually labeled data for NER training
├── models/                         # Saved fine-tuned models (ignored by git)
├── notebooks/
│   ├── 01_Data_Ingestion_and_Preprocessing.ipynb
│   ├── 02_Data_Labeling.ipynb
│   ├── 03_Model_Finetuning.ipynb
│   ├── 04_Model_Comparison.ipynb
│   ├── 05_Model_Interpretability.ipynb
│   └── 06_FinTech_Vendor_Scorecard.ipynb
├── reports/
│   ├── interim_submission.pdf
├── src/
│   └── analytics_engine.py         # Functions for the vendor scorecard
├── .env                            # For storing API keys (ignored by git)
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Setup & Installation

Follow these steps to set up the project environment locally.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/week4-amharic-ecommerce-extractor.git
    cd week4-amharic-ecommerce-extractor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the venv
    python3 -m venv week-4-venv

    # Activate it (on macOS/Linux)
    source week-4-venv/bin/activate
    
    # On Windows: venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Telegram API credentials:**
    *   Create a file named `.env` in the project's root directory.
    *   Add your API credentials obtained from [my.telegram.org](https://my.telegram.org):
        ```
        API_ID=YOUR_API_ID
        API_HASH="YOUR_API_HASH"
        ```

## ▶️ How to Run the Project

The project is organized into a series of Jupyter notebooks that should be run in order.

1.  **`notebooks/01_Data_Ingestion_and_Preprocessing.ipynb`**:
    *   This notebook connects to the Telegram API and scrapes data from the specified channels.
    *   **Note:** The first time you run this, you will be prompted in your terminal to enter your phone number, a login code sent to your Telegram app, and your 2FA password (if you have one).

2.  **`notebooks/02_Data_Labeling.ipynb`**:
    *   This notebook contains helper code to sample and view the scraped messages. The primary output of this task is the manually created `data/labeled_data.conll` file.
      
3.  `notebooks/03_Model_Finetuning.ipynb`:
    *   Reads the labeled data, tokenizes it, and fine-tunes the primary NER model. Saves the trained model to the models/ directory.

4.  Subsequent Notebooks (`04` to `06`):
    *   These notebooks handle model comparison, interpretability, and the final business logic for the FinTech scorecard, respectively.


## Author
Abenezer M. Woldesenbet
