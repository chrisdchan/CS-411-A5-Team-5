const MILLI_IN_HOUR = 3600000
const MILLI_IN_MIN = 60000
const MILLI_IN_SEC = 1000

export default function getDayDiff(startDate: Date, endDate: Date): string {
    if (startDate > endDate) {
        throw new Error('ERROR in getDatDiff: startDate comes after endDate')
    }

    let duration = endDate.getTime() - startDate.getTime();
    const hours = Math.floor(duration / MILLI_IN_HOUR)
    duration %= MILLI_IN_HOUR
    const minutes = Math.floor(duration / MILLI_IN_MIN)
    duration %= MILLI_IN_MIN
    const seconds = Math.floor(duration / MILLI_IN_SEC)
    return `${hours}:${minutes}:${seconds}`
}