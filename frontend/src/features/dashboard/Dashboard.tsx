import Header from '../component/header'

export default function Dashboard() {
    const transactions = [
        { name: 'Investments', date: '5 Aug 2025', amount: 500 },
        { name: 'Gift', date: '10 Aug 2025', amount: -100 },
        { name: 'Pet', date: '12 Aug 2025', amount: -200 },
        { name: 'Shopping', date: '15 Aug 2025', amount: -36 }
    ]

    return (
        <div className="min-h-screen bg-[#10192b] p-6">
            <Header />

            <div className="grid grid-cols-2 md:grid-cols-3 gap-4 py-4 md:py-8">
                {/* Balance */}
                <div className="col-span-2 md:col-span-1 bg-[#FACC15] rounded-xl p-6">
                    <p>Your balance</p>
                    <h2 className="text-3xl font-bold">$3,765.75</h2>

                    <div className="flex justify-between mt-4 text-sm">
                        <div>
                            <p>This month</p>
                            <p className="font-semibold">Aug 2025</p>
                        </div>
                        <div>
                            <p>Budget used</p>
                            <p className="font-semibold">62%</p>
                        </div>
                    </div>
                </div>

                {/* Expense */}
                <div className="bg-red-300/10 rounded-xl p-6">
                    <p className="text-white">Expenses</p>
                    <h3 className="text-xl font-bold text-red-500">
                        -$4934.25
                    </h3>
                </div>

                {/* Income */}
                <div className="bg-green-300/10 rounded-xl p-6">
                    <p className="text-white">Income</p>
                    <h3 className="text-xl font-bold text-green-500">
                        +$8700.00
                    </h3>
                </div>
            </div>
            {/* Transactions */}
            <div className="py-6">
                <div className="flex justify-between mb-4">
                    <h2 className="text-lg font-bold text-white">
                        Recent Transactions
                    </h2>
                    🔍
                </div>

                <div className="space-y-4">
                    {transactions.map((t, i) => {
                        const isExpense = t.amount < 0

                        return (
                            <div
                                key={i}
                                className="flex justify-between items-center bg-white/10 p-4 rounded-xl"
                            >
                                <div>
                                    <p className="font-medium text-white">
                                        {t.name}
                                    </p>
                                    <p className="text-sm text-gray-500">
                                        {t.date}
                                    </p>
                                </div>

                                <p
                                    className={`font-medium ${
                                        isExpense
                                            ? 'text-red-500'
                                            : 'text-green-500'
                                    }`}
                                >
                                    {isExpense ? '-' : '+'}${Math.abs(t.amount)}
                                </p>
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
    )
}
