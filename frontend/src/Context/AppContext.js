import React, { createContext, useState, useContext } from 'react';

const AppContext = createContext();

export const AppProvider = ({ children }) => {
    const [photos, setPhotos] = useState([]);
    const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')) || null);

    const updatePhotos = (newPhotos) => setPhotos(newPhotos);

    return (
        <AppContext.Provider value={{ photos, setPhotos, updatePhotos, user, setUser }}>
            {children}
        </AppContext.Provider>
    );
};

export const useApp = () => useContext(AppContext);