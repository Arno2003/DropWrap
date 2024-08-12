// lib/mongodb.js
import { MongoClient } from "mongodb";

const uri1 =
  "mongodb+srv://hindol_banerjee:" +
  process.env.MONGO_PASSWORD_NEW +
  "@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const uri2 =
  "mongodb+srv://hindol_banerjee:" +
  process.env.MONGO_PASSWORD_NEW +
  "@cluster1.jf2mcdo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1";

const options = {};

let client1, client2;
let clientPromise, clientPromise2;

async function connectToDatabase1() {
  if (!client1) {
    if (!global._mongoClientPromise1) {
      client1 = new MongoClient(uri1, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      });
      global._mongoClientPromise1 = await client1.connect();
      // await client1.connect();
    }
    clientPromise = global._mongoClientPromise1;
  }
  return clientPromise;
}

async function connectToDatabase2() {
  if (!client2) {
    if (!global._mongoClientPromise2) {
      client2 = new MongoClient(uri2, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      });
      global._mongoClientPromise2 = await client2.connect();
    }
    clientPromise2 = global._mongoClientPromise2;
  }
  return clientPromise2;
}

export { connectToDatabase1, connectToDatabase2 };

// if (!uri) {
//   throw new Error("Please add your Mongo URI to .env.local");
// }

// if (process.env.NODE_ENV === "development") {
//   // In development mode, use a global variable so we don't have to establish
//   // a new connection every time the function is called.
//   if (!global._mongoClientPromise) {
//     client = new MongoClient(uri, options);
//     client2 = new MongoClient(uri2, options);
//     global._mongoClientPromise = client.connect();
//     global._mongoClientPromise = client2.connect();
//   }
//   clientPromise = global._mongoClientPromise;
//   clientPromise2 = global._mongoClientPromise;
// } else {
//   // In production mode, it's best to not use a global variable.
//   client = new MongoClient(uri, options);
//   client2 = new MongoClient(uri2, options);
//   clientPromise = client.connect();
//   clientPromise2 = client2.connect();
// }

// export { clientPromise, clientPromise2 };
