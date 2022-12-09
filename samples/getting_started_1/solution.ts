let number: number = 100_000_000
let numbers: number[] = [number]
let people: [string, number] = ['meredith', 33]
const enum WeekDays { Monday=1, Tuesday, Wednesday, Thursday, Friday }

function getWeekDay(day: number | string | null | undefined = 1): WeekDays {
    let week_day: WeekDays = WeekDays.Monday;
    if (typeof day === "string")
        day = parseInt(day)

    if (day == 1) {
        week_day = WeekDays.Monday
    } else if (day == 2) {
        week_day = WeekDays.Tuesday
    } else if (day == 3) {
        week_day = WeekDays.Wednesday
    } else if (day == 4) {
        week_day = WeekDays.Thursday
    } else if (day == 5) {
        week_day = WeekDays.Friday
    }

    return week_day
}

getWeekDay(2)
getWeekDay(null)
getWeekDay(undefined)

type HHuman = {
    readonly id: number,
    name: string,
    surname: string,
    getName: () => void
}

type Mamal = {
    readonly species: string,
    age: number,
}

// type alias
let christina_yang: HHuman & Mamal = {
    id: 1,
    name: 'christina',
    surname: 'yang',
    species: 'human',
    age: 33,
    getName: () => console.log('christina')
}

christina_yang.getName()

// literal type
type Age = 30 | 35
let age: Age = 30

console.log(((param) => param ? 'guess whos back' : 'ternay op is back')())

function getHuman(id: number): (HHuman & Mamal) | null {
    return id < 0 ? null : christina_yang
}

let human = getHuman(0)
// optional property access operator: if the property exits, access it
human?.getName()

// optional element access operator
let humans: ((HHuman & Mamal) | null)[] = [human]
console.log(humans?.[0]?.id)

// optional call operator
let log = (msg: string): void => console.log(msg)
let logs = [log, null]
logs[0]?.('message')
logs[1]?.('message')