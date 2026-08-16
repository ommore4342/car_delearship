const mongoose = require('mongoose');

const DealerSchema = new mongoose.Schema({
  id:        { type: Number, required: true, unique: true },
  city:      { type: String, required: true },
  state:     { type: String, required: true },
  zip:       { type: String },
  address:   { type: String },
  full_name: { type: String, required: true },
  phone:     { type: String },
}, { timestamps: true });

module.exports = mongoose.model('Dealer', DealerSchema);
