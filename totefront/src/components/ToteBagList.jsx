import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ToteBagList = () => {
    const [totes, setTotes] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/totes/')
            .then(response => setTotes(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            {totes.map(tote => (
                <div key={tote.name}>
                    <h2>{tote.name}</h2>
                    <img src={tote.image} alt={tote.name} />
                    <p>{tote.description}</p>
                    <p>Price: ${tote.price}</p>
                    <p>Style: {tote.style}</p>
                </div>
            ))}
        </div>
    );
};

export default ToteBagList;