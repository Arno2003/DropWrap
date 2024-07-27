import React, { useEffect, useState, useRef } from "react";
import Head from "next/head";
import axios from "axios";
import Layout from "@/components/Layout";
import MapComponent3 from "@/components/MapComponent3";
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

const ReasonsTab2 = ({
  classes,
  dropDownList,
  reasonList,
  prop,
  setProp,
  std,
  category,
  dropLabel,
  head,
}) => {
  const [val, setVal] = useState([0, 0]);
  const parseQuery = (fact) => {
    let a;
    if (std === "") a = "prim";
    else if (std === "1") a = "upPrim";
    else a = "snr";
    return a + "_" + category + "_" + fact;
  };

  function roundToNDecimals(value, n) {
    const multiplier = Math.pow(10, n);
    return Math.round(value * multiplier) / multiplier;
  }
  const q = dropLabel === "State" ? "State" : "Location";
  // parseQuery("socialcat");
  // console.log(dropLabel, dropDownList);
  useEffect(() => {
    let temp1 = 0;
    let temp2 = 0;
    let k = 0;
    reasonList?.map((row) => {
      let f1 = parseQuery("income");
      let f2 = parseQuery("social_category");
      // console.log(row.Location.toLowerCase(), dist.toLowerCase());

      if (row[q].toLowerCase() === prop.toLowerCase()) {
        if (dropLabel === "District") {
          temp1 = row[f1].toFixed(2);
          temp2 = row[f2].toFixed(2);
          // setVal([, row[f2].toFixed(2)]);
        }
        if (dropLabel === "State") {
          temp1 = temp1 + parseFloat(row[f1]);
          temp2 = temp2 + parseFloat(row[f2]);
          k++;
        }
        // console.log(f1, f2, row);
      }
      if (dropLabel === "Total") {
        temp1 = temp1 + parseFloat(row[f1]);
        temp2 = temp2 + parseFloat(row[f2]);
        k++;
      }
    });
    if (k !== 0) {
      temp1 = roundToNDecimals(temp1 / k, 2);
      temp2 = roundToNDecimals(temp2 / k, 2);
    }
    setVal([temp1, temp2]);
  }, [reasonList, prop]);
  return (
    <div
      className={`${classes}  bg-secLight bg-opacity-25 mt-5 dark:bg-secDark rounded-lg  `}
    >
      <h3
        className={`w-full text-center py-4 text-xl tracking-wider uppercase text-light font-bold bg-secDark dark:bg-dark   rounded-t-lg border-solid border-t-2 border-x-2 dark:border-secDark ${head}`}
      >
        Reasons for Dropouts
      </h3>
      {dropLabel !== "Total" ? (
        <div className={`flex flex-row  justify-center items-center`}>
          <h2 className="text-xl dark:text-light text-dark px-3 py-1 my-2">
            Select {dropLabel}:
          </h2>
          <ChooseDistDropDown
            dropDownList={dropDownList}
            prop={prop}
            setProp={setProp}
            q={q}
            className="z-0"
          />
        </div>
      ) : (
        <h2 className="text-xl font-bold dark:text-light text-dark px-3 pt-2  w-full text-center">
          All over India
        </h2>
      )}

      <div className="flex flex-row text-dark dark:text-light mt-1">
        <h3 className="w-[50%] text-center border-r-2 border-b-2 border-dark dark:border-light py-2">
          Due to Caste
        </h3>
        <h3 className="w-[50%] text-center border-b-2  pt-2 pb-3 border-dark dark:border-light">
          Due to Family Income
        </h3>
      </div>
      <div className="flex flex-row text-dark dark:text-light  text-xl">
        <div className="w-[50%] text-center border-r-2 border-dark dark:border-light py-4 font-bold">
          {val[0]}&nbsp;%
        </div>
        <div className="w-[50%] text-center py-4 font-bold">
          {val[1]}&nbsp;%
        </div>
      </div>
    </div>
  );
};

const Geography = ({ mode }) => {
  const [category, setCategory] = useState("Overall");
  const [caste, setCaste] = useState("Overall");
  const [casteReason, setCasteReason] = useState("Overall");
  const [std, setStd] = useState("2");
  const [reasonList, setReasonList] = useState([]);
  const [avgRate, setAvgRate] = useState(-1);
  const [dist, setDist] = useState("ANANTAPUR");
  const [state, setState] = useState("GUJARAT");
  const [stateList, setStateList] = useState([]);
  const [districtList, setDistrictList] = useState([]);
  useEffect(() => {
    axios
      .get(`/api/reasons?caste=${caste}`)
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
  }, [category, avgRate, caste, std]);

  useEffect(() => {
    const distList = () => {
      let uniqueStates = [];
      let uniqueDistricts = [];
      const uniqueDistrictList = reasonList.filter((row) => {
        if (!uniqueDistricts.includes(row.Location)) {
          uniqueDistricts.push(row.Location);
          return true;
        }
        return false;
      });
      const uniqueStateList = reasonList.filter((row) => {
        if (!uniqueStates.includes(row.State)) {
          uniqueStates.push(row.State);
          return true;
        }

        return false;
      });
      setStateList(uniqueStateList);
      setDistrictList(uniqueDistrictList);
    };
    distList();
  }, [reasonList]);

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
                dropLabel="State"
                dropDownList={stateList}
                reasonList={reasonList}
                prop={state}
                setProp={setState}
                caste={caste}
                setCaste={setCaste}
                category={category}
                std={std}
                classes="text-dark w-[100%] mr-4 "
              />
              <ReasonsTab2
                head="hidden"
                dropLabel="District"
                dropDownList={districtList}
                reasonList={reasonList}
                prop={dist}
                setProp={setDist}
                caste={caste}
                setCaste={setCaste}
                category={category}
                std={std}
                classes="text-dark w-[100%] mr-4 "
              />
              <ReasonsTab2
                head="hidden"
                prop="State"
                dropLabel="Total"
                dropDownList={districtList}
                reasonList={reasonList}
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
            />
          </div>
        </Layout>
      </div>
    </>
  );
};

export default Geography;
