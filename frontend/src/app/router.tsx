import { createBrowserRouter } from 'react-router-dom'
import Dashboard from '../features/dashboard/Dashboard'

export const router = createBrowserRouter([
    { path: '/', element: <Dashboard /> }
])
