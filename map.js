var spawn = require('child_process').spawn;
var py = spawn('python', ['main.py']);
var dataString = '';

py.stdout.on('data', function(data){
    dataString += data.toString();
    }
);

py.stdout.on('end', function(){
    console.log(dataString);
    }
);



