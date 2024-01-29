import React from "react";
import { SunIcon, MoonIcon } from "./Icons";
import Link from "next/link";
const Header = ({ mode, setMode }) => {
  const handleClick = () => {
    mode == "dark" ? setMode("light") : setMode("dark");
  };

  return (
    <header className="text-dark dark:text-light bg-light dark:bg-dark mx-3 flex flex-row items-center text-xl justify-between h-[70px] px-5 border-b-2 border-solid border-dark dark:border-light">
      <div>
        <Link href="/" className="ml-6 mr-4">
          Home
        </Link>
        <Link href="/" className="ml-6 mr-4">
          About Us
        </Link>
        <Link href="/" className="ml-6 mr-4">
          Contact
        </Link>
      </div>
      <div>
        {mode == "dark" ? (
          <button
            onClick={handleClick}
            className=" mr-6 flex flex-row items-center"
          >
            <MoonIcon className="w-8" />
          </button>
        ) : (
          <button
            onClick={handleClick}
            className=" mr-6 flex flex-row items-center"
          >
            <SunIcon className="w-8" />
          </button>
        )}
      </div>
      <div className="font-extrabold tracking-widest absolute left-[50%] top-5 translate-x-[-50%]">
        DROPWRAP
      </div>
    </header>
  );
};

export default Header;
