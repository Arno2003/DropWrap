// import clientPromise from "../../../lib/mongodb.js";
import { connectToDatabase1, connectToDatabase2 } from "../../../lib/mongodb2";
// import stateList from "./stateList.js";

export default async (req, res) => {
  try {
    let fin = [];
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

    // console.log(req.query.dbName);
    for (let i = 0; i < stateList.length; i++) {
      const dbName = stateList[i];
      // console.log(dbName);
      if (i < 15) {
        const client = await connectToDatabase1();
        const db = client.db(dbName);
        const result = await db
          .collection("latlong")
          .find({
            "Social Category": req.query.caste,
          })
          .sort({ metacritic: -1 })
          .toArray();

        fin.push(...result);
      } else {
        const client2 = await connectToDatabase2();

        const db2 = client2.db(dbName);

        const result2 = await db2
          .collection("latlong")
          .find({
            "Social Category": req.query.caste,
          })
          .sort({ metacritic: -1 })
          .toArray();
        fin.push(...result2);
      }
    }

    res.json(fin);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: "Internal Server Error" });
  }
};