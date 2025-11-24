
// Set REACT_APP_CODESPACE_URL from environment variable
if (!process.env.REACT_APP_CODESPACE_URL) {
  const codespaceName = process.env.CODESPACE_NAME || window.location.hostname.split('-')[0];
  process.env.REACT_APP_CODESPACE_URL = codespaceName ? `https://${codespaceName}-8000.app.github.dev` : 'http://localhost:8000';
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
