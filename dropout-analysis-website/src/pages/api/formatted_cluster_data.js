import clientPromise from "../../../lib/mongodb.js";

export default async (req, res) => {
  try {
    const dbName = req.query.dbName || "Gujarat";
    const client = await clientPromise;
    const db = client.db(dbName); //  database name
    const result = await db
      .collection("formatted_cluster_data")
      .find({})
      .sort({ metacritic: -1 })
      .toArray();
    res.json(result);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};
