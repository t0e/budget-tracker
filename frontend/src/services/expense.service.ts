import { api } from './api'
import { Expense } from '../types/expense'

export const getExpenses = async (): Promise<Expense[]> => {
    const { data } = await api.get('/expenses')
    return data
}
