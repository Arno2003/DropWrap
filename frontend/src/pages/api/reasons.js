import { connectToDatabase1 } from "../../../lib/mongodb";

export default async (req, res) => {
  try {
    const collectionName = "reasons"; // Collection name
    // const dbName = req.query.dbName || "Gujarat";
    const dbName = "Other";
    const client = await connectToDatabase1();
    const db = client.db(dbName); //  database name
    const result = await db
      .collection("reasons")
      .find({ "Social Category": req.query.caste })
      .sort({ metacritic: -1 })
      .toArray();
    // console.log(result);
    res.json(result);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};
