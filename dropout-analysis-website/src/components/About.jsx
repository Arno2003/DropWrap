import React from "react";

const About = () => {
  return (
    <div className="font-raleway bg-light text-dark min-h-screen flex flex-col justify-between">
      <header className="bg-secDark text-light py-6 text-center">
        <h1 className="text-4xl font-bold">About Us</h1>
      </header>
      <main className="p-8">
        <section className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-3xl font-bold mb-4">Welcome to Dropwrap</h2>
          <p className="mb-4">
            Education is the cornerstone of personal and societal growth. Dropwrap is an innovative online platform that offers a comprehensive visual analysis of school dropout rates across India. Our tool delves into the various reasons behind student dropouts, providing insights by state and covering the entire nation. Through Dropwrap, we aim to shed light on the educational challenges India faces and drive data-informed strategies for improvement.
          </p>
          <p className="mb-4">
            At Dropwrap, we believe that every child deserves an education. Our platform is dedicated to presenting a detailed and interactive visual analysis of school dropout rates in India. By examining the diverse reasons for dropouts across different states, Dropwrap provides valuable insights to educators, policymakers, and stakeholders. Our goal is to foster understanding and inspire solutions to enhance educational retention nationwide.
          </p>
          <p className="mb-4">
            Dropwrap is committed to supporting educational advancement in India. We provide an online tool that visualizes school dropout rates, offering detailed analysis by state and identifying key dropout factors. Our platform serves as a resource for stakeholders to understand and address the challenges in the education system, ultimately working towards reducing dropout rates and promoting inclusive education for all.
          </p>
          <button
            className="bg-secLight text-white py-2 px-4 rounded hover:bg-alt"
            onClick={() => alert('Thank you for your interest! More information will be available soon.')}
          >
            Learn More
          </button>
        </section>
      </main>
      <footer className="bg-dark text-light py-6 text-center">
        <p>&copy; 2024 Dropwrap. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default About;
