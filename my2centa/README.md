# My2Centa - Inflation Calculator 💰

A fun web application that calculates the inflation-adjusted value of "two cents" from any given year to the present day. Ever wondered what someone's advice from 1990 would be worth today? Now you can find out!

## Features

- 🎯 Simple, intuitive interface
- 📊 Historical CPI data from U.S. Bureau of Labor Statistics
- 💵 Calculates inflation-adjusted values from 1913 to present
- 🎨 Beautiful, responsive design
- ⚡ Real-time calculations

## How It Works

The application uses the Consumer Price Index (CPI) data from the U.S. Bureau of Labor Statistics to calculate inflation. When someone says "here's my two cents," this app tells you what those 2 cents would actually be worth today after adjusting for inflation.

### Inflation Formula

```
Adjusted Value = (CPI_current / CPI_past) × Original Amount
```

Where:
- `CPI_current` = Current year's Consumer Price Index
- `CPI_past` = Past year's Consumer Price Index
- `Original Amount` = $0.02 (2 cents)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Navigate to the my2centa directory:
   ```bash
   cd my2centa
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode

Run the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Production Mode

For production deployment, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter the year when someone gave you their "two cents" of advice
3. Click "Calculate Worth Today"
4. See the inflation-adjusted value and percentage increase

## API Endpoints

### `GET /`
Returns the main HTML interface

### `POST /calculate`
Calculates inflation-adjusted value

**Request Body:**
```json
{
  "year": 1990
}
```

**Response:**
```json
{
  "original_year": 1990,
  "current_year": 2025,
  "original_value": 0.02,
  "adjusted_value": 0.0479,
  "adjusted_value_cents": 4.79,
  "percentage_increase": 139.5,
  "message": "Your '2 cents' from 1990 is worth $0.0479 (4.79 cents) in 2025 dollars!"
}
```

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "app": "my2centa"
}
```

## Data Source

The Consumer Price Index (CPI) data is sourced from the U.S. Bureau of Labor Statistics. The base period is 1982-84 = 100.

Available years: 1913 - 2025 (with recent years estimated)

## Project Structure

```
my2centa/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # HTML template
└── static/               # Static assets (if needed)
```

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Frontend:** HTML, CSS, JavaScript
- **Data:** U.S. Bureau of Labor Statistics CPI data

## Example Use Cases

- "My grandfather told me in 1950 that his two cents would be valuable someday..."
- "I gave someone my two cents in 2000, what's it worth now?"
- "How much has inflation affected the value of 2 cents since 1980?"

## Future Enhancements

- [ ] Add support for custom amounts (not just 2 cents)
- [ ] Include international inflation data
- [ ] Add visualization charts showing inflation trends
- [ ] Support for month-specific CPI data
- [ ] Compare multiple years side-by-side

## License

This project is part of the gemini-fullstack-langgraph-quickstart repository and follows the same Apache License 2.0.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with 💜 by the community
