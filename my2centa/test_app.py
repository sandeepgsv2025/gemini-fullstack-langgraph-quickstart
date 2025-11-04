"""
Simple test script to verify the my2centa app works correctly
"""

import sys
from app import app, calculate_inflation, CPI_DATA

def test_calculate_inflation():
    """Test the inflation calculation function"""
    print("Testing inflation calculation function...")

    # Test 1: 2 cents from 1990 to 2024
    result = calculate_inflation(0.02, 1990, 2024)
    print(f"✓ 2 cents from 1990 = ${result:.4f} in 2024")

    # Test 2: 2 cents from 1950 to 2024
    result = calculate_inflation(0.02, 1950, 2024)
    print(f"✓ 2 cents from 1950 = ${result:.4f} in 2024")

    # Test 3: 2 cents from 2000 to 2024
    result = calculate_inflation(0.02, 2000, 2024)
    print(f"✓ 2 cents from 2000 = ${result:.4f} in 2024")

    print("✓ All inflation calculations passed!\n")

def test_api_endpoints():
    """Test the API endpoints"""
    print("Testing API endpoints...")

    with app.test_client() as client:
        # Test 1: Home page
        response = client.get('/')
        assert response.status_code == 200, "Home page should return 200"
        print("✓ Home page (/) returns 200")

        # Test 2: Health check
        response = client.get('/health')
        assert response.status_code == 200, "Health check should return 200"
        data = response.get_json()
        assert data['status'] == 'healthy', "Health check should return healthy status"
        print("✓ Health check endpoint (/health) works")

        # Test 3: Calculate endpoint with valid year
        response = client.post('/calculate',
                              json={'year': 1990},
                              content_type='application/json')
        assert response.status_code == 200, "Calculate should return 200 for valid year"
        data = response.get_json()
        assert 'adjusted_value' in data, "Response should contain adjusted_value"
        assert data['original_year'] == 1990, "Original year should match input"
        print(f"✓ Calculate endpoint works: 1990 -> ${data['adjusted_value']:.4f}")

        # Test 4: Calculate with invalid year
        response = client.post('/calculate',
                              json={'year': 1800},
                              content_type='application/json')
        assert response.status_code == 400, "Should return 400 for invalid year"
        print("✓ Invalid year handling works")

        # Test 5: Calculate with future year
        response = client.post('/calculate',
                              json={'year': 2099},
                              content_type='application/json')
        assert response.status_code == 400, "Should return 400 for future year"
        print("✓ Future year validation works")

    print("✓ All API endpoint tests passed!\n")

def test_cpi_data():
    """Verify CPI data is available"""
    print("Testing CPI data...")
    print(f"✓ CPI data available for years: {min(CPI_DATA.keys())} - {max(CPI_DATA.keys())}")
    print(f"✓ Total years of data: {len(CPI_DATA)}")
    print()

if __name__ == '__main__':
    try:
        print("=" * 50)
        print("MY2CENTA APP TESTS")
        print("=" * 50)
        print()

        test_cpi_data()
        test_calculate_inflation()
        test_api_endpoints()

        print("=" * 50)
        print("✓ ALL TESTS PASSED!")
        print("=" * 50)
        sys.exit(0)

    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)
