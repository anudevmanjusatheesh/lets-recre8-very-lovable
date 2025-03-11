const express = require('express');
const path = require('path');
const app = express();

const PORT = 8050;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// For any other routes, send back index.html so that frontend routing can work if needed
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});