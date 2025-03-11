const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

// Folder from which to list files (adjust as needed)
const FILES_DIR = path.join(__dirname, 'files');

// Serve static files from the "public" folder
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to parse JSON bodies (for chat requests)
app.use(express.json());

// Helper function to recursively list files and directories
function listFiles(dirPath, relativePath = '') {
  const items = fs.readdirSync(dirPath, { withFileTypes: true });
  return items.map(item => {
    const itemRelativePath = path.join(relativePath, item.name);
    if (item.isDirectory()) {
      return {
        name: item.name,
        type: 'directory',
        path: itemRelativePath,
        children: listFiles(path.join(dirPath, item.name), itemRelativePath)
      };
    } else {
      return {
        name: item.name,
        type: 'file',
        path: itemRelativePath
      };
    }
  });
}

// Endpoint to return the file tree
app.get('/files', (req, res) => {
  try {
    const fileList = listFiles(FILES_DIR);
    res.json(fileList);
  } catch (error) {
    res.status(500).json({ error: error.toString() });
  }
});

// Endpoint to fetch file content given its relative path
app.get('/file', (req, res) => {
  const relPath = req.query.path;
  if (!relPath) {
    return res.status(400).json({ error: 'No file path specified' });
  }
  const filePath = path.join(FILES_DIR, relPath);
  // Ensure that filePath is within FILES_DIR for security
  if (!filePath.startsWith(FILES_DIR)) {
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

// Default route: serve the front‑end
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
