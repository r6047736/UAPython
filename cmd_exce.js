
var http = require("http");
var fs = require("fs");

var events = require("events");
var eventEmitter = new events.EventEmitter();


var listener1 = function listener1(){
    console.log("listen1 function called");

}

var listener2 = function listener2(){
    console.log("listener function called")
}
eventEmitter.addListener('connection',listener1);

eventEmitter.on('connection',listener2);

var c = events.EventEmitter.listenerCount(eventEmitter,'connection');
console.log(c + "listener is listening ");


eventEmitter.emit('connection');

////////

eventEmitter.removeListener('connection',listener1);
console.log("Listener1 will not listen now");


eventEmitter.emit('connection');

 c = events.EventEmitter.listenerCount(eventEmitter,'connection');
console.log(c + "listener is listening ");








/*
fs.readFile('input.txt', function (err, data) {
   if (err) return console.error(err);
   console.log("read 2 =========> "+data.toString());
});

console.log("Program Ended2");
*/








http.createServer(function(request, response){
	
	response.writeHead(200,{'Content-Type': 'text/plain'});
	
	response.end("Hello world")
}).listen(8001);

console.log('Server running at http://127.0.0.1:8001/');
/*
var exec = require('child_process').exec; 
exec('pwd', function(err,stdout,stderr){
    if(err) {
        console.log('get system crash');
    } else {
       
     //   var data = JSON.parse(stdout);
        console.log(stdout);
    }
});
*/

