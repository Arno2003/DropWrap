import mongoose from "mongoose";
// track the connection
let isConnected = false;
uri =
  "mongodb+srv://dropwrap:" +
  process.env.MONGO_PASSWORD +
  "@gujarat.jwam9ab.mongodb.net/?retryWrites=true&w=majority&appName=Gujarat";

export const connectToDataBase = async ({ db }) => {
  mongoose.set("strictQuery", true);
  if (isConnected) {
    console.log("DB connected already");
    return;
  }
  try {
    await mongoose.connect(uri, {
      dbName: db,
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    isConnected = true;
  } catch (error) {
    console.log(error);
  }
};
