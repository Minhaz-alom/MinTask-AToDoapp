#imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

#my app (Python hub starts)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# @app.template_filter('local_time')
# def local_time(utc_dt):
#     # Adjust for your timezone (e.g., +5:30 for IST)
#     local_dt = utc_dt + timedelta(hours=5, minutes=30)
#     return local_dt.strftime('%Y-%m-%d %H:%M:%S')

#Database model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)  # Changed to lowercase
    created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Task {self.id}"
    

with app.app_context():
        db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    #add tasks
    if request.method == 'POST':
        current_task = request.form['content']
        new_task = Task(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Error adding task: {e}"
        
    #see all tasks
    else:
        tasks = Task.query.order_by(Task.created).all()
    
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Error deleting task: {e}"

# Add this update route as well since you have it in your HTML
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Error updating task: {e}"
    
    return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)

