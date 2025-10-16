MinTasks - Your Task Scheduler
A simple and elegant task management web application built with Flask that helps you organize your daily tasks efficiently.

https://img.shields.io/badge/MinTasks-Task%2520Scheduler-blue
https://img.shields.io/badge/Python-3.7%252B-green
https://img.shields.io/badge/Flask-2.0%252B-lightgrey

✨ Features
✅ Add new tasks with a clean, intuitive interface
✏️ Edit existing tasks with an update form
🗑️ Delete tasks you no longer need
📱 Responsive design that works on all devices
🎨 Beautiful UI with Tailwind CSS styling
💾 SQLite database for data persistence
⏰ Automatic timestamps for task creation

🚀 Quick Start
Prerequisites
Python 3.7 or higher
pip (Python package manager)


Installation & Setup
Clone the repository

git clone https://github.com/yourusername/mintasks.git
cd mintasks
Create a virtual environment (Required)

# On Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
Run the application

python app.py
Open your browser and navigate to:

📁 Project Structure
text
mintasks/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── instance/
│   └── database.db       # SQLite database (created automatically)
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main tasks page
│   └── update.html       # Edit task page
└── static/
    └── # Static files (CSS, JS, images)
🛠️ Technology Stack
Backend: Flask, SQLAlchemy

Frontend: HTML, Tailwind CSS, JavaScript

Database: SQLite

Styling: Tailwind CSS (CDN)

📋 API Routes
Route	Method	Description
/	GET, POST	View all tasks and add new tasks
/update/<id>	GET, POST	Edit a specific task
/delete/<id>	GET	Delete a specific task
🎯 Usage
Adding a Task: Type your task in the input field and click "Add Task"

Editing a Task: Click the "Edit" button next to any task

Deleting a Task: Click the "Delete" button next to any task

Viewing Tasks: All tasks are displayed in a beautiful table with creation timestamps

🔧 Configuration
The application uses SQLite as the default database. The database file is automatically created in the instance folder when you first run the application.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🐛 Troubleshooting
Common Issues
Virtual Environment Not Activated

# Make sure you see (venv) in your terminal
# If not, activate it again:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
Port Already in Use

# If port 5000 is busy, use a different port:
python app.py --port 5001
Dependencies Not Found

# Make sure virtual environment is activated, then:
pip install -r requirements.txt
📞 Support
If you have any questions or run into issues, please open an issue on GitHub.

Happy Task Managing! 🎉

MinTasks - Organize your life, one task at a time.
