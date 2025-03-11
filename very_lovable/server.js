const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

// Set the absolute path to the external_sandbox folder.
// Change this path to your actual external sandbox location.
const EXTERNAL_SANDBOX_PATH = '../external_sandbox'; 

// Function to recursively list files while skipping "node_modules"
function listFiles(dirPath, relativePath = '') {
  const items = fs.readdirSync(dirPath, { withFileTypes: true });
  const result = [];
  items.forEach(item => {
    // Skip the node_modules folder entirely
    if (item.name === 'node_modules') return;
    const itemRelativePath = path.join(relativePath, item.name);
    if (item.isDirectory()) {
      result.push({
        name: item.name,
        type: 'directory',
        path: itemRelativePath,
        children: listFiles(path.join(dirPath, item.name), itemRelativePath)
      });
    } else {
      result.push({
        name: item.name,
        type: 'file',
        path: itemRelativePath
      });
    }
  });
  return result;
}

// Route to list the file structure from the external_sandbox folder
app.get('/external_sandbox', (req, res) => {
  try {
    const fileList = listFiles(EXTERNAL_SANDBOX_PATH);
    res.json(fileList);
  } catch (error) {
    res.status(500).json({ error: error.toString() });
  }
});

// Route to fetch content of a specific file from external_sandbox
app.get('/external_file', (req, res) => {
  const relPath = req.query.path;
  if (!relPath) {
    return res.status(400).json({ error: 'No file path specified' });
  }
  const filePath = path.join(EXTERNAL_SANDBOX_PATH, relPath);
  // Security check: ensure filePath is within EXTERNAL_SANDBOX_PATH
  if (!filePath.startsWith(EXTERNAL_SANDBOX_PATH)) {
    return res.status(400).json({ error: 'Invalid file path' });
  }
  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      return res.status(404).json({ error: 'File not found' });
    }
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) return res.status(500).json({ error: err.toString() });
      res.type('text/plain').send(data);
    });
  });
});

// Serve static files (your UI)
app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
