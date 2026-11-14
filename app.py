from flask import Flask, request, render_template_string
from salary import calculate_bonus, calculate_total_salary, check_salary

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Salary Management</title>
</head>
<body style="font-family: Arial; text-align: center; padding: 40px;">
    <h2>Employee Salary Management</h2>

    <form method="POST">
        <input type="number" step="any" name="salary"
               placeholder="Enter basic salary" required>
        <button type="submit">Calculate Salary</button>
    </form>

    {% if result %}
        <h3>{{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            salary = float(request.form["salary"])

            if check_salary(salary) == "Invalid Salary":
                result = "Invalid Salary"
            else:
                bonus = calculate_bonus(salary)
                total = calculate_total_salary(salary)

                result = (
                    f"Basic Salary: {salary:.2f} | "
                    f"Bonus: {bonus:.2f} | "
                    f"Total Salary: {total:.2f}"
                )
        except ValueError:
            result = "Please enter a valid salary"

    return render_template_string(HTML, result=result)


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(debug=True)