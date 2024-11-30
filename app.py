from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result='')

@app.route('/get_plan', methods=['POST'])
def get_plan():
    body_fat = float(request.form['bodyFat'])
    calories = int(request.form['calories'])
    workout_plan = request.form['workoutPlan']

    result = ''

    if body_fat < 15:
        result += 'You have a low body fat percentage. Consider a muscle gain plan.\n'
    elif body_fat < 25:
        result += 'You have a moderate body fat percentage. Consider a balanced plan.\n'
    else:
        result += 'You have a high body fat percentage. Consider a fat loss plan.\n'

    if calories < 2000:
        result += 'Your calorie intake is low. Consider increasing your calorie intake.\n'
    elif calories < 2500:
        result += 'Your calorie intake is moderate. Maintain this level for balanced results.\n'
    else:
        result += 'Your calorie intake is high. Consider a calorie deficit plan.\n'

    result += f'Your current workout plan: {workout_plan}'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

