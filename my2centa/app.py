"""
My2Centa - Inflation Calculator
Calculates the current value of 2 cents from a past year, adjusted for inflation.
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Historical CPI data (Annual averages from US Bureau of Labor Statistics)
# Base period: 1982-84 = 100
CPI_DATA = {
    1913: 9.9,
    1920: 20.0,
    1930: 16.7,
    1940: 14.0,
    1950: 24.1,
    1960: 29.6,
    1970: 38.8,
    1980: 82.4,
    1990: 130.7,
    2000: 172.2,
    2005: 195.3,
    2010: 218.056,
    2011: 224.939,
    2012: 229.594,
    2013: 232.957,
    2014: 236.736,
    2015: 237.017,
    2016: 240.007,
    2017: 245.120,
    2018: 251.107,
    2019: 255.657,
    2020: 258.811,
    2021: 270.970,
    2022: 292.655,
    2023: 304.702,
    2024: 310.0,  # Estimated
    2025: 313.5,  # Estimated
}

def calculate_inflation(amount, from_year, to_year):
    """
    Calculate inflation-adjusted value

    Args:
        amount: Original amount
        from_year: Year of the original amount
        to_year: Target year

    Returns:
        Inflation-adjusted amount
    """
    if from_year not in CPI_DATA or to_year not in CPI_DATA:
        return None

    cpi_from = CPI_DATA[from_year]
    cpi_to = CPI_DATA[to_year]

    # Inflation adjustment formula: (CPI_to / CPI_from) * amount
    adjusted_amount = (cpi_to / cpi_from) * amount

    return adjusted_amount

@app.route('/')
def index():
    """Render the main page"""
    current_year = datetime.now().year
    available_years = sorted(CPI_DATA.keys())
    return render_template('index.html',
                         current_year=current_year,
                         available_years=available_years)

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate the inflation-adjusted value of 2 cents"""
    try:
        data = request.get_json()
        advice_year = int(data.get('year'))
        current_year = datetime.now().year

        # Validate year
        if advice_year not in CPI_DATA:
            return jsonify({
                'error': f'CPI data not available for year {advice_year}. Available years: {min(CPI_DATA.keys())} - {max(CPI_DATA.keys())}'
            }), 400

        if advice_year > current_year:
            return jsonify({
                'error': 'Cannot calculate inflation for future years'
            }), 400

        # Calculate inflation-adjusted value
        original_amount = 0.02  # 2 cents

        # Use the most recent year available in our data
        to_year = min(current_year, max(CPI_DATA.keys()))
        adjusted_value = calculate_inflation(original_amount, advice_year, to_year)

        if adjusted_value is None:
            return jsonify({
                'error': 'Unable to calculate inflation'
            }), 500

        # Calculate percentage increase
        percentage_increase = ((adjusted_value - original_amount) / original_amount) * 100

        return jsonify({
            'original_year': advice_year,
            'current_year': to_year,
            'original_value': original_amount,
            'adjusted_value': round(adjusted_value, 4),
            'adjusted_value_cents': round(adjusted_value * 100, 2),
            'percentage_increase': round(percentage_increase, 2),
            'message': f'Your "2 cents" from {advice_year} is worth ${adjusted_value:.4f} ({adjusted_value * 100:.2f} cents) in {to_year} dollars!'
        })

    except ValueError as e:
        return jsonify({'error': 'Invalid year provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'app': 'my2centa'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
