import React from "react";
import styled from 'styled-components';

const Container = styled.div`
  font-family: 'Raleway', sans-serif;
  background-color: #EAF7FF;
  color: #0D0D0D;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
`;

const Header = styled.header`
  background-color: #244475;
  color: #EAF7FF;
  padding: 1.5rem 0;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const Title = styled.h1`
  font-size: 2.5rem;
  font-weight: bold;
`;

const Main = styled.main`
  padding: 2rem;
  flex-grow: 1;
`;

const Section = styled.section`
  background-color: #FFFFFF;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 0 auto;
`;

const SubTitle = styled.h2`
  color: #244475;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
`;

const Paragraph = styled.p`
  margin-bottom: 1rem;
  font-size: 1rem;
  line-height: 1.6;
`;

const Button = styled.button`
  background-color: #519CE1;
  color: #FFFFFF;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  transition: background-color 0.3s;
  cursor: pointer;

  &:hover {
    background-color: #D6B230;
  }
`;

const Footer = styled.footer`
  background-color: #0D0D0D;
  color: #EAF7FF;
  padding: 1.5rem 0;
  text-align: center;
`;

const About = () => {
  return (
    <Container>
      <Header>
        <Title>About Us</Title>
      </Header>
      <Main>
        <Section>
          <SubTitle>Welcome to Dropwrap</SubTitle>
          <Paragraph>
            Education is the cornerstone of personal and societal growth. Dropwrap is an innovative online platform that offers a comprehensive visual analysis of school dropout rates across India. Our tool delves into the various reasons behind student dropouts, providing insights by state and covering the entire nation. Through Dropwrap, we aim to shed light on the educational challenges India faces and drive data-informed strategies for improvement.
          </Paragraph>
          <Paragraph>
            At Dropwrap, we believe that every child deserves an education. Our platform is dedicated to presenting a detailed and interactive visual analysis of school dropout rates in India. By examining the diverse reasons for dropouts across different states, Dropwrap provides valuable insights to educators, policymakers, and stakeholders. Our goal is to foster understanding and inspire solutions to enhance educational retention nationwide.
          </Paragraph>
          <Paragraph>
            Dropwrap is committed to supporting educational advancement in India. We provide an online tool that visualizes school dropout rates, offering detailed analysis by state and identifying key dropout factors. Our platform serves as a resource for stakeholders to understand and address the challenges in the education system, ultimately working towards reducing dropout rates and promoting inclusive education for all.
          </Paragraph>
          <Button
            onClick={() => alert('Thank you for your interest! More information will be available soon.')}
          >
            Learn More
          </Button>
        </Section>
      </Main>
      
    </Container>
  );
};

export default About;
