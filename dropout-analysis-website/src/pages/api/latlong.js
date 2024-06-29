import clientPromise from "../../../lib/mongodb.js";

export default async (req, res) => {
  try {
    console.log(req.query.dbName);
    const dbName = req.query.dbName || "Gujarat";
    const client = await clientPromise;
    const db = client.db(dbName);
    const result = await db
      .collection("latlong")
      .find({})
      .sort({ metacritic: -1 })
      .limit(10)
      .toArray();
    res.json(result);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};
