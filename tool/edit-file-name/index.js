const fs = require('fs');
const path = require('path');

let load = 'D:\\test';

let files = fs.readdir(load, (err, files)=> {
    if (err) {
        console.warn(err);
        return false;
    }
    for (let file of files) {
        if (file.includes('SPSCF')) {
            let oldName = path.join(load, file);
            let fileType = path.parse(file).ext;
            let fileName = path.parse(file).name;
            let newName = 'CHD' + fileName.slice(5) + fileType;
            newName = path.join(load, newName);
            fs.rename(oldName, newName, (err) => {
                if (err) throw err;
            });
        }
    }
});
