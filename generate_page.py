# generate_page.py
import datetime

content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My GitHub Page</title>
    <meta name="github-token" content="GITHUB_TOKEN_PLACEHOLDER">
</head>
<body>
    <h1>Welcome to My GitHub Page</h1>
    <p>This page was generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.</p>
    <h2>Trigger Action</h2>
    <p>Click the button below to run the Python script and update this page:</p>
    <button id="run-action-button">Run Action</button>

    <script>
        document.getElementById("run-action-button").addEventListener("click", function(){
            const token = document.querySelector('meta[name="github-token"]').content;
            fetch('https://api.github.com/repos/Abilipro/abilipro.github.io/dispatches', {
                method: 'POST',
                headers: {
                    'Accept': 'application/vnd.github.everest-preview+json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    event_type: 'run-action'
                })
            }).then(response => {
                if(response.ok) {
                    alert("Action triggered successfully!");
                } else {
                    alert("Failed to trigger action.");
                }
            }).catch(error => {
                console.error('Error:', error);
                alert("Error triggering action.");
            });
        });
    </script>
</body>
</html>
"""

with open('exp_actions_1.html', 'w') as file:
    file.write(content)
