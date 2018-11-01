const fs = require('fs');

let load = 'C:\\Users\\lyfw2\\OneDrive\\Photos';

let files = fs.readdir(load, (err, file)=> {
    if (file.indexOf('SPSCF') == -1) {
    } else {
        console.log(file);
    }
});
