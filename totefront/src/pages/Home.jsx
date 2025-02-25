import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.jpeg';
import ContactForm from '../components/ContactForm';

const Home = () => {
    return (
        <>
            <div className='logo'>
                <img src={logo} alt="Tote Bags" />
            </div>
            <h1>Bienvenido a nuestra colección de Tote Bags</h1>
            <ContactForm  />
        </>
    );
};

export default Home;