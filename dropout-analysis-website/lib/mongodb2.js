import { MongoClient } from "mongodb";

const uri1 = `mongodb+srv://hindol_banerjee:${process.env.MONGO_PASSWORD_NEW}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;
const uri2 = `mongodb+srv://hindol_banerjee:${process.env.MONGO_PASSWORD_NEW}@cluster1.jf2mcdo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1`;

let client1;
let clientPromise1;

let client2;
let clientPromise2;

if (!process.env.MONGO_PASSWORD_NEW) {
  throw new Error("Please add your Mongo URI to .env.local");
}

if (process.env.NODE_ENV === "development") {
  // In development mode, use a global variable so we don't have to establish a new connection every time the function is called.
  if (!global._mongoClientPromise1) {
    client1 = new MongoClient(uri1, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    global._mongoClientPromise1 = client1.connect();
  }
  clientPromise1 = global._mongoClientPromise1;

  if (!global._mongoClientPromise2) {
    client2 = new MongoClient(uri2, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    global._mongoClientPromise2 = client2.connect();
  }
  clientPromise2 = global._mongoClientPromise2;
} else {
  // In production mode, it's best to not use a global variable.
  client1 = new MongoClient(uri1, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });
  clientPromise1 = client1.connect();

  client2 = new MongoClient(uri2, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });
  clientPromise2 = client2.connect();
}

async function connectToDatabase1() {
  if (!clientPromise1) {
    client1 = new MongoClient(uri1, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    clientPromise1 = client1.connect();
  }
  return clientPromise1;
}

async function connectToDatabase2() {
  if (!clientPromise2) {
    client2 = new MongoClient(uri2, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    clientPromise2 = client2.connect();
  }
  return clientPromise2;
}

export { connectToDatabase1, connectToDatabase2 };
