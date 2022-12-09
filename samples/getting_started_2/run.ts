import { Peter, Marie, Greeter, add } from "./solution";

let peter: Peter = new Peter('Peter', 'Blue')
let marie: Marie = new Marie('Marie', 'Yellow')
let greeterPeter: Greeter<Peter> = new Greeter(peter)
greeterPeter.greet()
Greeter.greet(marie)

console.log(add(peter, 2, 3))