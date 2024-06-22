# generate_page.py
import datetime

content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My GitHub Page</title>
</head>
<body>
    <h1>Welcome to My GitHub Page</h1>
    <p>This page was generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.</p>
    <h2>Trigger Action</h2>
    <p>Click the button below to run the Python script and update this page:</p>
    <a href="https://github-action-button.web.app/repos/Abilipro/abilipro.github.io/button?name=Run&eventType=run-action&type=simple&action=dispatch">
        <img src="https://github-action-button.web.app/buttons/simple.svg?name=Run&eventType=run-action&type=simple&action=dispatch" alt="Run Action">
    </a>
</body>
</html>
"""

with open('exp_actions_1.html', 'w') as file:
    file.write(content)
