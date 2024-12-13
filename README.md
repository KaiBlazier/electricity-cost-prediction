# electricity-cost-prediction
This project predicts future electricity costs based on historical data from 2019 to 2023.

## Setup

1. **Clone the repository**:
   git clone https://github.com/yourusername/electricity-cost-prediction.git
   cd electricity-cost-prediction
## Create a virtual enviorment:
python -m venv venv source
 venv/Scripts/activate
## install dependencies:
pip install -r requirements.txt
## convert Excel files to CSV:
python scripts/convert_to_csv.py
## Load and analyze data: 
python scripts/analyze_data.py
## Predict future costs:
python scripts/predict_future.py
