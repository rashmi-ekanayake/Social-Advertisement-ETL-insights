# Social Media Buying Behavior Analysis

## Project Overview
This project analyzes social media advertisement data to understand consumer buying behavior. It implements a complete ETL (Extract, Transform, Load) pipeline using Python to process the data, clean it, and generate meaningful insights through visualizations.
The goal is to explore how factors like age and estimated salary influence purchase decisions after viewing advertisements.

## ETL Pipeline

- **Extract** : Loads the dataset (`social_ads.csv`) from the `data/` folder.
- **Transform** : Cleans the data by removing duplicates and missing values, and categorizes age into groups.
- **Load** : Saves the cleaned dataset into the `insights/` folder for further analysis.
- **Insights Generation** : Creates visualizations (purchase distributions by age and salary) and calculates purchase rates, saving charts in the `insights/` folder.

## How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/social-media-buying-behavior.git
   cd social-media-buying-behavior
2. **Install dependencies**

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate           # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. **Download the dataset**

Download the dataset from Kaggle and place the file `social_ads.csv` into the `data/` folder:

👉 [Social Advertisement Dataset on Kaggle](https://www.kaggle.com/datasets/sakshisatre/social-advertisement-dataset/data)

4. **Run the pipeline**

```bash
python main.py
```
This will execute the ETL process and generate insights saved in the insights/ folder.

