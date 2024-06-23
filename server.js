const express = require('express');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
const port = 3000;

app.use(express.static('public'));

app.post('/trigger-workflow', async (req, res) => {
    const token = process.env.GH_PAT;

    const response = await fetch('https://api.github.com/repos/Abilipro/abilipro.github.io/dispatches', {
        method: 'POST',
        headers: {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            event_type: 'run-action'
        })
    });

    const responseBody = await response.text();  // Get the response body as text for logging

    console.log('GitHub API Response:', responseBody);

    if (response.ok) {
        res.status(200).send('Workflow triggered successfully!');
    } else {
        res.status(response.status).send(`Failed to trigger workflow. GitHub API Response: ${responseBody}`);
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
