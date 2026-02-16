// 🔥 Temporary global error handler (debug only)
window.onerror = function (message, _source, lineno, colno) {
    alert(`JS Error:\n${message}\nLine: ${lineno}\nColumn: ${colno}`)
}

window.onunhandledrejection = function (event) {
    alert('Unhandled Promise Error:\n' + event.reason)
}

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App'

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <App />
    </StrictMode>
)
