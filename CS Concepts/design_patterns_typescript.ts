/**
 * Design Patterns in TypeScript
 * 
 * Common design patterns implemented with TypeScript's type system
 * and modern features.
 */

// Singleton Pattern
class Database {
    private static instance: Database;
    private connection: string;

    private constructor() {
        this.connection = "Connected";
    }

    public static getInstance(): Database {
        if (!Database.instance) {
            Database.instance = new Database();
        }
        return Database.instance;
    }

    public query(sql: string): void {
        console.log(`Executing: ${sql}`);
    }
}

// Factory Pattern
interface Animal {
    makeSound(): void;
}

class Dog implements Animal {
    makeSound(): void {
        console.log("Woof!");
    }
}

class Cat implements Animal {
    makeSound(): void {
        console.log("Meow!");
    }
}

class AnimalFactory {
    static createAnimal(type: "dog" | "cat"): Animal {
        switch (type) {
            case "dog":
                return new Dog();
            case "cat":
                return new Cat();
        }
    }
}

// Observer Pattern
type Observer<T> = (data: T) => void;

class Observable<T> {
    private observers: Observer<T>[] = [];

    subscribe(observer: Observer<T>): () => void {
        this.observers.push(observer);
        // Return unsubscribe function
        return () => {
            this.observers = this.observers.filter(o => o !== observer);
        };
    }

    notify(data: T): void {
        this.observers.forEach(observer => observer(data));
    }
}

// Strategy Pattern
interface PaymentStrategy {
    pay(amount: number): void;
}

class CreditCardPayment implements PaymentStrategy {
    pay(amount: number): void {
        console.log(`Paid $${amount} using Credit Card`);
    }
}

class PayPalPayment implements PaymentStrategy {
    pay(amount: number): void {
        console.log(`Paid $${amount} using PayPal`);
    }
}

class PaymentProcessor {
    constructor(private strategy: PaymentStrategy) {}

    setStrategy(strategy: PaymentStrategy): void {
        this.strategy = strategy;
    }

    processPayment(amount: number): void {
        this.strategy.pay(amount);
    }
}

// Builder Pattern
class QueryBuilder {
    private selectFields: string[] = [];
    private fromTable: string = "";
    private whereConditions: string[] = [];

    select(fields: string[]): this {
        this.selectFields = fields;
        return this;
    }

    from(table: string): this {
        this.fromTable = table;
        return this;
    }

    where(condition: string): this {
        this.whereConditions.push(condition);
        return this;
    }

    build(): string {
        const select = `SELECT ${this.selectFields.join(", ")}`;
        const from = `FROM ${this.fromTable}`;
        const where = this.whereConditions.length > 0
            ? `WHERE ${this.whereConditions.join(" AND ")}`
            : "";
        return `${select} ${from} ${where}`;
    }
}

// Decorator Pattern (using TypeScript decorators)
function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${propertyKey} with args:`, args);
        const result = originalMethod.apply(this, args);
        console.log(`${propertyKey} returned:`, result);
        return result;
    };

    return descriptor;
}

class Calculator {
    @Log
    add(a: number, b: number): number {
        return a + b;
    }
}

export {
    Database,
    AnimalFactory,
    Observable,
    PaymentProcessor,
    CreditCardPayment,
    PayPalPayment,
    QueryBuilder,
    Calculator
};

