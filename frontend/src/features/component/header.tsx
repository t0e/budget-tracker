import Logo from '../../assets/budgetly_logo_small.png'

export default function Header() {
    return (
        <div className="flex justify-between items-center mb-6">
            <div>
                <img src={Logo} width={50} height={50} />
            </div>
            <div>
                <h1 className="text-2xl font-bold text-white">Budgetly</h1>
            </div>
        </div>
    )
}
