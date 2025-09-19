#!/bin/bash

# Sweet Shop - Simple Start Script
echo "🍭 Sweet Shop - Starting Application"
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Function to start backend
start_backend() {
    echo "🚀 Starting Backend Server..."
    cd backend
    if [ ! -d "venv" ]; then
        echo "📦 Creating virtual environment..."
        python3 -m venv venv
    fi
    
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
    
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    
    echo "🚀 Starting FastAPI server..."
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
    BACKEND_PID=$!
    echo "✅ Backend started (PID: $BACKEND_PID)"
    cd ..
}

# Function to start frontend
start_frontend() {
    echo "🚀 Starting Frontend Server..."
    cd frontend
    
    if [ ! -d "node_modules" ]; then
        echo "📦 Installing dependencies..."
        npm install
    fi
    
    echo "🚀 Starting React server..."
    npm start &
    FRONTEND_PID=$!
    echo "✅ Frontend started (PID: $FRONTEND_PID)"
    cd ..
}

# Function to run tests
run_tests() {
    echo "🧪 Running Backend Tests..."
    cd backend
    source venv/bin/activate
    python test_simple_tdd.py
    cd ..
    
    echo "🧪 Frontend tests available at: frontend/run_tests.html"
}

# Function to stop servers
stop_servers() {
    echo "🛑 Stopping servers..."
    pkill -f "uvicorn main:app"
    pkill -f "npm start"
    echo "✅ Servers stopped"
}

# Main menu
show_menu() {
    echo ""
    echo "Choose an option:"
    echo "1. Start Backend Only"
    echo "2. Start Frontend Only"
    echo "3. Start Both Servers"
    echo "4. Run Tests"
    echo "5. Stop Servers"
    echo "6. Exit"
    echo ""
}

# Handle user input
handle_choice() {
    case $1 in
        1)
            start_backend
            echo "🌐 Backend running at: http://localhost:8000"
            ;;
        2)
            start_frontend
            echo "🌐 Frontend running at: http://localhost:3000"
            ;;
        3)
            start_backend
            sleep 3
            start_frontend
            echo "🌐 Application running at: http://localhost:3000"
            echo "🌐 API running at: http://localhost:8000"
            ;;
        4)
            run_tests
            ;;
        5)
            stop_servers
            ;;
        6)
            echo "👋 Goodbye!"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice. Please try again."
            ;;
    esac
}

# Trap to stop servers on script exit
trap 'stop_servers; exit' INT TERM

# Main loop
while true; do
    show_menu
    read -p "Enter your choice (1-6): " choice
    handle_choice $choice
    
    if [ "$choice" != "6" ]; then
        echo ""
        read -p "Press Enter to continue..."
        clear
    fi
done

