#!/bin/bash

# Sweet Shop Management System Startup Script

echo "🍭 Starting Sweet Shop Management System..."
echo "=============================================="

# Check if MongoDB is running
if ! pgrep -x "mongod" > /dev/null; then
    echo "⚠️  MongoDB is not running. Please start MongoDB first:"
    echo "   brew services start mongodb-community"
    echo "   or"
    echo "   mongod"
    echo ""
fi

# Start backend
echo "🚀 Starting Backend Server..."
cd backend
source venv/bin/activate
python run_server.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
echo "🎨 Starting Frontend Server..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo ""
echo "✅ Both servers are starting up!"
echo "   Backend API: http://localhost:8000"
echo "   Frontend App: http://localhost:3000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ Servers stopped"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for both processes
wait
