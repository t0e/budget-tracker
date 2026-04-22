export type TransactionType = 'income' | 'expense'

export interface Transaction {
    id: string
    amount: number
    type: TransactionType
    category: {
        id: string
        name: string
        icon: string
        color: string
    }
    description?: string
    qty: number
    note?: string
    date: string
    created_at: string
    updated_at?: string
}
