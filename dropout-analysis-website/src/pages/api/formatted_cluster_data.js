// import clientPromise from "../../../lib/mongodb.js";
import { connectToDatabase1, connectToDatabase2 } from "../../../lib/mongodb2";
// import stateList from "./stateList.js";
export default async (req, res) => {
  try {
    const stateList = [
      "Andhra_Pradesh",
      "Assam",
      "Bihar",
      "Chhattisgarh",
      "Dadra_&_Nagar_Haveli_&_Daman_&_Diu",
      "Delhi",
      "Gujarat",
      "Haryana",
      "Himachal_Pradesh",
      "Jammu_&_Kashmir",
      "Jharkhand",
      "Karnataka",
      "Kerala",
      "Madhya_Pradesh",
      "Maharashtra",
      "Manipur",
      "Meghalaya",
      "Mizoram",
      "Nagaland",
      "Odisha",
      "Puducherry",
      "Punjab",
      "Rajasthan",
      "Sikkim",
      "Tamil_Nadu",
      "Telangana",
      "Tripura",
      "Uttarakhand",
      "Uttar_Pradesh",
      "West_Bengal",
    ];

    let fin = [];
    for (let i = 0; i < stateList.length; i++) {
      const dbName = stateList[i];
      // console.log(dbName);
      const client = await connectToDatabase1();
      const client2 = await connectToDatabase2();
      const db = client.db(dbName);
      const db2 = client2.db(dbName);

      const result = await db
        .collection("cluster")
        .find({
          "social category": req.query.caste,
        })
        .sort({ metacritic: -1 })
        .toArray();

      const result2 = await db2
        .collection("cluster")
        .find({
          "social category": req.query.caste,
        })
        .sort({ metacritic: -1 })
        .toArray();
      // console.log(result[0]);
      fin.push(...result);
      fin.push(...result2);
    }
    console.log(fin);
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
