const mongoose = require('mongoose');

const ReviewSchema = new mongoose.Schema({
  id:            { type: Number },
  name:          { type: String, required: true },
  dealership:    { type: Number, required: true },
  review:        { type: String, required: true },
  purchase:      { type: Boolean, default: false },
  purchase_date: { type: String },
  car_make:      { type: String },
  car_model:     { type: String },
  car_year:      { type: Number },
}, { timestamps: true });

module.exports = mongoose.model('Review', ReviewSchema);
