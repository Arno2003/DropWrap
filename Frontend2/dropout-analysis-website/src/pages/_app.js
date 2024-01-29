import "@/styles/globals.css";
import Head from "next/head";
import { Montserrat } from "next/font/google";
import useThemeSwitcher from "@/components/hooks/useThemeSwitcher";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import { useRouter } from "next/router";
const montserrat = Montserrat({
  subsets: ["latin"],
  variable: "--font-mont",
});

export default function App({ Component, pageProps }) {
  const router = useRouter();
  const [mode, setMode] = useThemeSwitcher();
  return (
    <>
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      {/* <main className={`${montserrat.variable}  bg-light w-full min-h-screen `}> */}
      <main
        className={` bg-light dark:bg-dark w-full min-h-screen font-raleway `}
      >
        <Header mode={mode} setMode={setMode} />
        <Component key={router.asPath} {...pageProps} />
        <Footer />
      </main>
    </>
  );
}
