import { api } from './api'
import { Transaction } from '../types/transaction'

export const getTransactions = async (): Promise<Transaction[]> => {
    const { data } = await api.get('/transactions')
    return data
}
