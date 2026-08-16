const Dealer = require('../models/dealer');
const Review = require('../models/review');

// GET /fetchDealers
const fetchDealers = async (req, res) => {
  try {
    const dealers = await Dealer.find({}, '-_id -__v -createdAt -updatedAt');
    res.json(dealers);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// GET /fetchDealers/:state
const fetchDealersByState = async (req, res) => {
  try {
    const dealers = await Dealer.find(
      { state: { $regex: new RegExp(`^${req.params.state}$`, 'i') } },
      '-_id -__v -createdAt -updatedAt'
    );
    res.json(dealers);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// GET /fetchDealer/:id
const fetchDealerById = async (req, res) => {
  try {
    const dealer = await Dealer.findOne({ id: Number(req.params.id) }, '-_id -__v -createdAt -updatedAt');
    if (!dealer) return res.status(404).json({ error: 'Dealer not found' });
    res.json(dealer);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// GET /fetchReviews/dealer/:id
const fetchReviewsByDealer = async (req, res) => {
  try {
    const reviews = await Review.find(
      { dealership: Number(req.params.id) },
      '-_id -__v -createdAt -updatedAt'
    );
    res.json(reviews);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// POST /insertReview
const insertReview = async (req, res) => {
  try {
    const review = new Review(req.body);
    await review.save();
    res.json({ status: 200, message: 'Review inserted successfully', review });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

module.exports = {
  fetchDealers,
  fetchDealersByState,
  fetchDealerById,
  fetchReviewsByDealer,
  insertReview,
};
