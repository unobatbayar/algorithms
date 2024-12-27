interface Car{
    year: number;
    model: string;
    electric: boolean;
}

let newCar: Car = {
    year: 1998,
    model: 'Toyota Camry',
    electric: false
}

newCar.year = 2014;

console.log(newCar.year)
