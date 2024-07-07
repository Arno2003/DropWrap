import clientPromise from "../../../lib/mongodb.js";
import stateList from "./stateList.js";
export default async (req, res) => {
  // const stateList = ["Gujarat"];
  try {
    let fin = [];
    // console.log(req.query.dbName);
    for (let i = 0; i < stateList.length; i++) {
      const dbName = stateList[i];
      // console.log(dbName);
      const client = await clientPromise;
      const db = client.db(dbName);
      const result = await db
        .collection("formatted_cluster_data")
        .find({
          Caste: req.query.caste,
        })
        .sort({ metacritic: -1 })
        .toArray();
      // console.log(result[0]);
      fin.push(...result);
    }

    res.json(fin);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};

// export default async (req, res) => {
//   try {
//     const dbName = req.query.dbName || "Gujarat";
//     const client = await clientPromise;
//     const db = client.db(dbName); //  database name
//     const result = await db
//       .collection("formatted_cluster_data")
//       .find({ Caste: req.query.caste })
//       .sort({ metacritic: -1 })
//       .toArray();
//     res.json(result);
//   } catch (e) {
//     console.error(e);
//     res.status(500).json({ error: "Internal Server Error" });
//   }
// };
