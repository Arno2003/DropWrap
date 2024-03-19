import React, { useState } from "react";

export const CategoryDropDown = ({ category, setCategory }) => {
  const [isOpen, setIsOpen] = useState(false);
  const cat = () => {
    if (category === "Overall") return "Both";
    if (category === "Boys") return "Boys";
    if (category === "Girls") return "Girls";
  };
  const handleClick = () => {
    isOpen === false ? setIsOpen(true) : setIsOpen(false);
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
        onClick={handleClick}
        className="mr-3 mb-2 py-3 px-3 text-dark font-bold bg-alt dark:text-alt dark:bg-dark dark:border-2 dark:border-solid dark:border-alt rounded-xl w-[130px] relative z-10  shadow-lg"
      >
        Sex : {cat()}
      </button>
      {isOpen && (
        <div className="text-light absolute flex flex-col text-md bg-dark dark:bg-secDark dark:bg-opacity-70 bg-opacity-70 dark:font-bold  rounded-lg backdrop-blur-sm w-[130px] z-10">
          <button
            onClick={handleOverallClick}
            className="py-4 px-3 border-b-2 border-solid border-light"
          >
            Both
          </button>
          <button
            onClick={handleBoysClick}
            className="py-4 px-3 border-b-2 border-solid border-light"
          >
            Boys
          </button>
          <button onClick={handleGirlsClick} className="py-4 px-3">
            Girls
          </button>
        </div>
      )}
    </div>
  );
};

export const CasteDropDown = ({ caste, setCaste }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
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
        onClick={handleClick}
        className="mr-3 mb-2 py-3 px-3 text-dark font-bold bg-alt dark:text-alt dark:bg-dark dark:border-2 dark:border-solid dark:border-alt rounded-xl w-[140px] relative z-10 shadow-lg"
      >
        Caste : {caste}
      </button>
      {isOpen && (
        <div className="text-light absolute flex flex-col text-md bg-dark dark:bg-secDark dark:bg-opacity-70 bg-opacity-70 dark:font-bold  rounded-lg backdrop-blur-sm w-[140px] z-10">
          {casteList.map((item) => {
            return (
              <button
                key={item.id}
                onClick={() => handleCasteClick(item)}
                className={`py-4 px-3 ${
                  item !== "Overall" && "border-b-2"
                } border-solid border-light`}
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
  const handleClick = () => {
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
        onClick={handleClick}
        className="mr-3 mb-2 py-3 px-3 text-dark font-bold bg-alt dark:text-alt dark:bg-dark dark:border-2 dark:border-solid dark:border-alt rounded-xl w-[160px] z-10 relative shadow-lg"
      >
        Std :{standard()}
      </button>
      {isOpen && (
        <div className="text-light absolute flex flex-col text-md bg-dark dark:bg-secDark dark:bg-opacity-70 bg-opacity-70 dark:font-bold  rounded-lg backdrop-blur-sm w-[160px] z-10">
          <button
            onClick={handlePClick}
            className="py-4 px-3 border-b-2 border-solid border-light"
          >
            Primary
          </button>
          <button
            onClick={handleUPClick}
            className="py-4 px-3 border-b-2 border-solid border-light"
          >
            Upper Primary
          </button>
          <button onClick={handleSClick} className="py-4 px-3 ">
            Secondary
          </button>
        </div>
      )}
    </div>
  );
};
