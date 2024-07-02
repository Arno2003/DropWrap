import clientPromise from "../../../lib/mongodb.js";

export default async (req, res) => {
  try {
    console.log(req.query.dbName);
    const dbName = req.query.dbName || "Gujarat";
    // console.log(req.query);
    const client = await clientPromise;
    const db = client.db(dbName);
    const result = await db
      .collection("latlong")
      .find({
        Social_Category: req.query.caste,
      })
      .sort({ metacritic: -1 })
      .toArray();
    res.json(result);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};
