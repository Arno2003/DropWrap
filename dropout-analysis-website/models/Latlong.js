const { Schema, model, models } = require("mongoose");

const LatlongSchema = new Schema({
  Location: String,
  Social_Category: String,
  Girls: Number,
  Boys: Number,
  Overall: Number,
  Girls1: Number,
  Boys1: Number,
  Overall1: Number,
  Girls2: Number,
  Boys2: Number,
  Overall2: Number,
  latitude: Number,
  longitude: Number,
});

const Latlong = models?.Product || model("Latlong", LatlongSchema);

export default Latlong;
