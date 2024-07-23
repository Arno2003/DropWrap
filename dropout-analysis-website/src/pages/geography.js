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
  ChooseDistDropDown,
} from "@/components/DropDown";

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

const ReasonsTab2 = ({
  classes,
  reasonList,
  dist,
  setDist,
  caste,
  std,
  category,
  setCaste,
}) => {
  const parseQuery = (fact) => {
    // console.log(category, std);
    let a;
    if (std === "") a = "prim";
    else if (std === "1") a = "upPrim";
    else a = "snr";
    return a + "_" + category + "_" + fact;
    // console.log(a + "_" + category + "_" + fact);
  };
  // parseQuery("socialcat");
  return (
    <div
      className={`${classes} bg-secLight bg-opacity-25 mt-5 dark:bg-secDark rounded-lg  `}
    >
      <h3 className="w-full text-center py-4 text-xl tracking-wider uppercase text-light font-bold bg-secDark dark:bg-dark   rounded-t-lg border-solid border-t-2 border-x-2 dark:border-secDark">
        Reasons for Dropouts
      </h3>
      <div className="flex flex-row  justify-center items-center my-3">
        <h2 className="text-xl dark:text-light text-dark px-3 py-1">
          Select District:
        </h2>
        <ChooseDistDropDown
          reasonList={reasonList}
          dist={dist}
          setDist={setDist}
          className="z-0"
        />
        {/* <CasteDropDown caste={casteReason} setCaste={setCasteReason} /> */}
      </div>
      <div className="flex flex-row text-dark dark:text-light mt-3">
        <h3 className="w-[50%] text-center border-r-2 border-b-2 border-dark dark:border-light py-4">
          Due to Caste
        </h3>
        <h3 className="w-[50%] text-center border-b-2  py-4 border-dark dark:border-light">
          Due to Family Income
        </h3>
      </div>
      {reasonList?.map((row) => {
        let f1 = parseQuery("income");
        let f2 = parseQuery("socialcat");
        console.log(row.Location.toLowerCase(), dist.toLowerCase());
        if (row.Location.toLowerCase() === dist.toLowerCase()) {
          // console.log(row[f1], row[f2]);
          return (
            <div className="flex flex-row text-dark dark:text-light  text-xl">
              <div className="w-[50%] text-center border-r-2 border-dark dark:border-light py-4 font-bold">
                {row[f1]}&nbsp;%
              </div>
              <div className="w-[50%] text-center py-4 font-bold">
                {row[f2]}&nbsp;%
              </div>
            </div>
          );
        }

        // console.log(row[f1], row[f2]);
      })}
    </div>
  );
};

const Geography = ({ mode }) => {
  const [stateName, setStateName] = useState("Gujarat");
  const [category, setCategory] = useState("Overall");
  const [caste, setCaste] = useState("Overall");
  const [casteReason, setCasteReason] = useState("Overall");
  const [std, setStd] = useState("2");
  const [reasonList, setReasonList] = useState([]);
  const [avgRate, setAvgRate] = useState(-1);
  const [dist, setDist] = useState("GUNTUR");

  useEffect(() => {
    axios
      .get(`/api/reasons?caste=${casteReason}`)
      .then((response) => {
        let res = [];
        response.data.map((row) => {
          if (row?.Location) res.push(row);
        });
        // console.log(res);
        setReasonList(res);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [stateName, category, avgRate]);

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
              {/* <ReasonsTab
                reasonList={reasonList}
                classes="text-dark w-[100%] mr-4 "
              /> */}
              <ReasonsTab2
                reasonList={reasonList}
                dist={dist}
                setDist={setDist}
                caste={caste}
                setCaste={setCaste}
                category={category}
                std={std}
                classes="text-dark w-[100%] mr-4 "
              />
            </div>

            <MapComponent2
              mode={mode}
              classes="w-[60%] "
              category={category}
              std={std}
              caste={caste}
              setAvgRate={setAvgRate}
              stateName={stateName}
            />
          </div>
        </Layout>
      </div>
    </>
  );
};

export default Geography;
