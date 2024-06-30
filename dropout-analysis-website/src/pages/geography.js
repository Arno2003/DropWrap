import React, { useEffect, useState, useRef } from "react";
import Head from "next/head";
import axios from "axios";
import Layout from "@/components/Layout";
import MapComponent2 from "@/components/MapComponent2";
import { motion, useSpring, useInView, useMotionValue } from "framer-motion";
import {
  CategoryDropDown,
  CasteDropDown,
  StdDropDown,
} from "@/components/DropDown";
const demoReasons = [
  {
    reason: "Not interested in education",
    rate: 19.85,
  },
  {
    reason: "Financial constraints",
    rate: 26.27,
  },
  {
    reason: "Engaged in domestic activities",
    rate: 4.62,
  },
];

const AnimatedNumbers = ({ value }) => {
  const ref = useRef(null);
  const motionValue = useMotionValue(0);
  const springValue = useSpring(motionValue, {
    duration: 1000,
  });
  const isInView = useInView(ref, { once: true });

  useEffect(() => {
    if (isInView) {
      motionValue.set(value);
    }
  }, [isInView, value, motionValue]);

  useEffect(() => {
    springValue.on("change", (latest) => {
      if (ref.current) {
        // Display the decimal value with two decimal places
        ref.current.textContent = latest.toFixed(2);
      }
    });
  }, [springValue]);

  return <span ref={ref}></span>;
};

const ReasonsTab = ({ classes, reasonList }) => {
  return (
    <div
      className={`${classes} bg-secLight bg-opacity-25 mt-5 dark:bg-secDark rounded-lg  `}
    >
      <h3 className="w-full text-center py-4 text-xl tracking-wider uppercase text-light font-bold bg-secDark dark:bg-dark   rounded-t-lg border-solid border-t-2 border-x-2 dark:border-secDark">
        Reasons for Dropouts
      </h3>

      {reasonList.map((item) => {
        return (
          <motion.div
            key={item.id}
            className={`w-[95%] flex flex-row px-5 py-4 ${
              reasonList.indexOf(item) !== reasonList.length - 1 && "border-b-2"
            } border-solid border-secDark dark:border-secLight dark:text-light mx-auto`}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
          >
            <div className="w-[80%] text-lg">{item.reason}</div>
            <div className="w-[20%] text-lg font-bold flex items-center justify-center tracking-widest">
              {item.rate === 0 ? <>0</> : <AnimatedNumbers value={item.rate} />}
              %
            </div>
          </motion.div>
        );
      })}
    </div>
  );
};

const Geography = ({ mode }) => {
  // .....................................................................
  const [latLongData, setLatLongData] = useState([]);
  const [reasonsData, setReasonsData] = useState([]);

  const stateName = "Gujarat";
  useEffect(() => {
    axios
      .get(`/api/latlong?dbName=${stateName}`)
      .then((response) => {
        setLatLongData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

    axios
      .get(`/api/reasons?dbName=${stateName}`)
      .then((response) => {
        setReasonsData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [stateName]);

  console.log(latLongData);
  console.log(reasonsData);

  // ........................................................................

  const [category, setCategory] = useState("Overall");
  const [caste, setCaste] = useState("Overall");
  const [std, setStd] = useState("2");
  const [reasonList, setReasonList] = useState(demoReasons);
  const [avgRate, setAvgRate] = useState(-1);

  useEffect(() => {
    // Function to fetch and parse the CSV file
    const fetchReasons = async () => {
      try {
        const response = await fetch("/data/reasons.csv");
        const text = await response.text();
        const rows = text.split("\n").slice(1); // Skip header row
        // console.log(rates);
        const reasons = rows.map((row) => {
          const [
            reason,
            boys71,
            girls71,
            overall71,
            boys75,
            girls75,
            overall75,
          ] = row.split(",");

          const getReasonRate = () => {
            if (avgRate === -1) {
              if (category === "Overall") return overall75;
              if (category === "Boys") return boys75;
              if (category === "Girls") return girls75;
            } else {
              if (category === "Overall")
                return ((overall75 * avgRate) / 100).toFixed(2);
              if (category === "Boys")
                return ((boys75 * avgRate) / 100).toFixed(2);
              if (category === "Girls")
                return ((girls75 * avgRate) / 100).toFixed(2);
            }
          };

          return { reason, rate: parseFloat(getReasonRate()) };
        });
        setReasonList(reasons);
      } catch (error) {
        console.error("Error fetching reasons:", error);
      }
    };

    // Call the fetchReasons function
    fetchReasons();
  }, [category, avgRate]);

  return (
    <>
      <Head>
        <title>Dropout Analysis</title>
        <meta name="description" content="Generated by create next app" />
      </Head>
      <div className="">
        <Layout classname="">
          <div className="flex flex-row justify-between h-[100px] items-center">
            <h2 className="text-acc dark:text-alt text-3xl text-left  font-extrabold ">
              GEOGRAPHICAL DISTRIBUTION
            </h2>
          </div>

          <div className="w-full h-[650px] mx-auto mb-10 flex flex-row ">
            <div className="w-[40%] mr-4">
              <div className="text-light mt-2 w-full flex flex-row mr-4 justify-evenly">
                <CategoryDropDown
                  category={category}
                  setCategory={setCategory}
                />
                <CasteDropDown caste={caste} setCaste={setCaste} />
                <StdDropDown std={std} setStd={setStd} />
              </div>
              <ReasonsTab
                reasonList={reasonList}
                classes="text-dark w-[100%] mr-4 "
              />
            </div>

            <MapComponent2
              mode={mode}
              classes="w-[60%] "
              category={category}
              caste={caste}
              std={std}
              setAvgRate={setAvgRate}
              // demoReasons={reasons}
            />
          </div>
        </Layout>
      </div>
    </>
  );
};

export default Geography;
