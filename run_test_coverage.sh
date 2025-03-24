#!/bin/bash

echo "🧪 Running test suite with coverage..."

# Exit immediately if a command exits with a non-zero status
set -e

# Run pytest with coverage
pytest --cov=app tests/ --cov-report=term-missing --cov-report=xml

echo ""
echo "✅ Tests completed successfully!"
echo "📊 Coverage report generated at: coverage.xml"

# Optional: generate HTML report too
# pytest --cov=app tests/ --cov-report=html
# echo "🌐 HTML coverage report: open htmlcov/index.html"

