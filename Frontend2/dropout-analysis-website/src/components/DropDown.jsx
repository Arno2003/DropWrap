import React, { useState } from "react";

export const CategoryDropDown = ({ category, setCategory }) => {
  const [isOpen, setIsOpen] = useState(false);
  const cat = () => {
    if (category === "O") return "Both";
    if (category === "B") return "Boys";
    if (category === "G") return "Girls";
  };
  const handleClick = () => {
    isOpen === false ? setIsOpen(true) : setIsOpen(false);
  };
  const handleOverallClick = () => {
    if (category !== "O") setCategory("O");
  };
  const handleBoysClick = () => {
    if (category !== "B") setCategory("B");
  };
  const handleGirlsClick = () => {
    if (category !== "G") setCategory("G");
  };
  return (
    <div>
      {/* <h3 className="text-dark">Gender:</h3> */}
      <button
        onClick={handleClick}
        className="mr-3 mb-2 py-3 px-3 bg-dark w-[130px] relative z-10"
      >
        Sex : {cat()}
      </button>
      {isOpen && (
        <div className="text-dark absolute flex flex-col text-md bg-acc w-[130px] z-10">
          <button
            onClick={handleOverallClick}
            className="py-4 px-3 border-b-2 border-solid border-dark"
          >
            Both
          </button>
          <button
            onClick={handleBoysClick}
            className="py-4 px-3 border-b-2 border-solid border-dark"
          >
            Boys
          </button>
          <button
            onClick={handleGirlsClick}
            className="py-4 px-3 border-b-2 border-solid border-dark"
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
        className="mr-3 mb-2 py-3 px-3 bg-dark w-[140px] relative z-10"
      >
        Caste : {caste}
      </button>
      {isOpen && (
        <div className="text-dark absolute flex flex-col text-md bg-acc w-[140px] z-10">
          {casteList.map((item) => {
            return (
              <button
                key={item.id}
                onClick={() => handleCasteClick(item)}
                className="py-4 px-3 border-b-2 border-solid border-dark"
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
    if (std === 0) return "Primary";
    if (std === 1) return "Upper Primary";
    if (std === 2) return "Secondary";
  };
  const handleClick = () => {
    isOpen === false ? setIsOpen(true) : setIsOpen(false);
  };
  const handlePClick = () => {
    if (std !== 0) setStd(0);
  };
  const handleUPClick = () => {
    if (std !== 1) setStd(1);
  };
  const handleSClick = () => {
    if (std !== 2) setStd(2);
  };
  return (
    <div>
      {/* <h3 className="text-dark">Standard:</h3> */}
      <button
        onClick={handleClick}
        className="mr-3 mb-2 py-3 px-3 bg-dark w-[160px] z-10 relative"
      >
        Std :{standard()}
      </button>
      {isOpen && (
        <div className="text-dark absolute flex flex-col text-md bg-acc w-[160px] z-10">
          <button
            onClick={handlePClick}
            className="py-4 px-3 border-b-2 border-solid border-dark"
          >
            Primary
          </button>
          <button
            onClick={handleUPClick}
            className="py-4 px-3 border-b-2 border-solid border-dark"
          >
            Upper Primary
          </button>
          <button
            onClick={handleSClick}
            className="py-4 px-3 border-b-2 border-solid border-dark"
          >
            Secondary
          </button>
        </div>
      )}
    </div>
  );
};
