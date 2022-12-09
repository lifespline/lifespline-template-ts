/**
 *
 */
interface IPerson {
    greet(): string
}

interface IGreeter<A extends Animal> {

    // had to be declared so that the static method could be declared,
    // otherwise: ``'A' is declared but its value is never read.ts(6133)``
    animal: A
    greet<A> (animal: A): void
}

class Animal implements IPerson {
    protected _name: string;
    protected _age: number;

    constructor(name: string) {
        this._name = name;
        this._age = 0;
    }

    /**
     *
     * @returns Greetings from the human
     */
    public greet(): string {
        return `Hello, my name is ${this._name}!`
    }

    /**
     *
     */
    public get name(): string {
        return this._name
    }

    /**
     *
     */
    public set name(name: string) {
        this._name = name
    }

    /**
     *
     */
    public get age(): number {
        return this._age
    }

    public set age(age: number) {
        this._age = age
    }
}

/**
 *
 */
class Human extends Animal {

    constructor(name: string) {
        super(name)
    }

    /** Human adds two numbers.
     * 
     * @param a The first operand
     * @param b The second operand
     * @returns The sum of the second and the first operands
     */
    public add(a: number, b: number): number {
        return a + b
    }
}

export class Peter extends Human {
    private _favColour: string;

    constructor(name: string, favColour: string) {
        super(name)
        this._favColour = favColour;
    }

    /**
     *
     * @returns Greetings from the human
     */
    public greet(): string {
        return `Bonjour, je m'appelle ${super.name}!`
    }

    public get favColour(): string {
        return this._favColour
    }

    public set favColour(colour: string) {
        this._favColour = colour
    }
}

export class Marie extends Human {
    private _favColour: string;

    constructor(name: string, favColour: string) {
        super(name)
        this._favColour = favColour;
    }

    /**
     *
     * @returns Greetings from the human
     */
    public greet(): string {
        return `Hi, jeg hedde ${super.name}!`
    }

    public get favColour(): string {
        return this._favColour
    }

    public set favColour(colour: string) {
        this._favColour = colour
    }
}

export class Greeter<A extends Animal> implements IGreeter<A> {

    public animal: A
    constructor(animal: A) {
        this.animal = animal;
    }

    public greet(): void {
        console.log(this.animal.greet())
    }

    public static greet<A extends Animal> (animal: A): void {
        console.log(animal.greet())
    }
}

/**
 * 
 * @param human The human performing the addition of the two operands
 * @param a The first operand
 * @param b The second operand
 * @returns The sum of the second and the first operands
 */
export function add<H extends Human>(human: H, a: number, b: number): number {
    return human.add(a, b)
}

