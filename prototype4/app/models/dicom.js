

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var dicomSchema = new Schema({
label: {type: String, required: true, unique: true},
pixel_array: String
});

var Dicom = mongoose.model('Dicom', dicomSchema);

module.exports = Dicom;
