# Bitcoin Price Prediction using LSTM

This project implements a Long Short-Term Memory (LSTM) neural network to predict Bitcoin prices using historical data.

## Files

- `CryptoPrediction_Fixed.ipynb` - Main Jupyter notebook with the LSTM model
- `CryptoPrediction.ipynb` - Original notebook (has import issues)
- `requirements.txt` - Required Python packages
- `test_imports.py` - Script to test if all imports work
- `fix_keras.py` - Script to fix Keras import issues
- `README.md` - This file

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test Imports** (Optional)
   ```bash
   python test_imports.py
   ```

3. **Run the Notebook**
   - Open `CryptoPrediction_Fixed.ipynb` in Jupyter Lab/Notebook
   - Or use VS Code with Jupyter extension

## What the Model Does

1. **Data Collection**: Downloads Bitcoin price data using yfinance
2. **Data Preprocessing**: 
   - Normalizes price data using MinMaxScaler
   - Creates time series sequences for LSTM input
3. **Model Architecture**:
   - LSTM layer with 10 units
   - Dense output layer
   - Uses Adam optimizer and MSE loss
4. **Training**: Trains on 60% of data, validates on 40%
5. **Prediction**: Predicts next 30 days of Bitcoin prices
6. **Visualization**: Creates interactive plots using Plotly

## Key Features

- **Time Series Analysis**: Uses 15-day windows to predict next day prices
- **Interactive Plots**: Plotly visualizations for better data exploration
- **Model Evaluation**: Multiple metrics (RMSE, MAE, R², etc.)
- **Future Predictions**: Predicts 30 days into the future

## Requirements

- Python 3.8+
- TensorFlow 2.10+
- pandas, numpy, matplotlib
- scikit-learn
- plotly
- yfinance
- jupyter

## Usage

1. Open the notebook in Jupyter:
   ```bash
   jupyter lab CryptoPrediction_Fixed.ipynb
   ```

2. Run all cells sequentially

3. The notebook will:
   - Download Bitcoin data automatically
   - Train the LSTM model
   - Generate predictions and visualizations

## Model Performance

The model provides:
- Training and validation loss curves
- Comparison between actual vs predicted prices
- Future price predictions with visualizations
- Multiple evaluation metrics

## Notes

- The model uses recent Bitcoin data (2023-2024) for better relevance
- Predictions are for educational purposes only
- Cryptocurrency markets are highly volatile and unpredictable
- Always do your own research before making investment decisions

## Troubleshooting

If you encounter import errors:
1. Run `python fix_keras.py` to fix Keras issues
2. Ensure all packages are installed: `pip install -r requirements.txt`
3. Check Python version compatibility

## License

This project is for educational purposes only.