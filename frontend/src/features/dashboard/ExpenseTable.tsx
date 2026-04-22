import { useQuery } from '@tanstack/react-query'
import { getTransactions } from '../../services/transaction.service'
import { Transaction } from '../../types/transaction'

export default function ExpensesTable() {
    const { data, isLoading, error } = useQuery({
        queryKey: ['expenses'],
        queryFn: getTransactions
    })

    if (isLoading) {
        return <div className="text-black p-8">Loading...</div>
    }

    if (error) {
        return <div className="text-red-500 p-8">Error loading expenses</div>
    }

    return (
        <div className="min-h-screen bg-[#0b1220] p-8">
            <div className="mx-auto max-w-6xl rounded-xl border border-white/10 bg-[#0f172a] shadow-lg">
                <div className="border-b border-white/10 px-6 py-5">
                    <h2 className="text-lg font-semibold text-white">
                        Expenses
                    </h2>
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full divide-y divide-white/10">
                        <thead>
                            <tr className="text-left text-sm font-semibold text-gray-300">
                                <th className="px-6 py-4">Date</th>
                                <th className="px-6 py-4">Description</th>
                                <th className="px-6 py-4">Category</th>
                                <th className="px-6 py-4">Qty</th>
                                <th className="px-6 py-4">Total</th>
                            </tr>
                        </thead>

                        <tbody className="divide-y divide-white/5">
                            {data?.map((expense: Transaction) => (
                                <tr
                                    key={expense.id}
                                    className="hover:bg-white/5"
                                >
                                    <td className="px-6 py-4 text-sm text-gray-300">
                                        {new Date(
                                            expense.date
                                        ).toLocaleDateString()}
                                    </td>
                                    <td className="px-6 py-4 text-sm text-white">
                                        {expense.description}
                                    </td>
                                    <td className="px-6 py-4 text-sm text-gray-300">
                                        {expense.category.name}
                                    </td>
                                    <td className="px-6 py-4 text-sm text-gray-300">
                                        {expense.qty}
                                    </td>
                                    <td className="px-6 py-4 text-sm text-green-400 font-medium">
                                        ${expense.amount.toFixed(2)}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>

                    {data?.length === 0 && (
                        <div className="text-center text-gray-400 py-10">
                            No expenses found.
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}
