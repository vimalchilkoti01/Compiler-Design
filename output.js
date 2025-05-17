const fs = require('fs');
setInterval(() => {
    const data = fs.readFileSync('website_logs', 'utf8');
    data.split('\n').forEach(line => console.log(line));
}, 10000);