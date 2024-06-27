import clientPromise from "../../../lib/mongodb.js";

export default async (req, res) => {
  try {
    const client = await clientPromise;
    const db = client.db("Long_Lat");
    const movies = await db
      .collection("Langlot_nos")
      .find({})
      .sort({ metacritic: -1 })
      .limit(10)
      .toArray();
    res.json(movies);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};
