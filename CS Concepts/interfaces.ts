/**
 * TypeScript Interfaces
 * 
 * Interfaces define the structure of objects and provide type checking.
 * They're essential for building maintainable, type-safe applications.
 * 
 * Key Concepts:
 * - Contract definition (what properties/methods an object must have)
 * - Optional properties
 * - Readonly properties
 * - Extending interfaces
 * - Function types in interfaces
 */

// Basic Interface
interface User {
    id: number;
    name: string;
    email: string;
}

// Optional Properties
interface UserProfile {
    id: number;
    name: string;
    email: string;
    age?: number;           // Optional property
    phone?: string;         // Optional property
}

// Readonly Properties
interface Config {
    readonly apiKey: string;  // Cannot be modified after initialization
    readonly baseUrl: string;
    timeout: number;
}

// Extending Interfaces
interface Animal {
    name: string;
    age: number;
}

interface Dog extends Animal {
    breed: string;
    bark(): void;
}

// Function Types in Interfaces
interface Calculator {
    add(a: number, b: number): number;
    subtract(a: number, b: number): number;
    multiply(a: number, b: number): number;
}

// Index Signatures (for dynamic properties)
interface Dictionary {
    [key: string]: string;
}

// Example Usage
const user: User = {
    id: 1,
    name: "John Doe",
    email: "john@example.com"
};

const profile: UserProfile = {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    age: 30  // Optional
};

const config: Config = {
    apiKey: "abc123",
    baseUrl: "https://api.example.com",
    timeout: 5000
};
// config.apiKey = "new"; // Error: Cannot assign to 'apiKey' because it is a read-only property

const dog: Dog = {
    name: "Buddy",
    age: 3,
    breed: "Golden Retriever",
    bark: () => console.log("Woof!")
};

const calc: Calculator = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b
};

export { User, UserProfile, Config, Dog, Calculator, Dictionary };

