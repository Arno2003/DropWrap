import "@/styles/globals.css";
import React, { useState, useEffect } from "react";
import Head from "next/head";
import { Montserrat } from "next/font/google";
import useThemeSwitcher from "@/components/hooks/useThemeSwitcher";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import { useRouter } from "next/router";
import Loading from "@/components/Loading";
const montserrat = Montserrat({
  subsets: ["latin"],
  variable: "--font-mont",
});

export default function App({ Component, pageProps }) {
  const router = useRouter();
  const [mode, setMode] = useThemeSwitcher();
  const [loading, setLoading] = useState(true);
  const handleStart = () => setLoading(true);
  const handleComplete = () => setLoading(false);

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setLoading(false);
    }, 1000);

    // Clear the timeout to prevent hiding the component if it unmounts before the timeout
    return () => clearTimeout(timeoutId);
  }, []);

  return (
    <>
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      {/* <main className={`${montserrat.variable}  bg-light w-full min-h-screen `}> */}

      {loading && <Loading />}
      <main
        className={` bg-light dark:bg-dark w-full min-h-screen font-raleway `}
      >
        <Header mode={mode} setMode={setMode} />
        <Component mode={mode} key={router.asPath} {...pageProps} />
        <Footer />
      </main>
    </>
  );
}
