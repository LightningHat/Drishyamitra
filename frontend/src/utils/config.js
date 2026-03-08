/**
 * Configuration Manager
 * Dynamically loads environment variables based on the current environment.
 * For Create React App, we use process.env.
 */
const config = {
    apiUrl: process.env.REACT_APP_API_URL || 'http://localhost:5000',
    appTitle: 'Drishyamitra AI',
    environment: process.env.NODE_ENV || 'development'
};

export default config;