// server.js

// =============================================================================

// call the packages we need
var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');
var util        = require('util')

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8060;        // set our port

// DATABASE CONNECTION
// =============================================================================

var mongoose = require('mongoose');

var uri = 'mongodb://127.0.0.1:27017';
mongoose.Promise = global.Promise
mongoose.connect(uri);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));

// var Dicom = require('./app/models/dicom');
//
// var dicom1 = new Dicom({
//   label: 'patient1',
//   pixel_array: '2048,2011,2048...'
// })
//
// dicom1.save(function(err) {
//   if (err) throw err;
//   console.log('dicom push successful');
// });

// PYTHON READER
var spawn = require("child_process").spawn;
var proc = spawn('python',["./app/scrpts/python/test.py"]);

proc.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
  console.log('something happend in here');
});

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router

// middleware to use for all requests
router.use(function(req, res, next) {
    // do logging
    console.log('Something is happening.');
    next(); // make sure we go to the next routes and don't stop here
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });
});

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);
