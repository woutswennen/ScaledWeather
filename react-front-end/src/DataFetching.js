import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataFetching = () => {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                debugger;
                const response = await axios.get('http://127.0.0.1:5000/weather/Alken/json');
                setData(response.data);
            } catch (error) {
                setError(error.message);
            }
        }
        fetchData();
    }, []);

    if (error) {
        return <div>Error: {error}</div>
    }

    return (
        <div>
            {
                data ? (
                    <p>
                        {data.current.temp_c}
                    </p>
                ) : (
                    <p>Loading data...</p>
                )
            }
        </div>
    )
}

export default DataFetching;
