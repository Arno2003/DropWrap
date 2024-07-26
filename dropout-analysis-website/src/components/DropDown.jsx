import React, { useState, useEffect } from "react";

export const CategoryDropDown = ({ category, setCategory }) => {
  const [isOpen, setIsOpen] = useState(false);
  const cat = () => {
    if (category === "Overall") return "Both";
    if (category === "Boys") return "Boys";
    if (category === "Girls") return "Girls";
  };
  const handleOverallClick = () => {
    if (category !== "Overall") setCategory("Overall");
  };
  const handleBoysClick = () => {
    if (category !== "Boys") setCategory("Boys");
  };
  const handleGirlsClick = () => {
    if (category !== "Girls") setCategory("Girls");
  };
  return (
    <div>
      {/* <h3 className="text-dark">Gender:</h3> */}
      <button
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
        // onClick={handleClick}
        className="mr-3 mb-0 py-3 px-3 text-dark font-bold border-solid border border-light border-b-dark dark:border-b-alt dark:border-dark bg-alt bg-opacity-0 dark:text-alt dark:bg-dark w-[130px] relative z-10"
      >
        Sex : {cat()}
      </button>
      {isOpen && (
        <div
          className="text-light absolute flex flex-col text-md bg-dark dark:text-dark dark:bg-light   dark:bg-opacity-70 bg-opacity-70 dark:font-bold  rounded-md backdrop-blur-sm w-[130px] z-50 "
          onMouseEnter={() => setIsOpen(true)}
          onMouseLeave={() => setIsOpen(false)}
        >
          <button
            onClick={handleOverallClick}
            className={`py-4 px-3 border-b-2 border-solid border-light hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90 rounded-t-md `}
          >
            Both
          </button>
          <button
            onClick={handleBoysClick}
            className="py-4 px-3 border-b-2 border-solid border-light hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90"
          >
            Boys
          </button>
          <button
            onClick={handleGirlsClick}
            className="py-4 px-3 hover:bg-acc hover:bg-opacity-90 hover:dark:bg-alt rounded-b-md"
          >
            Girls
          </button>
        </div>
      )}
    </div>
  );
};

export const CasteDropDown = ({ caste, setCaste }) => {
  const [isOpen, setIsOpen] = useState(false);

  const openDD = () => {
    isOpen === false ? setIsOpen(true) : setIsOpen(false);
  };
  const handleCasteClick = (item) => {
    setCaste(item);
  };

  const casteList = ["General", "OBC", "SC", "ST", "Overall"];

  return (
    <div>
      {/* <h3 className="text-dark">Caste:</h3> */}
      <button
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
        // onClick={handleClick}
        className="border-solid border border-light border-b-dark dark:border-b-alt dark:border-dark mr-3 mb-0 py-3 px-3 text-dark font-bold bg-alt dark:text-alt dark:bg-dark w-[140px] relative z-10 bg-opacity-0"
      >
        Caste : {caste}
      </button>
      {isOpen && (
        <div
          className="text-light absolute flex flex-col text-md bg-dark dark:text-dark dark:bg-light  dark:bg-opacity-70 bg-opacity-70 dark:font-bold  rounded-md backdrop-blur-sm w-[140px] z-50"
          onMouseEnter={() => setIsOpen(true)}
          onMouseLeave={() => setIsOpen(false)}
        >
          {casteList.map((item, i) => {
            return (
              <button
                key={i}
                onClick={() => handleCasteClick(item)}
                className={`py-4 px-3 ${
                  item !== "Overall" && "border-b-2"
                } border-solid border-light hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90`}
              >
                {item}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
};

export const StdDropDown = ({ std, setStd }) => {
  const [isOpen, setIsOpen] = useState(false);
  const standard = () => {
    if (std === "") return "Primary";
    if (std === "1") return "Upper Primary";
    if (std === "2") return "Secondary";
  };
  const openDD = () => {
    isOpen === false ? setIsOpen(true) : setIsOpen(false);
  };
  const handlePClick = () => {
    if (std !== "") setStd("");
  };
  const handleUPClick = () => {
    if (std !== "1") setStd("1");
  };
  const handleSClick = () => {
    if (std !== "2") setStd("2");
  };
  return (
    <div>
      {/* <h3 className="text-dark">Standard:</h3> */}
      <button
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
        className="border-solid border border-light border-b-dark dark:border-b-alt dark:border-dark mr-3 mb-0 py-3 px-3 text-dark font-bold bg-alt dark:text-alt dark:bg-dark bg-opacity-0 w-[170px] z-10 relative"
      >
        Std : {standard()}
      </button>
      {isOpen && (
        <div
          className="text-light dark:text-dark dark:bg-light absolute flex flex-col text-md bg-dark dark:bg-opacity-70 bg-opacity-70 dark:font-bold rounded-md backdrop-blur-sm w-[160px] z-50 shadow-xl"
          onMouseEnter={() => setIsOpen(true)}
          onMouseLeave={() => setIsOpen(false)}
        >
          <button
            onClick={handlePClick}
            className="py-4 px-3 border-b-2 border-solid border-light hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90 rounded-t-md"
          >
            Primary
          </button>
          <button
            onClick={handleUPClick}
            className="py-4 px-3 border-b-2 border-solid border-light hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90"
          >
            Upper Primary
          </button>
          <button
            onClick={handleSClick}
            className="py-4 px-3 hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90 rounded-b-md"
          >
            Secondary
          </button>
        </div>
      )}
    </div>
  );
};

export const ChooseDistDropDown = ({
  prop,
  setProp,
  dropDownList,
  className,
  q,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = (loc) => {
    setProp(loc);
  };
  // console.log(dist);
  return (
    <div className="">
      {/* <h3 className="text-dark">Standard:</h3> */}
      <button
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
        className={`border-solid border-2 dark:border-light border-light  rounded-md  mr-3 mb-0 py-1 px-3 font-bold  text-light !text-sm dark:!bg-dark !bg-secDark  bg-opacity-0 w-[170px]  z-10 relative ${className}`}
      >
        {prop}
      </button>
      {isOpen && (
        <div
          className="text-light dark:text-dark dark:bg-light absolute flex flex-col text-md bg-dark dark:bg-opacity-70 bg-opacity-70 dark:font-bold rounded-md backdrop-blur-sm w-[170px] h-[300px] z-50 shadow-xl overflow-y-auto overflow-x-hidden"
          onMouseEnter={() => setIsOpen(true)}
          onMouseLeave={() => setIsOpen(false)}
        >
          {dropDownList?.map((row) => {
            return (
              <button
                // onClick={handlePClick}
                className="py-3 px-3 border-b-2 border-solid border-light hover:bg-acc hover:dark:bg-alt hover:bg-opacity-90 rounded-t-md text-sm z-50"
                onClick={() => handleClick(row[q])}
                key={row._id}
              >
                {row[q]}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
};
