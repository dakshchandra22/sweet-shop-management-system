# 🧪 Testing Guide

This document provides comprehensive information about testing the Sweet Shop Management System.

## 📋 Test Overview

The project includes comprehensive test coverage for both backend (Python/FastAPI) and frontend (React) components.

### Test Structure

```
sweet-shop-management/
├── backend/
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py          # Pytest fixtures and configuration
│   │   ├── test_auth.py         # Authentication tests
│   │   ├── test_sweets.py       # Sweet management tests
│   │   └── test_database.py     # Database operation tests
│   └── pytest.ini              # Pytest configuration
├── frontend/
│   ├── src/
│   │   ├── __tests__/
│   │   │   ├── App.test.js
│   │   │   ├── components/
│   │   │   │   ├── SearchBar.test.js
│   │   │   │   ├── Login.test.js
│   │   │   │   └── SweetCard.test.js
│   │   │   └── contexts/
│   │   │       └── AuthContext.test.js
│   │   └── setupTests.js        # Jest setup
│   └── package.json             # Includes testing dependencies
├── run_tests.sh                 # Test runner script
└── .github/workflows/test.yml   # CI/CD pipeline
```

## 🐍 Backend Testing (Python/pytest)

### Prerequisites

- Python 3.8+
- MongoDB (local or test instance)
- Virtual environment activated

### Running Backend Tests

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v

# Run tests with markers
pytest -m auth
pytest -m unit
```

### Backend Test Categories

#### 1. Authentication Tests (`test_auth.py`)
- ✅ User registration (success, duplicate username/email, weak password)
- ✅ User login (success, invalid credentials, non-existent user)
- ✅ Admin user creation
- ✅ Password hashing and verification
- ✅ JWT token creation and verification

#### 2. Sweet Management Tests (`test_sweets.py`)
- ✅ Get all sweets (empty, with data)
- ✅ Create sweet (success, unauthorized, duplicate name)
- ✅ Update sweet (success, unauthorized, not found)
- ✅ Delete sweet (success, unauthorized)
- ✅ Purchase sweet (success, insufficient quantity, not found)

#### 3. Database Tests (`test_database.py`)
- ✅ User operations (get by username/email, create)
- ✅ Sweet operations (CRUD operations)
- ✅ Quantity updates
- ✅ Error handling

### Backend Test Configuration

The `pytest.ini` file configures:
- Test discovery patterns
- Coverage requirements (80% minimum)
- Output formatting
- Markers for test categorization

## ⚛️ Frontend Testing (React/Jest)

### Prerequisites

- Node.js 14+
- npm or yarn

### Running Frontend Tests

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run all tests
npm test

# Run tests with coverage
npm test -- --coverage

# Run tests in watch mode
npm test -- --watch

# Run tests without watch mode (CI)
npm test -- --watchAll=false
```

### Frontend Test Categories

#### 1. Component Tests
- ✅ **SearchBar**: Search functionality, sorting, admin features
- ✅ **Login**: Form validation, API calls, error handling
- ✅ **SweetCard**: Display, purchase, edit functionality
- ✅ **App**: Main application rendering

#### 2. Context Tests
- ✅ **AuthContext**: Login, logout, registration, token handling

### Frontend Test Configuration

The testing setup includes:
- **Jest**: Test runner and assertion library
- **React Testing Library**: Component testing utilities
- **@testing-library/jest-dom**: Custom matchers
- **@testing-library/user-event**: User interaction simulation

## 🚀 Running All Tests

### Using the Test Runner Script

```bash
# Make script executable (if not already)
chmod +x run_tests.sh

# Run all tests (backend + frontend)
./run_tests.sh
```

The script will:
1. Set up virtual environments
2. Install dependencies
3. Run backend tests with pytest
4. Run frontend tests with Jest
5. Display a summary of results

### Manual Test Execution

```bash
# Backend tests
cd backend && source venv/bin/activate && pytest

# Frontend tests
cd frontend && npm test -- --watchAll=false
```

## 📊 Test Coverage

### Backend Coverage
- **Target**: 80% minimum coverage
- **Current**: Comprehensive coverage of all modules
- **Report**: Generated in `backend/htmlcov/index.html`

### Frontend Coverage
- **Target**: 80% minimum coverage
- **Current**: Component and context coverage
- **Report**: Generated in `frontend/coverage/lcov-report/index.html`

## 🔧 Test Configuration

### Environment Variables

For testing, set these environment variables:

```bash
# Backend testing
export TEST_MONGODB_URL="mongodb://localhost:27017"
export MONGODB_URL="mongodb://localhost:27017"

# Frontend testing
export REACT_APP_API_BASE_URL="http://localhost:8000/api"
```

### Test Database

Tests use a separate test database (`sweet_shop_test`) to avoid affecting production data.

## 🎯 Test Markers

### Backend Markers
- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.auth`: Authentication tests
- `@pytest.mark.sweets`: Sweet management tests
- `@pytest.mark.database`: Database tests

### Usage
```bash
# Run only unit tests
pytest -m unit

# Run only authentication tests
pytest -m auth

# Run integration tests
pytest -m integration
```

## 🚦 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/test.yml`) runs:
1. **Backend Tests**: Python/pytest with MongoDB service
2. **Frontend Tests**: React/Jest with Node.js
3. **Integration Tests**: Full stack testing
4. **Coverage Reports**: Uploaded to Codecov

## 🐛 Debugging Tests

### Backend Debugging
```bash
# Run with detailed output
pytest -v -s

# Run specific test with debugging
pytest tests/test_auth.py::TestAuthentication::test_user_registration_success -v -s

# Run with pdb debugger
pytest --pdb
```

### Frontend Debugging
```bash
# Run tests in debug mode
npm test -- --verbose

# Run specific test file
npm test SearchBar.test.js

# Run with coverage and debug
npm test -- --coverage --verbose
```

## 📝 Writing New Tests

### Backend Test Template
```python
def test_feature_name(self, client, test_db, sample_data):
    """Test description"""
    # Arrange
    # Act
    # Assert
    assert response.status_code == 200
    assert data["key"] == "expected_value"
```

### Frontend Test Template
```javascript
test('renders component correctly', () => {
  render(<Component {...props} />);
  expect(screen.getByText('Expected Text')).toBeInTheDocument();
});
```

## 🎉 Test Best Practices

1. **Isolation**: Each test should be independent
2. **Mocking**: Mock external dependencies
3. **Coverage**: Aim for high test coverage
4. **Naming**: Use descriptive test names
5. **Setup/Teardown**: Clean up after tests
6. **Assertions**: Use specific assertions
7. **Error Cases**: Test both success and failure scenarios

## 📚 Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

---

**Happy Testing! 🧪✨**
